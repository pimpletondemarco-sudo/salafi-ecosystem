#!/usr/bin/env bash
# Installs the Etsy MCP server (github.com/aserper/etsy-mcp, MIT) at a pinned commit, once per session.
# The API key is NOT stored here: it is read from the environment secrets ETSY_API_KEY and
# ETSY_SHARED_SECRET (set in the cloud environment settings, never in chat or in the repo).
set -euo pipefail
COMMIT=77e764a5ccafecf9609fd873d1d19c9b7b30c9eb
DIR="${HOME}/.cache/etsy-mcp"
if [ -f "$DIR/dist/index.js" ] && [ "$(git -C "$DIR" rev-parse HEAD 2>/dev/null)" = "$COMMIT" ]; then
  exit 0
fi
rm -rf "$DIR"
git clone --quiet https://github.com/aserper/etsy-mcp.git "$DIR"
git -C "$DIR" checkout --quiet "$COMMIT"
cd "$DIR"
npm ci --silent --no-audit --no-fund >/dev/null 2>&1 || npm install --silent --no-audit --no-fund >/dev/null
npm run build --silent >/dev/null
echo "etsy-mcp ready at $DIR" >&2
