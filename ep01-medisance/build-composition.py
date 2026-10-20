"""Construit index.html : épisode 1 complet, minutage provisoire (voix pas encore enregistrée).
Usage, depuis la racine du dépôt : python3 -I ep01-medisance/build-composition.py [temps.json]

- Style V2 (styleframes/) : bleu nuit, ivoire, doré discret, fil de la parole, étoile à huit branches.
- Chaque phrase dite est à l'écran une seule fois : en carton (texte principal) ou en sous-titre (2 lignes max).
- Aucune citation n'est tapée ici : hadith (HadeethEnc) et verset (Hamidullah) sont lus dans les fichiers sources ;
  toute phrase de narration est contrôlée contre serie-coran/episodes/ep01/VOIX-OFF.txt (mot pour mot).
- Minutage : estimé à partir du nombre de mots. Après l'enregistrement, passer un fichier temps.json
  {"u01": [début, fin], ...} mesuré sur l'audio réel : il remplace l'estimation, unité par unité.
- Arabe : aucun texte arabe affiché tant qu'il n'est pas vérifié (emplacement réservé).
"""
import html, json, pathlib, re, sys

ICI = pathlib.Path(__file__).parent
EP = ICI.parent / "serie-coran/episodes/ep01"
VOIX = (EP / "VOIX-OFF.txt").read_text(encoding="utf-8")

# ---- citations, copiées depuis les sources -------------------------------------------------------------------------
brut = (EP / "sources-brutes/ep01-hadeethenc-5326.txt").read_text(encoding="utf-8")
TRAD = brut.split("TRADUCTION FRANÇAISE PUBLIÉE SUR HADEETHENC\n")[1].split("\n")[0]

def hadith(debut, fin):
    i = TRAD.index(debut); j = TRAD.index(fin, i) + len(fin)
    return TRAD[i:j]

H1 = hadith("Savez-vous", "médisance ?")
H2 = hadith("Allah et Son", "mieux !")
H3 = hadith("C'est que tu", "répugnerait.")
H4 = hadith("Et qu’en est-il", "en lui ?")
H5a = hadith("si ce que tu dis", "son sujet ;")
H5b = hadith("mais si ce n’est", "diffamé.")
V = (EP / "sources-brutes/ep01-qurancom-49-12.txt").read_text(encoding="utf-8").split("TRADUCTION FRANÇAISE\n")[1].split("\n")[0]
coupes = ["péché. ", "autres. ", "horreur. "]
V1, reste = V.split(coupes[0], 1); V1 += coupes[0].strip()
V2, reste = reste.split(coupes[1], 1); V2 += coupes[1].strip()
V3, V4 = reste.split(coupes[2], 1); V3 += coupes[2].strip()
assert " ".join([V1, V2, V3, V4]) == V
oral = lambda s: s.replace("[sur autrui]", "(sur autrui)")   # même adaptation que VOIX-OFF.txt
IMAGE = V3.split("? ")[0] + "?"                               # « L'un de vous … frère mort? »
FIN_V = V4[V4.index("Car Allah"):]                            # « Car Allah est … Très Miséricordieux »

