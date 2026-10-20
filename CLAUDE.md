# Série TikTok « Comprendre le Coran » : règles permanentes

Ce fichier complète `AGENTS.md` (garde-fous HyperFrames, toujours valables). Pour cette série, il remplace le format
16:9 « lancement produit » du skill `motion-design` : on réutilise ses outils, pas son ton publicitaire.

## Format
- Vertical 9:16, 1080×1920, 30 i/s, MP4, ~90 s. Une idée principale par épisode, une idée par écran.
- Voix off française posée, enregistrée par l'utilisateur (ElevenLabs web ou micro). Pas de musique. Bruitages rares.
- Aucune récitation coranique synthétique. Récitation seulement si l'enregistrement est identifié, autorisé, à vitesse
  d'origine. Sinon : lecture française annoncée comme « traduction du sens ».
- Sous-titres FR courts, 2 lignes max. Zone sûre TikTok (valeurs indicatives, à contrôler sur un aperçu réel) : rien d'essentiel dans les 220 px du haut, les 420 px du bas,
  ni les 160 px de droite.

## Fidélité religieuse (non négociable)
- Toujours séparer à l'écran et dans le script : texte arabe / traduction du sens (traducteur nommé) / explication
  (tafsir nommé) / illustration pédagogique.
- Chaque explication du script a une source précise et un court extrait dans `serie-coran/episodes/<ep>/SOURCES.md`.
- Rien de mémoire : aucune référence, citation, URL, circonstance de révélation, récit ou promesse non vérifiés.
  Si c'est invérifiable : retirer du script et le noter.
- Hadith : recueil, numéro, degré d'authenticité et qui l'établit ; sinon l'écarter.
- Ne jamais présenter une interprétation discutée comme un consensus, ni une paraphrase comme une citation.
- Une validation visuelle n'est jamais une validation religieuse. Texte validé = conservé mot pour mot.

## Visuel
- Bleu nuit, ivoire, or discret ; contrastes nets ; peu de halos ou de particules.
- Trois compositions : citation (arabe + traduction), explication (une phrase FR), schéma pédagogique.
- Ne pas représenter Allah, les prophètes, les anges, Satan, le paradis ni l'enfer. Typographie et formes abstraites.
- Arabe : texte vérifié, RTL, police coranique adaptée, jamais fragmenté, déformé ou animé lettre par lettre.
- Arabe toujours copié par script depuis le fichier source cité, jamais retapé ni « corrigé » à la main.

## Méthode et économie
- Étapes avec validation : A 3 sujets → B script + sources + storyboard → C 3 images fixes → D prototype 10-15 s →
  E vidéo complète et contrôles. Pas d'étape sautée, pas de sous-agent sans demande.
- Aperçus basse résolution pendant la conception ; rendu complet seulement après validation du prototype.
- Signaler tout service payant avant usage. Deux échecs identiques → s'arrêter et expliquer.

## Fichiers
- `serie-coran/SOURCES-OUTILS.md` : sources accessibles et limites. `serie-coran/HISTORIQUE.md` : sujets traités.
- `serie-coran/episodes/<ep>/` : sujets, script, sources, storyboard de l'épisode.
- Projet vidéo HyperFrames de l'épisode : dossier à la racine (`epNN-<slug>/`, créé par `new-project.sh`).
