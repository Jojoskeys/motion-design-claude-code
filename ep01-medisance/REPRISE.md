# Reprise : épisode 1 « La médisance » (état au 2026-10-20)

Branche : `claude/determined-tesla-akfm85`. Règles permanentes : `CLAUDE.md` (série) et `AGENTS.md` (garde-fous HyperFrames).

## Fichiers
- Script actuel (révision 6, structure validée, **texte définitif non validé**) : `serie-coran/episodes/ep01/SCRIPT.md`
- Sources et tableau script ↔ sources : `serie-coran/episodes/ep01/SOURCES.md`
- Extraits bruts : `serie-coran/episodes/ep01/sources-brutes/` (`ep01-extraits.json` : miroirs GitHub ;
  `ep01-hadeethenc-5326.txt` : page HadeethEnc, contenu fourni par l'utilisateur)
- Maquettes V2 retenues (style seulement) : `ep01-medisance/styleframes/01-accroche.png`, `02-hadith.png`,
  `03-coran.png` ; sources HTML/CSS au même endroit ; export : `python3 -I ep01-medisance/styleframes/build-styleframes.py`
- Notes de style et consignes des emplacements réservés : `ep01-medisance/styleframes/NOTES.md`

Le script et les maquettes V2 ne sont plus à modifier sans demande explicite.

## Direction graphique retenue (V2)
- Vertical 1080×1920, zone sûre : 220 px en haut, 420 px en bas, 160 px à droite.
- Palette : bleu nuit `#0b1630` / `#13254f` (dégradé radial très doux), ivoire `#f3ead7`, doré discret `#c6a15b`.
- Polices (SIL OFL, dans `assets/fonts/`) : Source Serif 4 (citations, accroche), Inter (étiquettes, références).
- Motif commun : **le fil de la parole** (pointillé doré à nœuds reliant des bulles abstraites) et **l'étoile à huit
  branches** au trait (trame très pâle, ornements). Accroche : bulles qui pâlissent, « vrai ? » en italique doré.
- Interdits : particules, lueur excessive, figures humaines, scène historique, illustration de la comparaison du verset.

## Vérifications encore ouvertes
1. Traduction Hamidullah de 49:12 (et 49:11, cité dans la description) : relire sur l'édition retenue, droit d'usage.
2. Texte arabe de 49:12 : comparer mot par mot avec un mushaf imprimé ; choisir une police coranique.
3. Commentaire HadeethEnc, point 5 : seul un résumé est enregistré ; texte exact à fournir s'il est cité.
4. Droit d'usage de la traduction HadeethEnc dans une vidéo.
5. Formule « paix et salut sur lui » : à confirmer.
Réseau de l'environnement cloud : sunnah.com, dorar.net, hadeethenc.com, quranenc.com, tanzil.net, jsDelivr bloqués.

## Prototype de l'accroche (étape D, en attente de retour)
- Composition : `ep01-medisance/index.html` (1080×1920, 7 s, muette), d'après la maquette V2 01 ; `meta.json` passé en 1080×1920.
- Aperçu : `ep01-medisance/prototypes/ep01-accroche-proto-540x960.mp4` (rendu `draft` 1080×1920 puis réduit par ffmpeg).
- Rythme : bulles et fil 0,1–1,9 s ; question 1,4 s ; « vrai ? » 2,35 s ; filet et étoile 2,7–3,55 s ; bulles à 60 % dès 3,6 s.
- GSAP 3.14.2 embarqué dans `assets/vendor/` (jsDelivr bloqué ; copié du paquet npm, licence GSAP « Standard no-charge »).
- Rendu : `npx hyperframes render -q draft -o renders/accroche-1080.mp4` depuis `ep01-medisance/`, puis
  `ffmpeg -i renders/accroche-1080.mp4 -vf scale=540:960:flags=lanczos -c:v libx264 -crf 20 -pix_fmt yuv420p -an …`.
Pas de vidéo complète, pas d'autre écran sans validation du prototype.

## Outils audio disponibles (constatés le 2026-10-20)
- `ffmpeg` / `ffprobe` : présents (`/usr/bin`).
- Voix off : à enregistrer par l'utilisateur (ElevenLabs web ou micro), après validation du texte ; aucune clé
  demandée ni stockée. Aucune voix n'existe encore.
- Minutage des mots : `.claude/skills/motion-design/scripts/mots.py` et `onsets.py` nécessitent le CLI local
  openai-whisper, **non installé** ; Kokoro (voix locale via media-use) **non installé**.
- Bruitages : 21 fichiers dans `.claude/skills/media-use/audio/assets/sfx/` (usage rare). Pas de musique.
- `node_modules` absent : lancer `npm ci` avant toute composition HyperFrames (CLI 0.8.82 épinglé, `npx hyperframes`).
