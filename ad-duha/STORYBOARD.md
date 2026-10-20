# Ad-Duha · storyboard illustré (suite de l'introduction validée)

Document de préparation. À l'image : seulement le sous-titre, des mentions discrètes (« Sens du verset 93:x »,
« Explication », une référence courte) et les titres prévus. Jamais de note technique, de réserve de travail ni de long
commentaire éditorial. Références complètes : description de la vidéo et `SOURCES.md`.

- Audio unique : `assets/audio/Dhuha.mp3` (107,47 s), jamais modifié. Minutage mesuré sur ce fichier : transcription
  locale mot à mot (`transcription/dhuha-mots.json`) recoupée avec la détection des silences (-45 dB). Chaque coupe
  tombe dans un silence ; aucune phrase n'est coupée.
- Narration : **transcription automatique**, recopiée telle qu'entendue ; seuls les noms propres mal reconnus sont
  rétablis entre crochets (« [Ad-Duha] », « [Muslim] », « [Jundub] »), à confirmer à l'écoute. Narration inchangée.
- Vignettes : `storyboard/frames/<id>.jpg` (540×960) ; planches : `storyboard/planche-1.jpg` à `planche-3.jpg`.
  Régénération : `node ad-duha/storyboard/build-storyboard.cjs` (depuis la racine du dépôt).
- Les vignettes montrent un instant représentatif ; le sous-titre y est indicatif (position et police du prototype).