# ---- unités de sens : (id, texte dit, rendu) — rendu « carton » (texte principal) ou « st » (sous-titre) ---------
U = [
    ("u01", "Dans le Coran, Allah interdit la médisance.", "carton"),
    ("u02", "Mais est-ce que tu sais vraiment ce qui en fait partie ?", "carton"),
    ("u03", "Pour mieux comprendre le Coran, abonne-toi.", "carton"),
    ("u04", "Pour comprendre la médisance, commençons par un échange entre le Prophète, paix et salut sur lui, et ses compagnons.", "st"),
    ("u05", "Dans un hadith rapporté par Muslim, il les interroge :", "st"),
    ("u06", H1, "carton"),
    ("u07", "Ses compagnons lui répondent :", "st"),
    ("u08", H2, "carton"),
    ("u09", "Il leur explique alors :", "st"),
    ("u10", H3, "carton"),
    ("u11", "Une question lui est alors posée :", "st"),
    ("u12", H4, "carton"),
    ("u13", "Autrement dit : et si ce qu’on dit de cette personne est vrai ?", "carton"),
    ("u14", "Le Prophète répond :", "st"),
    ("u15a", H5a, "carton"),
    ("u15b", H5b, "carton"),
    ("u16", "Ce qu’il explique ici, c’est que la médisance ne consiste pas forcément à inventer quelque chose sur quelqu’un.", "carton"),
    ("u17", "Évoquer un défaut réel qu’il détesterait voir mentionné peut déjà être de la médisance.", "st"),
    ("u18", "Lui attribuer ce qui n’est pas en lui, c’est de la diffamation.", "st"),
    ("u19", "Dire la vérité ne suffit donc pas, à lui seul, à justifier cette parole.", "carton"),
    ("u20", "Le hadith nous aide à reconnaître la médisance.", "st"),
    ("u21", "Le verset douze de la sourate Al-Hujurat élargit cette mise en garde :", "st"),
    ("u23a", oral(V1), "carton"),
    ("u23b", V2, "carton"),
    ("u23c", V3, "carton"),
    ("u23d", V4, "carton"),
    ("u24", "Le verset attire notre attention sur trois choses : l’excès de soupçons, l’espionnage et la médisance.", "st"),
    ("u25", "Le soupçon visé, c’est prêter à quelqu’un une mauvaise intention ou une faute sans preuve.", "st"),
    ("u26", "Espionner, c’est chercher à découvrir ce qu’il garde privé.", "st"),
    ("u27", "Médire, c’est évoquer de lui ce qui lui déplaît, même lorsque c’est vrai.", "st"),
    ("u28", "Ces interdictions protègent donc aussi ce qu’une personne ne peut pas défendre à cet instant : sa vie privée et sa réputation.", "carton"),
    ("u29", "Puis vient cette image du frère mort.", "st"),
    ("u30", "Le verset fait appel à une répulsion que l’on comprend immédiatement, pour nous faire mesurer la gravité de la médisance.", "st"),
    ("u31", "Ce verset nous apprend donc à faire attention à ce que nous supposons des autres, à respecter leur vie privée et à préserver leur réputation.", "st"),
    ("u32", "Et après ces mises en garde, il se termine sur le repentir et la miséricorde d’Allah.", "st"),
    ("u33", "Reconnaître ses paroles comme une faute, c’est aussi comprendre qu’il faut changer sa manière de parler des autres.", "carton"),
    ("u34", "Et toi, qu’est-ce que tu retiens de ce verset ?", "carton"),
    ("u35", "Dis-le en commentaire.", "carton"),
    ("u36", "Si cette explication t’a aidé à mieux le comprendre, partage-la et abonne-toi pour la suite.", "st"),
]
TXT = {k: t for k, t, _ in U}
for k, t, _ in U:                      # chaque unité existe mot pour mot dans le texte enregistré
    assert t in VOIX, k
# l'ensemble des unités couvre tout le texte (hors guillemets et sauts de ligne)
norm = lambda s: re.sub(r"[«»\s]+", " ", s).strip()
assert norm(" ".join(t for _, t, _ in U)) == norm(VOIX), "unités ≠ VOIX-OFF.txt"

# ---- minutage provisoire ------------------------------------------------------------------------------------------
CITATION = {"u06", "u08", "u10", "u12", "u15a", "u15b", "u23a", "u23b", "u23c", "u23d"}
PAUSE_LONGUE = {"u02", "u03", "u05", "u08", "u10", "u12", "u13", "u15b", "u16", "u18", "u19", "u21", "u23d",
                "u27", "u28", "u30", "u31", "u32", "u33", "u35"}
T, t = {}, 0.15
for k, txt, _ in U:
    mots = len(re.findall(r"\w+(?:[’'-]\w+)*", txt))
    d = mots / (2.2 if k in CITATION else 2.45) + 0.25
    T[k] = [round(t, 2), round(t + d, 2)]
    t += d + (0.25 if k == "u15a" else 0.75 if k in PAUSE_LONGUE else 0.4)
AUDIO = ""
VOIX_DEBUT = 0.3                       # la voix démarre 0,3 s après l'image 0 (accroche déjà lisible)
if len(sys.argv) > 1:                  # temps mesurés sur l'audio réel (secondes dans voix-ep01.wav)
    mesures = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"))
    assert set(mesures) == set(T), "temps.json doit couvrir toutes les unités"
    T = {k: [round(d + VOIX_DEBUT, 3), round(f + VOIX_DEBUT, 3)] for k, (d, f) in mesures.items()}
    AUDIO = (f'<audio id="voix-ep01" src="assets/audio/voix-ep01.wav" data-start="{VOIX_DEBUT}" '
             f'data-track-index="10" data-volume="1"></audio>')
