#!/usr/bin/env node
// Etsy seller sign-in for cloud sessions, where the server's own "authenticate" tool can't open a browser.
//
//   node scripts/etsy-signin.mjs start          -> prints a link; the owner opens it and clicks "Allow"
//   node scripts/etsy-signin.mjs finish "<URL>" -> the owner pastes the address their browser ended on
//
// Etsy then sends the browser to http://localhost:3003/callback?code=..., which shows "can't connect".
// That is expected: the code is in the address bar. That callback URL must be listed under the app's
// "Callback URLs" at etsy.com/developers/your-apps.
// Tokens are saved to ~/.etsy-mcp/tokens.json (where the Etsy MCP server reads them) and never printed.
// Scopes are only what the shop needs: no deleting, no addresses, no billing or cart.
import { createHash, randomBytes } from "node:crypto";
import { mkdir, readFile, writeFile, unlink } from "node:fs/promises";
import { homedir } from "node:os";
import { join } from "node:path";

const REDIRECT_URI = "http://localhost:3003/callback";
const SCOPES = ["shops_r", "shops_w", "listings_r", "listings_w", "transactions_r", "profile_r"];
const DIR = join(homedir(), ".etsy-mcp");
const PENDING = join(DIR, "pending-signin.json");
const TOKENS = join(DIR, "tokens.json");

const apiKey = process.env.ETSY_API_KEY;
if (!apiKey) {
  console.error("ETSY_API_KEY is not set in this session's environment.");
  process.exit(1);
}

async function start() {
  const verifier = randomBytes(32).toString("base64url");
  const challenge = createHash("sha256").update(verifier).digest("base64url");
  const state = randomBytes(16).toString("hex");
  await mkdir(DIR, { recursive: true, mode: 0o700 });
  await writeFile(PENDING, JSON.stringify({ verifier, state }), { mode: 0o600 });
  const params = new URLSearchParams({
    response_type: "code",
    client_id: apiKey,
    redirect_uri: REDIRECT_URI,
    scope: SCOPES.join(" "),
    state,
    code_challenge: challenge,
    code_challenge_method: "S256",
  });
  console.log(`https://www.etsy.com/oauth/connect?${params.toString().replace(/\+/g, "%20")}`);
}

async function finish(pasted) {
  if (!pasted) throw new Error('Paste the full address, e.g. finish "http://localhost:3003/callback?code=...&state=..."');
  const { verifier, state } = JSON.parse(await readFile(PENDING, "utf-8"));
  const url = new URL(pasted.trim());
  if (url.searchParams.get("error")) throw new Error(`Etsy said: ${url.searchParams.get("error")}`);
  const code = url.searchParams.get("code");
  if (!code) throw new Error("No code in that address.");
  if (url.searchParams.get("state") !== state) throw new Error("State does not match this sign-in. Run 'start' again.");

  const res = await fetch("https://api.etsy.com/v3/public/oauth/token", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({
      grant_type: "authorization_code",
      client_id: apiKey,
      redirect_uri: REDIRECT_URI,
      code,
      code_verifier: verifier,
    }).toString(),
  });
  if (!res.ok) throw new Error(`Token exchange failed (${res.status}): ${await res.text()}`);
  const data = await res.json();
  await writeFile(
    TOKENS,
    JSON.stringify({
      access_token: data.access_token,
      refresh_token: data.refresh_token,
      expires_at: Date.now() + data.expires_in * 1000,
    }, null, 2),
    { mode: 0o600 },
  );
  await unlink(PENDING).catch(() => {});
  console.log("Signed in. Tokens saved to ~/.etsy-mcp/tokens.json (not shown).");
}

const [cmd, arg] = process.argv.slice(2);
try {
  if (cmd === "start") await start();
  else if (cmd === "finish") await finish(arg);
  else console.error("Usage: etsy-signin.mjs start | finish \"<pasted URL>\"");
} catch (e) {
  console.error(e.message);
  process.exit(1);
}
