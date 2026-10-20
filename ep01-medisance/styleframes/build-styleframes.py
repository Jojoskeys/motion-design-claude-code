#!/usr/bin/env python3
"""Maquettes fixes ep01 : insère l'extrait du hadith copié depuis la source enregistrée, puis exporte les PNG.

Usage (depuis la racine du dépôt) : python3 -I ep01-medisance/styleframes/build-styleframes.py
Aucun réseau, aucun service payant : Chromium local en mode headless.
"""
import html
import pathlib
import re
import subprocess

ICI = pathlib.Path(__file__).resolve().parent
SOURCE = ICI.parents[1] / "serie-coran/episodes/ep01/sources-brutes/ep01-hadeethenc-5326.txt"
CHROMIUM = "/opt/pw-browsers/chromium"

# Extrait du hadith : la définition, copiée telle quelle depuis la traduction HadeethEnc enregistrée.
texte = SOURCE.read_text(encoding="utf-8")
traduction = texte.split("TRADUCTION FRANÇAISE PUBLIÉE SUR HADEETHENC\n", 1)[1].split("\n", 1)[0]
debut = traduction.index("C'est que tu évoques")
fin = traduction.index("répugnerait.") + len("répugnerait.")
extrait = traduction[debut:fin]
assert extrait in traduction
citation = f"«&nbsp;[…] {html.escape(extrait, quote=False)}&nbsp;»"

page = ICI / "02-hadith.html"
contenu = page.read_text(encoding="utf-8")
contenu = re.sub(r'(<p class="citation" id="citation">).*?(</p>)', lambda m: m.group(1) + citation + m.group(2),
                 contenu, count=1, flags=re.S)
page.write_text(contenu, encoding="utf-8")

for html_file in sorted(ICI.glob("0*.html")):
    png = html_file.with_suffix(".png")
    subprocess.run([CHROMIUM, "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                    "--force-device-scale-factor=1", "--window-size=1080,1920",
                    f"--screenshot={png}", html_file.as_uri()], check=True, capture_output=True)
    print(png.name)
