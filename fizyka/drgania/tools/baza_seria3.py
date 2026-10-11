"""Seria 3 (2026-10-11): więcej zadań z wykresów x(t) (amplituda, okres, częstotliwość) i ze sprężyną.
Zadania autorskie, w stylu skanów (formy z serii 1–2 z nowymi danymi). Pole "seria": 3.
dopisz(baza) jest idempotentne — wywoływane przez generuj_test.py."""

AUT = "autorskie, w stylu skanów"
SER = 3
PF_O = "Oceń prawdziwość zdań. Zakreśl <b>P</b>, jeśli zdanie jest prawdziwe, albo <b>F</b> — jeśli jest fałszywe."


def pf(id_, tekst, prawda, uzas, grupa=None, **extra):
    d = {"id": id_, "tekst": tekst, "prawda": prawda, "uzasadnienie": uzas, "zrodlo": AUT, "seria": SER}
    if grupa:
        d["grupa"] = grupa
    d.update(extra)
    return d


PF_NOWE = {
    "2-pf": [
        pf("2p17", "Okres drgań ciała wynosi {T} s. Częstotliwość tych drgań jest równa {T} Hz.", False,
           "f = 1/T = 1/{T} s = {f} Hz — częstotliwość jest odwrotnością okresu, a nie jego wartością.", "okres_f",
           param={"T": [0.2, 0.25, 0.5, 2, 4]}, pochodne=[["f", "1/T"]],
           tekst_prawda="Okres drgań ciała wynosi {T} s. Częstotliwość tych drgań jest równa {f} Hz."),
        pf("2p18", "Na wykresie położenia ciała od czasu w ciągu {t} s mieści się {n} pełnych drgań. Okres drgań tego ciała wynosi {Tz} s.", False,
           "T = t / n = {t} s / {n} = {T} s.", "okres_f",
           param={"para": [[4, 2], [5, 10], [10, 5], [4, 10], [8, 4], [5, 2]]},
           pochodne=[["n", "para[0]"], ["t", "para[1]"], ["T", "para[1]/para[0]"], ["Tz", "para[0]/para[1]"]],
           tekst_prawda="Na wykresie położenia ciała od czasu w ciągu {t} s mieści się {n} pełnych drgań. Okres drgań tego ciała wynosi {T} s."),
    ],
    "3-pf": [
        pf("3p16", "Gdy wózek na poziomej sprężynie przechodzi przez położenie równowagi, jego energia kinetyczna jest największa.", True,
           "W położeniu równowagi sprężyna jest nierozciągnięta, a cała energia układu jest energią kinetyczną wózka.", "wozek_eq"),
        pf("3p17", "Gdy wózek na poziomej sprężynie zbliża się do położenia równowagi, energia sprężystości sprężyny rośnie.", False,
           "Sprężyna jest coraz mniej odkształcona, więc energia sprężystości maleje (zamienia się w energię kinetyczną wózka).", "wozek_eq"),
        pf("3p18", "W skrajnym położeniu wózka sprężyna jest najbardziej rozciągnięta lub ściśnięta, więc energia sprężystości jest największa.", True,
           "Energia sprężystości zależy od odkształcenia sprężyny — jest największa przy największej zmianie jej długości.", "wozek_skraj"),
        pf("3p19", "W ruchu bez oporów suma energii kinetycznej wózka i energii sprężystości sprężyny jest stała.", True,
           "Bez oporów energia mechaniczna układu jest zachowana — energie tylko zamieniają się jedna w drugą."),
        pf("3p20", "Zwiększenie amplitudy drgań wózka na sprężynie powoduje wzrost największej energii kinetycznej wózka.", True,
           "Większa amplituda to większa energia całkowita układu, więc w położeniu równowagi energia kinetyczna jest większa.", "wozek_skraj"),
        pf("3p21", "Gdy wózek na sprężynie oddala się od położenia równowagi, jego energia kinetyczna rośnie.", False,
           "Wózek zwalnia, a energia kinetyczna zamienia się w energię sprężystości, więc maleje.", "wozek_eq"),
    ],
    "4-pf": [
        pf("4p03", "Na wykresie położenia ciała od czasu amplituda drgań wynosi {A} cm. Odległość między najwyższym a najniższym punktem wykresu jest równa {A} cm.", False,
           "Najwyższy punkt to +A, najniższy −A, więc ich odległość to 2A = {A2} cm.", "amplituda",
           param={"A": [1, 1.5, 2, 2.5, 3, 4]}, pochodne=[["A2", "2*A"]],
           tekst_prawda="Na wykresie położenia ciała od czasu amplituda drgań wynosi {A} cm. Odległość między najwyższym a najniższym punktem wykresu jest równa {A2} cm."),
        pf("4p04", "Częstotliwość drgań ciała, którego okres odczytany z wykresu wynosi {T} s, jest równa {T} Hz.", False,
           "f = 1/T = 1/{T} s = {f} Hz.", "okres_f",
           param={"T": [0.2, 0.25, 0.5, 2, 4]}, pochodne=[["f", "1/T"]],
           tekst_prawda="Częstotliwość drgań ciała, którego okres odczytany z wykresu wynosi {T} s, jest równa {f} Hz."),
        pf("4p05", "Im większa amplituda drgań ciała na sprężynie, tym większa jest jego częstotliwość drgań.", False,
           "Częstotliwość (okres) drgań nie zależy od amplitudy — zmienia się tylko wysokość wykresu, a nie odstęp między maksimami.", "amplituda"),
        pf("4p06", "Dwa ciała mają ten sam okres drgań, ale różne amplitudy. Ich częstotliwości są takie same.", True,
           "Częstotliwość to odwrotność okresu — przy tym samym okresie jest taka sama.", "okres_f"),
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
    # ---------- wykresy: amplituda, okres, częstotliwość ----------
    _obl("4-obl-wykres-f", 4, 3, rysunek="wykres", kolizja="wykresAT",
         param={"A": [1, 1.5, 2, 2.5, 3], "T": T_OKR, "faza": [0, 1]}, pochodne=[["f", "1/T"]],
         tekst="Na wykresie przedstawiono zależność położenia od czasu dla ciężarka zawieszonego na sprężynie. "
               "Odczytaj z wykresu amplitudę i okres drgań ciężarka, a następnie oblicz częstotliwość jego drgań.",
         wynik="f", jednostka="Hz", wynik_tekst="A = {A} cm; T = {T} s; f = {f} Hz",
         rozwiazanie=["Amplituda (największe wychylenie od położenia równowagi): A = {A} cm.",
                      "Okres odczytany z osi poziomej: T = {T} s.",
                      "Częstotliwość: f = 1/T = 1/{T} s = {f} Hz."],
         punktacja=["1 pkt — poprawna amplituda z jednostką (tolerancja ±0,1 cm)", "1 pkt — poprawny okres z jednostką",
                    "1 pkt — poprawna częstotliwość (f = 1/T) z jednostką"],
         zrodlo=AUT),
    _obl("2-obl-wykres-liczba", 2, 2, rysunek="wykres", kolizja="wykresAT",
         param={"A": [1, 1.5, 2, 2.5, 3], "T": T_OKR, "faza": [0, 1], "t": [8, 12, 16, 20]},
         pochodne=[["n", "t/T"]], warunek="(t/T) % 1 == 0",
         tekst="Na wykresie przedstawiono zależność położenia od czasu dla ciężarka drgającego na sprężynie. Odczytaj z wykresu okres drgań, "
               "a następnie oblicz, ile pełnych drgań wykona ten ciężarek w czasie {t} s.",
         wynik="n", jednostka="drgań", wynik_tekst="T = {T} s; {n} drgań",
         rozwiazanie=["Okres odczytany z osi poziomej: T = {T} s.", "Liczba drgań: n = t / T = {t} s / {T} s = {n}."],
         punktacja=["1 pkt — poprawny odczyt okresu", "1 pkt — poprawna liczba drgań (n = t / T)"],
         zrodlo=AUT),
    {"id": "2-quiz-wykres-f", "rozdzial": 2, "typ": "quiz", "pkt": 1, "seria": SER, "rysunek": "wykres", "kolizja": "wykresAT",
     "param": {"A": [1, 1.5, 2, 2.5, 3], "T": T_OKR, "faza": [0, 1]},
     "pochodne": [["f", "1/T"], ["f2", "2/T"], ["f3", "1/(2*T)"]],
     "pytanie": "Na wykresie przedstawiono zależność położenia od czasu dla kulki poruszającej się ruchem drgającym. Częstotliwość drgań tej kulki jest równa:",
     "opcje": [{"tekst": "{f} Hz", "poprawna": True}, {"tekst": "{T} Hz", "poprawna": False},
               {"tekst": "{f2} Hz", "poprawna": False}, {"tekst": "{f3} Hz", "poprawna": False}],
     "uzasadnienie": "Okres odczytany z wykresu to {T} s, więc f = 1/T = {f} Hz. {T} Hz to pomylenie częstotliwości z okresem, "
                     "{f2} Hz to wynik dla okresu o połowę krótszego, a {f3} Hz — dla okresu dwa razy dłuższego.",
     "zrodlo": AUT},
    {"id": "4-quiz-wykres-Esp", "rozdzial": 4, "typ": "quiz", "pkt": 1, "seria": SER, "rysunek": "wykres",
     "param": {"A": [1, 1.5, 2, 2.5, 3], "T": [0.8, 1.2, 1.6, 2.0, 2.4], "faza": [0], "k": [1, 3]},
     "pochodne": [["tq", "round(k*T/4, 2)"], ["t2", "round(T/2, 2)"]],
     "pytanie": "Na wykresie przedstawiono zależność położenia od czasu dla wózka przymocowanego do poziomej sprężyny (położenie równowagi: x = 0). "
                "W której z podanych chwil energia sprężystości sprężyny jest największa?",
     "opcje": [{"tekst": "t = {tq} s", "poprawna": True}, {"tekst": "t = 0 s", "poprawna": False},
               {"tekst": "t = {t2} s", "poprawna": False}, {"tekst": "t = {T} s", "poprawna": False}],
     "uzasadnienie": "Energia sprężystości jest największa, gdy odkształcenie sprężyny jest największe, czyli gdy wózek ma największe wychylenie (|x| = A): t = {tq} s. "
                     "W chwilach 0 s, {t2} s i {T} s wózek jest w położeniu równowagi (x = 0), gdzie energia sprężystości jest najmniejsza.",
     "zrodlo": AUT},
    {"id": "3-quiz-wykres-Ek", "rozdzial": 3, "typ": "quiz", "pkt": 1, "seria": SER, "rysunek": "wykres", "kolizja": "wykresAT",
     "param": {"A": [1, 1.5, 2, 2.5, 3], "T": [0.8, 1.2, 1.6, 2.0, 2.4], "faza": [0], "c": [2, 4, 6]},
     "pochodne": [["tc", "round(c*T/4, 2)"], ["q1", "round(T/4, 2)"], ["q3", "round(3*T/4, 2)"], ["q5", "round(5*T/4, 2)"]],
     "pytanie": "Na wykresie przedstawiono zależność położenia od czasu dla ciężarka drgającego bez oporów (położenie równowagi: x = 0). "
                "W której z podanych chwil energia kinetyczna ciężarka jest największa?",
     "opcje": [{"tekst": "t = {tc} s", "poprawna": True}, {"tekst": "t = {q1} s", "poprawna": False},
               {"tekst": "t = {q3} s", "poprawna": False}, {"tekst": "t = {q5} s", "poprawna": False}],
     "uzasadnienie": "Energia kinetyczna jest największa w położeniu równowagi (x = 0, prędkość największa): t = {tc} s. "
                     "W chwilach {q1} s, {q3} s i {q5} s ciężarek jest w skrajnym położeniu (|x| = A) i na chwilę się zatrzymuje.",
     "zrodlo": AUT},
    {"id": "4-quiz-wykresy-KL", "rozdzial": 4, "typ": "quiz", "pkt": 1, "seria": SER, "rysunek": "wykres2", "kolizja": "wykresy2",
     "param": PARA_KL,
     "pochodne": [["TK", "para[0]"], ["TL", "para[1]"],
                  ["kk", "para[1]/para[0] if para[1] > para[0] else para[0]/para[1]"], ["kk2", "2*kk"],
                  ["w", "'większa' if para[0] < para[1] else 'mniejsza'"], ["wp", "'mniejsza' if para[0] < para[1] else 'większa'"]],
     "pytanie": "Dwa ciężarki (K i L) poruszają się ruchem drgającym. Na wykresie przedstawiono zależność położenia od czasu dla obu ciężarków. "
                "Częstotliwość drgań ciężarka K jest:",
     "opcje": [{"tekst": "{kk} razy {w} niż częstotliwość drgań ciężarka L.", "poprawna": True},
               {"tekst": "{kk} razy {wp} niż częstotliwość drgań ciężarka L.", "poprawna": False},
               {"tekst": "{kk2} razy {w} niż częstotliwość drgań ciężarka L.", "poprawna": False},
               {"tekst": "{kk2} razy {wp} niż częstotliwość drgań ciężarka L.", "poprawna": False}],
     "uzasadnienie": "Okresy: T<sub>K</sub> = {TK} s, T<sub>L</sub> = {TL} s. Częstotliwość jest odwrotnością okresu, więc ciało o krótszym okresie "
                     "ma większą częstotliwość — częstotliwość ciężarka K jest {kk} razy {w} niż ciężarka L.",
     "zrodlo": AUT},
    # ---------- sprężyna ----------
    _obl("1-obl-droga", 1, 3, rysunek="linijka",
         param={"x0": {"od": 12.0, "do": 16.0, "krok": 0.1}, "A": {"od": 1.5, "do": 4.5, "krok": 0.5}, "kier": [1, -1]},
         pochodne=[["xk", "round(x0 + kier*A, 1)"], ["s4", "round(4*A, 1)"]],
         warunek="11.0 <= xk <= 19.0",
         tekst="Na ilustracji przedstawiono ciężarek zawieszony na sprężynie, uchwycony w dwóch momentach podczas drgań: w chwili, gdy jego prędkość była równa zero (po lewej), "
               "oraz w położeniu równowagi (po prawej). Odczytaj z linijek (w cm) położenia dolnej krawędzi ciężarka, wyznacz amplitudę drgań, "
               "a następnie oblicz drogę, jaką przebywa ciężarek w czasie jednego pełnego drgania.",
         wynik="s4", jednostka="cm", dokladnosc=1, wynik_tekst="A = {A} cm; droga w czasie jednego drgania: {s4} cm",
         rozwiazanie=["Odczyty: położenie skrajne x = {xk} cm, położenie równowagi x₀ = {x0} cm.",
                      "A = |x − x₀| = |{xk} cm − {x0} cm| = {A} cm.",
                      "W czasie jednego pełnego drgania ciężarek przebywa drogę równą 4 amplitudom: s = 4 · {A} cm = {s4} cm."],
         punktacja=["1 pkt — poprawna amplituda (odczyty ±0,1 cm)", "1 pkt — zauważenie, że droga w jednym drganiu to 4A",
                    "1 pkt — poprawny wynik z jednostką"],
         zrodlo=AUT),
    _obl("2-obl-sprezyna-nT", 2, 2,
         param={"para": [[10, 4], [20, 10], [8, 2], [15, 6], [12, 3], [5, 10], [10, 5]]},
         pochodne=[["n", "para[0]"], ["t", "para[1]"], ["T", "para[1]/para[0]"], ["f", "para[0]/para[1]"]],
         tekst="Ciężarek zawieszony na sprężynie wykonał {n} pełnych drgań w czasie {t} s. Oblicz okres oraz częstotliwość drgań tego ciężarka.",
         wynik="T", jednostka="s", wynik_tekst="T = {T} s; f = {f} Hz",
         rozwiazanie=["Okres: T = t / n = {t} s / {n} = {T} s.", "Częstotliwość: f = n / t = {n} / {t} s = {f} Hz (kontrola: f = 1/T = {f} Hz)."],
         punktacja=["1 pkt — poprawny okres z jednostką (T = t / n)", "1 pkt — poprawna częstotliwość z jednostką"],
         zrodlo=AUT),
    _obl("3-obl-sprezyna-Ek", 3, 2,
         param={"m": [0.2, 0.5, 1, 2], "v": [1, 2, 3, 4]}, pochodne=[["E", "0.5*m*v*v"]],
         tekst="Wózek o masie {m} kg, przymocowany do poziomej sprężyny, porusza się ruchem drgającym (pomiń opory ruchu). W położeniu równowagi jego prędkość wynosi {v} m/s. "
               "Oblicz energię kinetyczną wózka w tym położeniu, a następnie podaj, ile wynosi energia sprężystości sprężyny w skrajnym położeniu wózka.",
         wynik="E", jednostka="J", wynik_tekst="E<sub>k</sub> = {E} J; energia sprężystości w skrajnym położeniu = {E} J",
         rozwiazanie=["E<sub>k</sub> = m·v² / 2 = {m} kg · ({v} m/s)² / 2 = {E} J.",
                      "Bez oporów energia mechaniczna jest stała. W skrajnym położeniu wózek się zatrzymuje (E<sub>k</sub> = 0), więc cała energia jest energią sprężystości: {E} J."],
         punktacja=["1 pkt — poprawna energia kinetyczna (wzór, podstawienie, wynik z jednostką)",
                    "1 pkt — wniosek: energia sprężystości w skrajnym położeniu jest równa energii kinetycznej w położeniu równowagi"],
         zrodlo=AUT),
    {"id": "3-quiz-sprezyna2", "rozdzial": 3, "typ": "quiz_dwa", "pkt": 2, "seria": SER,
     "wstep": "Wózek przymocowany do poziomej sprężyny porusza się ruchem drgającym (pomiń opory ruchu). Wybierz właściwe dokończenie zdania spośród wariantów <b>A</b> i <b>B</b> "
              "oraz jego poprawne uzasadnienie spośród wariantów <b>1</b> i <b>2</b>.",
     "warianty": [
         {"zdanie": "Gdy wózek zbliża się do położenia równowagi, jego energia kinetyczna",
          "wybor": ["rośnie,", "maleje,"], "poprawny_wybor": 0,
          "powody": ["energia sprężystości sprężyny zamienia się w energię kinetyczną wózka.", "energia kinetyczna wózka zamienia się w energię sprężystości sprężyny."], "poprawny_powod": 0},
         {"zdanie": "Gdy wózek oddala się od położenia równowagi, jego prędkość",
          "wybor": ["maleje,", "rośnie,"], "poprawny_wybor": 0,
          "powody": ["energia kinetyczna wózka zamienia się w energię sprężystości sprężyny.", "zmiana długości sprężyny maleje."], "poprawny_powod": 0},
         {"zdanie": "Gdy zwiększymy amplitudę drgań wózka, jego największa prędkość",
          "wybor": ["wzrośnie,", "nie zmieni się,"], "poprawny_wybor": 0,
          "powody": ["energia całkowita układu jest wtedy większa.", "energia sprężystości w skrajnym położeniu nie zależy od amplitudy."], "poprawny_powod": 0},
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
