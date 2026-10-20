# Ad-Duha · storyboard illustré (suite de l'introduction validée)

Document de préparation : rien de ce qui suit (minutage, notes, sources, réserves) n'apparaît à l'image.

- Audio unique : `assets/audio/Dhuha.mp3` (107,47 s), jamais modifié. Minutage mesuré sur ce fichier : transcription
  locale mot à mot (`transcription/dhuha-mots.json`) recoupée avec la détection des silences (-45 dB). Chaque coupe
  tombe dans un silence ; aucune phrase n'est coupée.
- Narration : **transcription automatique**, recopiée telle qu'entendue ; seuls les noms propres mal reconnus sont
  rétablis entre crochets (« [Ad-Duha] », « [Muslim] », « [Jundub] »), à confirmer à l'écoute. Narration inchangée.
- Vignettes : `storyboard/frames/<id>.jpg` (540×960) ; planches : `storyboard/planche-1.jpg` à `planche-3.jpg`.
  Régénération : `node ad-duha/storyboard/build-storyboard.cjs` (depuis la racine du dépôt).
- Les vignettes montrent un instant représentatif ; le sous-titre y est indicatif (position et police du prototype).

## Fils de continuité
- **La chambre** (décor validé) ouvre, sert de pivot au milieu (S05-S06 : « deux moments que l'on connaît ») et
  ferme le film (S13-S15). Elle passe de la nuit pluvieuse à la nuit calme puis au matin : la lumière change pour
  des raisons naturelles (pluie, nuages, aube), jamais surnaturelles.
- **Le chemin** : apparaît dans la vallée (S02), est recouvert par la poussière (S03b), dégagé (S07), parcouru vers
  l'horizon (S09a), regardé en arrière (S10), vu d'en haut comme schéma (S12).
- **La façade** : appel à s'abonner la nuit (S01), carte de fin au matin (S16).
- Aucune figure humaine hors de la personne contemporaine anonyme de la chambre. La vallée, la maison, les paniers sont
  des **illustrations pédagogiques génériques** : aucune ne prétend reconstituer un lieu, un objet ou un événement historique.

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

### S02 · 13,45-21,25 · La vallée au crépuscule
« La sourate [Ad-Duha] s'adresse d'abord au Prophète, paix et salut sur lui. Pour en comprendre les premiers versets,
il faut revenir à ce qui se disait autour de lui. »
- On voit : une vallée aride générique, montagnes en plans successifs, rochers, un chemin clair. Personne.
- Action : sur « ce qui se disait », de fines lignes de vent ivoire traversent la vallée, comme des échos.
- Caméra : descente lente (grue avant) du ciel vers le chemin.
- Transition : coupe franche sur le même cadre, fixe (S03a).

### S03a · 21,25-26,40 · Les jours passent
« Dans un récit rapporté par [Muslim], [Jundub] raconte que Gabriel tarde à venir auprès du Prophète. »
- On voit : la même vallée, cadre fixe.
- Action : accéléré ; soleils et lunes se succèdent sur un arc pointillé, les ombres des rochers tournent : le temps
  passe. Aucune représentation de Gabriel ni du Prophète ; aucune lumière surnaturelle.
- Caméra : plan fixe (contraste avec les mouvements précédents).
- Transition : le vent se lève dans le même cadre (S03b).

### S03b · 26,40-29,25 · Le vent et la poussière
« Les polythéistes affirment alors qu'il a été abandonné. »
- On voit : la vallée envahie de rubans de poussière ocre ; le ciel se trouble.
- Action : la poussière recouvre peu à peu le chemin (les paroles qui circulent). Aucun personnage.
- Caméra : léger travelling latéral, comme poussé par le vent.
- Transition : la poussière retombe ; un cadre géométrique se referme sur l'image (S04).

### S04 · 29,25-32,60 · Le cadre se referme
« C'est dans ce contexte que sont révélés les premiers versets d'[Ad-Duha]. »
- On voit : la vallée apaisée, vue à travers une étoile à huit branches tracée en or discret ; titre « Ad-Duha ».
- Action : les branches de l'étoile se dessinent et cadrent la vallée : on « entre » dans le texte. La révélation
  n'est pas illustrée (ni rayon, ni éclat).
- Caméra : poussée lente dans l'ouverture de l'étoile.
- Transition : **raccord de forme** : le contour de l'étoile s'ouvre et devient le cadre de la fenêtre de la chambre (S05).

### S05 · 32,60-36,60 · La clarté de la matinée
« La sourate commence par deux moments que l'on connaît. La clarté de la matinée, »
- On voit : la chambre, sans personne, au matin ; ciel pâle, ville, lumière du soleil sur le sol et le tapis.
- Action : la tache de soleil glisse lentement sur le sol, les nuages blancs dérivent.
- Caméra : plan large frontal, presque fixe, sur la fenêtre (cadrage de « carte postale » qui revient en S06).
- Transition : volet doux de la gauche vers la droite : le même cadre passe au soir puis à la nuit (S06).

### S06 · 36,60-38,70 · La nuit calme
« puis la nuit lorsqu'elle devient calme. »
- On voit : même cadre, nuit claire sans pluie, lune, quelques fenêtres allumées.
- Action : les derniers mouvements s'arrêtent (rideaux immobiles, lumières qui se stabilisent) : le calme s'installe.
- Caméra : le même cadre que S05, immobile (le parallèle des deux moments se lit par le cadre identique).
- Transition : fondu enchaîné vers la vallée, de nuit à crépuscule clair (S07).

### S07 · 38,70-45,40 · Le vent retombe
« Vient ensuite la réponse. Son Seigneur ne l'a ni abandonné, ni détesté. Voilà ce que ces paroles viennent démentir. »
- On voit : la vallée de S03b, le chemin à nouveau dégagé.
- Action : les rubans de poussière de S03b retombent au sol et se dispersent ; le chemin réapparaît net, il ne s'est
  jamais interrompu.
- Caméra : contre-plongée basse au ras du chemin, poussée avant (cadrage nouveau, plus proche du sol).
- Transition : la caméra bascule vers le sol et passe en plongée verticale (S08).

### S08 · 45,40-49,60 · L'intervalle n'est pas une rupture
« Le retard de la révélation ne signifiait pas qu'Allah avait rejeté son prophète. »
- On voit : vue de dessus, sable ; une ligne de pierres (les jours) avec un intervalle ; un trait tracé dans le sable.
- Action : le trait continue à travers l'intervalle et relie les deux séries de pierres : l'attente reste sur le même
  chemin. Schéma pédagogique, sans texte.
- Caméra : plongée verticale, glissement le long du trait.
- Transition : la caméra se redresse et se retrouve face à l'horizon (S09a).

### S09a · 49,60-55,00 · Vers l'horizon
« Puis le passage se tourne vers l'avenir. Pour lui, la vie dernière sera meilleure que la vie présente. »
- On voit : un chemin sinueux entre des dunes, soleil bas naturel à l'horizon, décalé du chemin.
- Action : le chemin se dévoile en avançant ; rien n'y est montré « au bout » (pas d'image de l'au-delà ni du Paradis).
- Caméra : travelling avant, à hauteur d'épaule, le long du chemin.
- Transition : coupe sur un détail en gros plan (S09b).

### S09b · 55,00-58,85 · La jarre se remplit
« Son Seigneur lui accordera de ses bienfaits, jusqu'à ce qu'il soit satisfait. »
- On voit : une jarre de terre cuite sous une rigole de pierre.
- Action : l'eau coule et remplit la jarre jusqu'au bord, puis le filet s'arrête (image pédagogique du don « jusqu'à »
  satisfaction ; pas de jardin, pas de rivière).
