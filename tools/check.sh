#!/bin/bash
# Headless verification of index.html's inline script using macOS JavaScriptCore.
# Catches syntax errors (e.g. duplicate top-level consts) and runtime init errors
# that would otherwise blank the whole page. Run before every publish/commit.
set -e
cd "$(dirname "$0")/.."

python3 - <<'EOF'
import re
src = open('index.html').read()
m = re.search(r'<script>\n(.*)\n</script>', src, re.S)
assert m, "no inline <script> block found"
open('/tmp/vw_script.js', 'w').write(m.group(1))
ids_js = set(re.findall(r'\$\("([a-zA-Z0-9_-]+)"\)', m.group(1)))
ids_html = set(re.findall(r'id="([a-zA-Z0-9_-]+)"', src))
missing = sorted(i for i in ids_js if i not in ids_html)
if missing:
    raise SystemExit("ids referenced in JS but missing from HTML: %s" % missing)
print("element ids: OK")
EOF

JSC=/System/Library/Frameworks/JavaScriptCore.framework/Versions/Current/Helpers/jsc
"$JSC" -e "
load('tools/dom_shim.js');
var src = readFile('/tmp/vw_script.js');
try { new Function(src); print('syntax: OK'); } catch (e) { print('SYNTAX ERROR: ' + e); quit(1); }
try { eval(src); print('runtime init: OK'); } catch (e) {
  print('RUNTIME ERROR: ' + e);
  if (e.stack) print(e.stack.split('\n').slice(0, 8).join('\n'));
  quit(1);
}"
echo "all checks passed"
