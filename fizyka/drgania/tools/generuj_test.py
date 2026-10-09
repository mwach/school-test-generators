#!/usr/bin/env python3
"""Generator testów z fizyki (Drgania): arkusz + osobna karta odpowiedzi.

Przy pierwszym uruchomieniu tworzy bazę pytań baza_pytan.json (z baza_poczatkowa.py,
zbudowanej na skanach podręcznika), potem losuje z niej 2 zadania z każdego z 3 rozdziałów,
zmienia dane liczbowe, sprawdza losowość klucza i zapisuje HTML (opcjonalnie PDF).

    python3 fizyka/drgania/tools/generuj_test.py [--numer N] [--pdf] [--nowa-baza]

Zasady: fizyka/drgania/WYMAGANIA.md. Zero zależności poza python3 (PDF: Chrome headless, macOS).
"""
import argparse
import json
import math
import os
import random
import subprocess
import sys
from decimal import Decimal, ROUND_HALF_UP

KAT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
BAZA = os.path.join(KAT, "baza_pytan.json")
HIST = os.path.join(KAT, "historia_testow.json")
WYJ = os.path.join(KAT, "testy")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
LITERY = "ABCD"
SRC = [
    "https://pl.wikipedia.org/wiki/Ruch_drgaj%C4%85cy",
    "https://pl.wikipedia.org/wiki/Amplituda",
    "https://pl.wikipedia.org/wiki/Okres_(fizyka)",
    "https://pl.wikipedia.org/wiki/Cz%C4%99stotliwo%C5%9B%C4%87",
    "https://pl.wikipedia.org/wiki/Energia_mechaniczna",
    "https://pl.wikipedia.org/wiki/Wahad%C5%82o_matematyczne",
]


# ---------- liczby ----------
def fmt(x):
    if isinstance(x, str):
        return x
    if isinstance(x, float) and x == int(x) and abs(x) < 1e12:
        x = int(x)
    return ("%.10g" % x).replace(".", ",")


def zaokr(x, cyfry=None, miejsca=None):
    """Zaokrągla half-up do `cyfry` cyfr znaczących albo `miejsca` po przecinku; zwraca (str, float)."""
    if cyfry:
        m = cyfry - 1 - math.floor(math.log10(abs(x)))
    else:
        m = miejsca
    q = Decimal(1).scaleb(-m)
    d = Decimal(repr(x)).quantize(q, rounding=ROUND_HALF_UP) if m >= 0 else Decimal(round(x, m))
    return (f"{d:f}".replace(".", ",") if m > 0 else f"{int(d)}"), float(d)


def graniczne(x, cyfry):
    m = cyfry - 1 - math.floor(math.log10(abs(x)))
    s = x * 10 ** m
    return abs((s - math.floor(s)) - 0.5) < 0.06


def ev(expr, vals):
    env = {"__builtins__": {}, "round": round, "abs": abs, "sqrt": math.sqrt}
    return eval(expr, env, dict(vals))


def zakres(spec):
    if isinstance(spec, list):
        return spec
    n = int(round((spec["do"] - spec["od"]) / spec["krok"]))
    return [round(spec["od"] + i * spec["krok"], 10) for i in range(n + 1)]


def losuj_param(z, rng, maks=200):
    """Zwraca (wartosci_surowe, sformatowane) spełniające warunek zadania."""
    for _ in range(maks):
        v = {k: rng.choice(zakres(s)) for k, s in z.get("param", {}).items()}
        try:
            for nazwa, wyr in z.get("pochodne", []):
                v[nazwa] = ev(wyr, v)
            if "warunek" in z and not ev(z["warunek"], v):
                continue
            if z.get("cyfry") and graniczne(v[z["wynik"]], z["cyfry"]):
                continue
        except ZeroDivisionError:
            continue
        f = {k: fmt(x) for k, x in v.items() if not isinstance(x, (list, tuple))}
        if "wynik" in z and z["typ"] == "obliczenia":
            w = v[z["wynik"]]
            if z.get("cyfry"):
                f[z["wynik"]] = zaokr(w, cyfry=z["cyfry"])[0]
            elif z.get("dokladnosc") is not None:
                f[z["wynik"]] = zaokr(w, miejsca=z["dokladnosc"])[0]
        return v, f
    raise RuntimeError(f"Nie udało się dobrać danych dla {z['id']}")


