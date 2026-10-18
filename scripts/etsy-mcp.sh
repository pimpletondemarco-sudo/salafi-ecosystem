#!/usr/bin/env bash
# Starts the Etsy MCP server for Claude Code (installs it first if this session doesn't have it yet).
# Needs the environment secrets ETSY_API_KEY and ETSY_SHARED_SECRET. Nothing secret lives in the repo.
set -euo pipefail
"$(dirname "$0")/install-etsy-mcp.sh" 1>&2
if [ -z "${ETSY_API_KEY:-}" ] || [ -z "${ETSY_SHARED_SECRET:-}" ]; then
  echo "etsy-mcp: set ETSY_API_KEY and ETSY_SHARED_SECRET in the environment settings" >&2
fi
exec node "${HOME}/.cache/etsy-mcp/dist/index.js"