- Caméra : gros plan de profil, légère montée qui suit le niveau de l'eau.
- Transition : coupe vers le chemin, la caméra fait demi-tour (S10).

### S10 · 58,85-63,50 · Demi-tour : trois cairns
« Mais la sourate ne parle pas seulement de ce qui viendra. Elle lui rappelle aussi ce qu'il a déjà reçu. »
- On voit : le chemin déjà parcouru, lumière de fin d'après-midi, trois cairns le long du bord.
- Action : les trois cairns se révèlent l'un après l'autre (du plus proche au plus lointain).
- Caméra : panoramique filé de 180° (le seul de la vidéo), puis stabilisation sur le chemin derrière.
- Transition : poussée vers le premier cairn, qui laisse place à la porte (S11a).

### S11a · 63,50-65,40 · Un refuge
« Orphelin, il a été accueilli. »
- On voit : un mur de terre, une porte simple au crépuscule.
- Action : la porte s'ouvre ; la lumière chaude d'une lampe intérieure s'étend sur le sol. Aucun enfant, aucun adulte
  représenté ; la maison est générique et ne prétend pas être une maison historique.
- Caméra : plan fixe frontal, légère poussée vers le seuil.
- Transition : la lumière de la porte se resserre en point ; raccord sur la nuit étoilée (S11b).

### S11b · 65,40-70,65 · Une guidée
« Il a reçu la guidée. Avant la révélation, il ne connaissait pas encore le livre qui allait lui être révélé. »
- On voit : désert de nuit, ciel étoilé, une suite de bornes de pierre.
- Action : les bornes se découvrent une à une dans la lumière des étoiles et tracent la route. Aucun livre ni écriture
  représentés.
- Caméra : travelling qui suit les bornes en zigzag (rythme régulier, à la voix).
- Transition : fondu vers l'intérieur chaud (S11c).

