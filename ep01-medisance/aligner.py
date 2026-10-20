"""Alignement forcé local de la voix off sur les unités du montage (aucun réseau, aucun modèle téléchargé).
Usage, depuis la racine du dépôt : python3 -I ep01-medisance/aligner.py
Requis : numpy, ffmpeg, espeak-ng (apt-get install espeak-ng).

Méthode (type aeneas) : chaque unité de unites.json (texte validé) est lue par espeak-ng en français ; voix
synthétique et voix réelle sont comparées par DTW sur des MFCC ; les frontières d'unités, connues dans la synthèse,
sont reportées sur l'enregistrement puis recalées sur la pause réelle la plus proche (±0,45 s).
Les deux fichiers d'origine sont alignés séparément (début : u01-u08 ; suite : u09-u36), puis mis bout à bout.
Sortie : temps.json {unité: [début, fin]} en secondes dans voix-ep01.wav, et un rapport de contrôle.
"""
import json, pathlib, subprocess, tempfile
import numpy as np

ICI = pathlib.Path(__file__).parent
SR, HOP, NFFT = 16000, 320, 640            # 20 ms par trame
UNITES = json.loads((ICI / "unites.json").read_text(encoding="utf-8"))
PARTIES = [("assets/audio/voix-originaux/1-debut.mp3", "u01", "u08"),
           ("assets/audio/voix-originaux/2-suite.mp3", "u09", "u36")]
JONCTION = 0.26                            # silence ajouté entre les deux parties (voir REPRISE.md)

