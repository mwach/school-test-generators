"""Seria 5 (2026-10-12): kolejne zadania z wykresów x(t) (amplituda, okres, częstotliwość) i ze sprężyną.
Zadania autorskie, w stylu skanów. Pole "seria": 5. dopisz(baza) jest idempotentne."""

AUT = "autorskie, w stylu skanów"
SER = 5


def pf(id_, tekst, prawda, uzas, grupa=None, **extra):
    d = {"id": id_, "tekst": tekst, "prawda": prawda, "uzasadnienie": uzas, "zrodlo": AUT, "seria": SER}
    if grupa:
        d["grupa"] = grupa
    d.update(extra)
    return d


PF_NOWE = {
    "2-pf": [
        pf("2p20", "Ciężarek na sprężynie wykonuje {f} pełnych drgań w ciągu sekundy. Okres jego drgań wynosi {f} s.", False,
           "Częstotliwość f = {f} Hz, więc okres T = 1/f = 1/{f} Hz = {T} s.", "okres_f",
           param={"f": [2, 4, 5, 10]}, pochodne=[["T", "1/f"]],
           tekst_prawda="Ciężarek na sprężynie wykonuje {f} pełnych drgań w ciągu sekundy. Okres jego drgań wynosi {T} s."),
    ],
    "3-pf": [
        pf("3p26", "Bez oporów największa energia kinetyczna wózka na poziomej sprężynie jest równa energii sprężystości sprężyny w skrajnym położeniu wózka.", True,
           "Energia mechaniczna jest stała: w skrajnym położeniu jest cała energią sprężystości, a w położeniu równowagi — cała energią kinetyczną.", "wozek_skraj"),
        pf("3p27", "Gdy wózek na poziomej sprężynie przechodzi przez położenie równowagi, sprężyna jest najbardziej rozciągnięta.", False,
           "W położeniu równowagi sprężyna nie jest odkształcona; najbardziej rozciągnięta (lub ściśnięta) jest w skrajnych położeniach wózka.", "wozek_eq"),
    ],
    "4-pf": [
        pf("4p10", "W czasie jednego okresu ciało przechodzi przez położenie równowagi dwa razy — na wykresie położenia od czasu widać to jako dwa punkty przecięcia krzywej z osią czasu.", True,
           "W ciągu jednego pełnego drgania ciało mija położenie równowagi raz w jedną i raz w drugą stronę.", "rownowaga"),
        pf("4p11", "Okres drgań to czas między dwoma kolejnymi przejściami ciała przez położenie równowagi (dwoma kolejnymi punktami przecięcia wykresu z osią czasu).", False,
           "Między dwoma kolejnymi przejściami przez położenie równowagi mija połowa okresu; okres to np. czas między dwoma kolejnymi maksimami.", "rownowaga,maks"),
        pf("4p12", "Jeśli okres drgań ciężarka zmaleje dwa razy, to na wykresie położenia od czasu w tym samym przedziale czasu zmieści się dwa razy więcej pełnych drgań.", True,
           "Liczba drgań w czasie t to n = t / T — przy dwa razy krótszym okresie jest dwa razy większa (częstotliwość rośnie dwukrotnie).", "okres_f"),
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
    # ---------- wykresy ----------
    _obl("4-obl-wykres-czas-n", 4, 3, rysunek="wykres", kolizja="wykresAT",
         param={"A": [1, 1.5, 2, 2.5, 3], "T": T_OKR, "faza": [0, 1], "n": [10, 15, 20, 30]}, pochodne=[["f", "1/T"], ["t", "n*T"]],
         tekst="Na wykresie przedstawiono zależność położenia od czasu dla ciężarka zawieszonego na sprężynie. Odczytaj z wykresu okres drgań, "
               "oblicz ich częstotliwość, a następnie oblicz, ile czasu zajmie ciężarkowi wykonanie {n} pełnych drgań.",
         wynik="t", jednostka="s", wynik_tekst="T = {T} s; f = {f} Hz; {n} drgań w czasie {t} s",
         rozwiazanie=["Okres odczytany z osi poziomej (np. odstęp między kolejnymi maksimami): T = {T} s.", "f = 1/T = 1/{T} s = {f} Hz.",
                      "Czas {n} drgań: t = n · T = {n} · {T} s = {t} s."],
         punktacja=["1 pkt — poprawny okres", "1 pkt — poprawna częstotliwość z jednostką", "1 pkt — poprawny czas z jednostką (t = n · T)"], zrodlo=AUT),
    {"id": "2-quiz-wykres-T", "rozdzial": 2, "typ": "quiz", "pkt": 1, "seria": SER, "rysunek": "wykres", "kolizja": "wykresAT",
     "param": {"A": [1, 1.5, 2, 2.5, 3], "T": [0.5, 2, 4], "faza": [0, 1]}, "pochodne": [["f", "1/T"], ["T2", "2*T"], ["Tp", "T/2"]],
     "pytanie": "Na wykresie przedstawiono zależność położenia od czasu dla ciężarka drgającego na sprężynie. Okres drgań tego ciężarka jest równy:",
     "opcje": [{"tekst": "{T} s", "poprawna": True}, {"tekst": "{Tp} s", "poprawna": False},
               {"tekst": "{T2} s", "poprawna": False}, {"tekst": "{f} s", "poprawna": False}],
     "uzasadnienie": "Okres to czas jednego pełnego drgania, np. odstęp między kolejnymi maksimami: T = {T} s. {Tp} s to czas między kolejnymi przejściami "
                     "przez położenie równowagi (pół okresu), {T2} s — czas dwóch pełnych drgań (cały wykres), a {f} to częstotliwość w Hz, nie okres.",
     "zrodlo": AUT},
    {"id": "4-quiz-wykres-dwa-A", "rozdzial": 4, "typ": "quiz", "pkt": 1, "seria": SER, "rysunek": "wykres2", "kolizja": "wykresy2",
     "param": PARA_KL, "warunek": "AK != AL",
     "pochodne": [["TK", "para[0]"], ["TL", "para[1]"], ["fK", "1/para[0]"], ["fL", "1/para[1]"],
                  ["wA", "'większą' if AK > AL else 'mniejszą'"], ["nA", "'mniejszą' if AK > AL else 'większą'"],
                  ["wf", "'większą' if para[0] < para[1] else 'mniejszą'"], ["nf", "'mniejszą' if para[0] < para[1] else 'większą'"]],
     "pytanie": "Dwa ciężarki (K i L) poruszają się ruchem drgającym. Na wykresie przedstawiono zależność położenia od czasu dla obu ciężarków. Wskaż poprawne zdanie.",
     "opcje": [{"tekst": "Ciężarek K drga z {wA} amplitudą i z {wf} częstotliwością niż ciężarek L.", "poprawna": True},
               {"tekst": "Ciężarek K drga z {wA} amplitudą i z {nf} częstotliwością niż ciężarek L.", "poprawna": False},
               {"tekst": "Ciężarek K drga z {nA} amplitudą i z {wf} częstotliwością niż ciężarek L.", "poprawna": False},
               {"tekst": "Ciężarek K drga z {nA} amplitudą i z {nf} częstotliwością niż ciężarek L.", "poprawna": False}],
     "uzasadnienie": "Amplitudy: A<sub>K</sub> = {AK} cm, A<sub>L</sub> = {AL} cm. Okresy: T<sub>K</sub> = {TK} s, T<sub>L</sub> = {TL} s, więc "
                     "f<sub>K</sub> = {fK} Hz, f<sub>L</sub> = {fL} Hz — krótszy okres oznacza większą częstotliwość.",
     "zrodlo": AUT},
    _obl("4-obl-wykres-dwa-n", 4, 3, rysunek="wykres2", kolizja="wykresy2",
         param=dict(PARA_KL, t=[8, 12, 16, 20]), warunek="AK != AL",
         pochodne=[["TK", "para[0]"], ["TL", "para[1]"], ["nK", "t/para[0]"], ["nL", "t/para[1]"], ["d", "abs(t/para[0] - t/para[1])"],
                   ["kto", "'K' if para[0] < para[1] else 'L'"]],
         tekst="Dwa ciężarki (K i L) zawieszone na sprężynach poruszają się ruchem drgającym. Na wykresie przedstawiono zależność położenia od czasu dla obu ciężarków. "
               "Odczytaj z wykresu okresy drgań obu ciężarków, oblicz, ile pełnych drgań wykona każdy z nich w czasie {t} s, i podaj, o ile więcej drgań wykona w tym czasie "
               "ciężarek drgający z większą częstotliwością.",
         wynik="d", jednostka="drgań", wynik_tekst="T<sub>K</sub> = {TK} s, T<sub>L</sub> = {TL} s; liczba drgań: K — {nK}, L — {nL}; ciężarek {kto} wykona o {d} więcej",
         rozwiazanie=["Okresy: T<sub>K</sub> = {TK} s, T<sub>L</sub> = {TL} s.",
                      "n<sub>K</sub> = t / T<sub>K</sub> = {t} s / {TK} s = {nK}; n<sub>L</sub> = t / T<sub>L</sub> = {t} s / {TL} s = {nL}.",
                      "Większą częstotliwość (krótszy okres) ma ciężarek {kto}; różnica liczby drgań: |{nK} − {nL}| = {d}."],
         punktacja=["1 pkt — poprawne okresy obu ciężarków", "1 pkt — poprawne liczby drgań obu ciężarków", "1 pkt — poprawna różnica i wskazanie ciężarka"],
         zrodlo=AUT),
    {"id": "3-quiz-wykres-v0", "rozdzial": 3, "typ": "quiz", "pkt": 1, "seria": SER, "rysunek": "wykres", "kolizja": "wykresAT",
     "param": {"A": [1, 1.5, 2, 2.5, 3], "T": [0.8, 1.2, 1.6, 2.0, 2.4], "faza": [0], "k": [1, 3, 5]},
     "pochodne": [["tq", "round(k*T/4, 2)"], ["t2", "round(T/2, 2)"], ["t3", "round(3*T/2, 2)"]],
     "pytanie": "Na wykresie przedstawiono zależność położenia od czasu dla ciężarka drgającego bez oporów (położenie równowagi: x = 0). "
                "W której z podanych chwil prędkość ciężarka jest równa zero?",
     "opcje": [{"tekst": "t = {tq} s", "poprawna": True}, {"tekst": "t = 0 s", "poprawna": False},
               {"tekst": "t = {t2} s", "poprawna": False}, {"tekst": "t = {t3} s", "poprawna": False}],
     "uzasadnienie": "Prędkość jest równa zero w skrajnym położeniu (|x| = A), gdzie ciężarek zawraca: t = {tq} s. W chwilach 0 s, {t2} s i {t3} s ciężarek "
                     "przechodzi przez położenie równowagi (x = 0) — tam jego prędkość jest największa.",
     "zrodlo": AUT},
    # ---------- sprężyna ----------
    _obl("1-obl-sprezyna-n", 1, 3, rysunek="linijka",
         param={"x0": {"od": 12.0, "do": 16.0, "krok": 0.1}, "A": {"od": 1.5, "do": 4.5, "krok": 0.5}, "kier": [1, -1], "nn": [2, 3, 4, 5]},
         pochodne=[["xk", "round(x0 + kier*A, 1)"], ["s", "round(4*A*nn, 1)"], ["dr", "'pełne drgania' if nn < 5 else 'pełnych drgań'"]], warunek="11.0 <= xk <= 19.0",
         tekst="Na ilustracji przedstawiono ciężarek zawieszony na sprężynie, uchwycony w dwóch momentach podczas drgań: w chwili, gdy jego prędkość była równa zero (po lewej), "
               "oraz w położeniu równowagi (po prawej). Odczytaj z linijek (w cm) położenia dolnej krawędzi ciężarka i wyznacz amplitudę drgań. "
               "Podczas obserwacji ciężarek przebył drogę {s} cm (pomiń opory ruchu). Oblicz, ile pełnych drgań wykonał w tym czasie.",
         wynik="nn", jednostka="drgania", wynik_tekst="A = {A} cm; {nn} {dr} (droga w jednym drganiu: 4A)",
         rozwiazanie=["Odczyty: położenie skrajne x = {xk} cm, położenie równowagi x₀ = {x0} cm; A = |x − x₀| = {A} cm.",
                      "W czasie jednego pełnego drgania ciężarek przebywa drogę 4A = 4 · {A} cm.",
                      "Liczba drgań: n = {s} cm / (4 · {A} cm) = {nn}."],
         punktacja=["1 pkt — poprawna amplituda (odczyty ±0,1 cm)", "1 pkt — zauważenie, że droga w jednym drganiu to 4A", "1 pkt — poprawna liczba drgań"],
         zrodlo=AUT),
    _obl("2-obl-sprezyna-tn", 2, 2,
         param={"T": [0.2, 0.25, 0.4, 0.5, 0.8], "n": [10, 20, 25, 50]}, pochodne=[["f", "1/T"], ["t", "round(n*T, 6)"]],
         tekst="Ciężarek zawieszony na sprężynie drga z okresem {T} s. Oblicz częstotliwość jego drgań oraz czas, w jakim wykona {n} pełnych drgań.",
         wynik="t", jednostka="s", wynik_tekst="f = {f} Hz; t = {t} s",
         rozwiazanie=["Częstotliwość: f = 1/T = 1/{T} s = {f} Hz.", "Czas {n} drgań: t = n · T = {n} · {T} s = {t} s."],
         punktacja=["1 pkt — poprawna częstotliwość z jednostką", "1 pkt — poprawny czas z jednostką"], zrodlo=AUT),
    _obl("3-obl-sprezyna-m", 3, 3,
         param={"m": [0.5, 1, 2, 4], "v": [1, 2, 3, 4]}, pochodne=[["E", "0.5*m*v*v"], ["v2", "v*v"]],
         tekst="Wózek przymocowany do poziomej sprężyny porusza się ruchem drgającym (pomiń opory ruchu). W skrajnym położeniu energia sprężystości sprężyny wynosi {E} J, "
               "a w położeniu równowagi prędkość wózka jest równa {v} m/s. Oblicz masę wózka.",
         wynik="m", jednostka="kg",
         rozwiazanie=["Bez oporów energia mechaniczna jest stała: energia kinetyczna w położeniu równowagi = energia sprężystości w skrajnym położeniu = {E} J.",
                      "m·v² / 2 = E, stąd m = 2E / v² = 2 · {E} J / ({v} m/s)² = 2 · {E} J / {v2} m²/s².", "m = {m} kg."],
         punktacja=["1 pkt — wniosek: E<sub>k</sub> w położeniu równowagi = energia sprężystości w skrajnym położeniu",
                    "1 pkt — poprawne przekształcenie wzoru (m = 2E / v²)", "1 pkt — poprawny wynik z jednostką"], zrodlo=AUT),
    {"id": "3-quiz-sprezyna4", "rozdzial": 3, "typ": "quiz_dwa", "pkt": 2, "seria": SER,
     "wstep": "Wózek przymocowany do poziomej sprężyny porusza się ruchem drgającym (pomiń opory ruchu). Wybierz właściwe dokończenie zdania spośród wariantów <b>A</b> i <b>B</b> "
              "oraz jego poprawne uzasadnienie spośród wariantów <b>1</b> i <b>2</b>.",
     "warianty": [
         {"zdanie": "Gdy wózek przechodzi przez położenie równowagi, energia sprężystości sprężyny jest",
          "wybor": ["równa zero,", "największa,"], "poprawny_wybor": 0,
          "powody": ["sprężyna nie jest wtedy odkształcona.", "wózek porusza się wtedy najszybciej."], "poprawny_powod": 0},
         {"zdanie": "Gdy wózek przechodzi przez położenie równowagi, jego prędkość jest",
          "wybor": ["największa,", "równa zero,"], "poprawny_wybor": 0,
          "powody": ["cała energia układu jest wtedy energią kinetyczną wózka.", "sprężyna jest wtedy najbardziej odkształcona."], "poprawny_powod": 0},
         {"zdanie": "Gdy wózek zbliża się do skrajnego położenia, energia kinetyczna wózka",
          "wybor": ["maleje,", "rośnie,"], "poprawny_wybor": 0,
          "powody": ["zamienia się w energię sprężystości sprężyny.", "sprężyna jest coraz mniej odkształcona."], "poprawny_powod": 0},
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