### S11c · 70,65-72,80 · Des moyens de vivre
« Démuni, il a été enrichi. »
- On voit : une natte et des paniers tressés, vides au départ.
- Action : les paniers se remplissent de dattes et de grain.
- Caméra : plongée en trois-quarts, très légère rotation.
- Transition : la caméra s'élève et les trois images se rangent sur le chemin vu d'en haut (S12).
- À retravailler à l'animation : les paniers vus de dessus se lisent mal (ajouter le bord tressé, un angle plus bas).

### S12 · 72,80-83,10 · Le chemin vu d'en haut
« Trois rappels successifs. Un refuge, une guidée, des moyens de vivre. Après avoir répondu à l'accusation d'abandon
et annoncé l'avenir, le passage rappelle ainsi les bienfaits du passé. »
- On voit : schéma pédagogique au sol : le chemin vu de dessus, trois cairns gravés (porte, borne, panier), un point
  « réponse », une flèche « avenir ». Mots courts : passé / réponse / avenir.
- Action : sur « un refuge, une guidée, des moyens de vivre », chaque cairn s'allume ; puis le point « réponse » et la
  flèche « avenir » se tracent ; enfin le passé est souligné à nouveau sur « bienfaits du passé ».
- Caméra : grue montante jusqu'à la vue verticale, puis léger recul pour tout voir.
- Transition : le dessin du chemin s'efface en traînées de pluie : raccord sur la vitre (S13).

### S13 · 83,10-92,55 · La pluie occupe tout
« Et nous, en méditant [ces] versets, nous pouvons examiner notre propre regard. Quand une épreuve occupe toute la
place, les soutiens et les bienfaits déjà reçus peuvent devenir difficiles à voir. »
- On voit : retour dans la chambre, la personne de dos, la pluie forte sur la vitre.
- Action : sur « occupe toute la place », la pluie gagne toute la vitre ; les objets de la pièce (tasse, livres,
  plante, cadre, tapis plié) s'enfoncent dans l'ombre.
- Caméra : plan serré derrière l'épaule (cadrage de S00 à 4,4 s), mise au point sur la vitre, le reste flou.
- Transition : la mise au point bascule de la vitre vers l'intérieur de la pièce (S14).

### S14 · 92,55-98,65 · Ce qui était déjà là
« Les reconnaître ne veut pas dire que notre peine n'existe pas. Cela permet de ne pas réduire toute notre vie à cette
peine. »
- On voit : la chambre ; la pluie diminue sans disparaître, l'horizon s'éclaircit (aube naturelle).
- Action : les objets réapparaissent un à un dans la lumière chaude de la lampe ; la pluie reste visible sur la vitre
  (la peine n'est pas niée).
- Caméra : recul lent jusqu'au plan large, qui fait entrer toute la pièce dans le cadre.
- Transition : fondu lumineux naturel vers le matin, même cadre (S15).

### S15 · 98,65-101,40 · Le matin
« Aujourd'hui, de quel bienfait te souviens-tu ? »
- On voit : la chambre au matin, ciel pâle, la personne toujours de dos.
- Action : la lampe s'éteint parce que le jour suffit ; le soleil gagne le tapis.
- Caméra : légère poussée vers la fenêtre (écho inverse du recul de S00).
- Transition : la caméra traverse la fenêtre et recule hors de l'immeuble (S16, reprise de S01 au matin).

### S16 · 101,40-108,00 · Fin : la façade au matin
« Si cette vidéo t'a aidé à mieux comprendre ce passage, aime-la et partage-la. Abonne-toi pour les prochaines
explications ! »
- On voit : la façade de S01, au matin ; la fenêtre de la chambre, rideaux ouverts.
- Action : pictogrammes dorés (cœur, partage, cloche) au rythme de la voix ; titre discret « Ad-Duha · Comprendre les
  premiers versets » en haut, dans la zone sûre.
- Caméra : recul lent, puis arrêt ; image tenue après la fin de la voix.
- Fin : la voix va jusqu'au bout du fichier (≈ 107,4 s, sans silence final) : image tenue jusqu'à ~108,0 s sur le
  silence ajouté **après** le fichier (aucune modification de l'audio).

## Variété des cadrages (contrôle)
Recul et grue (S00-S01), descente (S02), plan fixe accéléré (S03a), travelling latéral (S03b), raccord de forme
(S04→S05), plan frontal répété volontairement (S05-S06), contre-plongée au sol (S07), plongée verticale (S08),
travelling avant (S09a), gros plan de profil (S09b), panoramique filé (S10), plan frontal sur un seuil (S11a),
suivi en zigzag (S11b), trois-quarts plongeant (S11c), grue montante (S12), plan serré avec bascule de point (S13),
recul (S14), poussée (S15), recul final (S16).