# ---------- SVG ----------
def svg_miska(katy, litery):
    """katy: {litera: kąt w stopniach od pionu}; zwraca SVG miski z kulkami."""
    R, r, cx, by = 110, 11, 150, 135
    cy = by - R
    a0, a1 = math.radians(-64), math.radians(64)
    p0 = (cx + R * math.sin(a0), cy + R * math.cos(a0))
    p1 = (cx + R * math.sin(a1), cy + R * math.cos(a1))
    s = [f'<svg viewBox="0 38 300 112" width="300" height="112" xmlns="http://www.w3.org/2000/svg" class="fig">',
         f'<line x1="40" y1="{by+4}" x2="260" y2="{by+4}" stroke="#444" stroke-width="3"/>',
         f'<path d="M{p0[0]:.1f},{p0[1]:.1f} A{R},{R} 0 0 0 {p1[0]:.1f},{p1[1]:.1f}" fill="none" stroke="#333" stroke-width="3.5"/>']
    for lit in litery:
        t = math.radians(katy[lit])
        bx = cx + (R - r - 2) * math.sin(t)
        byy = cy + (R - r - 2) * math.cos(t)
        s.append(f'<circle cx="{bx:.1f}" cy="{byy:.1f}" r="{r}" fill="#3b82d6" stroke="#1d4f91" stroke-width="1.5"/>')
        s.append(f'<text x="{bx:.1f}" y="{byy-r-4:.1f}" font-size="13" font-weight="700" text-anchor="middle" fill="#172033">{lit}</text>')
    s.append("</svg>")
    return "".join(s)


def svg_linijka(x0, xk):
    PX, TOP = 28, 40  # px na cm; y dla 10 cm

    def panel(ox, x, podpis):
        y = TOP + (x - 10) * PX
        mh = 22
        pts = []
        top, bot = 8, y - mh
        n = 12
        for i in range(n + 1):
            yy = top + (bot - top) * i / n
            xx = ox + 50 + (0 if i in (0, n) else (9 if i % 2 else -9))
            pts.append(f"{xx:.1f},{yy:.1f}")
        o = [f'<line x1="{ox+20}" y1="8" x2="{ox+90}" y2="8" stroke="#333" stroke-width="3"/>',
             f'<polyline points="{" ".join(pts)}" fill="none" stroke="#666" stroke-width="2"/>',
             f'<rect x="{ox+36}" y="{y-mh:.1f}" width="28" height="{mh}" fill="#c9a227" stroke="#7a5f0a" stroke-width="1.5"/>',
             f'<rect x="{ox+105}" y="{TOP-12}" width="34" height="{10*PX+24}" fill="#cfe3f5" stroke="#8fb4d6"/>',
             f'<line x1="{ox+64}" y1="{y:.1f}" x2="{ox+105}" y2="{y:.1f}" stroke="#d33" stroke-width="1" stroke-dasharray="3,2"/>']
        for mm in range(0, 101):
            yy = TOP + mm * PX / 10
            ln = 14 if mm % 10 == 0 else (9 if mm % 5 == 0 else 5)
            o.append(f'<line x1="{ox+105}" y1="{yy:.1f}" x2="{ox+105+ln}" y2="{yy:.1f}" stroke="#222" stroke-width="{1 if mm%10 else 1.3}"/>')
            if mm % 10 == 0:
                o.append(f'<text x="{ox+123}" y="{yy+4:.1f}" font-size="11" text-anchor="start" fill="#172033">{10+mm//10}</text>')
        o.append(f'<text x="{ox+20}" y="{TOP+10*PX+34}" font-size="11" fill="#172033">{podpis}</text>')
        return "".join(o)

    h = TOP + 10 * PX + 44
    return (f'<svg viewBox="0 0 330 {h}" width="330" height="{h}" xmlns="http://www.w3.org/2000/svg" class="fig lin">'
            + panel(0, xk, "v = 0 (skrajne położenie)") + panel(175, x0, "położenie równowagi")
            + '<text x="165" y="12" font-size="9" fill="#666" text-anchor="middle">(cm)</text></svg>')


