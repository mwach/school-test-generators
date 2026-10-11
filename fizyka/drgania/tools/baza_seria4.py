"""Seria 4 (2026-10-11): kolejne zadania z wykresów x(t) (amplituda, okres, częstotliwość) i ze sprężyną.
Zadania autorskie, w stylu skanów. Pole "seria": 4. dopisz(baza) jest idempotentne."""

AUT = "autorskie, w stylu skanów"
SER = 4


def pf(id_, tekst, prawda, uzas, grupa=None, **extra):
    d = {"id": id_, "tekst": tekst, "prawda": prawda, "uzasadnienie": uzas, "zrodlo": AUT, "seria": SER}
    if grupa:
        d["grupa"] = grupa
    d.update(extra)
    return d


PF_NOWE = {
    "2-pf": [
        pf("2p19", "Ciało wykonuje {n} drgań w czasie {t} s. Częstotliwość jego drgań jest równa {fz} Hz.", False,
           "f = n / t = {n} / {t} s = {f} Hz; {fz} Hz to okres, a nie częstotliwość.", "okres_f",
           param={"para": [[10, 5], [8, 4], [20, 10], [6, 3], [12, 3]]},
           pochodne=[["n", "para[0]"], ["t", "para[1]"], ["f", "para[0]/para[1]"], ["fz", "para[1]/para[0]"]],
           tekst_prawda="Ciało wykonuje {n} drgań w czasie {t} s. Częstotliwość jego drgań jest równa {f} Hz."),
    ],
    "3-pf": [
        pf("3p22", "W skrajnym położeniu wózka na poziomej sprężynie jego energia kinetyczna jest największa.", False,
           "W skrajnym położeniu wózek na chwilę się zatrzymuje (v = 0), więc energia kinetyczna jest równa zero.", "wozek_skraj"),
        pf("3p23", "Gdy zmniejszymy amplitudę drgań wózka na sprężynie (bez oporów), jego największa prędkość zmaleje.", True,
           "Mniejsza amplituda to mniejsza energia całkowita układu, więc w położeniu równowagi wózek ma mniejszą energię kinetyczną.", "wozek_skraj"),
        pf("3p24", "Energia sprężystości sprężyny jest największa wtedy, gdy wózek porusza się najszybciej.", False,
           "Najszybciej wózek porusza się w położeniu równowagi, gdzie sprężyna nie jest odkształcona (energia sprężystości najmniejsza).", "wozek_eq"),
        pf("3p25", "W położeniu równowagi cała energia mechaniczna wózka na sprężynie jest jego energią kinetyczną.", True,
           "Sprężyna nie jest wtedy odkształcona, więc energia sprężystości jest równa zero.", "wozek_eq"),
    ],
    "4-pf": [
        pf("4p07", "Odległość między kolejnymi maksimami na wykresie położenia od czasu wynosi {T} s. Ciało wykonuje więc {T} drgań w ciągu sekundy.", False,
           "Odległość między maksimami to okres: T = {T} s, więc w ciągu sekundy ciało wykonuje f = 1/T = {f} drgań.", "okres_f",
           param={"T": [0.25, 0.5, 2, 4]}, pochodne=[["f", "1/T"]],
           tekst_prawda="Odległość między kolejnymi maksimami na wykresie położenia od czasu wynosi {T} s. Ciało wykonuje więc {f} drgań w ciągu sekundy."),
        pf("4p08", "Dwa ciała mają ten sam okres drgań, ale różne amplitudy. Na wykresie położenia od czasu ich maksima przypadają w tych samych chwilach.", True,
           "Odstęp między maksimami to okres — przy równych okresach maksima (przy tej samej fazie) pojawiają się równie często; różnią się tylko wysokością.", "amplituda"),
        pf("4p09", "Ciało o większej amplitudzie drgań ma zawsze dłuższy okres drgań.", False,
           "Okres nie zależy od amplitudy (np. dla wahadła przy niewielkich wychyleniach).", "amplituda"),
    ],
}