DUREE = round(T["u36"][1] + 2.5, 2)

# ---- outils HTML --------------------------------------------------------------------------------------------------
def e(s):
    """Échappe et lie les signes doubles à leur mot (espace insécable), sans changer le texte."""
    s = html.escape(s, quote=False)
    return re.sub(r" ([?!:;»])", "&nbsp;\\1", s).replace("« ", "«&nbsp;")

def surligne(s, *parts, cls="or"):
    out = e(s)
    for p in parts:
        assert e(p) in out, p
        out = out.replace(e(p), f'<span class="{cls}">{e(p)}</span>', 1)
    return out

def guill(s, ouvre=True, ferme=True):
    return ("«&nbsp;" if ouvre else "") + e(s) + ("&nbsp;»" if ferme else "")

ETOILE = '<rect x="-14" y="-14" width="28" height="28"/><rect x="-14" y="-14" width="28" height="28" transform="rotate(45)"/>'
def etoile(x, y, cls="", s=1.0, plein=False, idx=""):
    fill = "#0b1630" if plein else "none"
    return (f'<g transform="translate({x} {y}) scale({s})"><g {idx} class="{cls}" fill="{fill}" stroke="#c6a15b" '
            f'stroke-width="2.5">{ETOILE}</g></g>')

FILS = []                              # (id du tracé de masque, longueur estimée côté JS)
def fil(fid, d, opacite=0.9):
    """Fil de la parole pointillé, révélé par un tracé plein dans un masque (dessiné au temps voulu)."""
    FILS.append(fid)
    return (f'<mask id="{fid}-m" maskUnits="userSpaceOnUse" x="0" y="0" width="1080" height="1920">'
            f'<path id="{fid}" fill="none" stroke="#fff" stroke-width="16" d="{d}"/></mask>'
            f'<path fill="none" mask="url(#{fid}-m)" d="{d}" stroke="#c6a15b" stroke-width="3" '
            f'stroke-dasharray="2 14" opacity="{opacite}"/>')

SCENES, JS = [], []
def a(sel, k, decal=0.0, dy=18, dur=0.45, de=0.0):
    """Fait apparaître `sel` au début de l'unité k."""
    JS.append(f'tl.fromTo({json.dumps(sel)}, {{opacity: {de}, y: {dy}}}, {{opacity: 1, y: 0, duration: {dur}, ease: "power2.out"}}, {T[k][0] + decal:.2f});')
def trace(fid, k, decal=0.0, dur=0.6):
    JS.append(f'trace({json.dumps(fid)}, {T[k][0] + decal:.2f}, {dur});')
def eclaire(sel, k, decal=0.0):
    JS.append(f'tl.to({json.dumps(sel)}, {{color: "#c6a15b", duration: 0.35, ease: "power1.out"}}, {T[k][0] + decal:.2f});')
    JS.append(f'tl.to({json.dumps(sel)}, {{color: "#f3ead7", duration: 0.35, ease: "power1.inOut"}}, {T[k][1] + 0.1:.2f});')
def scene(sid, debut_k, fin_k, contenu, etiquette):
    SCENES.append((sid, debut_k, fin_k, contenu, etiquette))

