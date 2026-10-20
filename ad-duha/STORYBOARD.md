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

## Écarts de l'animation par rapport aux vignettes (2026-10-20)
Le storyboard révision 2 reste la base ; l'animation (`index.html`) y apporte seulement ceci :
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
- **Un décor = une idée** (révision 2, pour éviter la répétition de la vallée et du chemin) :
  la vallée n'apparaît qu'une fois (S02, le contexte) ; un grand ciel à horizon bas porte l'attente (S03a) ;
  un acacia isolé porte le couple accusation / réponse (S03b dans le vent, S07 au calme : même arbre, action inverse) ;
  un tracé dans le sable porte l'idée de continuité (S08) ; un horizon ouvert sans chemin porte l'avenir (S09a) ;
  l'étoile à huit branches porte la structure du texte (S04 cadre, S10 retour vers le passé, S12 triptyque).
- **La façade** : appel à s'abonner la nuit (S01), carte de fin au matin (S16).
- Aucune figure humaine hors de la personne contemporaine anonyme de la chambre. Ciel, arbre, maison, bornes, paniers
  sont des **illustrations pédagogiques génériques** : aucune ne prétend reconstituer un lieu, un objet ou un événement
  historique, ni une durée.

## Mentions à l'écran (révision 2)
- Paraphrases des versets : mention discrète au-dessus du sous-titre, Inter capitales dorées 22 px :
  « Sens des versets 93:1–2 », « Sens du verset 93:3 »… Aucun guillemet autour d'une reformulation libre.
- Explications : mention « Explication » quand la phrase pourrait être prise pour le texte (S08, S11b 2e phrase,
  S12, S07 2e phrase).