def charge(chemin):
    """Décode en mono 16 kHz float32 avec ffmpeg."""
    brut = subprocess.run(["ffmpeg", "-v", "error", "-i", str(chemin), "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                          check=True, capture_output=True).stdout
    return np.frombuffer(brut, dtype=np.float32).copy()

def trames(y):
    n = 1 + max(0, (len(y) - NFFT) // HOP)
    idx = np.arange(NFFT)[None, :] + HOP * np.arange(n)[:, None]
    return y[idx] * np.hanning(NFFT)[None, :]

def _mel(nf=26):
    hz = lambda m: 700 * (10 ** (m / 2595) - 1)
    pts = hz(np.linspace(0, 2595 * np.log10(1 + 8000 / 700), nf + 2))
    b = np.floor((NFFT + 1) * pts / SR).astype(int)
    fb = np.zeros((nf, NFFT // 2 + 1))
    for i in range(1, nf + 1):
        fb[i - 1, b[i - 1]:b[i]] = (np.arange(b[i - 1], b[i]) - b[i - 1]) / max(b[i] - b[i - 1], 1)
        fb[i - 1, b[i]:b[i + 1]] = (b[i + 1] - np.arange(b[i], b[i + 1])) / max(b[i + 1] - b[i], 1)
    return fb
MEL = _mel()
DCT = np.cos(np.pi / 26 * (np.arange(26)[None, :] + 0.5) * np.arange(13)[:, None])

def mfcc(y):
    p = np.abs(np.fft.rfft(trames(y), axis=1)) ** 2
    m = np.log(p @ MEL.T + 1e-10) @ DCT.T
    return ((m - m.mean(0)) / (m.std(0) + 1e-6)).astype(np.float32)   # (trames, 13)

def rms_db(y):
    return 20 * np.log10(np.sqrt((trames(y) ** 2).mean(1)) + 1e-9)

def dtw(A, B):
    """DTW (pas 1-1, 1-0, 0-1) calculée par anti-diagonales ; renvoie le chemin [(i, j)] du début à la fin."""
    n, m = len(A), len(B)
    D = np.full((n + 1, m + 1), np.inf, dtype=np.float32); D[0, 0] = 0
    for k in range(2, n + m + 1):
        i = np.arange(max(1, k - m), min(n, k - 1) + 1); j = k - i
        c = np.sqrt(((A[i - 1] - B[j - 1]) ** 2).sum(1))
        D[i, j] = c + np.minimum(np.minimum(D[i - 1, j], D[i, j - 1]), D[i - 1, j - 1])
    i, j, chemin = n, m, []
    while i > 0 and j > 0:
        chemin.append((i - 1, j - 1))
        c = int(np.argmin([D[i - 1, j - 1], D[i - 1, j], D[i, j - 1]]))
        i, j = (i - 1, j - 1) if c == 0 else (i - 1, j) if c == 1 else (i, j - 1)
    return np.array(chemin[::-1])

def pauses(y, seuil_db=-42, mini=0.12):
    """Intervalles de silence [début, fin] en secondes."""
    calme = rms_db(y) < seuil_db
    out, i = [], 0
    while i < len(calme):
        if calme[i]:
            j = i
            while j < len(calme) and calme[j]:
                j += 1
            if (j - i) * HOP / SR >= mini:
                out.append([i * HOP / SR, j * HOP / SR])
            i = j
        else:
            i += 1
    return out

def synthese(textes, dossier):
    """Lit chaque unité avec espeak-ng ; renvoie le signal et les bornes [début, fin] de chaque unité."""
    morceaux, bornes, t = [], [], 0.0
    blanc = np.zeros(int(0.35 * SR), dtype=np.float32)
    for i, txt in enumerate(textes):
        f = pathlib.Path(dossier) / f"{i}.wav"
        subprocess.run(["espeak-ng", "-v", "fr", "-s", "175", "-w", str(f), txt], check=True)
        y = charge(f)
        db = rms_db(y); actif = np.where(db > db.max() - 40)[0]
        y = y[actif[0] * HOP: (actif[-1] + 1) * HOP + NFFT]
        bornes.append([t, t + len(y) / SR]); t += (len(y) + len(blanc)) / SR
        morceaux += [y, blanc]
    return np.concatenate(morceaux), bornes

def report(t, idx_s, idx_r):
    """Temps de la synthèse → temps réel, par le chemin DTW (moyenne des trames réelles associées)."""
    f = min(max(int(round(t * SR / HOP)), idx_s.min()), idx_s.max())
    return float(idx_r[idx_s == f].mean()) * HOP / SR

def recale(t, ps, sens):
    """'debut' : fin de la pause la plus proche ; 'fin' : début de la pause la plus proche."""
    best = None
    for a, b in ps:
        cible = b if sens == "debut" else a
        if abs(cible - t) <= 0.45 and (best is None or abs(cible - t) < abs(best - t)):
            best = cible
    return (best, True) if best is not None else (t, False)

temps, rapport, decalage = {}, [], 0.0
ids = [k for k, _ in UNITES]
with tempfile.TemporaryDirectory() as d:
    for chemin, k0, k1 in PARTIES:
        sel = UNITES[ids.index(k0): ids.index(k1) + 1]
        reel = charge(ICI / chemin)
        synth, bornes = synthese([t for _, t in sel], d)
        ch = dtw(mfcc(synth), mfcc(reel))
        idx_s, idx_r = ch[:, 0], ch[:, 1]
        ps = pauses(reel)
        for (k, txt), (s0, s1) in zip(sel, bornes):
            r0, ok0 = recale(report(s0, idx_s, idx_r), ps, "debut")
            r1, ok1 = recale(report(s1, idx_s, idx_r), ps, "fin")
            temps[k] = [round(r0 + decalage, 3), round(r1 + decalage, 3)]
            rapport.append((k, temps[k], ok0, ok1, len(txt)))
        decalage += len(reel) / SR + JONCTION

print(f"{'unité':6} {'début':>8} {'fin':>8}  calage  car/s")
prec = 0.0
for k, (d0, d1), ok0, ok1, n in rapport:
    alerte = []
    if d0 < prec - 0.02: alerte.append("CHEVAUCHE")
    if d1 <= d0: alerte.append("VIDE")
    debit = n / max(d1 - d0, 0.01)
    if not 14 <= debit <= 30: alerte.append("DÉBIT?")
    print(f"{k:6} {d0:8.2f} {d1:8.2f}  {'P' if ok0 else '-'}{'P' if ok1 else '-'}     {debit:5.1f}  {' '.join(alerte)}")
    prec = d1
(ICI / "temps.json").write_text(json.dumps(temps, indent=0), encoding="utf-8")
print("temps.json écrit")