# ---- 1. Accroche : bulles et fil de la maquette V2, question d'abord ---------------------------------------------
scene("s-accroche", "u01", "u03", f'''
<svg class="decor" viewBox="0 0 1080 1920" aria-hidden="true">
  <g id="bulles" fill="#0f1d40" stroke-linecap="round" stroke-linejoin="round">
    <g id="bulle1"><path d="M150 330 h250 a46 46 0 0 1 46 46 v84 a46 46 0 0 1 -46 46 h-176 l-46 40 v-40 h-28 a46 46 0 0 1 -46 -46 v-84 a46 46 0 0 1 46 -46 z" stroke="#f3ead7" stroke-opacity=".55" stroke-width="3"/>
      <g fill="#f3ead7" fill-opacity=".55"><circle cx="232" cy="418" r="9"/><circle cx="275" cy="418" r="9"/><circle cx="318" cy="418" r="9"/></g></g>
    <g id="bulle2"><path d="M560 560 h250 a46 46 0 0 1 46 46 v84 a46 46 0 0 1 -46 46 h-28 v40 l-46 -40 h-176 a46 46 0 0 1 -46 -46 v-84 a46 46 0 0 1 46 -46 z" stroke="#f3ead7" stroke-opacity=".32" stroke-width="3"/>
      <g fill="#f3ead7" fill-opacity=".32"><circle cx="642" cy="648" r="9"/><circle cx="685" cy="648" r="9"/><circle cx="728" cy="648" r="9"/></g></g>
    <g id="bulle3"><path d="M210 790 h170 a40 40 0 0 1 40 40 v58 a40 40 0 0 1 -40 40 h-140 l-38 34 v-34 h-0 a40 40 0 0 1 -32 -40 v-58 a40 40 0 0 1 40 -40 z" stroke="#f3ead7" stroke-opacity=".22" stroke-width="3" stroke-dasharray="10 12"/></g>
    {fil("fa1", "M224 546 C 300 640, 430 580, 512 650")}
    {fil("fa2", "M736 776 C 700 850, 520 820, 422 858", .7)}
  </g>
</svg>
<p class="bloc hook1" id="a-u01">{e(TXT["u01"])}</p>
<p class="bloc hook2" id="a-u02">{surligne(TXT["u02"], "ce qui en fait partie ?", cls="or-it")}</p>
<p class="bloc hook2" id="a-u03">{surligne(TXT["u03"], "abonne-toi.", cls="cta")}</p>
''', "La médisance · Coran 49:12")
JS.append(f'tl.fromTo("#a-u01", {{opacity: 0.6, y: 10}}, {{opacity: 1, y: 0, duration: 0.4, ease: "power2.out"}}, 0);')
JS.append('tl.fromTo("#bulle1", {opacity: 0, scale: .94}, {opacity: 1, scale: 1, duration: .45, transformOrigin: "50% 100%"}, 0);')
trace("fa1", "u01", 0.35, 0.45)
JS.append('tl.fromTo("#bulle2", {opacity: 0, scale: .94}, {opacity: 1, scale: 1, duration: .45, transformOrigin: "50% 100%"}, 0.6);')
trace("fa2", "u01", 0.9, 0.45)
JS.append('tl.fromTo("#bulle3", {opacity: 0, scale: .94}, {opacity: 1, scale: 1, duration: .45, transformOrigin: "50% 100%"}, 1.2);')
a("#a-u02", "u02", -0.15)
JS.append(f'tl.to("#a-u02", {{opacity: 0, duration: 0.3}}, {T["u03"][0] - 0.3:.2f});')
JS.append(f'tl.to("#bulles", {{opacity: 0.6, duration: 0.6}}, {T["u03"][0] - 0.3:.2f});')
a("#a-u03", "u03", 0.0)

# ---- 2. L'échange (hadith) ----------------------------------------------------------------------------------------
REF_H = '<p class="bloc ref"><strong>Sahih Muslim 2589</strong> · authentique · traduction&nbsp;: HadeethEnc</p>'
scene("s-echange", "u04", "u05", f'''
<svg class="decor" viewBox="0 0 1080 1920" aria-hidden="true"><g fill="#0f1d40" stroke-linecap="round" stroke-linejoin="round">
  <g id="e-b1"><path d="M150 520 h300 a50 50 0 0 1 50 50 v100 a50 50 0 0 1 -50 50 h-210 l-50 44 v-44 h-40 a50 50 0 0 1 -50 -50 v-100 a50 50 0 0 1 50 -50 z" stroke="#c6a15b" stroke-opacity=".6" stroke-width="3"/>
    <g fill="#c6a15b" fill-opacity=".7"><circle cx="252" cy="620" r="10"/><circle cx="300" cy="620" r="10"/><circle cx="348" cy="620" r="10"/></g></g>
  <g id="e-b2"><path d="M580 860 h300 a50 50 0 0 1 50 50 v100 a50 50 0 0 1 -50 50 h-40 v44 l-50 -44 h-210 a50 50 0 0 1 -50 -50 v-100 a50 50 0 0 1 50 -50 z" stroke="#f3ead7" stroke-opacity=".45" stroke-width="3"/>
    <g fill="#f3ead7" fill-opacity=".5"><circle cx="682" cy="960" r="10"/><circle cx="730" cy="960" r="10"/><circle cx="778" cy="960" r="10"/></g></g>
  {fil("fe1", "M250 770 C 300 880, 470 900, 576 940")}
</g></svg>
{REF_H}''', "Hadith · un échange")
a("#e-b1", "u04", 0.3); trace("fe1", "u04", 1.6, 0.8); a("#e-b2", "u04", 2.2)

