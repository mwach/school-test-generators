"""Seria 2 zadań z działu Drgania — dopisana na podstawie skanów IMG_2402–2405.jpeg
(sekcje „Sprawdź się!”: s. 34–35 „Ruch drgający na wykresach” oraz s. 44–45 „Powtórzenie”).
Wzorzec formy, nie bank pytań: dane liczbowe i treści są zmienione/przeformułowane.

dopisz(baza) jest idempotentne: dokłada nowe zadania i zdania P/F (po `id`) do istniejącej
bazy (baza_pytan.json) — wywoływane przez generuj_test.py. Nowe zadania mają pole "seria": 2."""

S = "skan s."
AUT = "autorskie, w stylu skanów"
SER = 2


def pf(id_, tekst, prawda, uzas, zrodlo, grupa=None, **extra):
    d = {"id": id_, "tekst": tekst, "prawda": prawda, "uzasadnienie": uzas, "zrodlo": zrodlo, "seria": SER}
    if grupa:
        d["grupa"] = grupa
    d.update(extra)
    return d


PF_NOWE = {
    "1": [
        pf("1p13", "Na osi pionowej wykresu zależności położenia drgającego ciała od czasu zaznaczamy czas.", False,
           "Na osi pionowej zaznaczamy położenie ciała, a czas — na osi poziomej.", S + " 34 zad.1.1", "osie"),
        pf("1p14", "Z wykresu zależności położenia ciała od czasu można odczytać amplitudę jego drgań.", True,
           "Amplituda to największe wychylenie od położenia równowagi — widać ją na osi pionowej.", S + " 34 zad.1.2"),
        pf("1p15", "Okres drgań ciała można odczytać z osi pionowej wykresu zależności jego położenia od czasu.", False,
           "Okres to czas — odczytujemy go z osi poziomej (czasu); oś pionowa pokazuje położenie.", S + " 34 zad.1.3", "osie"),
        pf("1p16", "Im bliżej położenia równowagi znajduje się kulka wahadła, tym mniejsze jest jej wychylenie.", True,
           "Wychylenie to odległość od położenia równowagi.", S + " 34 zad.1.4", "wychylenie"),
        pf("1p17", "Im dalej od położenia równowagi znajduje się kulka wahadła, tym mniejsze jest jej wychylenie.", False,
           "Wychylenie to odległość od położenia równowagi — im dalej od niego, tym większe.", S + " 44 zad.1.3", "wychylenie"),
        pf("1p18", "Na wykresie położenia ciała drgającego od czasu największa wartość położenia wynosi {x} cm, a najmniejsza −{x} cm. Amplituda drgań jest równa {x2} cm.", False,
           "Amplituda to największe wychylenie od położenia równowagi, czyli {x} cm; {x2} cm to odległość między skrajami (2A).",
           AUT, "amplituda", param={"x": [1, 1.5, 2, 2.5, 3, 4]}, pochodne=[["x2", "2*x"]],
           tekst_prawda="Na wykresie położenia ciała drgającego od czasu największa wartość położenia wynosi {x} cm, a najmniejsza −{x} cm. Amplituda drgań jest równa {x} cm."),
    ],
    "2": [
        pf("2p13", "Ciało drgające po upływie okresu zaczyna poruszać się ponownie po tym samym torze w tę samą stronę.", True,
           "Okres to czas jednego pełnego drgania — po nim ruch się powtarza.", S + " 44 zad.1.1"),
        pf("2p14", "Im większa jest amplituda drgań wahadła, tym dłuższy jest okres jego drgań.", False,
           "Okres wahadła (przy niewielkich wychyleniach) nie zależy od amplitudy.", S + " 44 zad.1.5"),
        pf("2p15", "Kamera nagrywa film z częstotliwością {f} klatek na sekundę. Odstęp czasu między kolejnymi klatkami wynosi {f} s.", False,
           "Odstęp między klatkami to okres: T = 1/f = 1/{f} s⁻¹ = {T} s.", AUT, None,
           param={"f": [5, 10, 20, 25, 50]}, pochodne=[["T", "1/f"]],
           tekst_prawda="Kamera nagrywa film z częstotliwością {f} klatek na sekundę. Odstęp czasu między kolejnymi klatkami wynosi {T} s."),
        pf("2p16", "Ciało wykonuje {n} drgań w ciągu minuty. Częstotliwość jego drgań jest równa {n} Hz.", False,
           "1 minuta to 60 s, więc f = {n}/60 s = {fh} Hz.", AUT, None,
           param={"n": [6, 12, 18, 24, 30, 45]}, pochodne=[["fh", "n/60"]],
           tekst_prawda="Ciało wykonuje {n} drgań w ciągu minuty. Częstotliwość jego drgań jest równa {fh} Hz."),
    ],
    "3": [
        pf("3p13", "Gdy kulka wahadła zbliża się do położenia równowagi, jej energia potencjalna grawitacji rośnie.", False,
           "Kulka opada, więc jej energia potencjalna maleje (zamienia się w kinetyczną).", S + " 44 zad.1.4", "kin,pot"),
        pf("3p14", "Gdy wózek na poziomej sprężynie znajduje się w skrajnym położeniu, jego energia kinetyczna jest równa zero.", True,
           "W skrajnym położeniu wózek na chwilę się zatrzymuje (v = 0).", AUT, "skraj"),
        pf("3p15", "Im większa amplituda drgań wahadła (bez oporów), tym większa jest największa prędkość jego kulki.", True,
           "Z większego wychylenia kulka spada z większej wysokości, więc w położeniu równowagi ma większą energię kinetyczną.", AUT),
    ],
}