# ---------- budowa zadań ----------
def zbuduj(z, rng):
    """Zwraca zadanie testowe: słownik z polami html_arkusz, html_klucz, klucz_zamkniety, pkt."""
    typ = z["typ"]
    out = {"id": z["id"], "typ": typ, "kategoria": {"pf": "pf", "obliczenia": "obliczenia", "otwarte": "otwarte"}.get(typ, "quiz"),
           "pkt": z["pkt"], "rozdzial": z["rozdzial"], "zrodlo": z.get("zrodlo", "")}
    if typ == "pf":
        for _ in range(500):
            wyb = rng.sample(z["pula"], 4)
            grupy = [p["grupa"] for p in wyb if p.get("grupa")]
            if len(grupy) != len(set(grupy)):
                continue
            poz = []
            for p in wyb:
                if "tekst_prawda" in p:
                    prawda = rng.random() < 0.5
                    v, f = losuj_param(p, rng)
                    poz.append((p["tekst_prawda" if prawda else "tekst"].format(**f), prawda, p["uzasadnienie"].format(**f)))
                else:
                    poz.append((p["tekst"], p["prawda"], p["uzasadnienie"]))
            wz = "".join("P" if x[1] else "F" for x in poz)
            if 1 <= wz.count("P") <= 3 and wz not in ("PFPF", "FPFP"):
                break
        else:
            raise RuntimeError("PF: nie dobrano zdań")
        out["poz"] = poz
        out["odp"] = wz
        out["html_arkusz"] = (f"<p>{z['polecenie']}</p><table class='grid'>"
                              + "".join(f"<tr><td class='num'>{i+1}.</td><td>{t}</td><td class='pf'>P</td><td class='pf'>F</td></tr>"
                                        for i, (t, _, _) in enumerate(poz)) + "</table>")
        out["html_klucz"] = (f"<p><b>Odpowiedzi:</b> <span class='zamkniete' data-typ='pf'>{', '.join(wz)}</span></p><ul>"
                             + "".join(f"<li>{i+1}. <b>{'P' if p else 'F'}</b> — {u}</li>" for i, (_, p, u) in enumerate(poz)) + "</ul>")
        out["punktacja"] = "4 poprawne = 2 pkt, 3 poprawne = 1 pkt, mniej = 0 pkt."
    elif typ == "obliczenia":
        v, f = losuj_param(z, rng)
        tekst = z["tekst"].format(**f)
        rys = ""
        if z.get("rysunek") == "linijka":
            rys = f"<div class='figwrap'>{svg_linijka(v['x0'], v['xk'])}</div>"
            tekst += " <span class='small'>(Odczyt wykonaj dla dolnej krawędzi ciężarka.)</span>"
        out["html_arkusz"] = (f"<p>{tekst}</p>{rys}<div class='calc-space'><span>Dane / szukane / obliczenia:</span></div>"
                              "<p class='ans'>Odpowiedź: <span class='blank l'></span></p>")
        wynik = f"{f[z['wynik']]} {z['jednostka']}"
        out["wynik"] = wynik
        out["html_klucz"] = ("<ul>" + "".join(f"<li>{x.format(**f)}</li>" for x in z["rozwiazanie"]) + "</ul>"
                             f"<p><b>Odpowiedź:</b> {wynik}.</p>")
        out["punktacja"] = "; ".join(z["punktacja"])
        out["dane"] = {k: x for k, x in v.items() if isinstance(x, (int, float))}
    elif typ in ("quiz", "quiz_miska"):
        if typ == "quiz_miska":
            katy = {}
            wys = [rng.choice([-1, 1]) * rng.uniform(6, 12), rng.choice([-1, 1]) * rng.uniform(26, 33), rng.choice([-1, 1]) * rng.uniform(46, 54)]
            lit = list("ABC")
            rng.shuffle(lit)
            for l, a in zip(lit, wys):
                katy[l] = a
            najw = rng.random() < 0.5
            pyt = ("największa" if najw else "najmniejsza")
            popr = lit[0] if najw else lit[2]
            out["html_arkusz"] = (f"<p>Na rysunku przedstawiono trzy położenia kulki poruszającej się ruchem drgającym w kulistej misie. "
                                  f"Wskaż punkt — A, B czy C — w którym znajduje się kulka, gdy jej prędkość jest <b>{pyt}</b>.</p>"
                                  f"<div class='figwrap'>{svg_miska(katy, 'ABC')}</div><p class='ans'>Odpowiedź: punkt <span class='blank s'></span></p>")
            wyjasn = ("W położeniu najniższym (najbliżej położenia równowagi) energia kinetyczna, a więc prędkość, jest największa." if najw else
                      "W położeniu najwyżej (najdalej od położenia równowagi) energia potencjalna jest największa, a prędkość — najmniejsza.")
            out["html_klucz"] = f"<p><b>Odpowiedź:</b> <span class='zamkniete' data-typ='wybor'>{popr}</span> — {wyjasn}</p>"
            out["odp"] = popr
        else:
            for _ in range(200):
                v, f = losuj_param(z, rng)
                op = [dict(tekst=o["tekst"].format(**f), poprawna=o["poprawna"]) for o in z["opcje"]]
                if len({o["tekst"] for o in op}) == 4:
                    break
            rng.shuffle(op)
            popr = LITERY[[o["poprawna"] for o in op].index(True)]
            out["html_arkusz"] = (f"<p>{z['pytanie'].format(**f)}</p><div class='choices'>"
                                  + "".join(f"<div>{LITERY[i]}. {o['tekst']}</div>" for i, o in enumerate(op)) + "</div>")
            out["html_klucz"] = (f"<p><b>Odpowiedź:</b> <span class='zamkniete' data-typ='wybor'>{popr}</span> — "
                                 f"{z['uzasadnienie'].format(**f)}</p>")
            out["odp"] = popr
        out["punktacja"] = "1 pkt za poprawną odpowiedź."
    elif typ == "quiz_dwa":
        w = rng.choice(z["warianty"])
        wyb = list(enumerate(w["wybor"]))
        pow_ = list(enumerate(w["powody"]))
        rng.shuffle(wyb)
        rng.shuffle(pow_)
        a = "AB"[[i for i, _ in wyb].index(w["poprawny_wybor"])]
        b = "12"[[i for i, _ in pow_].index(w["poprawny_powod"])]
        out["html_arkusz"] = (f"<p>{z['wstep']}</p><p>{w['zdanie']}</p>"
                              "<table class='grid two'><tr><td class='num'>" + "</td><td rowspan='2' class='since'>ponieważ</td><td class='num'>".join(
                                  [f"A.</td><td>{wyb[0][1]}", f"1.</td><td>{pow_[0][1]}"]) + "</td></tr>"
                              f"<tr><td class='num'>B.</td><td>{wyb[1][1]}</td><td class='num'>2.</td><td>{pow_[1][1]}</td></tr></table>"
                              "<p class='ans'>Odpowiedź: <span class='blank s'></span></p>")
        out["odp"] = a + b
        out["html_klucz"] = (f"<p><b>Odpowiedź:</b> <span class='zamkniete' data-typ='wybor'>{a}{b}</span> — "
                             f"{w['zdanie']} {w['wybor'][w['poprawny_wybor']]} ponieważ {w['powody'][w['poprawny_powod']]}</p>")
        out["punktacja"] = "1 pkt za poprawny wybór A/B, 1 pkt za poprawne uzasadnienie 1/2."
    elif typ == "otwarte":
        w = rng.choice(z["warianty"]) if "warianty" in z else z
        pol = w["polecenie"]
        rys = f"<div class='figwrap'>{svg_miska({'A': -34, 'B': 0, 'C': 34}, 'ABC')}</div>" if z.get("rysunek") == "miska" else ""
        out["html_arkusz"] = f"<p>{pol}</p>{rys}<div class='answer-space'></div><div class='answer-space'></div><div class='answer-space'></div>"
        out["html_klucz"] = "<ul>" + "".join(f"<li>{x}</li>" for x in z["odpowiedz"]) + "</ul>"
        out["punktacja"] = " ".join(z["klucz"])
    return out


