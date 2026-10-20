// Exports the storyboard stills and the contact sheets.
// Usage (from the repository root):
//   node ad-duha/storyboard/build-storyboard.cjs [chromium path]
// Room shots reuse the validated scene (../index.html) seeked to a time, with a variant applied in the page;
// the other shots come from scenes.html#<id>. Output: storyboard/frames/*.jpg and storyboard/planche-*.jpg.
const path = require("path");
const fs = require("fs");
const { execFileSync } = require("child_process");
const puppeteer = require(path.resolve(__dirname, "../../node_modules/puppeteer-core"));
const CHROME = process.argv[2] || "/opt/pw-browsers/chromium";
const DIR = __dirname;
const FRAMES = path.join(DIR, "frames");
fs.mkdirSync(FRAMES, { recursive: true });

// id, time range, short title (sheet captions: preparation document, never shown in the film)
const SHOTS = [
  ["S00", "0,00–7,40", "Introduction (validée)", { room: 0.8, variant: "intro" }],
  ["S01", "7,40–13,45", "Appel : la façade la nuit", { scene: "s01" }],
  ["S02", "13,45–21,25", "La vallée au crépuscule", { scene: "s02" }],
  ["S03a", "21,25–26,40", "L'attente : un grand ciel", { scene: "s03a" }],
  ["S03b", "26,40–29,25", "L'acacia dans le vent", { scene: "s03b" }],
  ["S04", "29,25–32,60", "Le cadre se referme", { scene: "s04" }],
  ["S05", "32,60–36,60", "La clarté de la matinée", { room: 8.3, variant: "morning", tag: "Sens des versets 93:1–2" }],
  ["S06", "36,60–38,70", "La nuit calme", { room: 1.2, variant: "calm", tag: "Sens des versets 93:1–2" }],
  ["S07", "38,70–45,40", "L'acacia au calme", { scene: "s07" }],
  ["S08", "45,40–49,60", "L'intervalle n'est pas une rupture", { scene: "s08" }],
  ["S09a", "49,60–55,00", "L'horizon ouvert", { scene: "s09a" }],
  ["S09b", "55,00–58,85", "La formulation du verset", { scene: "s09b" }],
  ["S10", "58,85–63,50", "L'étoile se tourne vers le passé", { scene: "s10" }],
  ["S11a", "63,50–65,40", "Un refuge", { scene: "s11a" }],
  ["S11b", "65,40–70,65", "Une guidée", { scene: "s11b" }],
  ["S11c", "70,65–72,80", "Des moyens de vivre", { scene: "s11c" }],
  ["S12", "72,80–83,10", "Triptyque et frise", { scene: "s12" }],
  ["S13", "83,10–92,55", "La pluie occupe tout", { room: 5.0, variant: "rain" }],
  ["S14", "92,55–98,65", "Ce qui était déjà là", { room: 7.6, variant: "objects" }],
  ["S15", "98,65–101,40", "Le matin", { room: 2.0, variant: "morningPerson" }],
  ["S16", "101,40–108,0", "Fin : la façade au matin", { scene: "s16" }],
];

const SUBS = {
  intro: "Il y a des moments où tu invoques…",
  morning: "La clarté de la matinée,",
  calm: "puis la nuit lorsqu’elle devient calme.",
  rain: "Quand une épreuve occupe toute la place,",
  objects: "Les reconnaître ne veut pas dire que notre peine n’existe pas.",
  morningPerson: "Aujourd’hui, de quel bienfait te souviens-tu ?",
};

// Variants of the validated room, applied inside the page after seeking.
function applyVariant(variant, sub, tag) {
  const $ = (s) => document.querySelector(s);
  const all = (s) => document.querySelectorAll(s);
  const stops = (id, colors) => all(`#${id} stop`).forEach((st, i) => colors[i] && st.setAttribute("stop-color", colors[i]));
  const hidePerson = () => { const g = all("#p-person svg > g"); g[2].style.display = "none"; all("#p-person svg > ellipse")[0].style.display = "none"; };
  const morning = () => {
    stops("g-sky", ["#8fa6c4", "#b9c4cf", "#e2d2b4", "#f0dcb4"]);
    stops("g-wall", ["#3e4a68", "#323e5c", "#26304a"]);
    stops("g-floor", ["#5e4e46", "#463830", "#2c2220"]);
    stops("g-moonshaft", ["#f3dcb0", "#f3dcb0"]);
    ["#moon", "#moon-halo", "#stars", "#townlights", "#rain"].forEach((s) => ($(s).style.display = "none"));
    all("#clouds path").forEach((p) => { p.setAttribute("fill", "#d8d4cc"); p.setAttribute("opacity", "0.55"); });
    $("#town").setAttribute("fill", "#6e7a94");
    $("#moonshaft").style.opacity = "1";
    $("#lampglow").style.opacity = "0";
  };
  const root = $("#root"); root.style.width = "1080px"; root.style.height = "1920px"; // sized by the runtime in HyperFrames
  all(".sub").forEach((s) => (s.style.opacity = "0"));
  $("#title").style.opacity = "0";
  if (variant === "intro") { $("#title").style.opacity = "0.92"; }
  if (variant === "morning") { morning(); hidePerson(); }
  if (variant === "morningPerson") { morning(); }
  if (variant === "calm") {
    hidePerson();
    ["#rain", "#clouds"].forEach((s) => ($(s).style.display = "none"));
    $("#moon-halo").style.opacity = "1"; $("#moonshaft").style.opacity = "1";
    all("#townlights rect").forEach((r) => (r.style.opacity = "0.6"));
  }
  if (variant === "rain") {
    const rain = $("#rain"); rain.style.opacity = "1";
    for (let i = 0; i < 90; i++) {
      const l = document.createElementNS("http://www.w3.org/2000/svg", "line");
      const x = 320 + ((i * 97) % 520), y = 350 + ((i * 211) % 720);
      l.setAttribute("x1", x); l.setAttribute("y1", y); l.setAttribute("x2", x + 2); l.setAttribute("y2", y + 30 + (i % 5) * 9);
      l.setAttribute("stroke-width", 1.6 + (i % 3)); l.setAttribute("opacity", 0.4 + (i % 4) * 0.12); rain.appendChild(l);
    }
    $("#lampglow").style.opacity = "0.4";
  }
  if (variant === "objects") {
    stops("g-sky", ["#0e1a3a", "#24345a", "#7a6a70", "#c49a74"]);
    $("#rain").style.opacity = "0.35";
    $("#moon").style.display = "none"; $("#moon-halo").style.display = "none";
    const add = (planeSel, cx, cy, r) => {
      const svg = document.querySelector(planeSel + " svg");
      const c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
      c.setAttribute("cx", cx); c.setAttribute("cy", cy); c.setAttribute("r", r);
      c.setAttribute("fill", "#f2c98a"); c.setAttribute("opacity", "0.38"); c.setAttribute("filter", "url(#f-blur-xl)");
      c.style.mixBlendMode = "screen"; svg.appendChild(c);
    };
    add("#p-table", 240, 1168, 70);   // mug
    add("#p-table", 156, 1300, 90);   // books
    add("#p-room", 800, 1030, 80);    // plant on the sill
    add("#p-room", 1075, 565, 90);    // framed picture
    add("#p-person", 850, 1390, 90);  // folded prayer rug
  }
  const s = document.getElementById("s1"); s.textContent = sub; s.style.opacity = "1"; s.style.transform = "none";
  if (tag) { // discreet mention above the subtitle (same style as scenes.html .tag)
    const t = document.createElement("div"); t.textContent = tag;
    t.style.cssText = "position:absolute;left:100px;right:160px;top:1296px;text-align:center;font:500 22px/1.2 Inter,sans-serif;letter-spacing:.12em;text-transform:uppercase;color:#c6a15b;opacity:.9";
    document.getElementById("root").appendChild(t);
  }
}

