// Light preview of one passage of the film, with the real audio of that passage (test before any full render).
// Usage (from the repository root): node ad-duha/apercu-extrait.cjs 26.4 49.6 [out.mp4]
// Seeks the film timeline of index.html frame by frame (30 fps) in Chromium, at 540x960 (device scale 0.5), applies
// the clip windows (data-start / data-duration) like the HyperFrames runtime, then muxes the matching cut of
// Dhuha.mp3 (stream copy of the decoded samples, re-encoded AAC; no change of speed or pitch).
const path = require("path");
const fs = require("fs");
const { execFileSync } = require("child_process");
const puppeteer = require(path.resolve(__dirname, "../node_modules/puppeteer-core"));
const [A, B] = process.argv.slice(2, 4).map(Number);
if (!(B > A)) throw new Error("usage: node ad-duha/apercu-extrait.cjs <start> <end> [out.mp4]");
const OUT = path.resolve(process.argv[4] || path.join(__dirname, `prototype/extrait-${A}-${B}.mp4`));
const FPS = 30, N = Math.round((B - A) * FPS);
const TMP = path.join(__dirname, "renders", `.frames-${A}-${B}`);
fs.rmSync(TMP, { recursive: true, force: true }); fs.mkdirSync(TMP, { recursive: true });
(async () => {
  const browser = await puppeteer.launch({ executablePath: "/opt/pw-browsers/chromium", args: ["--no-sandbox", "--allow-file-access-from-files"] });
  const page = await browser.newPage();
  await page.setViewport({ width: 1080, height: 1920, deviceScaleFactor: 0.5 });
  page.on("pageerror", (e) => console.log("pageerror:", e.message));
  await page.evaluateOnNewDocument(() => { window.__timelines = {}; });
  await page.goto("file://" + path.join(__dirname, "index.html"), { waitUntil: "load" });
  await page.evaluate(() => document.fonts.ready.then(() => true));
  await page.evaluate(() => { const r = document.getElementById("root"); r.style.width = "1080px"; r.style.height = "1920px"; });
  for (let f = 0; f < N; f++) {
    const t = A + f / FPS;
    await page.evaluate((t) => {
      document.querySelectorAll("[data-start]").forEach((e) => {
        if (e.tagName === "AUDIO" || e.id === "root") return;
        const s = +e.dataset.start, d = +e.dataset.duration;
        e.style.visibility = t >= s && t < s + d ? "visible" : "hidden";
      });
      window.__timelines["ad-duha"].seek(t, false);
    }, t);
    await page.screenshot({ path: path.join(TMP, String(f).padStart(5, "0") + ".jpg"), type: "jpeg", quality: 92 });
    if (f % 90 === 0) console.log("frame", f, "/", N);
  }
  await browser.close();
  execFileSync("ffmpeg", ["-v", "error", "-y", "-framerate", String(FPS), "-i", path.join(TMP, "%05d.jpg"),
    "-ss", String(A), "-t", String(B - A), "-i", path.join(__dirname, "assets/audio/Dhuha.mp3"),
    "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-crf", "24", "-preset", "slow", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "128k", "-shortest", "-movflags", "+faststart", OUT]);
  fs.rmSync(TMP, { recursive: true, force: true });
  console.log(OUT);
})();