def bulle(bid, texte, cote, qui, top, grand=False):
    return (f'<div class="bulle {cote}{" grand" if grand else ""}" id="{bid}" style="top:{top}px">'
            f'<p class="qui">{qui}</p><p class="cit">{texte}</p></div>')
scene("s-h1", "u06", "u08", bulle("b-u06", guill(H1), "g", "Le Prophète", 360)
      + bulle("b-u08", guill(H2), "d", "Ses compagnons", 760) + REF_H, "Hadith · Sahih Muslim 2589")
a("#b-u06", "u06", -0.2); a("#b-u08", "u08", -0.2)
JS.append(f'tl.to("#b-u06", {{opacity: 0.55, duration: 0.4}}, {T["u07"][0]:.2f});')
scene("s-h2", "u09", "u10", bulle("b-u10", guill(H3), "g", "Le Prophète", 520, True) + REF_H, "Hadith · Sahih Muslim 2589")
a("#b-u10", "u10", -0.2)
scene("s-h3", "u11", "u12", bulle("b-u12", guill(H4), "d", "Une question", 560, True) + REF_H, "Hadith · Sahih Muslim 2589")
a("#b-u12", "u12", -0.2)

# ---- 3. Reformulation : reprend la composition de l'accroche V2 (« vrai ? » en italique doré) --------------------
r = TXT["u13"]
scene("s-autrement", "u13", "u13", f'''
<p class="bloc lab-autrement" id="r-1">{e(r[:r.index(":") + 1])}</p>
<p class="bloc question" id="r-2"><span class="debut">{e(r[r.index(":") + 2:r.index("vrai")].strip())}</span> <span class="vrai">{e(r[r.index("vrai"):])}</span></p>
<svg class="decor" viewBox="0 0 1080 1920" aria-hidden="true"><line id="r-filet" x1="88" y1="1196" x2="520" y2="1196" stroke="#c6a15b" stroke-width="3" opacity=".75"/>
{etoile(548, 1196, idx='id="r-etoile"', s=0.86)}</svg>''', "Autrement dit")
a("#r-1", "u13", -0.2); a("#r-2", "u13", 0.0)
JS.append(f'tl.fromTo("#r-filet", {{scaleX: 0}}, {{scaleX: 1, duration: 0.5, ease: "power2.inOut", transformOrigin: "0% 50%"}}, {T["u13"][0] + 1.0:.2f});')
JS.append(f'tl.fromTo("#r-etoile", {{opacity: 0, rotation: -45}}, {{opacity: 1, rotation: 0, duration: 0.45, svgOrigin: "0 0"}}, {T["u13"][0] + 1.4:.2f});')

scene("s-h4", "u14", "u15b", bulle("b-u15a", guill(H5a, ferme=False), "g", "Le Prophète", 380)
      + bulle("b-u15b", guill(H5b, ouvre=False), "g", "", 780) + REF_H, "Hadith · Sahih Muslim 2589")
a("#b-u15a", "u15a", -0.2); a("#b-u15b", "u15b", -0.2)

# ---- 4. Explication et distinction médisance / diffamation ---------------------------------------------------------
def carton(cid, k, *or_, note=""):
    return (f'<p class="bloc expl" id="{cid}">{surligne(TXT[k], *or_)}</p>'
            + (f'<p class="bloc note" id="{cid}-note">{note}</p>' if note else ""))
scene("s-expl1", "u16", "u16", carton("c-u16", "u16", "ne consiste pas forcément à inventer"), "Explication · d'après le hadith")
a("#c-u16", "u16", -0.2)

scene("s-schema", "u17", "u18", f'''
<svg class="decor" viewBox="0 0 1080 1920" aria-hidden="true">
  {etoile(504, 430, s=1.1)}
  {fil("fs1", "M490 470 C 420 560, 300 560, 270 660")}
  {fil("fs2", "M518 470 C 590 560, 710 560, 740 660")}
</svg>
<p class="bloc tete">Ce que tu dis de lui…</p>
<div class="bloc branche g" id="br-g"><p class="cle">est présent en lui</p><p class="mot">médisance</p></div>
<div class="bloc branche d" id="br-d"><p class="cle">n’est pas en lui</p><p class="mot">diffamation</p></div>''', "Explication · d'après le hadith")
trace("fs1", "u17", 0.0, 0.6); a("#br-g", "u17", 0.4)
trace("fs2", "u18", 0.0, 0.6); a("#br-d", "u18", 0.4)

