"""Construit VOIX-OFF.txt (révision 7) : narration validée + citations copiées depuis les fichiers sources.
Usage, depuis la racine du dépôt : python3 -I serie-coran/episodes/ep01/build-voix-off.py
Aucune citation n'est tapée ici : {H1}..{H5} viennent de la traduction HadeethEnc, {V} de Hamidullah 49:12."""
import json, pathlib, re

D = pathlib.Path(__file__).parent
brut = (D / "sources-brutes/ep01-hadeethenc-5326.txt").read_text(encoding="utf-8")
trad = brut.split("TRADUCTION FRANÇAISE PUBLIÉE SUR HADEETHENC\n")[1].split("\n")[0]

def extrait(debut, fin):
    """Sous-chaîne exacte de la traduction HadeethEnc, de `debut` à `fin` inclus (une seule occurrence)."""
    i = trad.index(debut); j = trad.index(fin, i) + len(fin)
    assert trad.count(debut) == 1
    return trad[i:j]

H = {
    "H1": extrait("Savez-vous", "médisance ?"),
    "H2": extrait("Allah et Son", "mieux !"),
    "H3": extrait("C'est que tu", "répugnerait."),
    "H4": extrait("Et qu’en est-il", "en lui ?"),
    "H5": extrait("si ce que tu dis", "diffamé."),
}
v = json.loads((D / "sources-brutes/ep01-extraits.json").read_text(encoding="utf-8"))
V = v["coran_49_11_12"]["fra-muhammadhamidul"]["12"]
# Seule adaptation pour ElevenLabs : les crochets du traducteur « [sur autrui] » deviendraient une balise audio
# (le modèle v3 lit les crochets comme des indications de jeu) ; ils passent en parenthèses. Aucun mot changé.
V_oral = V.replace("[sur autrui]", "(sur autrui)")
assert V_oral.count("(") == 2 and "[" not in V_oral

narration = (D / "NARRATION-r7.txt").read_text(encoding="utf-8")
texte = narration.format(V=V_oral, **H)
assert "{" not in texte and "[" not in texte
(D / "VOIX-OFF.txt").write_text(texte, encoding="utf-8")

mots = len(re.findall(r"[0-9A-Za-zÀ-ÿœŒ]+(?:[’'-][0-9A-Za-zÀ-ÿœŒ]+)*", texte))
print(texte)
print(f"--- {mots} mots")