def _obl(id_, r, pkt, **kw):
    d = {"id": id_, "rozdzial": r, "typ": "obliczenia", "pkt": pkt, "seria": SER}
    d.update(kw)
    return d


T_OKR = [0.5, 1, 2, 4]
PARA_KL = {"para": [[0.5, 1.0], [1.0, 2.0], [0.5, 2.0], [2.0, 4.0], [1.0, 0.5], [2.0, 1.0], [2.0, 0.5], [4.0, 2.0]],
           "AK": [1, 1.5, 2, 2.5], "AL": [1, 1.5, 2, 2.5], "zk": [1, -1], "zl": [1, -1]}

NOWE = [
    _obl("4-obl-wykres-dwa", 4, 3, rysunek="wykres2", kolizja="wykresy2", param=PARA_KL,
         pochodne=[["TK", "para[0]"], ["TL", "para[1]"], ["fK", "1/para[0]"], ["fL", "1/para[1]"]], warunek="AK != AL",
         tekst="Dwa ciężarki (K i L) zawieszone na sprężynach poruszają się ruchem drgającym. Na wykresie przedstawiono zależność położenia od czasu dla obu ciężarków. "
               "Odczytaj z wykresu amplitudy i okresy drgań obu ciężarków, a następnie oblicz częstotliwość drgań każdego z nich.",
         wynik="fK", jednostka="Hz", wynik_tekst="K: A = {AK} cm, T = {TK} s, f = {fK} Hz; L: A = {AL} cm, T = {TL} s, f = {fL} Hz",
         rozwiazanie=["Amplitudy: A<sub>K</sub> = {AK} cm, A<sub>L</sub> = {AL} cm.", "Okresy: T<sub>K</sub> = {TK} s, T<sub>L</sub> = {TL} s.",
                      "f<sub>K</sub> = 1/T<sub>K</sub> = {fK} Hz, f<sub>L</sub> = 1/T<sub>L</sub> = {fL} Hz."],
         punktacja=["1 pkt — poprawne amplitudy obu ciężarków (±0,1 cm)", "1 pkt — poprawne okresy", "1 pkt — poprawne częstotliwości z jednostką"],
         zrodlo=AUT),
    _obl("4-obl-wykres-droga", 4, 2, rysunek="wykres", kolizja="wykresAT",
         param={"A": [1, 1.5, 2, 2.5, 3], "T": [0.8, 1.2, 1.6, 2.0, 2.4], "faza": [0, 1]}, pochodne=[["s4", "4*A"]],
         tekst="Na wykresie przedstawiono zależność położenia od czasu dla ciężarka zawieszonego na sprężynie. Odczytaj z wykresu amplitudę drgań, "
               "a następnie oblicz drogę, jaką przebywa ciężarek w czasie jednego pełnego drgania.",
         wynik="s4", jednostka="cm", wynik_tekst="A = {A} cm; droga w czasie jednego drgania: {s4} cm",
         rozwiazanie=["Amplituda: A = {A} cm.", "W czasie jednego pełnego drgania ciężarek przebywa drogę równą 4 amplitudom: s = 4 · {A} cm = {s4} cm."],
         punktacja=["1 pkt — poprawna amplituda (±0,1 cm)", "1 pkt — poprawna droga (4A) z jednostką"], zrodlo=AUT),
    _obl("2-obl-wykres-minuta", 2, 3, rysunek="wykres", kolizja="wykresAT",
         param={"A": [1, 1.5, 2, 2.5, 3], "T": T_OKR, "faza": [0, 1]}, pochodne=[["f", "1/T"], ["N", "60/T"]],
         tekst="Na wykresie przedstawiono zależność położenia od czasu dla ciężarka drgającego na sprężynie. Odczytaj z wykresu okres drgań, "
               "oblicz ich częstotliwość, a następnie podaj, ile pełnych drgań wykona ciężarek w ciągu minuty.",
         wynik="N", jednostka="drgań", wynik_tekst="T = {T} s; f = {f} Hz; {N} drgań w ciągu minuty",
         rozwiazanie=["Okres odczytany z osi poziomej: T = {T} s.", "f = 1/T = {f} Hz.", "Minuta to 60 s, więc liczba drgań: N = 60 s / {T} s = {N}."],
         punktacja=["1 pkt — poprawny okres", "1 pkt — poprawna częstotliwość z jednostką", "1 pkt — poprawna liczba drgań w ciągu minuty"], zrodlo=AUT),
    {"id": "4-quiz-wykres-zdania", "rozdzial": 4, "typ": "quiz", "pkt": 1, "seria": SER, "rysunek": "wykres", "kolizja": "wykresAT",
     "param": {"A": [1, 1.5, 2, 2.5, 3], "T": T_OKR, "faza": [0, 1]}, "pochodne": [["f", "1/T"], ["A2", "2*A"]],
     "pytanie": "Na wykresie przedstawiono zależność położenia od czasu dla ciężarka poruszającego się ruchem drgającym. Wskaż poprawne zdanie.",
     "opcje": [{"tekst": "Amplituda drgań jest równa {A} cm, a ich częstotliwość — {f} Hz.", "poprawna": True},
               {"tekst": "Amplituda drgań jest równa {A2} cm, a ich częstotliwość — {f} Hz.", "poprawna": False},
               {"tekst": "Amplituda drgań jest równa {A} cm, a ich częstotliwość — {T} Hz.", "poprawna": False},
               {"tekst": "Amplituda drgań jest równa {A2} cm, a ich częstotliwość — {T} Hz.", "poprawna": False}],
     "uzasadnienie": "Amplituda to największe wychylenie: {A} cm ({A2} cm to odległość między skrajami). Okres to {T} s, więc f = 1/T = {f} Hz ({T} Hz to pomylenie częstotliwości z okresem).",
     "zrodlo": AUT},
    _obl("1-obl-rozmach", 1, 3, rysunek="linijka",
         param={"x0": {"od": 12.0, "do": 16.0, "krok": 0.1}, "A": {"od": 1.5, "do": 4.5, "krok": 0.5}, "kier": [1, -1]},
         pochodne=[["xk", "round(x0 + kier*A, 1)"], ["d", "round(2*A, 1)"]], warunek="11.0 <= xk <= 19.0",
         tekst="Na ilustracji przedstawiono ciężarek zawieszony na sprężynie, uchwycony w dwóch momentach podczas drgań: w chwili, gdy jego prędkość była równa zero (po lewej), "
               "oraz w położeniu równowagi (po prawej). Odczytaj z linijek (w cm) położenia dolnej krawędzi ciężarka, wyznacz amplitudę drgań, "
               "a następnie oblicz odległość między najwyższym a najniższym położeniem ciężarka.",
         wynik="d", jednostka="cm", dokladnosc=1, wynik_tekst="A = {A} cm; odległość między skrajnymi położeniami: {d} cm",
         rozwiazanie=["Odczyty: położenie skrajne x = {xk} cm, położenie równowagi x₀ = {x0} cm.", "A = |x − x₀| = {A} cm.",
                      "Skrajne położenia leżą po obu stronach położenia równowagi, każde w odległości A, więc odległość między nimi to 2A = {d} cm."],
         punktacja=["1 pkt — poprawna amplituda (odczyty ±0,1 cm)", "1 pkt — zauważenie, że odległość między skrajami to 2A", "1 pkt — poprawny wynik z jednostką"], zrodlo=AUT),
    _obl("2-obl-sprezyna-fn", 2, 2,
         param={"f": [0.5, 2, 2.5, 4], "t": [10, 20, 30, 60]}, pochodne=[["n", "f*t"], ["T", "1/f"]], warunek="(f*t) % 1 == 0",
         tekst="Ciężarek zawieszony na sprężynie drga z częstotliwością {f} Hz. Oblicz okres jego drgań oraz liczbę pełnych drgań, które wykona w czasie {t} s.",
         wynik="n", jednostka="drgań", wynik_tekst="T = {T} s; {n} drgań",
         rozwiazanie=["Okres: T = 1/f = 1/{f} Hz = {T} s.", "Liczba drgań: n = f · t = {f} Hz · {t} s = {n}."],
         punktacja=["1 pkt — poprawny okres z jednostką", "1 pkt — poprawna liczba drgań"], zrodlo=AUT),
    _obl("3-obl-sprezyna-v", 3, 3,
         param={"m": [0.5, 1, 2, 4], "v": [1, 2, 3, 4]}, pochodne=[["E", "0.5*m*v*v"]],
         tekst="Wózek o masie {m} kg, przymocowany do poziomej sprężyny, porusza się ruchem drgającym (pomiń opory ruchu). W skrajnym położeniu energia sprężystości sprężyny wynosi {E} J. "
               "Oblicz największą prędkość wózka podczas drgań.",
         wynik="v", jednostka="m/s",
         rozwiazanie=["W skrajnym położeniu wózek się zatrzymuje, więc cała energia jest energią sprężystości: E = {E} J.",
                      "W położeniu równowagi cała energia jest energią kinetyczną: m·v² / 2 = {E} J, stąd v² = 2 · {E} J / {m} kg.",
                      "v = {v} m/s."],
         punktacja=["1 pkt — wniosek: energia kinetyczna w położeniu równowagi = energia sprężystości w skrajnym", "1 pkt — poprawne przekształcenie wzoru E<sub>k</sub> = m·v² / 2",
                    "1 pkt — poprawny wynik z jednostką"], zrodlo=AUT),
    {"id": "3-quiz-sprezyna3", "rozdzial": 3, "typ": "quiz_dwa", "pkt": 2, "seria": SER,
     "wstep": "Wózek przymocowany do poziomej sprężyny porusza się ruchem drgającym (pomiń opory ruchu). Wybierz właściwe dokończenie zdania spośród wariantów <b>A</b> i <b>B</b> "
              "oraz jego poprawne uzasadnienie spośród wariantów <b>1</b> i <b>2</b>.",
     "warianty": [
         {"zdanie": "Gdy wózek oddala się od położenia równowagi, energia sprężystości sprężyny",
          "wybor": ["rośnie,", "maleje,"], "poprawny_wybor": 0,
          "powody": ["zmiana długości sprężyny rośnie.", "prędkość wózka rośnie."], "poprawny_powod": 0},
         {"zdanie": "W skrajnym położeniu energia kinetyczna wózka jest",
          "wybor": ["równa zero,", "największa,"], "poprawny_wybor": 0,
          "powody": ["wózek na chwilę się zatrzymuje.", "sprężyna nie jest odkształcona."], "poprawny_powod": 0},
         {"zdanie": "Gdy mocniej ściśniemy sprężynę przed puszczeniem wózka, jego największa prędkość",
          "wybor": ["wzrośnie,", "zmaleje,"], "poprawny_wybor": 0,
          "powody": ["więcej energii sprężystości zamieni się w energię kinetyczną.", "sprężyna ma wtedy mniejszą energię sprężystości."], "poprawny_powod": 0},
     ],
     "zrodlo": AUT},
]


def dopisz(baza):
    zad = baza["zadania"]
    for t in zad:
        if t["typ"] == "pf":
            t["pula"] = [p for p in t["pula"] if p.get("seria") != SER]
    zad[:] = [z for z in zad if z.get("seria") != SER]
    n = 0
    for z in NOWE:
        zad.append(dict(z))
        n += 1
    for tid, zdania in PF_NOWE.items():
        next(z for z in zad if z["id"] == tid)["pula"].extend(zdania)
        n += len(zdania)
    return n