(async () => {
  const browser = await puppeteer.launch({ executablePath: CHROME, args: ["--no-sandbox", "--allow-file-access-from-files"] });
  const page = await browser.newPage();
  await page.setViewport({ width: 1080, height: 1920 });
  await page.evaluateOnNewDocument(() => { window.__timelines = {}; });
  for (const [id, , , spec] of SHOTS) {
    if (spec.scene) {
      await page.goto("file://" + path.join(DIR, "scenes.html") + "#" + spec.scene, { waitUntil: "load" });
      await page.reload({ waitUntil: "load" });
    } else {
      await page.goto("file://" + path.resolve(DIR, "../index.html"), { waitUntil: "load" });
      await page.evaluate((t) => { window.__timelines["ad-duha-intro"].seek(t, false); return true; }, spec.room);
      await page.evaluate(applyVariant, spec.variant, SUBS[spec.variant], spec.tag || "");
    }
    await page.evaluate(() => document.fonts.ready.then(() => true));
    const png = path.join(FRAMES, id + ".png");
    await page.screenshot({ path: png });
    execFileSync("ffmpeg", ["-v", "error", "-y", "-i", png, "-vf", "scale=540:960", "-q:v", "3", path.join(FRAMES, id + ".jpg")]);
    fs.unlinkSync(png);
    console.log("frame", id);
  }
  // Contact sheets, 4 x 2 per page.
  const per = 8;
  for (let p = 0; p * per < SHOTS.length; p++) {
    const cells = SHOTS.slice(p * per, p * per + per).map(([id, tc, title]) =>
      `<figure><img src="frames/${id}.jpg"><figcaption><b>${id}</b> · ${tc} s<br>${title}</figcaption></figure>`).join("");
    const html = `<!doctype html><meta charset="utf-8"><style>
      @font-face { font-family: Inter; src: url("../assets/fonts/inter-latin-500-normal.woff2"); }
      body { margin: 0; background: #0b1020; font-family: Inter, sans-serif; color: #f3ead7; }
      h1 { font-size: 26px; font-weight: 500; letter-spacing: .06em; margin: 28px 36px 8px; color: #c6a15b; }
      .grid { display: grid; grid-template-columns: repeat(4, 360px); gap: 22px 28px; padding: 18px 36px 36px; }
      figure { margin: 0; } img { width: 360px; height: 640px; display: block; border-radius: 6px; }
      figcaption { font-size: 19px; line-height: 1.35; margin-top: 10px; } b { color: #c6a15b; }
    </style><h1>Ad-Duha · storyboard · planche ${p + 1}/${Math.ceil(SHOTS.length / per)}</h1><div class="grid">${cells}</div>`;
    const file = path.join(DIR, `_planche-${p + 1}.html`);
    fs.writeFileSync(file, html);
    await page.setViewport({ width: 1620, height: 1500 });
    await page.goto("file://" + file, { waitUntil: "load" });
    await page.evaluate(() => document.fonts.ready.then(() => true));
    const h = await page.evaluate(() => document.body.scrollHeight);
    await page.setViewport({ width: 1620, height: h });
    const png = path.join(DIR, `planche-${p + 1}.png`);
    await page.screenshot({ path: png });
    execFileSync("ffmpeg", ["-v", "error", "-y", "-i", png, "-q:v", "3", path.join(DIR, `planche-${p + 1}.jpg`)]);
    fs.unlinkSync(png); fs.unlinkSync(file);
    await page.setViewport({ width: 1080, height: 1920 });
    console.log("sheet", p + 1);
  }
  await browser.close();
})();
