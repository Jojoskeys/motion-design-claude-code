# Reprise : Ad-Duha, premiers versets (état au 2026-10-20, film complet animé, aperçu léger)


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

## Prototype de l'introduction (historique, intégré au film)
- Composition d'origine : `index.html` au commit 0b0d40a (HyperFrames 0.8.82, 1080×1920, 30 i/s, 8,4 s). GSAP 3.14.2 vendu localement
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
- **Introduction V2 validée** par l'utilisateur (animation + correction du personnage). Elle est conservée telle quelle
  au début de `index.html` (0-8,4 s) ; seule retouche : le dernier sous-titre de l'introduction s'efface à 7,25 s
  au lieu de 7,9 s, pour laisser place à la phrase suivante de l'audio complet (7,50 s).
- **Storyboard retenu par l'utilisateur** (ensemble et continuité chambre début / fin), corrigé en révision 2 : `STORYBOARD.md` (17 séquences, minutage réel, passage,
  image, action, caméra, transition), vignettes `storyboard/frames/S00…S16.jpg`, planches `storyboard/planche-1.jpg` à
  `planche-3.jpg`. Vignettes : `storyboard/scenes.html` (décors hors chambre, SVG peint) et variantes de la chambre
  validée appliquées dans la page ; export `node ad-duha/storyboard/build-storyboard.cjs`.
- Minutage mot à mot du fichier entier : `transcription/dhuha-mots.json` (transcription automatique, indicative).
- Affirmations religieuses à vérifier, séparément : `VERIFICATIONS.md` (liste unique ; aucun point vérifié à ce stade).

