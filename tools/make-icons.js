// Render icons/icon.svg to the PNG sizes phones and browsers need.
// Run from the repo root:  node tools/make-icons.js   (needs Playwright + Chromium)
const { chromium } = require("playwright");
const fs = require("fs");
const path = require("path");

const root = path.resolve(__dirname, "..");
const svg = fs.readFileSync(path.join(root, "icons/icon.svg"), "utf8");
const dataUrl = "data:image/svg+xml;base64," + Buffer.from(svg).toString("base64");

// pad: shrink the art inside the canvas (icon.svg already keeps its art inside the maskable safe zone, so 0 everywhere)
const outputs = [
  { file: "icon-192.png", size: 192, pad: 0 },
  { file: "icon-512.png", size: 512, pad: 0 },
  { file: "maskable-512.png", size: 512, pad: 0 },
  { file: "apple-touch-icon.png", size: 180, pad: 0 },
  { file: "favicon-32.png", size: 32, pad: 0 },
];

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ deviceScaleFactor: 1 });
  for (const o of outputs) {
    await page.setViewportSize({ width: o.size, height: o.size });
    const inner = Math.round(o.size * (1 - o.pad * 2));
    await page.setContent(
      `<html><body style="margin:0;width:${o.size}px;height:${o.size}px;background:#05080f;display:grid;place-items:center;overflow:hidden">` +
      `<img src="${dataUrl}" width="${inner}" height="${inner}" style="display:block"></body></html>`
    );
    await page.waitForFunction(() => document.images[0].complete);
    await page.screenshot({ path: path.join(root, "icons", o.file), clip: { x: 0, y: 0, width: o.size, height: o.size } });
    console.log("wrote icons/" + o.file);
  }
  await browser.close();
})();