def sprawdz_klucz(zadania):
    bl = []
    for z in zadania:
        if z["typ"] == "pf" and (set(z["odp"]) == {"P"} or set(z["odp"]) == {"F"} or z["odp"] in ("PFPF", "FPFP")):
            bl.append(f"PF {z['id']}: przewidywalny wzór {z['odp']}")
    pfs = [z["odp"] for z in zadania if z["typ"] == "pf"]
    if len(pfs) != len(set(pfs)):
        bl.append(f"PF: powtórzony wzór odpowiedzi {pfs}")
    lit = [z["odp"] for z in zadania if z["kategoria"] == "quiz"]
    if len(lit) >= 2 and len({x[0] for x in lit}) == 1:
        bl.append(f"quizy: wszystkie odpowiedzi zaczynają się od {lit[0][0]}")
    return bl


# ---------- wybór zadań ----------
def wybierz(baza, hist, rng):
    wybrane = []
    for r in ("1", "2", "3"):
        pula = [z for z in baza["zadania"] if str(z["rozdzial"]) == r]
        uzyte = set(hist.get(r, []))
        wolne = [z for z in pula if z["id"] not in uzyte]
        if len({z["typ"].split("_")[0] for z in wolne}) < 2:
            wolne, hist[r] = pula, []
        for _ in range(500):
            a, b = rng.sample(wolne, 2)
            if a["typ"].split("_")[0] != b["typ"].split("_")[0] and ({a["typ"], b["typ"]} != {"quiz", "quiz_miska"}):
                break
        wybrane.append(sorted([a, b], key=lambda z: pula.index(z)))
    return wybrane


