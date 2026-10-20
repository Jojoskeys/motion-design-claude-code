# Sources et outils réellement disponibles (vérifié le 2026-10-20)

## Accès réseau de cet environnement cloud
Bloqués par la politique réseau : api.quran.com, quran.com, sunnah.com, tanzil.net, quranenc.com, dorar.net.
Joignables : GitHub (raw.githubusercontent.com) et npm. Les textes sont donc lus sur des **miroirs GitHub** des
sources officielles, pas sur les sites d'origine. Toute citation finale doit être relue sur la source d'origine
(mushaf imprimé ou quranenc.com) par un humain.

| Contenu | Miroir lu | Source d'origine déclarée |
|---|---|---|
| Texte arabe (Hafs, rasm uthmani) | github.com/fawazahmed0/quran-api, édition `ara-quranuthmanihaf` | Complexe du Roi Fahd (qurancomplex.gov.sa), v13 |
| Traduction Hamidullah | idem, `fra-muhammadhamidul` | tanzil.net |
| Traduction Rachid Maach | idem, `fra-rashidmaash` | quranenc.com |
| Al-Mukhtasar fi tafsir (FR) | github.com/spa5k/tafsir_api, `french-mokhtasar` | Markaz Tafsir (quranenc.com) |
| Tafsir Ibn Kathir (EN abrégé), Al-Muyassar, As-Sa'di (AR) | idem | quran.com |
| Sahih Muslim (AR + FR) | github.com/fawazahmed0/hadith-api, `ara-muslim`, `fra-muslim` | numérotation Fu'ad 'Abd al-Baqi |

Point d'attention : dans le miroir, certains tanwin s'affichent séparés de l'alif (ex. 94:6 « يُسۡرࣰ ا »). Problème
d'encodage/police : pour l'écran, utiliser une police coranique (KFGQPC Uthmanic Hafs ou Amiri Quran) et vérifier
chaque mot sur image.

## Outils vidéo (projet)
- HyperFrames 0.8.82 épinglé (`npx hyperframes ...`) : composition HTML, aperçu, rendu MP4, ffmpeg présent.
  `node_modules` absent : lancer `npm ci` avant la première composition.
- Voix : faite par l'utilisateur (ElevenLabs web, offre gratuite limitée ; offres payantes : à signaler). Option locale
  Kokoro via media-use (`--local-only`), voix française à tester avant tout choix.
- Sous-titres et minutage des mots : scripts `motion-design/scripts/mots.py` et `onsets.py` (transcription locale).
