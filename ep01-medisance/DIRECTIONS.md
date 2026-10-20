# {{TITRE_DU_FILM}} : trois directions de storyboard (à choisir avant d'écrire le storyboard complet)

<!--
Modèle de l'étape 4 de la méthode (premier prompt : « Propose-moi 3 directions de storyboard vraiment différentes pour
ce script, avec 3 images de style chacune »). Copie-le en <projet>/DIRECTIONS.md, remplace chaque {{...}}
(grep -n "{{" DIRECTIONS.md ne doit rien afficher), puis supprime ce commentaire.

- Lis d'abord patterns/STORYBOARD-CRAFT.md (les 10 lois) et patterns/PATTERNS.md (quoi montrer).
- Trois directions VRAIMENT différentes : trois lieux, trois façons de faire le pont entre les idées, pas trois
  habillages du même film. Même script, même voix, même minutage pour les trois (chaque musique ira avec chaque image).
- Une image de style = une image figée du futur film, en qualité finale (vraies interfaces, vraie typographie, vraie
  lumière), avec le mouvement suggéré dans l'image elle-même (flou de mouvement, flou de profondeur, élément qui arrive
  trop grand et flou). Une page HTML autonome de 1920 × 1080 par image, dans <projet>/styleframes/<A1 à C3>.html, rendue
  en PNG par : python3 .claude/skills/motion-design/scripts/render-styleframes.py <projet>
- Choisis les trois moments de chaque direction là où elle se joue : l'accroche, le cœur de la douleur, le retournement
  ou la preuve. Donne leur temps exact dans la voix.
- Montre les 9 images côte à côte, direction par direction, et attends le choix. Corriger une image coûte dix fois
  moins cher que corriger une vidéo.
Exemple rempli : examples/C-le-devis-v7a/DIRECTIONS.md.
-->

Même voix, même musique, mêmes bruitages pour les trois directions : l'horloge ne bouge pas, seule la mise en scène
change. Grammaire visée : `patterns/STORYBOARD-CRAFT.md` (un monde, une caméra qui s'y déplace, un objet-pont à chaque
transition, deux vitesses, un événement toutes les 0,5 à 1 s, rien d'immobile). Vraies interfaces, épurées et
actuelles : {{INTERFACES_ET_CAPTURES_DE_REFERENCE}}.

## Minutage global de la voix (secondes du film)

{{MOT TEMPS · MOT TEMPS · … (depuis onsets.json ; marque le pivot, par exemple [Stop. 14.02, musique coupée])}}

## A. « {{NOM_A}} » {{(recommandée)}}

**Concept.** {{En deux ou trois phrases : le lieu du film (le décor que la caméra parcourt), ce qu'il dit du message,
pourquoi il sert cette voix. Ce qui change entre le monde de la douleur et celui de la solution.}}

**Fil des objets-ponts.** {{Le parcours de la caméra et, à chaque idée de la voix, l'objet qui survit et change de rôle :
« mot ou temps : objet → nouveau rôle ». Par exemple : le prix arrive trop grand et se pose dans sa case ; la case
grandit et devient le téléphone ; le devis rétrécit en notification. Nomme les 1 ou 2 mécanismes signature qui
reviendront 4 à 8 fois, et la rime (le geste de la fin qui rejoue le début).}}

**Images de style à dessiner.**
- A1 ({{t}} s) : {{cadrage, sujet net, avant-plan flou, fond, lumière, ce qui est en mouvement, texte à l'écran}}
- A2 ({{t}} s) : {{…}}
- A3 ({{t}} s) : {{…}}

## B. « {{NOM_B}} »

**Concept.** {{…}}

**Fil des objets-ponts.** {{…}}

**Images de style à dessiner.**
- B1 ({{t}} s) : {{…}}
- B2 ({{t}} s) : {{…}}
- B3 ({{t}} s) : {{…}}

## C. « {{NOM_C}} »

**Concept.** {{…}}

**Fil des objets-ponts.** {{…}}

**Images de style à dessiner.**
- C1 ({{t}} s) : {{…}}
- C2 ({{t}} s) : {{…}}
- C3 ({{t}} s) : {{…}}

## Choix

Direction retenue : {{lettre}}, {{avec ses emprunts éventuels aux deux autres, par exemple un objet-pont de B}}.
Images de style de référence pour la charte et le storyboard : {{styleframes/A1.png, A2.png, A3.png}}.