def kat(z):
    return {"pf": "pf", "obliczenia": "obliczenia", "otwarte": "otwarte"}.get(z["typ"], "quiz")


def wybierz_pelny(baza, hist, rng):
    for _ in range(300):
        h2 = json.loads(json.dumps(hist))
        w = wybierz(baza, h2, rng)
        kategorie = {kat(z) for par in w for z in par}
        ile_obl = sum(kat(z) == "obliczenia" for par in w for z in par)
        if {"pf", "obliczenia", "quiz"} <= kategorie and ile_obl >= 2:
            return w, h2
    raise RuntimeError("Nie udało się dobrać zestawu pokrywającego wszystkie typy")


# ---------- HTML ----------
def html_arkusz(n, rozdz, zad, suma):
    cz = []
    nr = 1
    for r, pary in zip(("1", "2", "3"), zad):
        cz.append(f"<h2>Rozdział {r}. {rozdz[r]}</h2>")
        for t in pary:
            cz.append(f"<div class='task' data-zad='{nr}' data-pkt='{t['pkt']}'><div class='task-head'><div class='task-title'>Zadanie {nr}.</div>"
                      f"<div class='points'>{t['pkt']} pkt</div></div>{t['html_arkusz']}</div>")
            nr += 1
    return f"""<!doctype html>
<html lang="pl"><head><meta charset="utf-8"><title>Test z fizyki — Drgania (test {n})</title>
<link rel="stylesheet" href="../drgania.css"></head><body>
<div class="group-badge">{n}</div>
<h1>Test z fizyki: Drgania</h1>
<div class="subtitle">Fizyka · szkoła podstawowa · test {n} · czas pracy: 45 minut</div>
<div class="meta">
  <div>Imię i nazwisko: <span class="line">&nbsp;</span></div>
  <div>Klasa: <span class="line" style="min-width:20mm;">&nbsp;</span></div>
  <div>Data: <span class="line" style="min-width:20mm;">&nbsp;</span></div>
  <div>Liczba punktów: <span class="line" style="min-width:20mm;">&nbsp;</span> / <span data-suma>{suma}</span></div>
</div>
{''.join(cz)}
</body></html>"""


