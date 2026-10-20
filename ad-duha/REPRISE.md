# Reprise : Ad-Duha, premiers versets (état au 2026-10-20)

Branche : `claude/determined-tesla-akfm85`. Règles : `../CLAUDE.md` (série) et `../AGENTS.md` (garde-fous HyperFrames).
Dossier distinct de `ep01-medisance/` (conservé tel quel ; sa direction visuelle n'est pas reprise).

## Audio de référence (unique)
- `assets/audio/Dhuha.mp3` = copie octet pour octet du fichier fourni (non versionné, exclu par `.gitignore`).
  Durée **107,47 s**, mono 44,1 kHz, 128 kb/s. Jamais régénéré, ni accéléré, ni transposé. Tous les anciens audios d'Ad-Duha sont caducs.
- Transcription automatique locale (Whisper small, poids ONNX du paquet npm `sts-whisper-small`, Hugging Face bloqué par
  le réseau) : `transcription/dhuha-segments.json` (fichier entier) et `transcription/intro-mots.json` (mots, 0-9,5 s).
  Transcription **indicative** : noms propres et termes arabes mal reconnus (« Adboha », « Muslime »…), à relire à l'oreille.

## Introduction (prototype)
Mots enregistrés, vérifiés : « Il y a des moments où tu invoques, et où l'attente devient lourde. Tu regardes tes
épreuves, et tu te sens seul. » (conforme au texte attendu).
Phrases (silencedetect -45 dB) : 0,00-1,89 / 2,33-3,89 / 4,44-5,58 / 6,10-6,96 s. Phrase suivante (« Pour mieux
comprendre le Coran, abonne-toi. ») à 7,55 s. Coupe audio à **7,30 s** (dans le silence), image jusqu'à 8,40 s.
Contrôle après rendu : décalage 0 ms avec l'original, mêmes pauses, silence total après 7,3 s.

## Prototype
- Composition : `index.html` (HyperFrames 0.8.82, 1080×1920, 30 i/s, 8,4 s). GSAP 3.14.2 vendu localement
  (`assets/vendor/gsap.min.js`, jsDelivr bloqué). Polices : Inter, Source Serif 4 (OFL) dans `assets/fonts/`.
- Rendu : `npx hyperframes render -q draft -o renders/ad-duha-intro-draft.mp4` (≈ 1 min), puis version légère
  `prototype/ad-duha-intro-prototype.mp4` (540×960, non versionnée) : `ffmpeg -i renders/ad-duha-intro-draft.mp4 -vf scale=540:960 -c:v libx264 -crf 26 -preset slow -pix_fmt yuv420p -c:a copy prototype/ad-duha-intro-prototype.mp4`
- Captures versionnées : `prototype/capture-0.8s.jpg`, `capture-3.7s.jpg`, `capture-7.5s.jpg`.
- Aperçus rapides : `npx hyperframes snapshot --at 0.5,3.6,5.0,7.6 --no-end`.

## Direction visuelle retenue (à valider)
- Illustration 2D vectorielle construite en SVG (aucun outil gratuit de génération d'images disponible : les modèles
  de media-use passent par des API payantes). Texture « peinte » : bords légèrement déformés (feTurbulence +
  feDisplacementMap), marbrures du mur et du sol, grain papier ; tout est statique et déterministe (PRNG à graine).
- Cinq plans de profondeur animés par une caméra virtuelle commune (parallaxe) : ciel/lune/nuages/ville (0,25),
  pièce : mur, fenêtre, rideaux, horloge, sol, lumière lunaire (0,6), tapis + personne (0,75), table, lampe, tasse (0,88),
  premier plan flou : fauteuil, table basse, plante (1,35).
- Palette : bleu nuit, terre, sable, ivoire ; lumière chaude de la lampe à gauche, froide de la fenêtre à droite.
- Narration : plan large glissé (« invoques ») → poussée lente, pluie qui commence, aiguilles qui avancent, nuages sur la
  lune, tête qui s'incline (« lourde ») → coupe plus serrée derrière l'épaule vers la fenêtre (« épreuves ») → recul,
  les fenêtres de la ville s'éteignent une à une (« seul »).
- Personne contemporaine anonyme, de dos, sans visage ; aucun drame précis (pas de larmes, de maladie, de téléphone).
  Un tapis de prière plié, à bordure géométrique sans écriture, évoque l'invocation sans geste mis en scène.
- Texte à l'écran : titre discret « Ad-Duha · Comprendre les premiers versets » (0,25-3,3 s), sous-titres Source Serif 4
  dans la zone sûre (haut 220, bas 420, droite 160). Aucun arabe, aucune source ni note à l'image.

## Limites connues
- Rendu « peint » imité par filtres SVG : plus proche d'une illustration vectorielle soignée que d'une vraie peinture.
- Personnage stylisé et peu articulé (respiration, inclinaison de tête seulement).
- Rendu `draft` ; rendu final de qualité après validation seulement.

## Prochaine tâche
Attendre la validation du prototype. Ensuite seulement : script complet découpé sur `transcription/`, sources
(`serie-coran/episodes/<ep>/SOURCES.md`), storyboard, et déclinaison des illustrations sur toute la vidéo.
