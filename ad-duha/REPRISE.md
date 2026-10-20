# Reprise : Ad-Duha, premiers versets (état au 2026-10-20, storyboard complet)

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

## Direction visuelle retenue (validée avec l'introduction V2)
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

## Correctif v2 : tête solidaire du corps
- Défaut corrigé : la tête était animée seule (groupe frère du torse), avec une translation `y` et un
  `transformOrigin` en px que GSAP rapporte à la boîte de la tête, d'où une dérive jusqu'à 92 px par rapport au col.
- Structure : `#upperbody` (parent, respiration `scaleY` autour de `svgOrigin 548 1272`) contient `#head` (dessiné sous
  le torse) puis `#torso`. La tête ne fait que pivoter et se raccourcir légèrement autour de la jonction du cou
  (`svgOrigin 548 946`), sans translation. Cou allongé jusqu'à y = 1000 : il passe sous le col (chevauchement caché).
- Contrôle automatique sur les 253 images (puppeteer, `getScreenCTM`) : écart du pivot tête/torse 0 px, base du cou
  toujours dans la capuche, cou visible 32-34 px. Ancienne version : 92 px d'écart, 70 points hors du col.
- Aperçu léger : `prototype/ad-duha-intro-prototype-v2.mp4` (non versionné). Audio inchangé (mêmes silences).

## Limites connues
- Rendu « peint » imité par filtres SVG : plus proche d'une illustration vectorielle soignée que d'une vraie peinture.
- Personnage stylisé et peu articulé (respiration, inclinaison de tête seulement).
- Rendu `draft` ; rendu final de qualité après validation seulement.

## Statut
- **Introduction V2 validée** par l'utilisateur (animation + correction du personnage). Ne plus modifier `index.html`
  sans demande ; la séquence et sa direction artistique sont la référence de tout le film.
- **Storyboard complet préparé, en attente de validation** : `STORYBOARD.md` (17 séquences, minutage réel, passage,
  image, action, caméra, transition), vignettes `storyboard/frames/S00…S16.jpg`, planches `storyboard/planche-1.jpg` à
  `planche-3.jpg`. Vignettes : `storyboard/scenes.html` (décors hors chambre, SVG peint) et variantes de la chambre
  validée appliquées dans la page ; export `node ad-duha/storyboard/build-storyboard.cjs`.
- Minutage mot à mot du fichier entier : `transcription/dhuha-mots.json` (transcription automatique, indicative).
- Affirmations religieuses à vérifier, séparément : `VERIFICATIONS.md` (16 points, aucun vérifié à ce stade).

## Choix visuels du storyboard
- Trois décors récurrents pour la continuité : la chambre (nuit pluvieuse → nuit calme → matin), la vallée et son
  chemin (crépuscule, poussière, chemin dégagé, horizon, demi-tour, schéma vu d'en haut), la façade (nuit / matin).
- Aucune figure hors de la personne contemporaine anonyme ; pas de Prophète, d'ange, de foule, ni de lieu historique
  reconstitué ; pas de lumière surnaturelle ; aucune image de l'au-delà ou du Paradis (horizon naturel, jarre).
- Schémas pédagogiques en illustration (pierres et intervalle S08, chemin passé/réponse/avenir S12), mots très courts.
- Cadrages variés (liste de contrôle en fin de `STORYBOARD.md`) ; raccord de forme étoile → fenêtre (S04 → S05).
- Fin : image tenue ~0,5 s après la fin du fichier audio (silence ajouté après, audio intact).

## Prochaines tâches
1. Validation du storyboard par l'utilisateur (séquences, métaphores visuelles, cadrages).
2. Vérifications religieuses de `VERIFICATIONS.md` avec sources et extraits dans `serie-coran/episodes/<ep>/SOURCES.md` ;
   décision sur la distinction paraphrase de verset / explication dans les sous-titres.
3. Ensuite seulement : animation séquence par séquence (aperçus basse résolution), en réutilisant les plans de
   profondeur et la caméra de `index.html` ; rendu complet après validation.