NOTE_CAS = ("Le commentaire de ce hadith sur HadeethEnc mentionne des situations particulières (plainte d’une "
            "personne opprimée, consultation). Elles ne sont pas traitées ici.")
scene("s-expl2", "u19", "u19", carton("c-u19", "u19", "à lui seul", note=e(NOTE_CAS)), "À retenir")
a("#c-u19", "u19", -0.2); a("#c-u19-note", "u19", 1.2)

# ---- 5. Le verset ---------------------------------------------------------------------------------------------------
scene("s-transition", "u20", "u21", f'''
<svg class="decor" viewBox="0 0 1080 1920" aria-hidden="true">
  {fil("ft1", "M120 520 C 260 520, 300 760, 504 800")}
  {etoile(540, 800, s=1.8, idx='id="t-etoile"')}
</svg>
<p class="bloc titre-sourate" id="t-titre">Sourate Al-Hujurat</p>
<p class="bloc sous-titre-sourate" id="t-ref">Coran · 49:12</p>''', "Coran · 49:12")
trace("ft1", "u20", 0.2, 1.0)
JS.append(f'tl.fromTo("#t-etoile", {{opacity: 0, rotation: -45}}, {{opacity: 1, rotation: 0, duration: 0.6, svgOrigin: "0 0"}}, {T["u20"][0] + 1.1:.2f});')
a("#t-titre", "u21", 0.0); a("#t-ref", "u21", 0.3)

CADRE = '''<svg class="decor" viewBox="0 0 1080 1920" aria-hidden="true">
  <rect x="88" y="300" width="832" height="1140" rx="28" fill="#0f1d40" fill-opacity=".6" stroke="#c6a15b" stroke-opacity=".6" stroke-width="2.5"/>
  <rect x="104" y="316" width="800" height="1108" rx="18" fill="none" stroke="#c6a15b" stroke-opacity=".22" stroke-width="1.5"/>
  ''' + "".join(etoile(x, y, plein=True) for x, y in [(88, 300), (920, 300), (88, 1440), (920, 1440)]) + '''
  <g fill="#f3ead7" fill-opacity=".13"><rect x="180" y="420" width="650" height="44" rx="22"/><rect x="290" y="500" width="540" height="44" rx="22"/></g>
  <line x1="250" y1="690" x2="512" y2="690" stroke="#c6a15b" stroke-opacity=".6" stroke-width="2"/>
  <line x1="568" y1="690" x2="830" y2="690" stroke="#c6a15b" stroke-opacity=".6" stroke-width="2"/>
  ''' + etoile(540, 690) + '''
</svg>
<p class="bloc tag tag-ar">Texte arabe de 49:12 · provisoire, non affiché <span style="display:block">(vérification sur mushaf imprimé en cours)</span></p>
<p class="bloc ref-v"><strong>Traduction du sens</strong> — Muhammad Hamidullah</p>'''
vers = [("u23a", V1, True, False), ("u23b", V2, False, False), ("u23c", V3, False, False), ("u23d", V4, False, True)]
scene("s-verset", "u23a", "u23d", CADRE + "".join(
    f'<p class="bloc verset" id="v-{k}">{guill(txt, o, f)}</p>' for k, txt, o, f in vers), "Coran · 49:12 · verset entier")
for i, (k, *_r) in enumerate(vers):
    a(f"#v-{k}", k, -0.25, dy=12)
    if i < 3:
        JS.append(f'tl.to("#v-{k}", {{opacity: 0, duration: 0.3}}, {T[vers[i + 1][0]][0] - 0.55:.2f});')

# ---- 6. Les trois mises en garde ------------------------------------------------------------------------------------
def trois(prefixe, libelles, fid):
    svg = (f'<svg class="decor" viewBox="0 0 1080 1920" aria-hidden="true">{fil(fid, "M150 400 L 150 1060")}'
           + "".join(etoile(150, y, plein=True, idx=f'id="{prefixe}-e{i}"') for i, y in enumerate([480, 730, 980])) + '</svg>')
    return svg + "".join(f'<p class="bloc noeud" id="{prefixe}-n{i}" style="top:{y - 44}px">{lib}</p>'
                         for i, (y, lib) in enumerate(zip([480, 730, 980], libelles)))