## Écarts de l'animation par rapport aux vignettes (2026-10-20, aperçu complet)
Notes de l'aperçu complet, avant la révision 3 (qui remplace S02-S04, S07, S08, S09a, S10, S12). Le storyboard révision 2 restait la base ; l'animation (`index.html`) y apporte seulement ceci :
- S01 / S16 : pictogrammes au-dessus du sous-titre (y ≈ 1210, sur un disque sombre) plutôt que dans les 420 px du bas.
- S04 : la phrase est affichée en deux sous-titres (« … sont révélés » / « les premiers versets d'Ad-Duha. »).
- S09b : la formulation du verset 5 en quatre groupes de mots, 56 px, sans sous-titre en double.
- S11a : cadrage plus large (la lumière de la porte reste au-dessus du sous-titre) ; la lumière se resserre en point.
- S11c : nouvel angle plus bas ; paniers à parois et bord tressés, contenu qui monte au-dessus du bord.
- S12 : arches un peu plus hautes, frise à y = 1110, étiquettes en 34 px.
- Mentions : Inter 26 px (au lieu de 22) pour la lecture sur téléphone.
- Fin : image tenue jusqu'à 108,2 s (dernier mot ~107,33 s).

## Fils de continuité
- **La chambre** (décor validé) ouvre, sert de pivot au milieu (S05-S06 : « deux moments que l'on connaît ») et
  ferme le film (S13-S15). Elle passe de la nuit pluvieuse à la nuit calme puis au matin : la lumière change pour
  des raisons naturelles (pluie, nuages, aube), jamais surnaturelles.
- **Un décor pour le récit rapporté** (révision 3) : le grand ciel à horizon bas, du crépuscule (S02) à la nuit
  (S03a-S08), porte des compositions éditoriales courtes : bulles vides (paroles qui circulent), intervalle ouvert,
  accusation attribuée, titre, réponse, « Un retard ≠ un rejet ». Les mêmes éléments reviennent pour la réponse (S07
  reprend S03b). Les trois arches (S10, S12) contiennent les miniatures des trois rappels illustrés (S11a-c).
- **La façade** : appel à s'abonner la nuit (S01), carte de fin au matin (S16).
- Aucune figure humaine hors de la personne contemporaine anonyme de la chambre. Ciel, maison, bornes, paniers
  sont des **illustrations pédagogiques génériques** : aucune ne prétend reconstituer un lieu, un objet ou un événement
  historique, ni une durée.

## Mentions à l'écran (révision 2)
- Paraphrases des versets : mention discrète au-dessus du sous-titre, Inter capitales dorées 22 px :
  « Sens des versets 93:1–2 », « Sens du verset 93:3 »… Aucun guillemet autour d'une reformulation libre.
- Explications : mention « Explication » quand la phrase pourrait être prise pour le texte (S08, S11b 2e phrase,
  S12, S07 2e phrase).
- Référence courte autorisée : « Ṣaḥīḥ Muslim 1797a » en S03a (référence communiquée par l'utilisateur, voir REPRISE).
- Numéros de versets, traductions et références complètes : à confirmer avant rendu (liste dans `REPRISE.md`).

## Révision 3 (2026-10-20) : plans remplacés pour suivre la narration
Correction ciblée demandée par l'utilisateur après l'aperçu : l'acacia, le trait dans le sable et l'étoile tournante
demandaient une interprétation impossible à deviner. Plans modifiés : S02, S03a, S03b, S04, S07, S08, S09a, S10, S12,
S15 (et précision de l'action en S13-S14). Conservés : audio, introduction V2, S01, S05-S06, S09b, illustrations de
S11a-c, chambre S13-S15, S16. Vignettes des seuls plans modifiés : `storyboard/frames-r3/`, planches
`storyboard/planche-r3-1.jpg` et `planche-r3-2.jpg` (`node ad-duha/storyboard/build-storyboard.cjs --r3`).
Règle : jamais le même texte en grand et en sous-titre au même moment (S07b et S12a sans sous-titre, comme S09b).

### Ambiguïtés signalées (illustration contemporaine / parole rapportée / explication)
1. **S03a** « La venue de Gabriel tarde » est un résumé du récit, pas une citation ; il se lit avec la référence
   « Ṣaḥīḥ Muslim 1797a », non consultée ici (VERIFICATIONS 1).
2. **S03b** « Propos des polythéistes » : attribution de la version de Muslim ; une autre version attribuerait la parole
   à une femme (VERIFICATIONS 3). « Abandonné » résume leur parole ; ce n'est pas la formulation arabe, d'où l'absence
   de guillemets et la précision « selon le récit rapporté ».
3. **S04** : le titre arrive après l'effacement complet de l'accusation, pour qu'aucune image n'associe « Ad-Duha » et
   « Abandonné ».
4. **S07b** : « Son Seigneur ne l'a ni abandonné ni détesté » est la paraphrase de la narration, à la troisième
   personne (le verset s'adresse au Prophète) ; elle est donnée comme « Sens du verset 93:3 », jamais comme traduction
   (VERIFICATIONS 7). Le trait qui barre l'accusation (S07c) relève de l'explication (mention « Explication »).
5. **S08** : « Un retard ≠ un rejet » est une explication, à rattacher à un tafsir nommé (VERIFICATIONS 8).
6. **S09a** : le schéma fixe la lecture « vie dernière / vie présente » ; une autre lecture (« la fin meilleure que le
   début ») existe et n'est pas montrée (VERIFICATIONS 9). Le décor de dune n'illustre pas l'au-delà.
7. **S10-S12** : porte, bornes, paniers sont des illustrations pédagogiques génériques, pas des reconstitutions ; la
   route balisée illustre la « guidée » par une image (verset 7, point sensible, VERIFICATIONS 10). La suite
   « Réponse · Avenir · Passé » est la lecture de la narration (VERIFICATIONS 11).
8. **S13-S15** : la personne de la chambre est contemporaine et représente le spectateur, jamais le Prophète ; le passage
   est marqué par « Et nous » et le retour au décor de l'introduction.

## Séquences

### S00 · 0,00-7,40 · Introduction (validée, inchangée)
« Il y a des moments où tu invoques… et où l'attente devient lourde. Tu regardes tes épreuves, et tu te sens seul. »
Prototype V2 conservé tel quel (`index.html`). Sa dernière action (le recul de caméra) se prolonge dans S01.

### S01 · 7,40-13,45 · Appel : la façade la nuit
« Pour mieux comprendre le Coran, abonne-toi. Et si ces explications te sont utiles, aime la vidéo et partage-la. »
- On voit : l'immeuble sous la pluie, la fenêtre de la chambre est la seule à lampe chaude parmi quelques autres.
- Action : la caméra sort par la fenêtre ; trois pictogrammes dorés au trait (cloche, cœur, partage) se dessinent
  sous le sous-titre au rythme de « abonne-toi », « aime », « partage ».
- Caméra : recul continu (grue arrière) de la vitre jusqu'à la façade entière.
- Transition : la caméra monte le long de la façade vers les nuages ; fondu enchaîné nuage → ciel de crépuscule (S02).

### S02 · 13,45-21,25 · Le contexte d'Ad-Duha · **modifié (révision 3)**
- Phrase exacte : « La sourate Ad-Duha s'adresse d'abord au Prophète, paix et salut sur lui. Pour en comprendre les
  premiers versets, il faut revenir à ce qui se disait autour de lui. »
- Action visible : la caméra quitte la façade (S01) par le haut ; le grand ciel au crépuscule et son horizon bas
  remplacent l'immeuble. Sur « Pour en comprendre » (17,4 s), le titre « Le contexte d'Ad-Duha » se pose ; sur
  « ce qui se disait » (19,8 s), des bulles vides (trois points, jamais de mots) apparaissent et circulent sur des
  trajectoires courbes. Aucun personnage, aucun dialogue inventé.
- Le spectateur comprend : on quitte la chambre d'aujourd'hui pour entrer dans un récit rapporté.
- Texte à l'écran : « Le contexte d'Ad-Duha » (titre) ; sous-titres de la narration.
- Remplace : la vallée au crépuscule. Le grand ciel devient le décor unique du récit (S02 à S08), du crépuscule à la nuit.

### S03a · 21,25-26,40 · L'attente · **modifié**
- Phrase exacte : « Dans un récit rapporté par Muslim, Jundub raconte que Gabriel tarde à venir auprès du Prophète. »
- Action visible : les bulles s'effacent ; une ligne fine traverse le ciel. Un premier repère doré se pose à gauche ;
  le trait avance puis se change en pointillés qui pâlissent ; le second repère (contour seul) reste non atteint :
  l'intervalle reste ouvert. Sur « tarde à venir » (24,5 s) apparaît « La venue de Gabriel tarde ». Le ciel passe une
  seule fois du crépuscule à la nuit.
- Le spectateur comprend : un délai, sans durée précise et sans explication de sa cause.
- Texte à l'écran : « La venue de Gabriel tarde » ; mention « Ṣaḥīḥ Muslim 1797a » au-dessus du sous-titre.
- Interdits respectés : ni calendrier, ni nombre de jours, ni personnage, ni représentation de Gabriel.
- Remplace : le grand ciel seul.

### S03b · 26,40-29,25 · L'accusation · **modifié**
- Phrase exacte : « Les polythéistes affirment alors qu'il a été abandonné. »
- Action visible : sur « affirment » (27,3 s), un seul bloc apparaît d'un coup : l'attribution « Propos des
  polythéistes · selon le récit rapporté » et le mot « Abandonné » (italique), jamais l'un sans l'autre. Des bulles
  vides poussées par le vent restent sur les bords.
- Le spectateur comprend : c'est leur accusation, rapportée par le récit ; le narrateur ne la confirme pas.
- Texte à l'écran : attribution + « Abandonné », sans guillemets (résumé, pas citation du texte arabe).
- Remplace : l'acacia dans le vent. Aucune personne délaissée, aucune figure du Prophète.

### S04 · 29,25-32,60 · Le passage coranique arrive · **modifié**
- Phrase exacte : « C'est dans ce contexte que sont révélés les premiers versets d'Ad-Duha. »
- Action visible : le bloc de l'accusation se floute et s'efface **entièrement** avant l'apparition du titre (aucune
  image où « Abandonné » et « Ad-Duha » sont lisibles ensemble) ; seules quelques bulles vides restent floues à
  l'arrière-plan. Le titre « Ad-Duha » se pose au centre (30,6 s), dans un cadre doré aux proportions de la fenêtre de la
  chambre ; ce cadre devient la fenêtre de S05 (raccord de forme).
- Le spectateur comprend : les paroles rapportées passent au second plan ; on arrive au texte de la sourate.
- Interdits respectés : aucun rayon, éclat ou présence censés représenter la révélation.
- Remplace : l'étoile à huit branches.

### S05 · 32,60-36,60 · La clarté de la matinée
« La sourate commence par deux moments que l'on connaît. La clarté de la matinée, »
- On voit : la chambre, sans personne, au matin ; ciel pâle, ville, lumière du soleil sur le sol et le tapis.
  Mention « Sens des versets 93:1–2 » (garde la même place en S06).
- Action : la tache de soleil glisse lentement sur le sol, les nuages blancs dérivent.
- Caméra : plan large frontal, presque fixe, sur la fenêtre (cadrage de « carte postale » qui revient en S06).
- Transition : volet doux de la gauche vers la droite : le même cadre passe au soir puis à la nuit (S06).

### S06 · 36,60-38,70 · La nuit calme
« puis la nuit lorsqu'elle devient calme. »
- On voit : même cadre, nuit claire sans pluie, lune, quelques fenêtres allumées.
- Action : les derniers mouvements s'arrêtent (rideaux immobiles, lumières qui se stabilisent) : le calme s'installe.
- Caméra : le même cadre que S05, immobile (le parallèle des deux moments se lit par le cadre identique).
- Transition : fondu enchaîné vers le grand ciel de nuit et la composition de l'accusation (S07, révision 3).

### S07 · 38,70-45,40 · La réponse · **modifié**
- Phrases exactes : « Vient ensuite la réponse. » (38,8-40,4) · « Son Seigneur ne l'a ni abandonné ni détesté. »
  (40,4-43,4) · « Voilà ce que ces paroles viennent démentir. » (43,4-45,6)
- Action visible :
  1. S07a, « Vient ensuite la réponse » : retour de la composition de S03b (même place, ciel de nuit calme) :
     attribution + « Abandonné ».
  2. S07b, juste avant « Son Seigneur » (40,3 s) : le bloc de l'accusation s'efface entièrement ; la phrase de la réponse
     apparaît **en une fois, complète** (jamais mot par mot : aucune image ne montre « abandonné » sans sa négation),
     avec « Sens du verset 93:3 » au-dessus. Pas de sous-titre pendant cette phrase (même texte déjà à l'écran).
  3. S07c, « démentir » : la réponse remonte et pâlit ; l'accusation attribuée revient en petit, sous elle, et un trait
     doré la barre sur « démentir » (44,7 s). Mention « Explication » au-dessus du sous-titre.
- Le spectateur comprend : le verset dément l'accusation.
- Remplace : l'acacia au calme.

### S08 · 45,40-49,60 · L'explication · **modifié**
- Phrase exacte : « Le retard de la révélation ne signifiait pas qu'Allah avait rejeté Son Prophète. »
- Action visible : même ciel nocturne. « Un retard » apparaît sur « retard » (45,7 s) à gauche ; « un rejet » sur
  « rejeté » (48,3 s) à droite ; puis le signe ≠, tracé en or, se dessine entre les deux (48,8 s).
- Le spectateur comprend : le délai et le rejet sont deux choses distinctes.
- Texte à l'écran : « Un retard ≠ un rejet » ; mention « Explication ».
- Remplace : le trait dans le sable.

### S09a · 49,60-55,00 · L'avenir · **modifié**
- Phrases exactes : « Puis le passage se tourne vers l'avenir. » · « Pour lui, la vie dernière sera meilleure que la vie
  présente. »
- Action visible : décor discret, une crête de dune sombre au bas de l'image, ciel de nuit sans lueur d'aube. Sur
  « vie dernière » (52,7 s), « Vie présente » apparaît à gauche ; une flèche dorée se trace vers « Vie dernière » ;
  sur « meilleure » (53,4 s), « meilleure pour lui » s'inscrit sous « Vie dernière ».
- Le spectateur comprend : une promesse adressée au Prophète.
- Texte à l'écran : « Vie présente → Vie dernière · meilleure pour lui » ; mention « Sens du verset 93:4 ».
- Interdits respectés : le paysage n'est pas présenté comme l'au-delà (pas de lumière à l'horizon, le schéma n'est pas
  posé sur l'horizon, aucun chemin vers lui).
- Remplace : l'horizon ouvert au petit jour.

### S09b · 55,00-58,85 · La formulation du verset
« Son Seigneur lui accordera de ses bienfaits, jusqu'à ce qu'il soit satisfait. »
- On voit : composition sobre, bleu nuit texturé, étoile à huit branches très pâle ; la formulation au centre en
  Source Serif ivoire, mention « Sens du verset 93:5 » au-dessus, sans guillemets. Pas de sous-titre en double.
- Action : la phrase apparaît par groupes de mots au rythme de la voix (jamais lettre par lettre) ; un trait doré se
  trace sous « jusqu'à ce qu'il soit satisfait ». Aucune forme n'est donnée aux bienfaits promis (remplace la jarre).
- Caméra : fixe ; très légère respiration de l'ornement.
- Transition (révision 3) : la composition monte et pâlit sur « ce qui viendra » ; les arches de S10 apparaissent.

### S10 · 58,85-63,50 · Retour aux bienfaits passés · **modifié**
- Phrases exactes : « Mais la sourate ne parle pas seulement de ce qui viendra. » · « Elle lui rappelle aussi ce qu'il a
  déjà reçu. »
- Action visible : la composition du verset 5 (S09b) monte et pâlit sur « ce qui viendra » ; puis trois arches dorées
  s'ouvrent l'une après l'autre, chacune avec la miniature du plan qui suit : la porte du refuge (61,5 s), le parcours
  balisé (62,2 s), le panier des moyens de vivre (62,9 s). La caméra entre ensuite dans la première arche (raccord S11a).
- Le spectateur comprend : l'annonce concrète des trois rappels qui suivent.
- Remplace : l'étoile tournante.

### S11a · 63,50-65,40 · Un refuge · *illustration conservée*
« Orphelin, il a été accueilli. » — Action simple : la porte s'ouvre, la lumière gagne le sol. Mention « Sens du verset
93:6 ». Illustration pédagogique générique, pas une reconstitution ; aucun personnage.

### S11b · 65,40-70,65 · Une guidée · *illustration conservée*
« Il a reçu la guidée. Avant la révélation, il ne connaissait pas encore le livre qui allait lui être révélé. » — Action
simple : les bornes apparaissent une à une, le parcours devient lisible. « Sens du verset 93:7 », puis « Explication ».
Aucun livre ni écriture représentés ; aucun personnage.

### S11c · 70,65-72,80 · Des moyens de vivre · *illustration conservée (version animée retravaillée)*
« Démuni, il a été enrichi. » — Action simple : le contenu des paniers apparaît et monte au-dessus du bord. « Sens du
verset 93:8 ». L'image se réduit ensuite dans la troisième arche de S12.

### S12 · 72,80-83,10 · Synthèse · **modifié**
- Phrases exactes : « Trois rappels successifs. » · « Un refuge, une guidée, des moyens de vivre. » · « Après avoir
  répondu à l'accusation d'abandon et annoncé l'avenir, le passage rappelle ainsi les bienfaits du passé. »
- Action visible :
  1. Les trois mêmes arches qu'en S10, avec les mêmes miniatures (porte, parcours balisé, panier).
  2. S12a : chaque nom s'inscrit sous la bonne image, sur le mot entendu : « Refuge » (74,6 s), « Guidée » (75,5 s),
     « Moyens de vivre » (76,4 s). Pas de sous-titre pendant cette phrase : les noms à l'écran la disent déjà.
  3. S12b : les noms s'effacent ; trois mots seulement, sans ligne ni points : « Réponse » (78,0 s), « Avenir »
     (79,8 s), « Passé » (82,0 s), ce dernier en or et souligné, sous l'arche du panier ; les arches restent visibles.
- Le spectateur comprend : les trois bienfaits sont ceux du passé ; le passage suit l'ordre réponse, avenir, passé.
- Mention « Explication ». Aucun nouveau symbole abstrait.
- Transition : les arches s'effacent en traînées de pluie (raccord sur la vitre, S13).

### S13 · 83,10-92,55 · La pluie occupe l'attention · *décor conservé, action précisée*
- Phrases exactes : « Et nous, en méditant ces versets, nous pouvons examiner notre propre regard. » · « Quand une
  épreuve occupe toute la place, les soutiens et les bienfaits déjà reçus peuvent devenir difficiles à voir. »
- Action visible : plan serré derrière l'épaule ; la pluie occupe la vitre et l'attention ; la pièce est dans l'ombre.
- Le spectateur comprend : on revient à soi ; l'épreuve prend toute la place du regard.

### S14 · 92,55-98,65 · Ce qui était déjà là · *décor conservé, action précisée*
- Phrases exactes : « Les reconnaître ne veut pas dire que notre peine n'existe pas. » · « Cela permet de ne pas réduire
  toute notre vie à cette peine. »
- Action visible : le cadrage s'élargit lentement et révèle les éléments chaleureux déjà présents (lampe, tasse, livres,
  plante, tapis plié) ; la pluie reste visible sur la vitre.
- Le spectateur comprend : reconnaître ce qui est là n'efface pas la peine.

### S15 · 98,65-101,40 · Le matin · **modifié (la pluie reste visible)**
- Phrase exacte : « Aujourd'hui, de quel bienfait te souviens-tu ? »
- Action visible : le jour se lève, la lampe s'éteint ; une pluie légère reste visible sur la vitre (au lieu de
  disparaître) : le matin ne promet pas la fin immédiate de toute peine.
- Le spectateur comprend : une question adressée à lui, sans promesse que tout disparaît.
- Transition inchangée vers S16.

### S16 · 101,40-108,00 · Fin : la façade au matin
« Si cette vidéo t'a aidé à mieux comprendre ce passage, aime-la et partage-la. Abonne-toi pour les prochaines
explications ! »
- On voit : la façade de S01, au matin ; la fenêtre de la chambre, rideaux ouverts.
- Action : pictogrammes dorés (cœur, partage, cloche) au rythme de la voix ; titre discret « Ad-Duha · Comprendre les
  premiers versets » en haut, dans la zone sûre.
- Caméra : recul lent, puis arrêt ; image tenue après la fin de la voix.
- Fin : la voix va jusqu'au bout du fichier (≈ 107,4 s, sans silence final) : image tenue jusqu'à ~108,0 s sur le
  silence ajouté **après** le fichier (aucune modification de l'audio).

## Variété des images et des cadrages (contrôle, révision 3)
| Séq. | Décor | Ce que l'image raconte | Caméra |
|------|-------|------------------------|--------|
| S00-S01 | chambre, façade | solitude ; appel | recul, grue arrière |
| S02 | grand ciel, bulles vides | entrée dans le récit rapporté | sortie de la façade par le haut, descente vers l'horizon |
| S03a | grand ciel, deux repères | un délai sans durée | fixe, le ciel passe à la nuit |
| S03b | grand ciel, accusation attribuée | leur parole, pas un fait | légère poussée |
| S04 | grand ciel, titre dans un cadre | arrivée du texte | poussée vers le cadre, raccord fenêtre |
| S05-S06 | chambre vide | deux moments connus | frontal identique |
| S07 | même composition que S03b | le verset dément l'accusation | même cadre, puis léger recul |
| S08 | grand ciel, deux mots et un signe | délai ≠ rejet | glissement latéral lent |
| S09a | crête sombre, schéma | une promesse pour lui | légère montée |
| S09b | typographie | la formulation, sans image des bienfaits | fixe |
| S10 | trois arches | annonce des trois rappels | recul, puis entrée dans la première arche |
| S11a-c | seuil, nuit, natte | refuge, guidée, moyens de vivre | frontal, suivi, trois-quarts |
| S12 | trois arches nommées, trois mots | synthèse | léger recul |
| S13-S15 | chambre | regard sur sa propre épreuve | serré, élargissement, poussée |
| S16 | façade au matin | fin | recul final |
