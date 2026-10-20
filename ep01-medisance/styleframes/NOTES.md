# Maquettes fixes ep01 : notes (version 2 du style)

Maquettes de **style** : elles ne valident pas l'exactitude du contenu. Script inchangé (révision 6, `serie-coran/episodes/ep01/SCRIPT.md`).
Export : `python3 -I ep01-medisance/styleframes/build-styleframes.py` depuis la racine (Chromium local, sans réseau).

## Motif commun
- **Le fil de la parole** : ligne dorée en pointillé, partant d'un nœud (petit disque doré), qui relie des bulles
  abstraites (contours ivoire, trois points). Accroche : la parole passe de bulle en bulle et pâlit (la dernière est
  en pointillé), puis aboutit au filet sous « vrai ? ». Hadith : le fil part d'une petite bulle et entre dans la grande
  bulle qui porte la citation. Coran : le fil arrive sur l'étoile centrale du séparateur, entre arabe et traduction.
- **L'étoile à huit branches** (deux carrés superposés, au trait) : trame très discrète en fond (opacité 8-9 %,
  fondue), ornement ponctuel (fin du filet, coin de bulle, angles du cadre, séparateur).
- Pas de particules, pas de halo ; un seul dégradé radial très doux sur le fond. Aucune figure humaine, aucune scène
  historique, aucune illustration de la comparaison du verset.
- Pistes pour l'animation (non réalisées, à valider) : le fil se trace, les bulles apparaissent l'une après l'autre,
  les étoiles de la trame restent fixes ; le même fil assure les transitions d'un écran à l'autre.

## Emplacements réservés (maquette 3)
Consignes retirées du visuel :
- **Texte arabe** : à copier par script depuis la source vérifiée (comparaison mot par mot avec un mushaf imprimé,
  rasm uthmani, lecture Hafs) ; jamais retapé ni corrigé à la main ; police coranique adaptée à choisir (rendu à
  contrôler sur image fixe) ; RTL ; jamais fragmenté, déformé ou animé lettre par lettre.
- **Traduction** : extrait de 49:12 à relire sur l'édition Hamidullah retenue (et son droit d'usage) avant affichage.
- Les barres pâles indiquent seulement l'encombrement prévu (2 lignes d'arabe, 4 lignes de traduction).

## Hadith (maquette 2)
Extrait copié par script depuis `serie-coran/episodes/ep01/sources-brutes/ep01-hadeethenc-5326.txt` ; « […] »
signale la coupure. Apostrophes mixtes (' et ’) conservées telles qu'elles figurent dans la traduction HadeethEnc.

## Zone sûre
Contenu entre 220 px (haut) et 1500 px (bas), à gauche de 920 px. La mention « Maquette n/3 » est dans la bande haute
couverte par l'interface et disparaîtra de la version finale.