def _obl(id_, r, pkt, **kw):
    d = {"id": id_, "rozdzial": r, "typ": "obliczenia", "pkt": pkt, "seria": SER}
    d.update(kw)
    return d


NOWE = [
    # ---------- rozdział 1 ----------
    _obl("1-obl-piasek", 1, 2, rysunek="piasek",
         param={"xmin": {"od": 3.0, "do": 5.0, "krok": 0.5}, "A": {"od": 1.5, "do": 3.5, "krok": 0.5}},
         pochodne=[["xmax", "round(xmin + 2*A, 1)"], ["x0", "round(xmin + A, 1)"]],
         warunek="xmax <= 11.0",
         tekst="Uczniowie zawiesili na nitce wahadło z butelki, z której wysypywał się piasek, i wprawili je w ruch drgający nad linijką. "
               "Piasek utworzył ślad pokazany na rysunku (widok z góry). Na podstawie rysunku odpowiedz na pytania. "
               "<b>a)</b> W którym miejscu skali linijki znajduje się położenie równowagi? <b>b)</b> Jaka była amplituda drgań?",
         wynik="A", jednostka="cm", dokladnosc=1,
         wynik_tekst="położenie równowagi: {x0} cm; amplituda: {A} cm",
         rozwiazanie=["Ślad piasku sięga od {xmin} cm do {xmax} cm — to skrajne położenia wahadła.",
                      "Położenie równowagi leży w środku między skrajami: ({xmin} cm + {xmax} cm) / 2 = {x0} cm.",
                      "Amplituda to odległość od położenia równowagi do skraju: A = {xmax} cm − {x0} cm = {A} cm."],
         punktacja=["1 pkt — poprawne położenie równowagi (tolerancja ±0,1 cm)", "1 pkt — poprawna amplituda z jednostką (tolerancja ±0,1 cm)"],
         zrodlo=S + " 34 zad.3"),
    {"id": "1-quiz-wykres", "rozdzial": 1, "typ": "quiz", "pkt": 1, "seria": SER, "rysunek": "wykres",
     "param": {"A": [1, 1.5, 2, 2.5, 3], "T": [0.8, 1.2, 1.6, 2.0, 2.4], "faza": [0, 1]},
     "pochodne": [["A2", "2*A"], ["T2", "T/2"], ["T4", "2*T"]],
     "pytanie": "Na wykresie przedstawiono zależność położenia od czasu dla kulki poruszającej się ruchem drgającym. Które odczyty amplitudy i okresu drgań są poprawne?",
     "opcje": [{"tekst": "amplituda {A} cm, okres {T} s", "poprawna": True},
               {"tekst": "amplituda {A2} cm, okres {T} s", "poprawna": False},
               {"tekst": "amplituda {A} cm, okres {T2} s", "poprawna": False},
               {"tekst": "amplituda {A} cm, okres {T4} s", "poprawna": False}],
     "uzasadnienie": "Amplituda to największe wychylenie od położenia równowagi (x = 0): {A} cm; okres to czas jednego pełnego drgania: {T} s. "
                     "{A2} cm to odległość między skrajami (2A), {T2} s to pół okresu, a {T4} s to czas dwóch drgań (cały zakres wykresu).",
     "zrodlo": S + " 34 zad.2"},
    # ---------- rozdział 2 ----------
    _obl("2-obl-klatki", 2, 3, rysunek="wykres_kropki",
         param={"para": [[0.8, 10], [0.8, 15], [0.8, 20], [1.2, 10], [1.6, 10], [2.0, 5], [2.0, 8]],
                "A": [2, 2.5, 3], "faza": [0, 1]},
         pochodne=[["T", "para[0]"], ["fps", "para[1]"], ["N", "round(para[0]*para[1])"]],
         tekst="Uczniowie zarejestrowali kamerą drgania kulki zawieszonej na nici. Na podstawie zapisu wideo sporządzili wykres zależności położenia kulki od czasu; "
               "punkty na wykresie odpowiadają kolejnym klatkom filmu. <b>a)</b> Odczytaj z wykresu okres drgań kulki. "
               "<b>b)</b> Ile klatek na sekundę rejestrowała użyta kamera?",
         wynik="fps", jednostka="klatek/s",
         wynik_tekst="T = {T} s; {fps} klatek/s",
         rozwiazanie=["Okres odczytany z wykresu: T = {T} s.",
                      "W czasie jednego okresu na wykresie jest {N} punktów (klatek).",
                      "Liczba klatek na sekundę: {N} / {T} s = {fps} klatek/s (odstęp między klatkami = 1/{fps} s)."],
         punktacja=["1 pkt — poprawny odczyt okresu", "1 pkt — poprawna liczba klatek w czasie jednego okresu (lub odstępu między punktami)",
                    "1 pkt — poprawna liczba klatek na sekundę z jednostką"],
         zrodlo=S + " 35 zad.4"),
    _obl("2-obl-dwa-wykresy", 2, 3, rysunek="wykres2", kolizja="wykresy2",
         param={"para": [[0.5, 1.0], [1.0, 2.0], [0.5, 2.0], [2.0, 4.0], [1.0, 0.5], [2.0, 1.0], [2.0, 0.5], [4.0, 2.0]],
                "AK": [1, 1.5, 2, 2.5], "AL": [1, 1.5, 2, 2.5], "zk": [1, -1], "zl": [1, -1]},
         pochodne=[["TK", "para[0]"], ["TL", "para[1]"], ["fK", "1/para[0]"], ["fL", "1/para[1]"]],
         warunek="AK != AL",
         tekst="Dwa ciężarki zawieszone na różnych sprężynach poruszają się ruchem drgającym. Na wykresie przedstawiono zależność położenia od czasu "
               "dla obu ciężarków (K i L). Na podstawie wykresu wyznacz amplitudy oraz częstotliwości drgań tych ciężarków.",
         wynik="fK", jednostka="Hz",
         wynik_tekst="K: A = {AK} cm, f = {fK} Hz; L: A = {AL} cm, f = {fL} Hz",
         rozwiazanie=["Amplitudy odczytane z osi pionowej: A<sub>K</sub> = {AK} cm, A<sub>L</sub> = {AL} cm.",
                      "Okresy odczytane z osi poziomej: T<sub>K</sub> = {TK} s, T<sub>L</sub> = {TL} s.",
                      "Częstotliwości: f<sub>K</sub> = 1/T<sub>K</sub> = {fK} Hz, f<sub>L</sub> = 1/T<sub>L</sub> = {fL} Hz."],
         punktacja=["1 pkt — poprawne amplitudy obu ciężarków (tolerancja ±0,1 cm)", "1 pkt — poprawne okresy obu ciężarków",
                    "1 pkt — poprawne częstotliwości (f = 1/T) z jednostką"],
         zrodlo=S + " 45 zad.9"),
    _obl("2-obl-mlot", 2, 2,
         param={"n": [9, 12, 15, 18, 24, 36, 40, 45]}, pochodne=[["T", "60/n"]],
         tekst="Młot pneumatyczny pracuje z częstotliwością {n} uderzeń na minutę. Oblicz okres drgań tego młota. Wynik podaj z dokładnością do dwóch cyfr znaczących.",
         wynik="T", jednostka="s", cyfry=2,
         rozwiazanie=["{n} uderzeń na minutę to {n} drgań w ciągu 60 s.", "T = 60 s / {n} ≈ {T} s."],
         punktacja=["1 pkt — poprawna metoda (T = 60 s / liczba uderzeń, zamiana minuty na sekundy)",
                    "1 pkt — wynik z dokładnością do 2 cyfr znaczących i jednostką"],
         zrodlo=S + " 44 zad.5"),
    _obl("2-obl-polokres", 2, 2,
         param={"t": [0.3, 0.4, 0.5, 0.6, 0.8, 1.2, 1.5, 2.4]}, pochodne=[["T", "2*t"]],
         tekst="Uczniowie zauważyli, że czas, w którym ciężarek zawieszony na sprężynie i poruszający się ruchem drgającym przemieszcza się od najniższego do najwyższego położenia, "
               "wynosi dokładnie {t} s. Ile wynosi okres drgań tego ciężarka?",
         wynik="T", jednostka="s",
         rozwiazanie=["Przejście od jednego skrajnego położenia do drugiego to połowa pełnego drgania.", "T = 2 · {t} s = {T} s."],
         punktacja=["1 pkt — zauważenie, że czas przejścia między skrajami to pół okresu", "1 pkt — poprawny wynik z jednostką"],
         zrodlo=S + " 44 zad.4"),
    {"id": "2-quiz-dwa-wykresy", "rozdzial": 2, "typ": "quiz", "pkt": 1, "seria": SER, "rysunek": "wykres2", "kolizja": "wykresy2",
     "param": {"para": [[0.5, 1.0], [1.0, 2.0], [0.5, 2.0], [2.0, 4.0], [1.0, 0.5], [2.0, 1.0], [2.0, 0.5], [4.0, 2.0]],
               "AK": [1, 1.5, 2, 2.5], "AL": [1, 1.5, 2, 2.5], "zk": [1, -1], "zl": [1, -1]},
     "pochodne": [["TK", "para[0]"], ["TL", "para[1]"], ["fK", "1/para[0]"], ["fL", "1/para[1]"],
                  ["wa", "'K' if AK > AL else 'L'"], ["wa2", "'L' if AK > AL else 'K'"],
                  ["wf", "'K' if para[0] < para[1] else 'L'"], ["wf2", "'L' if para[0] < para[1] else 'K'"]],
     "warunek": "AK != AL",
     "pytanie": "Dwa ciężarki (K i L) poruszają się ruchem drgającym. Na wykresie przedstawiono zależność położenia od czasu dla obu ciężarków. Wskaż poprawne zdanie.",
     "opcje": [{"tekst": "Większą amplitudę ma ciężarek {wa}, a większą częstotliwość — ciężarek {wf}.", "poprawna": True},
               {"tekst": "Większą amplitudę ma ciężarek {wa2}, a większą częstotliwość — ciężarek {wf}.", "poprawna": False},
               {"tekst": "Większą amplitudę ma ciężarek {wa}, a większą częstotliwość — ciężarek {wf2}.", "poprawna": False},
               {"tekst": "Większą amplitudę ma ciężarek {wa2}, a większą częstotliwość — ciężarek {wf2}.", "poprawna": False}],
     "uzasadnienie": "Amplitudy: A<sub>K</sub> = {AK} cm, A<sub>L</sub> = {AL} cm. Okresy: T<sub>K</sub> = {TK} s, T<sub>L</sub> = {TL} s — krótszy okres oznacza większą "
                     "częstotliwość (f<sub>K</sub> = {fK} Hz, f<sub>L</sub> = {fL} Hz).",
     "zrodlo": S + " 45 zad.9"},
    # ---------- rozdział 3 ----------
    {"id": "3-quiz-sprezyna", "rozdzial": 3, "typ": "quiz_dwa", "pkt": 2, "seria": SER,
     "wstep": "Na sprężynie zawieszono ciężarek. Następnie wychylono go z położenia równowagi i puszczono swobodnie, tak że zaczął wykonywać drgania (pomiń opory ruchu). "
              "Wybierz właściwe dokończenie zdania spośród wariantów <b>A</b> i <b>B</b> oraz jego poprawne uzasadnienie spośród wariantów <b>1</b> i <b>2</b>.",
     "warianty": [
         {"zdanie": "Gdy ciężarek mija położenie równowagi, jego energia kinetyczna jest",
          "wybor": ["największa,", "najmniejsza,"], "poprawny_wybor": 0,
          "powody": ["prędkość ciężarka jest wtedy największa.", "zmiana długości sprężyny jest wtedy największa."], "poprawny_powod": 0},
         {"zdanie": "Gdy ciężarek znajduje się w skrajnym położeniu, jego energia kinetyczna jest",
          "wybor": ["najmniejsza,", "największa,"], "poprawny_wybor": 0,
          "powody": ["ciężarek na chwilę się zatrzymuje, więc jego prędkość jest równa zero.", "zmiana długości sprężyny jest wtedy najmniejsza."], "poprawny_powod": 0},
     ],
     "zrodlo": S + " 44 zad.2"},
]

# zadania P/F, które w serii 2 dostały nowe zdania (wymuszają ≥2 nowe zdania, gdy generator dostaje --seria 2)
PF_ZADANIA = {"1": "1-pf", "2": "2-pf", "3": "3-pf"}


def dopisz(baza):
    """Dokłada do `baza` nowe zdania P/F i zadania (idempotentnie, po id). Zwraca liczbę dopisanych elementów."""
    zad = baza["zadania"]
    ids = {z["id"] for z in zad}
    n = 0
    for r, tid in PF_ZADANIA.items():
        t = next(z for z in zad if z["id"] == tid)
        t["seria"] = SER
        have = {p["id"] for p in t["pula"]}
        for p in PF_NOWE[r]:
            if p["id"] not in have:
                t["pula"].append(p)
                n += 1
    for z in NOWE:
        if z["id"] not in ids:
            zad.append(z)
            n += 1
    return n