u24 = TXT["u24"]
lib3 = ["l’excès de soupçons", "l’espionnage", "la médisance"]
assert all(x in u24 for x in lib3)
scene("s-trois", "u24", "u27", trois("t3", [e(x) for x in lib3], "f3"), "Coran 49:12 · trois mises en garde")
trace("f3", "u24", 0.0, 1.2)
def au_mot(k, x):
    """Décalage (s) où le passage x est dit dans l'unité k, au prorata des caractères."""
    return (T[k][1] - T[k][0]) * TXT[k].index(x) / len(TXT[k])
for i, x in enumerate(lib3):
    a(f"#t3-n{i}", "u24", au_mot("u24", x) - 0.1)
for i, k in enumerate(["u25", "u26", "u27"]):
    eclaire(f"#t3-n{i}", k)
JS.append(f'tl.fromTo("#t3-note", {{opacity: 0}}, {{opacity: 1, duration: 0.4}}, {T["u27"][0] + 0.8:.2f});')
SCENES[-1] = SCENES[-1][:3] + (SCENES[-1][3] + f'<p class="bloc note bas" id="t3-note">{e(NOTE_CAS)}</p>',) + SCENES[-1][4:]

scene("s-expl3", "u28", "u28", carton("c-u28", "u28", "sa vie privée et sa réputation"), "Explication")
a("#c-u28", "u28", -0.2)

scene("s-image", "u29", "u30", f'''<p class="bloc rappel" id="i-cit">{guill(IMAGE, ferme=False)}&nbsp;…&nbsp;»</p>
<p class="bloc ref-rappel" id="i-ref"><strong>Coran 49:12</strong> · traduction du sens&nbsp;: Muhammad Hamidullah</p>
<p class="bloc ref-rappel bas2" id="i-taf">Voir aussi&nbsp;: tafsir Al-Mukhtasar et As-Sa'di, 49:12</p>''', "Coran 49:12 · l’image du verset")
a("#i-cit", "u29", 0.0); a("#i-ref", "u29", 0.5); a("#i-taf", "u30", 0.5)

u31 = TXT["u31"]
lib_r = ["faire attention à ce que nous supposons des autres", "respecter leur vie privée", "préserver leur réputation"]
assert all(x in u31 for x in lib_r)
scene("s-recap", "u31", "u31", trois("rc", [e(x) for x in lib_r], "f4"), "Ce que le verset nous apprend")
trace("f4", "u31", -0.2, 0.9)
for i, x in enumerate(lib_r):
    a(f"#rc-n{i}", "u31", au_mot("u31", x) - 0.1)

scene("s-fin-verset", "u32", "u32", f'''<p class="bloc rappel" id="f-cit">«&nbsp;…&nbsp;{e(FIN_V)}&nbsp;»</p>
<p class="bloc ref-rappel" id="f-ref"><strong>Coran 49:12, fin du verset</strong> · traduction du sens&nbsp;: Muhammad Hamidullah</p>''', "Coran 49:12 · fin du verset")
a("#f-cit", "u32", 0.6); a("#f-ref", "u32", 1.0)

scene("s-expl4", "u33", "u33", carton("c-u33", "u33", "changer sa manière de parler des autres"), "Explication")
a("#c-u33", "u33", -0.2)

# ---- 7. Appels à l'action et fin --------------------------------------------------------------------------------------
scene("s-question", "u34", "u35", f'''<p class="bloc expl grand" id="q-u34">{e(TXT["u34"])}</p>
<p class="bloc pilule" id="q-u35">{e(TXT["u35"])}</p>''', "Et toi ?")
a("#q-u34", "u34", -0.2); a("#q-u35", "u35", -0.1)

scene("s-fin", "u36", "u36", f'''
<p class="bloc fin-titre" id="z-titre">La médisance</p>
<p class="bloc fin-ref" id="z-ref">Coran 49:12 · Sahih Muslim 2589</p>
<div class="bloc pilules" id="z-cta"><span class="pilule-i">Partager</span><span class="pilule-i or-fond">S’abonner</span></div>
<p class="bloc fin-sources" id="z-src">Hadith&nbsp;: Sahih Muslim 2589, traduction HadeethEnc · Coran&nbsp;: traduction du sens de Muhammad Hamidullah · Tafsir&nbsp;: Al-Mukhtasar, Al-Muyassar, As-Sa'di</p>''', "Comprendre le Coran · épisode 1")
a("#z-titre", "u36", -0.2); a("#z-ref", "u36", 0.1); a("#z-cta", "u36", 2.4); a("#z-src", "u36", 0.6)

