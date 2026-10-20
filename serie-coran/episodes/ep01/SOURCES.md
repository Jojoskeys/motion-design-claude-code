# Épisode 1 : sources (lues le 2026-10-20)

Copie des extraits lus : `sources-brutes/ep01-extraits.json`. Tous les textes viennent de **miroirs GitHub** (les sites
d'origine sont bloqués dans cet environnement) : à relire sur la source d'origine avant publication.

## 1. Fichiers exacts lus et origine déclarée

| Contenu | URL exacte du miroir | Origine déclarée par le miroir |
|---|---|---|
| Arabe Hafs, sourate 49 | https://raw.githubusercontent.com/fawazahmed0/quran-api/1/editions/ara-quranuthmanihaf/49.json | qurancomplex.gov.sa, version 13, avec remplacement de 3 caractères par le mainteneur du miroir (voir § 4) |
| Arabe, 49:12 (édition retenue pour l'écran) | https://raw.githubusercontent.com/fawazahmed0/quran-api/1/editions/ara-qurankhaledhosn/49/12.json | https://github.com/khaledhosny/quran-data (README : « The text have not been formally reviewed ») |
| Hamidullah, sourate 49 | https://raw.githubusercontent.com/fawazahmed0/quran-api/1/editions/fra-muhammadhamidul/49.json | tanzil.net |
| Rachid Maach (comparaison) | https://raw.githubusercontent.com/fawazahmed0/quran-api/1/editions/fra-rashidmaash/49.json | quranenc.com/en/browse/french_rashid |
| Al-Mukhtasar FR, 49:11 et 49:12 | https://raw.githubusercontent.com/spa5k/tafsir_api/main/tafsir/french-mokhtasar/49/11.json et `.../49/12.json` | Markaz Tafsir (quranenc.com), via quran.com |
| Al-Muyassar AR, 49:12 | https://raw.githubusercontent.com/spa5k/tafsir_api/main/tafsir/ar-tafsir-muyassar/49/12.json | quran.com |
| As-Sa'di AR, 49:12 (lu, non cité) | https://raw.githubusercontent.com/spa5k/tafsir_api/main/tafsir/ar-tafseer-al-saddi/49/12.json | quran.com |
| Sahih Muslim AR et FR | https://raw.githubusercontent.com/fawazahmed0/hadith-api/1/editions/ara-muslim.json et `.../fra-muslim.json` | numérotation 'Abd al-Baqi ; traducteur français **non indiqué** par le miroir |
| Sahih Muslim 2589, page HadeethEnc (AR, traduction FR publiée, référence, commentaire) | https://hadeethenc.com/fr/browse/hadith/5326 | **Contenu fourni par l'utilisateur depuis la page d'origine** (non consulté par Claude, site injoignable ici) ; copie : `sources-brutes/ep01-hadeethenc-5326.txt` |

## 2. Tableau script ↔ sources

| # | Formulation du script | Source | Extrait justificatif |
|---|---|---|---|
| 1 | Accroche « Et si ce que je dis sur lui est vrai ? » (formulation éditoriale, sans guillemets) | Sahih Muslim 2589 (HadeethEnc 5326) | FR HadeethEnc : « Et qu’en est-il si cette caractéristique est présente en lui ? » ; AR : « أَفَرَأَيْتَ إِنْ كَانَ فِي أَخِي مَا أَقُولُ » |
| 2 | Hadith cité en entier, sans coupure | Sahih Muslim 2589, traduction publiée sur HadeethEnc (https://hadeethenc.com/fr/browse/hadith/5326), contenu fourni par l'utilisateur | « Savez-vous ce qu’est la médisance ? - Ils répondirent : Allah et Son Messager savent mieux ! - Il a dit : C'est que tu évoques ton frère en des termes qu’il répugnerait. » On demanda : « Et qu’en est-il si cette caractéristique est présente en lui ? - Il répondit : si ce que tu dis est présent en lui, tu auras alors médit à son sujet ; mais si ce n’est pas le cas, tu l'auras alors diffamé. » |
| 3 | Citation du verset (extrait annoncé) | Hamidullah 49:12 | « … et ne médisez pas les uns des autres. L'un de vous aimerait-il manger la chair de son frère mort? (Non!) vous en aurez horreur. Et craignez Allah. Car Allah est Grand Accueillant au repentir, Très Miséricordieux » |
| E1 | « Donc, si c'est vrai, c'est de la médisance. Si c'est faux, c'est de la diffamation. » (révision 5) | Sahih Muslim 2589, traduction HadeethEnc | « si ce que tu dis est présent en lui, tu auras alors médit à son sujet ; mais si ce n’est pas le cas, tu l'auras alors diffamé » |
| E2 | « Dans le Coran, sourate Al-Hujurat, verset douze : après le soupçon et l'espionnage, vient la médisance. » (révision 5) | Hamidullah 49:12 | « Evitez de trop conjecturer [sur autrui] car une partie des conjectures est péché. Et n'espionnez pas; et ne médisez pas les uns des autres » |
| E3 | « Selon le tafsir Al-Mukhtasar, on devrait ressentir la même répulsion devant la médisance. » (révision 5, paraphrase attribuée, sans l'image du cadavre) | Al-Mukhtasar 49:12 ; concordant : Al-Muyassar 49:12 | « ayez donc la même répulsion à l’égard de ces deux méfaits » ; « فأنتم تكرهون ذلك، فاكرهوا اغتيابه » |
| E4 | « Alors, avant de parler de quelqu'un, demande-toi : est-ce qu'il aimerait entendre ça ? » (illustration pédagogique, présentée comme une question à se poser, pas comme une règle) | Sahih Muslim 2589, traduction HadeethEnc | « C'est que tu évoques ton frère en des termes qu’il répugnerait. » |
| E5 | « Et si une parole t'a échappé, le verset se termine sur le repentir et la miséricorde. » (révision 5) | Hamidullah 49:12, fin | « Car Allah est Grand Accueillant au repentir, Très Miséricordieux » |
| Écran / description | Verset 11 (moquerie, dénigrement, surnoms) ; situations particulières | Hamidullah 49:11 ; commentaire HadeethEnc 5326, point 5 (résumé fourni par l'utilisateur) | voir lignes ci-dessus et `sources-brutes/ep01-hadeethenc-5326.txt` ; retirés de la voix off en révision 5 |

Retirés en révision 3 : la paraphrase d'Al-Mukhtasar (« dévorer le cadavre »), la section « La nuance » (aucune
source lue ne traite les cas où parler d'un absent serait permis ou nécessaire) et la citation d'Al-Mukhtasar en
conclusion. Al-Mukhtasar et Al-Muyassar restent utilisés seulement pour le cadrage (l'image porte sur la médisance).

Degré du hadith : affiché sur HadeethEnc « [Authentique] — [Rapporté par Muslim] — [Sahîh Muslim — 2589] » (contenu
fourni par l'utilisateur). Concorde avec la numérotation 2589 du miroir et son texte arabe (mêmes mots ; vocalisation
et ponctuation un peu différentes). La traduction anonyme du miroir n'est plus utilisée dans le script.

## 3. Lu mais volontairement non utilisé
- Al-Mukhtasar 49:11 : sobriquets « comme cela était le cas de certains Ansar » : aucune référence de hadith dans le
  texte lu → non vérifié, exclu.
- As-Sa'di 49:12 : la médisance comme « grand péché » (من الكبائر) : avis de l'auteur, non nécessaire à l'idée
  et contraire au ton non culpabilisant → non utilisé.
- Ibn Kathir (EN) 49:12 : autres hadiths (Abu Dawud, At-Tirmidhi) dont les verdicts n'ont pas été vérifiés → exclus.
- Cas où parler d'un absent est permis selon des savants : non présent dans les sources lues → non abordé (voir § 5).

## 4. Le texte arabe : anomalie dans le fichier, pas seulement à l'affichage
Analyse caractère par caractère de 49:12 dans `ara-quranuthmanihaf` :
- « كَثِيرࣰ ا » et « مَيۡتࣰ ا » contiennent un **vrai caractère espace (U+0020)** entre le tanwin ouvert (U+08F0) et
  l'alif (U+0627) : le mot est coupé en deux dans les données. Le verset compte 33 « mots » au lieu de 31.
- Le même motif touche 1 933 versets sur 6 236 dans ce fichier.
- Le miroir déclare avoir remplacé U+0657 → U+08F0, U+065E → U+08F1, U+0656 → U+08F2 ; l'espace vient
  probablement de ce traitement, mais je ne peux pas le confirmer sans le fichier officiel du Complexe du Roi Fahd.
- `ara-qurankhaledhosn` (identique à `ara-quranacademy`) : 31 mots, « كَثِیرࣰا » et « مَیۡتࣰا » sans espace. Il emploie
  le ya U+06CC et des signes coraniques spécifiques (U+06E4, U+06DF…) : leur rendu dépend de la police.

Choix proposé : afficher le texte de `ara-qurankhaledhosn` tel quel, sans retouche manuelle. Son auteur précise qu'il
n'est pas formellement révisé : une comparaison mot par mot avec un mushaf imprimé (rasm uthmani, lecture Hafs)
reste indispensable. Le rendu de la police sera contrôlé sur image fixe à l'étape C.

Extrait affiché (mots 14 à 31 de l'édition retenue) :
« وَلَا یَغۡتَب بَّعۡضُكُم بَعۡضًاۚ أَیُحِبُّ أَحَدُكُمۡ أَن یَأۡكُلَ لَحۡمَ أَخِیهِ مَیۡتࣰا فَكَرِهۡتُمُوهُۚ وَٱتَّقُوا۟ ٱللَّهَۚ إِنَّ ٱللَّهَ تَوَّابࣱ رَّحِیمࣱ »

## 5. Points à vérifier par un humain avant publication
1. Texte arabe de l'extrait : comparer mot par mot avec un mushaf imprimé.
2. Hamidullah : la version de tanzil.net peut différer d'autres éditions révisées. Vérifier sur l'édition que vous
   choisissez d'afficher (et son droit d'usage).
3. [Réglé en révision 4, voir § 6] Sahih Muslim 2589 : vérifier numéro et degré ; choisir une traduction française publiée et nommée (celle du
   miroir n'a pas de traducteur indiqué). Note : « les Compagnons » est un ajout de cette traduction, l'arabe dit
   « ils dirent ».
4. Formule « paix et salut sur lui » : choix de formulation à confirmer.
5. Des spectateurs demanderont s'il est permis de parler d'un absent pour avertir ou demander conseil : sujet non
   traité ici, possible épisode futur après recherche sourcée.

## 6. État des vérifications (révision 4, inchangé par la révision 5 de style)

**Vérifié** :
- Hadith, traduction FR : la citation du script est identique, caractère pour caractère, au texte HadeethEnc fourni par
  l'utilisateur (`sources-brutes/ep01-hadeethenc-5326.txt`), contrôle fait par script. Claude n'a pas consulté la page
  lui-même : la fidélité de la copie repose sur le contenu fourni.
- Hadith, référence et degré : « Authentique », Sahih Muslim 2589, tels qu'affichés sur HadeethEnc (contenu fourni).
- Hamidullah 49:12 et 49:11 : citations identiques aux extraits du miroir GitHub (`sources-brutes/ep01-extraits.json`).
  Une correspondance avec un miroir ne valide pas la source d'origine.

**Restant à vérifier** :
1. Passage coranique, traduction : relire l'extrait de 49:12 (et 49:11 pour le contexte) dans l'édition Hamidullah
   que vous afficherez (la version de tanzil.net peut différer d'autres éditions révisées) ; vérifier le droit d'usage.
2. Passage coranique, texte arabe affiché : comparer mot par mot avec un mushaf imprimé (rasm uthmani, Hafs) ; voir § 4.
3. Commentaire HadeethEnc, point 5 : le script ne s'appuie que sur le résumé fourni ; si vous voulez une attribution
   plus précise à l'écran, fournir le texte exact de ce point.
4. Formule « paix et salut sur lui » : à confirmer.
5. Droit d'usage de la traduction HadeethEnc dans une vidéo : à vérifier sur le site.