## Choix visuels du storyboard
- Trois décors récurrents pour la continuité : la chambre (nuit pluvieuse → nuit calme → matin), la vallée et son
  chemin (crépuscule, poussière, chemin dégagé, horizon, demi-tour, schéma vu d'en haut), la façade (nuit / matin).
- Aucune figure hors de la personne contemporaine anonyme ; pas de Prophète, d'ange, de foule, ni de lieu historique
  reconstitué ; pas de lumière surnaturelle ; aucune image de l'au-delà ou du Paradis (horizon naturel, jarre).
- Schémas pédagogiques en illustration (pierres et intervalle S08, chemin passé/réponse/avenir S12), mots très courts.
- Cadrages variés (liste de contrôle en fin de `STORYBOARD.md`) ; raccord de forme étoile → fenêtre (S04 → S05).
- Fin : image tenue ~0,5 s après la fin du fichier audio (silence ajouté après, audio intact).

## Storyboard révision 2 (corrections demandées)
- Répétition vallée / chemin supprimée : vallée seulement en S02 ; S03a grand ciel à horizon bas ; S03b et S07 un même
  acacia (vent / calme) ; S08 tracé dans le sable ; S09a horizon ouvert sans chemin ; S10 étoile-schéma tournée vers
  le passé ; S12 triptyque en arches + frise réponse · avenir · passé.
- S09b : la jarre est remplacée par une composition typographique sobre (formulation du verset, aucune forme donnée
  aux bienfaits promis).
- Aucune durée suggérée : plus de suite de soleils et de lunes (S03a), plus de pierres dénombrables (S08).
- Mentions à l'écran : « Sens des versets 93:1–2 », « Sens du verset 93:3 » à « 93:8 » au-dessus du sous-titre ;
  « Explication » si nécessaire ; référence courte « Ṣaḥīḥ Muslim 1797a » en S03a. Sans guillemets autour des
  reformulations. Les notes techniques, réserves et commentaires restent hors de l'image. Références complètes :
  description de la vidéo et `SOURCES.md` (à créer dans `serie-coran/episodes/<ep>/`).
- Notation retenue « 93:x » (sourate:verset) pour la mention demandée « Sens des versets 93–y » ; à changer si l'utilisateur
  préfère une autre forme.
- Vignettes régénérées : S03a, S03b, S04, S05, S06, S07, S08, S09a, S09b, S10, S11a, S11b, S11c, S12 et les planches.

## Référence externe communiquée
- Sahih Muslim 1797a, https://sunnah.com/muslim:1797a : selon l'utilisateur, rapporte d'après Jundub le retard de la
  venue de Gabriel et les propos des polythéistes. **Communiquée par l'utilisateur, non consultée ici** (sunnah.com est
  bloqué dans cet environnement ; ne pas relancer l'accès). Elle ne vaut pas vérification des autres affirmations.

## Vérifications restantes
Liste unique et à jour : `VERIFICATIONS.md` (réconciliée le 2026-10-20 ; 12 points religieux, 4 points de forme).
L'ancienne liste de ce fichier y a été fusionnée ; ne plus tenir de liste ici.

## Film complet animé (2026-10-20)
- Base : storyboard révision 2 (commit e48a8a1), retenu. Audio : `Dhuha.mp3` joint, contrôlé identique (107,47 s,
  mono 44,1 kHz, 128 kb/s, md5 29953d71…), utilisé entier, sans changement de mots, de vitesse ni de hauteur.
- `index.html` = le film (composition `ad-duha`, 108,2 s ; voix 0-107,47 s ; image tenue après le dernier mot,
  ~107,33 s). Le script du film suit celui de l'introduction dans la même page et prolonge la même timeline.
  Il reprend les dessins des vignettes retenues (`storyboard/scenes.html`), découpés en plans de profondeur animés
  (caméra virtuelle par scène), et la chambre validée pour S05-S06 et S13-S15 (états matin / nuit calme / pluie /
  aube / matin par changements de couleurs, sans redessiner).
- Synchronisation : coupes et sous-titres sur le minutage mot à mot (`transcription/dhuha-mots.json`) recoupé avec les
  silences ; 43 sous-titres corrigés (Ad-Duha, Muslim, Jundub, sourate, paix, « annoncé », « ces versets »), 2 lignes
  max ; mentions « Sens du verset… », « Explication », « Ṣaḥīḥ Muslim 1797a » (glyphes étendus : Inter Medium complet,
  `assets/fonts/inter-medium-full.otf`, OFL, chargé seulement pour ces caractères).
- S11c retravaillé : angle plus bas, paniers à parois tressées et bord tressé lisibles, contenu qui monte au-dessus
  du bord ; l'image se réduit ensuite dans la troisième arche de S12.
- Les scènes cachées sont mises en `display:none` (Chrome peint les filtres feTurbulence d'un élément en
  `visibility:hidden` : bruit visible sur tout le film sinon).
- Contrôles : articulations (`getScreenCTM`, 836 images de 0-8,8 s et 82,8-101,8 s) : pivot tête/torse 0 px, base du
  cou ≤ 5,7 px du point équivalent du torse (sous la capuche) ; 64 blocs de texte : aucun > 2 lignes, aucun
  débordement, rien sous y = 1500 ni à droite de x = 920.
- Aperçu : `npx hyperframes render -q draft -o renders/ad-duha-draft.mp4`, puis
  `ffmpeg -i renders/ad-duha-draft.mp4 -vf scale=540:960 -c:v libx264 -crf 26 -preset slow -pix_fmt yuv420p -c:a aac -b:a 128k prototype/ad-duha-apercu.mp4`
  (non versionnés). Captures de contrôle versionnées : `prototype/apercu-planche-*.jpg`.

## Défauts non résolus de l'aperçu (à trancher au retour)
- S11a (64-65 s) : la mention « Sens du verset 93:6 » passe sur la lumière claire de la porte : lisible mais faible.
- S11b (66-69 s) : une borne au premier plan passe un instant derrière le sous-titre.
- Transitions S10 → S11a et S11c → S12 : surimpressions brèves (≈0,4 s) où deux images se superposent visiblement.
- S01 (8-9 s) : en gros plan, la pluie au premier plan est épaisse sur la fenêtre éclairée.
- Personnage : articulations limitées à la respiration et à l'inclinaison de la tête (comme l'introduction validée).
- Dernier mot : décroissance naturelle jusqu'à 107,35 s ; à confirmer à l'oreille (VERIFICATIONS.md, point 15).
- Défaut corrigé avant livraison : ligne claire au bord gauche pendant les secousses de S03b (cadre de finition
  élargi ; un seul nouveau rendu).

## Prochaines tâches
1. Retour de l'utilisateur sur l'aperçu complet (`prototype/ad-duha-apercu.mp4`).
2. Corrections éventuelles, puis export final haute résolution (`-q delivery`) seulement après accord.
3. En parallèle et avant publication : points de `VERIFICATIONS.md`, avec extraits dans `SOURCES.md`.