def html_klucz(n, rozdz, zad, suma):
    karta = []
    nr = 1
    for pary in zad:
        for t in pary:
            odp = t.get("odp") or t.get("wynik") or "(otwarte)"
            karta.append((nr, odp if t["kategoria"] != "pf" else " ".join(t["odp"]), t["pkt"]))
            nr += 1
    tab = "".join(f"<tr><td class='num'>{a}</td><td>{b}</td><td class='num'>{c}</td></tr>" for a, b, c in karta)
    cz = []
    nr = 1
    for r, pary in zip(("1", "2", "3"), zad):
        cz.append(f"<h2>Rozdział {r}. {rozdz[r]}</h2>")
        for t in pary:
            cz.append(f"<div class='key-item' data-zad='{nr}' data-pkt='{t['pkt']}'><span class='num'>Zadanie {nr}.</span> "
                      f"<span class='pk'>({t['pkt']} pkt)</span> <span class='small'>[{t['zrodlo']}]</span>{t['html_klucz']}"
                      f"<p class='accept'>Punktacja: {t['punktacja']}</p></div>")
            nr += 1
    zr = "".join(f"<li>{u}</li>" for u in SRC)
    return f"""<!doctype html>
<html lang="pl"><head><meta charset="utf-8"><title>Karta odpowiedzi — Drgania (test {n})</title>
<link rel="stylesheet" href="../drgania.css"></head><body>
<div class="group-badge">{n}</div>
<h1>Karta odpowiedzi: Drgania</h1>
<div class="subtitle">Fizyka · test {n} · razem <span data-suma>{suma}</span> pkt</div>
<table class="grid"><tr><th>Zad.</th><th>Odpowiedź</th><th>Pkt</th></tr>{tab}</table>
<h2>Szczegółowe rozwiązania i punktacja</h2>
<div class="key-group">{''.join(cz)}</div>
<h2>Źródła</h2><ul class="sources"><li>Podręcznik — skany stron 13, 14, 22, 28 (fizyka/drgania/IMG_2395–2398.jpeg), wzorzec formy zadań.</li>{zr}</ul>
</body></html>"""


def pdf(sciezka_html):
    out = sciezka_html[:-5] + ".pdf"
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer", f"--print-to-pdf={out}",
                    "file://" + sciezka_html], check=True, capture_output=True)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--numer", type=int)
    ap.add_argument("--pdf", action="store_true")
    ap.add_argument("--nowa-baza", action="store_true")
    a = ap.parse_args()

    if a.nowa_baza or not os.path.exists(BAZA):
        import baza_poczatkowa
        json.dump(baza_poczatkowa.baza(), open(BAZA, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print("Utworzono bazę pytań:", BAZA)
    baza = json.load(open(BAZA, encoding="utf-8"))
    hist = json.load(open(HIST, encoding="utf-8")) if os.path.exists(HIST) else {"rozdzialy": {}, "testy": {}}
    n = a.numer or (max([int(k) for k in hist["testy"]] + [0]) + 1)
    for proba in range(100):
        rng = random.Random(f"drgania-{n}-{proba}")
        wybrane, h2 = wybierz_pelny(baza, hist["rozdzialy"], rng)
        zad = [[zbuduj(z, rng) for z in par] for par in wybrane]
        plaskie = [t for par in zad for t in par]
        if not sprawdz_klucz(plaskie):
            break
    else:
        sys.exit("Kontrola klucza: nie udało się uzyskać losowego klucza")
    suma = sum(t["pkt"] for t in plaskie)
    os.makedirs(WYJ, exist_ok=True)
    pa = os.path.join(WYJ, f"test_drgania_{n}_arkusz.html")
    pk = os.path.join(WYJ, f"test_drgania_{n}_karta_odpowiedzi.html")
    open(pa, "w", encoding="utf-8").write(html_arkusz(n, baza["rozdzialy"], zad, suma))
    open(pk, "w", encoding="utf-8").write(html_klucz(n, baza["rozdzialy"], zad, suma))
    for r, par in zip(("1", "2", "3"), zad):
        h2.setdefault(r, [])
        for t in par:
            if t["id"] not in h2[r]:
                h2[r].append(t["id"])
    hist["rozdzialy"] = h2
    hist["testy"][str(n)] = {"zadania": [t["id"] for t in plaskie], "klucz": {t["id"]: t.get("odp") or t.get("wynik") for t in plaskie},
                             "suma": suma}
    json.dump(hist, open(HIST, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"Test {n}: {suma} pkt;", ", ".join(t["id"] for t in plaskie))
    if a.pdf:
        print(pdf(pa))
        print(pdf(pk))


if __name__ == "__main__":
    main()
