#!/usr/bin/env python3
"""Build index.html (the installable web app) from app.html (the shared source).

app.html is written in Claude-artifact form: no <html>/<head>/<body> tags.
This script moves its <title>, links and <style> into a real <head>, adds the
PWA tags (manifest, icons, iOS meta) plus the install/service-worker script,
and stamps sw.js with a content hash so phones pick up new versions.

Run from the repo root:  python3 tools/build.py
"""
import hashlib
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
src = (ROOT / "app.html").read_text(encoding="utf-8")

split = src.index('<div id="app">')
head_part, body_part = src[:split], src[split:]
head_part = re.sub(r'<meta name="claude:[^>]*>\s*', "", head_part)

PWA_HEAD = """<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="description" content="Personal level-up fitness tracker: daily quests, ranks, bosses and stats.">
<meta name="theme-color" content="#060a13">
<meta name="color-scheme" content="dark">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Ascend">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icons/icon.svg" type="image/svg+xml">
<link rel="icon" href="icons/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>
"""

PWA_SCRIPT = """<script>
// Install support + offline service worker (web app only; not used inside Claude).
(() => {
  let deferred = null;
  const ping = () => window.dispatchEvent(new Event("ascend-pwa"));
  window.ascendPWA = {
    canPrompt: () => !!deferred,
    isIOS: () => /iphone|ipad|ipod/i.test(navigator.userAgent) || (navigator.platform === "MacIntel" && navigator.maxTouchPoints > 1),
    isStandalone: () => matchMedia("(display-mode: standalone)").matches || navigator.standalone === true,
    prompt: async () => { if (!deferred) return; deferred.prompt(); try { await deferred.userChoice; } catch (e) {} deferred = null; ping(); },
  };
  addEventListener("beforeinstallprompt", e => { e.preventDefault(); deferred = e; ping(); });
  addEventListener("appinstalled", () => { deferred = null; ping(); });
  if ("serviceWorker" in navigator && (location.protocol === "https:" || location.hostname === "localhost")) {
    addEventListener("load", () => navigator.serviceWorker.register("sw.js").catch(() => {}));
  }
})();
</script>
"""

html = (
    "<!doctype html>\n<html lang=\"en\">\n<head>\n"
    + PWA_HEAD
    + head_part.strip()
    + "\n</head>\n<body>\n"
    + PWA_SCRIPT
    + body_part.strip()
    + "\n</body>\n</html>\n"
)
(ROOT / "index.html").write_text(html, encoding="utf-8")

# Stamp the service worker cache name so installed copies update.
digest = hashlib.sha256(html.encode()).hexdigest()[:10]
sw = ROOT / "sw.js"
sw.write_text(re.sub(r'const VERSION = "[^"]*";', f'const VERSION = "ascend-{digest}";', sw.read_text()), encoding="utf-8")
print(f"index.html built ({len(html):,} bytes), sw cache ascend-{digest}")
