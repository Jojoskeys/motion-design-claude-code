<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=1080, height=1920">
  <title>ep01 La médisance : montage (minutage provisoire)</title>
  <!-- Fichier généré par build-composition.py depuis composition.tpl : modifier le générateur, pas index.html. -->
  <!-- GSAP 3.14.2 embarqué en local (jsDelivr bloqué dans cet environnement), copié depuis le paquet npm gsap@3.14.2 -->
  <script src="assets/vendor/gsap-3.14.2.min.js"></script>
  <style>
    @font-face { font-family: "Source Serif 4"; font-weight: 400; src: url(assets/fonts/source-serif-4-latin-400-normal.woff2); }
    @font-face { font-family: "Source Serif 4"; font-weight: 600; src: url(assets/fonts/source-serif-4-latin-600-normal.woff2); }
    @font-face { font-family: "Source Serif 4"; font-weight: 400; font-style: italic; src: url(assets/fonts/source-serif-4-latin-400-italic.woff2); }
    @font-face { font-family: "Inter"; font-weight: 400; src: url(assets/fonts/inter-latin-400-normal.woff2); }
    @font-face { font-family: "Inter"; font-weight: 500; src: url(assets/fonts/inter-latin-500-normal.woff2); }
    @font-face { font-family: "Inter"; font-weight: 600; src: url(assets/fonts/inter-latin-600-normal.woff2); }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    html, body { background: #0b1630; }
    #root {
      position: relative; width: 100%; height: 100%; overflow: hidden;
      background: radial-gradient(110% 60% at 35% 45%, #13254f 0%, #0b1630 72%);
      color: #f3ead7; font-family: "Inter", sans-serif;
    }
    svg.decor { position: absolute; inset: 0; width: 100%; height: 100%; }
    .scene, .lab { opacity: 0; }
    .scene { position: absolute; inset: 0; }
    .bloc { position: absolute; }
    /* Zone sûre : contenu entre 220 et 1500 px, à gauche de 920 px. */
    .etiquette { left: 88px; top: 236px; width: 832px; font: 600 28px/1.2 "Inter", sans-serif; letter-spacing: .16em; text-transform: uppercase; color: #c6a15b; }
    .or { color: #c6a15b; }
    .or-it { display: block; margin-top: 10px; font: 400 italic 88px/1.1 "Source Serif 4", serif; color: #c6a15b; }
    .cta { color: #c6a15b; }

    .hook1 { left: 88px; top: 1030px; width: 832px; font: 600 60px/1.15 "Source Serif 4", serif; }
    .hook2 { left: 88px; top: 1196px; width: 832px; font: 600 62px/1.15 "Source Serif 4", serif; }

    .bulle { position: absolute; width: 760px; padding: 34px 46px 40px; border-radius: 44px; background: #0f1d40; border: 2.5px solid rgba(198,161,91,.6); }
    .bulle.g { left: 88px; }
    .bulle.d { left: 160px; border-color: rgba(243,234,215,.42); }
    .bulle::after { content: ""; position: absolute; bottom: -19px; width: 34px; height: 34px; background: #0f1d40; border: inherit; border-top: 0; border-left: 0; transform: rotate(45deg); }
    .bulle.g::after { left: 92px; }
    .bulle.d::after { right: 92px; }
    .qui { font: 600 24px/1.2 "Inter", sans-serif; letter-spacing: .14em; text-transform: uppercase; color: #c6a15b; margin-bottom: 14px; }
    .bulle.d .qui { color: #b9b3a5; }
    .qui:empty { display: none; }
    .cit { font: 400 52px/1.3 "Source Serif 4", serif; }
    .bulle.grand .cit { font-size: 58px; }
    .ref { left: 88px; top: 1196px; width: 832px; font: 500 28px/1.4 "Inter", sans-serif; color: #b9b3a5; }
    .ref strong, .ref-v strong, .ref-rappel strong { color: #f3ead7; font-weight: 600; }

    .lab-autrement { left: 88px; top: 700px; font: 600 54px/1.15 "Source Serif 4", serif; color: #b9b3a5; }
    .question { left: 88px; top: 790px; width: 832px; font: 600 76px/1.12 "Source Serif 4", serif; letter-spacing: -.01em; }
    .question .debut { display: block; }
    .question .vrai { display: block; width: max-content; margin-top: 14px; font: 400 italic 140px/1 "Source Serif 4", serif; color: #c6a15b; }

    .expl { left: 88px; top: 600px; width: 832px; font: 600 62px/1.2 "Source Serif 4", serif; }
    .expl.grand { top: 640px; font-size: 76px; }
    .note { left: 88px; top: 1180px; width: 800px; font: 400 29px/1.42 "Inter", sans-serif; color: #b9b3a5; }
    .note.bas { top: 1110px; }

    .tete { left: 88px; top: 316px; width: 832px; text-align: center; font: 400 italic 46px/1.2 "Source Serif 4", serif; color: #b9b3a5; }
    .branche { top: 690px; width: 360px; text-align: center; }
    .branche.g { left: 88px; }
    .branche.d { left: 560px; }
    .cle { font: 500 32px/1.3 "Inter", sans-serif; color: #f3ead7; }
    .mot { margin-top: 16px; font: 400 italic 70px/1.1 "Source Serif 4", serif; color: #c6a15b; }

    .titre-sourate { left: 88px; top: 960px; width: 832px; text-align: center; font: 600 76px/1.1 "Source Serif 4", serif; }
    .sous-titre-sourate { left: 88px; top: 1066px; width: 832px; text-align: center; font: 600 30px/1.2 "Inter", sans-serif; letter-spacing: .16em; text-transform: uppercase; color: #c6a15b; }

    .tag { font: 500 24px/1.5 "Inter", sans-serif; letter-spacing: .14em; text-transform: uppercase; color: #b9b3a5; opacity: .75; }
    .tag-ar { left: 88px; width: 832px; top: 590px; text-align: center; }
    .verset { left: 150px; width: 708px; top: 760px; text-align: center; font: 400 50px/1.32 "Source Serif 4", serif; }
    .ref-v { left: 88px; width: 832px; top: 1340px; text-align: center; font: 500 28px/1.4 "Inter", sans-serif; color: #b9b3a5; }

    .noeud { left: 204px; width: 716px; font: 600 54px/1.15 "Source Serif 4", serif; color: #f3ead7; }

    .rappel { left: 88px; top: 620px; width: 832px; font: 400 italic 62px/1.3 "Source Serif 4", serif; }
    .ref-rappel { left: 88px; top: 1010px; width: 832px; font: 500 28px/1.4 "Inter", sans-serif; color: #b9b3a5; }
    .ref-rappel.bas2 { top: 1070px; }

    .pilule { left: 88px; top: 1010px; padding: 18px 34px; border: 2px solid #c6a15b; border-radius: 999px; font: 600 32px/1.2 "Inter", sans-serif; color: #c6a15b; }

    .fin-titre { left: 88px; top: 600px; width: 832px; font: 600 108px/1.05 "Source Serif 4", serif; }
    .fin-ref { left: 88px; top: 750px; width: 832px; font: 600 30px/1.2 "Inter", sans-serif; letter-spacing: .16em; text-transform: uppercase; color: #c6a15b; }
    .pilules { left: 88px; top: 860px; display: flex; gap: 22px; }
    .pilule-i { padding: 16px 32px; border: 2px solid #c6a15b; border-radius: 999px; font: 600 30px/1.2 "Inter", sans-serif; color: #f3ead7; }
    .pilule-i.or-fond { background: #c6a15b; color: #0b1630; }
    .fin-sources { left: 88px; top: 1010px; width: 800px; font: 400 26px/1.5 "Inter", sans-serif; color: #b9b3a5; }

    /* Sous-titres : 2 lignes au plus, au-dessus des 420 px du bas */
    .st { position: absolute; left: 88px; top: 1290px; width: 832px; font: 500 44px/1.3 "Inter", sans-serif; color: #f3ead7; opacity: 0; }
  </style>
</head>
<body>
  <div id="root" data-composition-id="ep01-medisance" data-start="0" data-width="1080" data-height="1920" data-duration="%%DUREE%%">
    <svg class="decor" viewBox="0 0 1080 1920" aria-hidden="true">
      <defs>
        <pattern id="trame" width="132" height="132" patternUnits="userSpaceOnUse">
          <g transform="translate(66 66)" fill="none" stroke="#c6a15b" stroke-width="1.4">
            <rect x="-26" y="-26" width="52" height="52"/><rect x="-26" y="-26" width="52" height="52" transform="rotate(45)"/>
          </g>
        </pattern>
        <radialGradient id="fondu" cx="85%" cy="12%" r="55%"><stop offset="0" stop-color="#fff" stop-opacity="1"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>
        <mask id="m"><rect width="1080" height="1920" fill="url(#fondu)"/></mask>
      </defs>
      <!-- Trame fixe, commune à tout l'épisode -->
      <rect width="1080" height="1920" fill="url(#trame)" opacity=".09" mask="url(#m)"/>
    </svg>
    %%ETIQUETTES%%
    %%SCENES%%
    %%AUDIO%%
  </div>
  <script>
    const tl = gsap.timeline({ paused: true });
    // Fil de la parole : un tracé plein, dans un masque, se déroule et révèle le pointillé
    const LONGUEURS = {};
    for (const id of %%FILS%%) {
      const p = document.getElementById(id);
      const L = p.getTotalLength();
      // trait L, puis vide L + 40 ; départ décalé de L + 20 : aucun reste visible avant le tracé
      LONGUEURS[id] = L + 20;
      gsap.set(p, { strokeDasharray: L + " " + (L + 40), strokeDashoffset: L + 20 });
    }
    const trace = (id, at, d) => tl.fromTo("#" + id,
      { strokeDashoffset: LONGUEURS[id] }, { strokeDashoffset: 0, duration: d, ease: "power1.inOut" }, at);
    %%JS%%
    window.__timelines["ep01-medisance"] = tl;
  </script>
</body>
</html>
