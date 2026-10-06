#!/usr/bin/env bash
# Copy the shared kit (fonts, GSAP, images, kit.css/js) into a project so it is self-contained.
# usage: ./sync_shared.sh projects/<name>
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"; p="$here/$1"
mkdir -p "$p/fonts" "$p/vendor" "$p/img"
cp "$here/shared/fonts/Fredoka.ttf" "$p/fonts/"
cp "$here/shared/vendor/gsap.min.js" "$p/vendor/"
cp "$here/shared/img/"*.png "$p/img/" 2>/dev/null || true
cp "$here/shared/kit.css" "$here/shared/kit.js" "$p/"
echo "synced shared kit into $p"