# ---- sous-titres : unités « st », découpées en morceaux de 2 lignes au plus ---------------------------------------
def morceaux(s, maxc=62):
    mots, out, cur = s.split(" "), [], ""
    for m in mots:
        if cur and len(cur) + 1 + len(m) > maxc:
            out.append(cur); cur = m
        else:
            cur = f"{cur} {m}".strip()
        if cur.endswith((",", ".", ":", "?")) and len(cur) > maxc * 0.55:
            out.append(cur); cur = ""
    if cur:
        out.append(cur)
    # pas de morceau d'un ou deux mots isolés en fin
    if len(out) > 1 and len(out[-1]) < 14:
        dernier = out.pop(); out[-1] += " " + dernier
    return out
ST = []
SUIVANT = {U[i][0]: U[i + 1][0] for i in range(len(U) - 1)}
for k, txt, rendu in U:
    if rendu != "st":
        continue
    parts = morceaux(txt)
    assert " ".join(parts) == txt
    d0, d1 = T[k]; tot = sum(len(p) for p in parts); c = d0
    for i, p in enumerate(parts):
        fin = c + (d1 - d0) * len(p) / tot
        # le dernier morceau reste pendant la pause qui suit (0,8 s au plus) : lecture plus confortable
        tenue = min(T[SUIVANT[k]][0] - 0.05, d1 + 0.8) - d1 if k in SUIVANT else 0.8
        ST.append((f"st-{k}-{i}", p, c, fin + (max(tenue, 0.15) if i == len(parts) - 1 else 0)))
        c = fin

# ---- assemblage -------------------------------------------------------------------------------------------------------
bornes = [T[s[1]][0] - (0.0 if i == 0 else 0.3) for i, s in enumerate(SCENES)] + [DUREE]
corps, etiquettes = [], []
for i, (sid, k0, k1, contenu, etiq) in enumerate(SCENES):
    corps.append(f'<section class="scene" id="{sid}">{contenu}</section>')
    etiquettes.append(f'<p class="bloc etiquette lab" id="lab-{sid}">{e(etiq)}</p>')
    d, f = bornes[i], bornes[i + 1]
    if i == 0:
        JS.insert(0, f'tl.set("#{sid}, #lab-{sid}", {{opacity: 1}}, 0);')
    else:
        JS.append(f'tl.fromTo("#{sid}, #lab-{sid}", {{opacity: 0}}, {{opacity: 1, duration: 0.35, ease: "power1.out"}}, {d:.2f});')
    if i < len(SCENES) - 1:
        JS.append(f'tl.to("#{sid}, #lab-{sid}", {{opacity: 0, duration: 0.3, ease: "power1.in"}}, {f - 0.32:.2f});')
for sid, p, d, f in ST:
    corps.append(f'<p class="st" id="{sid}">{e(p)}</p>')
    JS.append(f'tl.fromTo("#{sid}", {{opacity: 0}}, {{opacity: 1, duration: 0.15}}, {d:.2f});')
    JS.append(f'tl.to("#{sid}", {{opacity: 0, duration: 0.15}}, {f - 0.15:.2f});')

page = (ICI / "composition.tpl").read_text(encoding="utf-8")
page = (page.replace("%%DUREE%%", f"{DUREE}").replace("%%AUDIO%%", AUDIO)
            .replace("%%ETIQUETTES%%", "\n    ".join(etiquettes))
            .replace("%%SCENES%%", "\n    ".join(corps))
            .replace("%%FILS%%", json.dumps(FILS))
            .replace("%%JS%%", "\n    ".join(JS)))
(ICI / "index.html").write_text(page, encoding="utf-8")
(ICI / "unites.json").write_text(json.dumps([[k, t] for k, t, _ in U], ensure_ascii=False, indent=0), encoding="utf-8")
(ICI / "temps-provisoires.json").write_text(json.dumps(T, ensure_ascii=False, indent=0), encoding="utf-8")
print(f"index.html : {len(SCENES)} scènes, {len(ST)} sous-titres, durée provisoire {DUREE} s")
