# Épisode 1 : storyboard bref (9:16, 1080×1920)

Zone utile : x 60 → 920, y 220 → 1500 (hors interface TikTok, à confirmer sur aperçu). Sous-titres : bande y 1300 →
1460, 2 lignes max, ivoire sur bandeau bleu nuit. Fond bleu nuit uni avec un léger grain ; or réservé aux références et
au mot-clé de l'écran. Aucun personnage, aucune image de corps ou de nourriture : l'image du verset reste du texte.
Codes visuels constants : **citation coranique** = cadre fin doré + mention « Traduction du sens · Hamidullah » ;
**hadith** = filet vertical ivoire + « Sahih Muslim 2589 » ; **commentaire** = texte sans cadre + « Al-Mukhtasar » ;
**à retenir** = pastille dorée « À retenir ».

| # | Temps | Type | À l'écran | Mouvement |
|---|---|---|---|---|
| 1 | 0 – 7 s | explication | « Parler de quelqu'un qui n'est pas là… » en grand, centré | le texte apparaît par groupes de mots, sans effet sur les lettres |
| 2 | 7 – 12 s | citation | Référence « Al-Hujurat · 49:12 » + bandeau « Extrait du verset » | la référence se pose, le bandeau glisse sous elle |
| 3 | 12 – 30 s | citation | Arabe de l'extrait (2 à 3 lignes, coupures entre mots seulement) au-dessus, traduction Hamidullah en dessous, ajouts du traducteur entre parenthèses | fondu du bloc arabe entier, puis la traduction ligne à ligne au rythme de la voix |
| 4 | 30 – 41 s | schéma | Verset 12 en trois cases : « trop soupçonner » · « espionner » · « médire » ; une ligne au-dessus « v. 11 : se moquer · dénigrer · surnoms blessants » ; la case « médire » s'allume en or | les cases se posent l'une après l'autre ; la caméra resserre sur « médire » |
| 5 | 41 – 50 s | hadith | « Savez-vous ce qu'est la médisance ? » | la question seule, au centre, temps de silence |
| 6 | 50 – 64 s | hadith | Définition, puis schéma à deux branches : « c'est vrai → médisance » / « c'est faux → calomnie » | les deux branches partent d'un même point, l'une après l'autre |
| 7 | 64 – 72 s | commentaire | « Médire ⟷ l'image du verset : même répulsion » + « Al-Mukhtasar » | les deux termes se rapprochent, le signe ⟷ s'allume |
| 8 | 72 – 82 s | à retenir | « Aimerait-il entendre ce que je vais dire ? » puis « Même si c'est vrai. » | apparition simple, maintien long pour la lecture |
| 9 | 82 – 90 s | citation | « Allah est Grand Accueillant au repentir, Très Miséricordieux » + « Al-Hujurat · 49:12 » | fondu lent, fin sur la référence |

Son : voix seule. Bruitage éventuel : un seul son doux au plan 4 (case « médire »), à valider. Pas de musique.

## Étape C : maquettes fixes de style (2026-10-20)
`ep01-medisance/styleframes/` (version 2 du style, notes dans `NOTES.md`) : 01-accroche, 02-hadith, 03-coran (HTML + PNG 1080×1920, export Chromium local par
`build-styleframes.py`). Elles valident le style, pas l'exactitude du contenu : le texte arabe et la traduction de
49:12 sont des emplacements réservés tant que leur vérification reste ouverte. L'extrait du hadith est copié par script
depuis `sources-brutes/ep01-hadeethenc-5326.txt`. Polices : Source Serif 4 et Inter (SIL OFL 1.1, paquets npm
@fontsource 5.1.0, licences dans `ep01-medisance/assets/fonts/`).