- Référence courte autorisée : « Ṣaḥīḥ Muslim 1797a » en S03a (référence communiquée par l'utilisateur, voir REPRISE).
- Numéros de versets, traductions et références complètes : à confirmer avant rendu (liste dans `REPRISE.md`).

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
- Transition : la caméra bascule vers le haut, le relief sort du cadre, il ne reste que le ciel (S03a).
- Seule apparition de la vallée et de son chemin dans le film.

### S03a · 21,25-26,40 · L'attente : un grand ciel
« Dans un récit rapporté par [Muslim], [Jundub] raconte que Gabriel tarde à venir auprès du Prophète. »
- On voit : un très grand ciel au-dessus d'un horizon bas et sombre ; nuages étirés. Mention discrète
  « Ṣaḥīḥ Muslim 1797a ».
- Action : le ciel passe **une seule fois**, lentement, du crépuscule à la nuit ; les nuages dérivent, quelques étoiles
  apparaissent. Ni soleils ni lunes successifs, ni accéléré : l'image dit l'attente sans compter de jours ni suggérer de
  durée. Aucune représentation de Gabriel ni du Prophète ; aucune lumière surnaturelle.
- Caméra : plan fixe, horizon très bas (le ciel occupe presque tout le cadre).
- Transition : un souffle de vent fait entrer du sable par la gauche ; coupe sur l'acacia (S03b).

### S03b · 26,40-29,25 · L'acacia dans le vent
« Les polythéistes affirment alors qu'il a été abandonné. »
- On voit : un acacia isolé, cadré de près et en légère contre-plongée, ciel ocre.
- Action : le vent se lève ; le sable file en rubans, l'arbre plie, quelques feuilles s'arrachent : les paroles qui
  circulent et pèsent. Aucun personnage, aucune scène reconstituée.
- Caméra : plan fixe légèrement secoué par les rafales.
- Transition : une rafale emplit l'image de sable ; quand elle retombe, on est revenu au grand ciel apaisé (S04).

### S04 · 29,25-32,60 · Le cadre se referme
« C'est dans ce contexte que sont révélés les premiers versets d'[Ad-Duha]. »
- On voit : le grand ciel de S03a, nocturne et calme, vu à travers une étoile à huit branches tracée en or discret ;
  titre « Ad-Duha ».
- Action : les branches de l'étoile se dessinent et cadrent le ciel : on « entre » dans le texte. La révélation
  n'est pas illustrée (ni rayon, ni éclat).
- Caméra : poussée lente dans l'ouverture de l'étoile.
- Transition : **raccord de forme** : le contour de l'étoile s'ouvre et devient le cadre de la fenêtre de la chambre (S05).

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
- Transition : fondu enchaîné vers l'acacia de S03b, au calme (S07).

### S07 · 38,70-45,40 · L'acacia au calme
« Vient ensuite la réponse. Son Seigneur ne l'a ni abandonné, ni détesté. Voilà ce que ces paroles viennent démentir. »
- On voit : le même acacia qu'en S03b, même cadre, au crépuscule clair ; sable lisse, premières étoiles.
  Mention « Sens du verset 93:3 » sur la deuxième phrase, « Explication » sur la troisième.
- Action : l'inverse exact de S03b : le vent tombe, l'arbre se redresse, le sable retombe en rides régulières.
  La réponse se lit par contraste avec l'image de l'accusation, sans rien ajouter au récit.
- Caméra : même cadre que S03b, désormais immobile (le contraste vient de l'action, pas du cadrage).
- Transition : la caméra descend le long du tronc jusqu'au sable et passe en plongée verticale (S08).

### S08 · 45,40-49,60 · L'intervalle n'est pas une rupture
« Le retard de la révélation ne signifiait pas qu'Allah avait rejeté son prophète. »
- On voit : vue de dessus, sable ; un trait tracé, qui s'efface sur une portion puis reprend. Mention « Explication ».
  Rien de dénombrable (ni pierres, ni marques de jours) : la longueur de l'interruption n'a aucune valeur de durée.
- Action : un fin trait doré repasse dans la portion effacée et relie les deux parties : c'est le même tracé.
- Caméra : plongée verticale, glissement le long du trait.
- Transition : la caméra se redresse et découvre un horizon (S09a).

### S09a · 49,60-55,00 · L'horizon ouvert
« Puis le passage se tourne vers l'avenir. Pour lui, la vie dernière sera meilleure que la vie présente. »
- On voit : la crête d'une dune dans l'ombre au premier plan, puis une plaine et un horizon très ouvert au petit jour ;
  ni chemin, ni disque solaire, rien « au bout ». Mention « Sens du verset 93:4 ».
- Action : la lumière naturelle gagne la crête ; on ne montre aucune image de l'au-delà ni du Paradis.
- Caméra : panoramique vertical lent de la crête vers le ciel (seul mouvement de bascule du film).
- Transition : le ciel se fond dans le bleu nuit de la composition suivante (S09b).

### S09b · 55,00-58,85 · La formulation du verset
« Son Seigneur lui accordera de ses bienfaits, jusqu'à ce qu'il soit satisfait. »
- On voit : composition sobre, bleu nuit texturé, étoile à huit branches très pâle ; la formulation au centre en
  Source Serif ivoire, mention « Sens du verset 93:5 » au-dessus, sans guillemets. Pas de sous-titre en double.
- Action : la phrase apparaît par groupes de mots au rythme de la voix (jamais lettre par lettre) ; un trait doré se
  trace sous « jusqu'à ce qu'il soit satisfait ». Aucune forme n'est donnée aux bienfaits promis (remplace la jarre).
- Caméra : fixe ; très légère respiration de l'ornement.
- Transition : l'étoile pâle se rapproche et devient le schéma de S10.

### S10 · 58,85-63,50 · L'étoile se tourne vers le passé
« Mais la sourate ne parle pas seulement de ce qui viendra. Elle lui rappelle aussi ce qu'il a déjà reçu. »
- On voit : l'étoile à huit branches en schéma ; une flèche courbe dans le sens inverse des aiguilles d'une montre.
- Action : sur « ne parle pas seulement de ce qui viendra », l'étoile tourne en arrière ; sur « ce qu'il a déjà reçu »,
  trois branches s'allument l'une après l'autre (les trois rappels qui suivent).
- Caméra : fixe, légère poussée vers la première branche allumée.
- Transition : la branche allumée s'ouvre comme une porte : raccord sur S11a.

### S11a · 63,50-65,40 · Un refuge
« Orphelin, il a été accueilli. »
- On voit : un mur de terre, une porte simple au crépuscule. Mention « Sens du verset 93:6 ».
- Action : la porte s'ouvre ; la lumière chaude d'une lampe intérieure s'étend sur le sol. Aucun enfant, aucun adulte
  représenté ; la maison est générique et ne prétend pas être une maison historique.
- Caméra : plan fixe frontal, légère poussée vers le seuil.
- Transition : la lumière de la porte se resserre en point ; raccord sur la nuit étoilée (S11b).

### S11b · 65,40-70,65 · Une guidée
« Il a reçu la guidée. Avant la révélation, il ne connaissait pas encore le livre qui allait lui être révélé. »
- On voit : désert de nuit, ciel étoilé, une suite de bornes de pierre. Mention « Sens du verset 93:7 », puis
  « Explication » sur « Avant la révélation… ».
- Action : les bornes se découvrent une à une dans la lumière des étoiles et tracent la route. Aucun livre ni écriture
  représentés.
- Caméra : travelling qui suit les bornes en zigzag (rythme régulier, à la voix).
- Transition : fondu vers l'intérieur chaud (S11c).

### S11c · 70,65-72,80 · Des moyens de vivre
« Démuni, il a été enrichi. »
- On voit : une natte et des paniers tressés, vides au départ. Mention « Sens du verset 93:8 ».
- Action : les paniers se remplissent de dattes et de grain.
- Caméra : plongée en trois-quarts, très légère rotation.
- Transition : l'image se réduit et prend place dans la troisième arche du triptyque (S12).
- À retravailler à l'animation : les paniers vus de dessus se lisent mal (ajouter le bord tressé, un angle plus bas).

### S12 · 72,80-83,10 · Triptyque et frise
« Trois rappels successifs. Un refuge, une guidée, des moyens de vivre. Après avoir répondu à l'accusation d'abandon
et annoncé l'avenir, le passage rappelle ainsi les bienfaits du passé. »
- On voit : trois arches dorées contenant en miniature la porte (S11a), les bornes (S11b), le panier (S11c) ; dessous,
  une frise courte réponse · avenir · passé. Mention « Explication ».
- Action : les arches s'allument une à une sur « un refuge, une guidée, des moyens de vivre » ; puis les trois points de
  la frise s'allument dans l'ordre de la phrase, le dernier (« passé ») reste souligné.
- Caméra : léger recul pour tout cadrer, puis immobile.
- Transition : les arches s'effacent en traînées de pluie : raccord sur la vitre (S13).

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

## Variété des images et des cadrages (contrôle, révision 2)
| Séq. | Décor | Ce que l'image raconte | Caméra |
|------|-------|------------------------|--------|
| S00-S01 | chambre, façade | solitude ; appel | recul, grue arrière |
| S02 | vallée (unique) | le contexte, les échos | descente |
| S03a | grand ciel | l'attente, sans durée | fixe, horizon bas |
| S03b | acacia | les paroles qui pèsent | fixe secoué |
| S04 | étoile + ciel | entrée dans le texte | poussée |
| S05-S06 | chambre vide | deux moments connus | frontal identique |
| S07 | acacia | la réponse (inverse de S03b) | même cadre, immobile |
| S08 | sable vu de dessus | l'interruption n'est pas une rupture | plongée verticale |
| S09a | horizon | l'avenir | bascule verticale |
| S09b | typographie | la formulation, sans image des bienfaits | fixe |
| S10 | étoile-schéma | retour vers ce qui est déjà reçu | fixe, poussée |
| S11a-c | seuil, nuit, natte | refuge, guidée, moyens de vivre | frontal, suivi, trois-quarts |
| S12 | triptyque, frise | la structure du passage | recul |
| S13-S15 | chambre | regard sur sa propre épreuve | serré, recul, poussée |
| S16 | façade au matin | fin | recul final |
