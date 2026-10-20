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

## 2. Tableau script ↔ sources

| # | Formulation du script | Source | Extrait justificatif |
|---|---|---|---|
| 1 | « Parler de quelqu'un qui n'est pas là » (la médisance concerne une personne absente) | Al-Muyassar 49:12 | « ولا يقل بعضكم في بعضٍ بظهر الغيب ما يكره » (que nul ne dise de l'autre, en son absence, ce qu'il déteste) |
| 2 | Citation du verset (extrait) | Hamidullah 49:12 | « … et ne médisez pas les uns des autres. L'un de vous aimerait-il manger la chair de son frère mort? (Non!) vous en aurez horreur. Et craignez Allah. Car Allah est Grand Accueillant au repentir, Très Miséricordieux » |
| 3 | « Le même verset demande aussi d'éviter de trop soupçonner et de ne pas espionner » | Hamidullah 49:12 | « Evitez de trop conjecturer [sur autrui] car une partie des conjectures est péché. Et n'espionnez pas » |
| 4 | « Le verset précédent interdit de se moquer, de dénigrer et de donner des surnoms blessants » | Hamidullah 49:11 | « Qu'un groupe ne se raille pas d'un autre groupe […] Ne vous dénigrez pas et ne vous lancez pas mutuellement des sobriquets (injurieux) » |
| 5 | Question, définition, réponse sur « et si c'est vrai ? » | Sahih Muslim n° 2589 (Livre de la vertu, des bonnes manières et des liens de parenté), Abu Hurayra | FR : « Savez-vous ce qu'est la médisance ? […] La médisance, c'est de parler de ton frère d'une manière qu'il n'aime pas. […] Si ce défaut est vraiment en lui, tu as médit de lui ; et s'il n'y est pas, tu l'as calomnié. » AR : « أَتَدْرُونَ مَا الْغِيبَةُ … ذِكْرُكَ أَخَاكَ بِمَا يَكْرَهُ … إِنْ كَانَ فِيهِ مَا تَقُولُ فَقَدِ اغْتَبْتَهُ وَإِنْ لَمْ يَكُنْ فِيهِ فَقَدْ بَهَتَّهُ » |
| 6 | « Pour le tafsir Al-Mukhtasar, médire revient à dévorer le cadavre de son frère : la même répulsion doit valoir pour les deux » (paraphrase attribuée) | Al-Mukhtasar 49:12 | « Médire de son frère revient en effet à dévorer son cadavre, ayez donc la même répulsion à l'égard de ces deux méfaits. » Concordant : Al-Muyassar « فأنتم تكرهون ذلك، فاكرهوا اغتيابه » |
| 7 | « Aimerait-il entendre ce que je vais dire ? Même si c'est vrai. » | Illustration pédagogique tirée du n° 5 (définition et cas « si c'est vrai ») | même extrait que n° 5 : à l'écran, étiquette « à retenir », pas « citation » |
| 8 | « Le verset se termine sur le repentir » | Hamidullah 49:12, fin ; Al-Mukhtasar 49:12 | « Allah accepte le repentir de Ses serviteurs et leur fait miséricorde. » |

Degré du hadith : rapporté par Muslim dans son Sahih. Le miroir ne donne aucun verdict propre à ce hadith (champ
« grades » vide) : à confirmer sur dorar.net ou sunnah.com (Sahih Muslim 2589).

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
3. Sahih Muslim 2589 : vérifier numéro et degré ; choisir une traduction française publiée et nommée (celle du
   miroir n'a pas de traducteur indiqué). Note : « les Compagnons » est un ajout de cette traduction, l'arabe dit
   « ils dirent ».
4. Formule « paix et salut sur lui » : choix de formulation à confirmer.
5. Des spectateurs demanderont s'il est permis de parler d'un absent pour avertir ou demander conseil : sujet non
   traité ici, possible épisode futur après recherche sourcée.
