"""Początkowa baza zadań z działu Drgania — zbudowana na podstawie skanów podręcznika
(IMG_2395–2398.jpeg, sekcje „Sprawdź się!”, s. 13, 14, 22, 28). Zapisywana do
baza_pytan.json przy pierwszym uruchomieniu generuj_test.py."""

ROZDZIALY = {
    "1": "Drgania wokół nas",
    "2": "Okres i częstotliwość drgań",
    "3": "Energia w ruchu drgającym",
}

S = "skan s."  # prefiks pola zrodlo


def pf(id_, r, tekst, prawda, uzas, zrodlo, grupa=None, **extra):
    d = {"id": id_, "tekst": tekst, "prawda": prawda, "uzasadnienie": uzas, "zrodlo": zrodlo}
    if grupa:
        d["grupa"] = grupa
    d.update(extra)
    return d


def pula_pf(r):
    if r == 1:
        return [
            pf("1p01", 1, "Ruch drgający to ruch, w którym ciało porusza się ze stałą prędkością tam i z powrotem po tym samym torze.", False,
               "Prędkość ciała drgającego się zmienia (w skrajnych położeniach jest równa zero).", S + " 13 zad.1.1", "predkosc"),
            pf("1p02", 1, "Podczas ruchu ciała drgającego jego prędkość w położeniu równowagi jest największa.", True,
               "W położeniu równowagi ciało ma największą energię kinetyczną, więc największą prędkość.", S + " 13 zad.1.2", "predkosc"),
            pf("1p03", 1, "Kolejka linowa poruszająca się tam i z powrotem między dwiema stacjami ruchem jednostajnym jest przykładem ciała w ruchu drgającym.", False,
               "Ruch drgający wymaga wychylenia z położenia równowagi i ruchu okresowego ze zmienną prędkością; kolejka porusza się ruchem jednostajnym.", S + " 13 zad.1.3"),
            pf("1p04", 1, "Amplituda drgań to odległość pomiędzy dwoma skrajnymi położeniami ciała drgającego.", False,
               "Amplituda to odległość od położenia równowagi do jednego ze skrajnych wychyleń; odległość między skrajami to 2A.", S + " 13 zad.1.4", "amplituda"),
            pf("1p05", 1, "Amplituda drgań to odległość od położenia równowagi do jednego ze skrajnych wychyleń ciała drgającego.", True,
               "Definicja amplitudy drgań.", S + " 13 (Podsumujmy!)", "amplituda"),
            pf("1p06", 1, "W skrajnych położeniach ciała drgającego jego prędkość chwilowo jest równa zero.", True,
               "W skrajnym położeniu ciało zmienia kierunek ruchu, więc na chwilę się zatrzymuje.", S + " 14 zad.5 (v = 0)"),
            pf("1p07", 1, "Położenie równowagi to położenie, w którym znajduje się nieruchome ciało przed rozpoczęciem ruchu drgającego.", True,
               "Definicja położenia równowagi.", S + " 13 (Podsumujmy!)"),
            pf("1p08", 1, "Ruch drgający jest ruchem okresowym — powtarza się w jednakowych odstępach czasu.", True,
               "Ruch drgający to ruch okresowy (cykliczny).", S + " 13 (Podsumujmy!)"),
            pf("1p09", 1, "Ciało drgające porusza się po tym samym torze tam i z powrotem.", True,
               "Tak opisuje ruch drgający podręcznik.", S + " 13 (Podsumujmy!)", grupa="predkosc"),
            pf("1p10", 1, "Huśtawka, struna gitary i ciężarek na sprężynie to przykłady ciał wykonujących ruch drgający.", True,
               "Każde z tych ciał porusza się okresowo wokół położenia równowagi.", "autorskie, w stylu skanów"),
            pf("1p11", 1, "Ciało drgające porusza się zawsze po okręgu.", False,
               "Ruch drgający odbywa się tam i z powrotem po tym samym torze (np. odcinek), nie po okręgu.", "autorskie, w stylu skanów"),
            pf("1p12", 1, "Wahadło wychylono o {x} cm od położenia równowagi i puszczono. Amplituda jego drgań wynosi {x2} cm.", False,
               "Amplituda jest równa wychyleniu początkowemu ({x} cm), a nie jego wielokrotności.",
               "autorskie, w stylu skanów", "amplituda",
               param={"x": [3, 4, 5, 6, 8, 10]}, pochodne=[["x2", "2*x"]],
               tekst_prawda="Wahadło wychylono o {x} cm od położenia równowagi i puszczono. Amplituda jego drgań wynosi {x} cm."),
        ]
    if r == 2:
        return [
            pf("2p01", 2, "Jednostka okresu jest taka sama jak jednostka czasu.", True,
               "Okres to czas jednego drgania, więc mierzymy go np. w sekundach.", S + " 22 zad.1.1", "jednostka_T"),
            pf("2p02", 2, "Jeżeli częstotliwość drgań huśtawki jest równa {f} Hz, to okres jej drgań jest równy {f} s.", False,
               "T = 1/f = 1/{f} Hz = {T} s, a nie {f} s.", S + " 22 zad.1.2", None,
               param={"f": [0.2, 0.25, 0.5, 2, 4, 5]}, pochodne=[["T", "1/f"]],
               tekst_prawda="Jeżeli częstotliwość drgań huśtawki jest równa {f} Hz, to okres jej drgań jest równy {T} s."),
            pf("2p03", 2, "Częstotliwość drgań możemy wyrażać w kHz.", True,
               "1 kHz = 1000 Hz; kiloherc jest wielokrotnością herca.", S + " 22 zad.1.3"),
            pf("2p04", 2, "Spośród dwóch ciał drgających większą częstotliwość ma to, które w tym samym czasie wykonuje więcej drgań.", True,
               "Częstotliwość to liczba drgań w jednostce czasu.", S + " 22 zad.1.4"),
            pf("2p05", 2, "Jednostką częstotliwości jest sekunda.", False,
               "Jednostką częstotliwości jest herc (1 Hz = 1/s); sekunda jest jednostką okresu.", "autorskie, w stylu skanów", "jednostka_T"),
            pf("2p06", 2, "Im większa częstotliwość drgań ciała, tym krótszy jest okres jego drgań.", True,
               "f = 1/T — wielkości odwrotnie proporcjonalne.", "autorskie, w stylu skanów", "zalezn"),
            pf("2p07", 2, "Im większa częstotliwość drgań ciała, tym dłuższy jest okres jego drgań.", False,
               "f = 1/T — im większa częstotliwość, tym krótszy okres.", "autorskie, w stylu skanów", "zalezn"),
            pf("2p08", 2, "Ciało, które wykonuje {N} drgań w ciągu {t} s, ma częstotliwość {f} Hz.", False,
               "f = N/t = {N}/{t} s = {fp} Hz.", "autorskie, w stylu skanów", None,
               param={"para": [[10, 5], [20, 4], [30, 6], [12, 3], [40, 8], [18, 6]]},
               pochodne=[["N", "para[0]"], ["t", "para[1]"], ["fp", "N/t"], ["f", "t/N"]],
               tekst_prawda="Ciało, które wykonuje {N} drgań w ciągu {t} s, ma częstotliwość {fp} Hz."),
            pf("2p09", 2, "Częstotliwość 1 Hz oznacza jedno pełne drganie w ciągu sekundy.", True,
               "1 Hz = 1 drganie na sekundę.", "autorskie, w stylu skanów"),
            pf("2p10", 2, "Okres drgań wyraża się w hercach.", False,
               "Okres jest czasem — wyraża się w sekundach; w hercach wyraża się częstotliwość.", "autorskie, w stylu skanów", "jednostka_T"),
            pf("2p11", 2, "Okres drgań to czas potrzebny na wykonanie jednego pełnego drgania.", True,
               "Definicja okresu drgań.", S + " 22 (Podsumujmy!)"),
            pf("2p12", 2, "Częstotliwość drgań i okres drgań są związane zależnością f = 1/T.", True,
               "Podstawowa zależność między f i T.", S + " 22 (Podsumujmy!)"),
        ]
    return [
        pf("3p01", 3, "Do opisu przemian energii w ruchu drgającym odbywającym się bez oporów ruchu można stosować zasadę zachowania energii mechanicznej.", True,
           "Bez oporów energia mechaniczna układu jest stała.", S + " 28 zad.1.1", "emech"),
        pf("3p02", 3, "Gdy kulka wahadła zbliża się do położenia równowagi, jej energia kinetyczna rośnie.", True,
           "Kulka przyspiesza — energia potencjalna zamienia się w kinetyczną.", S + " 28 zad.1.2", "kin"),
        pf("3p03", 3, "Gdy kulka wahadła oddala się od położenia równowagi, jej energia potencjalna rośnie.", True,
           "Kulka wznosi się i zwalnia — energia kinetyczna zamienia się w potencjalną.", S + " 28 zad.1.3", grupa="pot"),
        pf("3p04", 3, "Podczas drgań ciężarka zawieszonego na sprężynie energia potencjalna sprężystości jest stała.", False,
           "Zmienia się wraz ze zmianą długości sprężyny.", S + " 28 zad.1.4"),
        pf("3p05", 3, "Gdy kulka wahadła oddala się od położenia równowagi, jej energia kinetyczna rośnie.", False,
           "Kulka zwalnia, więc jej energia kinetyczna maleje.", "autorskie, w stylu skanów", "kin"),
        pf("3p06", 3, "W skrajnym położeniu wahadła energia kinetyczna kulki jest największa.", False,
           "W skrajnym położeniu prędkość jest równa zero, więc Ek = 0; największa jest energia potencjalna.", "autorskie, w stylu skanów", grupa="skraj"),
        pf("3p07", 3, "W położeniu równowagi energia kinetyczna kulki wahadła jest największa.", True,
           "Tam kulka ma największą prędkość.", "autorskie, w stylu skanów"),
        pf("3p08", 3, "Całkowita energia mechaniczna wahadła poruszającego się bez oporów jest w czasie ruchu stała.", True,
           "Zasada zachowania energii mechanicznej.", "autorskie, w stylu skanów", "emech"),
        pf("3p09", 3, "Gdy wózek przymocowany do poziomej sprężyny przechodzi przez położenie równowagi, energia sprężystości sprężyny jest największa.", False,
           "W położeniu równowagi sprężyna nie jest odkształcona — energia sprężystości jest najmniejsza (zero).", "autorskie, w stylu skanów"),
        pf("3p10", 3, "W ruchu drgającym z oporami energia mechaniczna układu maleje, a amplituda drgań się zmniejsza.", True,
           "Część energii zamienia się na energię wewnętrzną (ogrzewanie) — drgania gasną.", "autorskie, w stylu skanów"),
        pf("3p11", 3, "Gdy kulka wahadła zbliża się do skrajnego położenia, jej energia potencjalna maleje.", False,
           "Kulka wznosi się, więc jej energia potencjalna rośnie.", "autorskie, w stylu skanów", grupa="pot"),
        pf("3p12", 3, "W skrajnym położeniu wahadła cała jego energia mechaniczna jest energią potencjalną.", True,
           "Prędkość jest równa zero, więc Ek = 0.", "autorskie, w stylu skanów", grupa="skraj"),
    ]


def zadania():
    z = []
    for r in (1, 2, 3):
        z.append({
            "id": f"{r}-pf", "rozdzial": r, "typ": "pf", "pkt": 2,
            "polecenie": "Oceń prawdziwość zdań. Zakreśl <b>P</b>, jeśli zdanie jest prawdziwe, albo <b>F</b> — jeśli jest fałszywe.",
            "pula": pula_pf(r), "zrodlo": S + {1: " 13", 2: " 22", 3: " 28"}[r] + " zad.1",
        })

    # --- Rozdział 1 ---
    z.append({
        "id": "1-otw-przyklady", "rozdzial": 1, "typ": "otwarte", "pkt": 2,
        "polecenie": "Podaj dwa przykłady sytuacji (inne niż huśtawka, wahadło i ciężarek na sprężynie), w których obserwujemy ruch drgający.",
        "klucz": ["1 pkt — pierwszy poprawny przykład, 1 pkt — drugi poprawny przykład (różny od pierwszego)."],
        "odpowiedz": ["Uznajemy np.: struna gitary, membrana głośnika, igła maszyny do szycia, tłok w silniku, skoczek na trampolinie, "
                      "linijka zamocowana jednym końcem i odchylona, drzewo kołysane wiatrem, dziecko na koniku na sprężynie, kulka w misce.",
                      "Nie uznajemy ruchów jednostajnych (jazda samochodu, kolejka linowa) ani ruchu po okręgu."],
        "zrodlo": S + " 13 zad.2",
    })
    z.append({
        "id": "1-quiz-miska", "rozdzial": 1, "typ": "quiz_miska", "pkt": 1,
        "zrodlo": S + " 13 zad.3",
    })
    z.append({
        "id": "1-quiz-bombka", "rozdzial": 1, "typ": "quiz", "pkt": 1,
        "pytanie": "Dziecko wytrąciło z położenia równowagi bombkę choinkową wiszącą na nitce. Czy gdy bombka dotrze ponownie do położenia równowagi (bez uwzględniania oporów), to się zatrzyma?",
        "opcje": [
            {"tekst": "Nie, ponieważ w położeniu równowagi ma największą prędkość i dalej porusza się z powodu bezwładności.", "poprawna": True},
            {"tekst": "Tak, ponieważ w położeniu równowagi jest najniżej i ma tam najmniejszą energię.", "poprawna": False},
            {"tekst": "Tak, ponieważ wróciła do miejsca, w którym była na początku.", "poprawna": False},
            {"tekst": "Nie, ponieważ w położeniu równowagi ma największą energię potencjalną.", "poprawna": False},
        ],
        "uzasadnienie": "W położeniu równowagi bombka ma największą prędkość (największą energię kinetyczną), więc nie zatrzymuje się, tylko mija je i wychyla się w drugą stronę.",
        "zrodlo": S + " 14 zad.4",
    })
    z.append({
        "id": "1-obl-amplituda", "rozdzial": 1, "typ": "obliczenia", "pkt": 3, "rysunek": "linijka",
        "param": {"x0": {"od": 12.0, "do": 16.0, "krok": 0.1}, "A": {"od": 1.5, "do": 4.5, "krok": 0.1}, "kier": [1, -1]},
        "pochodne": [["xk", "round(x0 + kier*A, 1)"]],
        "warunek": "11.0 <= xk <= 19.0",
        "tekst": "Na ilustracji przedstawiono ciężarek zawieszony na sprężynie, uchwycony w dwóch momentach podczas drgań: w chwili, gdy jego prędkość była równa zero (po lewej), oraz w położeniu równowagi (po prawej). Odczytaj z linijek (w cm) położenia dolnej krawędzi ciężarka i wyznacz amplitudę drgań ciężarka.",
        "wynik": "A", "jednostka": "cm", "dokladnosc": 1,
        "rozwiazanie": ["Odczyty: położenie skrajne x = {xk} cm, położenie równowagi x₀ = {x0} cm.",
                        "A = |x − x₀| = |{xk} cm − {x0} cm| = {A} cm."],
        "punktacja": ["1 pkt — poprawne odczyty obu położeń (tolerancja ±0,1 cm)", "1 pkt — metoda: amplituda = odległość od położenia równowagi do skrajnego",
                      "1 pkt — poprawny wynik z jednostką"],
        "zrodlo": S + " 14 zad.5",
    })

    # --- Rozdział 2 ---
    z.append({
        "id": "2-obl-hustawka", "rozdzial": 2, "typ": "obliczenia", "pkt": 2,
        "param": {"t": [1, 1.5, 2, 2.5, 3, 4]}, "pochodne": [["T", "2*t"]],
        "tekst": "Uczniowie zauważyli, że huśtawka mija położenie równowagi dokładnie co {t} s. Ile wynosi okres jej drgań?",
        "wynik": "T", "jednostka": "s",
        "rozwiazanie": ["W czasie jednego pełnego drgania huśtawka mija położenie równowagi dwa razy (raz w każdą stronę).", "T = 2 · {t} s = {T} s."],
        "punktacja": ["1 pkt — zauważenie, że w jednym okresie są dwa przejścia przez położenie równowagi", "1 pkt — poprawny wynik z jednostką"],
        "zrodlo": S + " 22 zad.2",
    })
    z.append({
        "id": "2-obl-metronom", "rozdzial": 2, "typ": "obliczenia", "pkt": 2,
        "param": {"f": [0.5, 0.75, 1, 1.2, 1.5, 2, 2.5], "tm": [20, 40, 60, 120]},
        "pochodne": [["N", "round(f*tm)"], ["N2", "2*round(f*tm)"]],
        "warunek": "abs(f*tm - round(f*tm)) < 1e-9",
        "tekst": "Metronom mechaniczny wykonał w ciągu {tm} s {N} pełnych drgań, czemu towarzyszyło {N2} stuknięć. Oblicz częstotliwość drgań tego metronomu.",
        "wynik": "f", "jednostka": "Hz",
        "rozwiazanie": ["Jedno pełne drganie to dwa stuknięcia — do obliczeń bierzemy liczbę drgań.", "f = N / t = {N} / {tm} s = {f} Hz."],
        "punktacja": ["1 pkt — poprawna metoda (f = liczba drgań / czas, liczba drgań, nie stuknięć)", "1 pkt — poprawny wynik z jednostką"],
        "zrodlo": S + " 22 zad.3",
    })
    z.append({
        "id": "2-obl-T-na-f", "rozdzial": 2, "typ": "obliczenia", "pkt": 2,
        "param": {"obiekt": ["Samochód zabawka drga na sprężynach podtrzymujących jego osie.", "Igła maszyny do szycia porusza się ruchem drgającym.",
                             "Membrana małego głośnika wykonuje drgania.", "Tłok w modelu silnika porusza się ruchem drgającym."],
                  "T": [0.12, 0.16, 0.18, 0.24, 0.28, 0.35, 0.45, 0.6, 0.75]},
        "pochodne": [["f", "1/T"]],
        "tekst": "{obiekt} Okres tego ruchu jest równy {T} s. Oblicz częstotliwość drgań. Wynik podaj z dokładnością do dwóch cyfr znaczących.",
        "wynik": "f", "jednostka": "Hz", "cyfry": 2,
        "rozwiazanie": ["f = 1/T = 1 / {T} s ≈ {f} Hz."],
        "punktacja": ["1 pkt — wzór f = 1/T i podstawienie", "1 pkt — wynik z dokładnością do 2 cyfr znaczących i jednostką"],
        "zrodlo": S + " 22 zad.4",
    })
    z.append({
        "id": "2-obl-f-na-T", "rozdzial": 2, "typ": "obliczenia", "pkt": 2,
        "param": {"obiekt": ["ubijaka do gruntu", "membrany głośnika", "wibratora w telefonie", "młota udarowego"],
                  "f": [20, 25, 40, 45, 60, 75, 80, 90, 120, 150]},
        "pochodne": [["T", "1/f"]],
        "tekst": "Częstotliwość drgań {obiekt} wynosi {f} Hz. Oblicz okres drgań. Wynik podaj z dokładnością do dwóch cyfr znaczących.",
        "wynik": "T", "jednostka": "s", "cyfry": 2,
        "rozwiazanie": ["T = 1/f = 1 / {f} Hz ≈ {T} s."],
        "punktacja": ["1 pkt — wzór T = 1/f i podstawienie", "1 pkt — wynik z dokładnością do 2 cyfr znaczących i jednostką"],
        "zrodlo": S + " 22 zad.5",
    })
    z.append({
        "id": "2-quiz-kHz", "rozdzial": 2, "typ": "quiz", "pkt": 1,
        "param": {"k": [2, 3, 4, 5, 6, 0.5, 1.5, 2.5]},
        "pochodne": [["a", "round(k*1000, 6)"], ["b", "round(k*100, 6)"], ["c", "round(k/1000, 9)"], ["d", "round(k*10, 6)"]],
        "pytanie": "Częstotliwość drgań struny wynosi {k} kHz. Ile to herców?",
        "opcje": [{"tekst": "{a} Hz", "poprawna": True}, {"tekst": "{b} Hz", "poprawna": False},
                  {"tekst": "{c} Hz", "poprawna": False}, {"tekst": "{d} Hz", "poprawna": False}],
        "uzasadnienie": "1 kHz = 1000 Hz, więc {k} kHz = {a} Hz.",
        "zrodlo": "autorskie, w stylu skanów (s. 22 zad.1.3)",
    })
    z.append({
        "id": "2-quiz-okres", "rozdzial": 2, "typ": "quiz", "pkt": 1,
        "param": {"para": [[120, 60], [30, 60], [40, 10], [25, 50], [8, 2], [10, 20], [48, 12], [15, 60], [100, 25]]},
        "pochodne": [["N", "para[0]"], ["tm", "para[1]"], ["T", "tm/N"], ["inv", "N/tm"]],
        "pytanie": "Ciało drgające wykonało {N} pełnych drgań w czasie {tm} s. Okres drgań tego ciała jest równy:",
        "opcje": [{"tekst": "{T} s", "poprawna": True}, {"tekst": "{inv} s", "poprawna": False},
                  {"tekst": "{N} s", "poprawna": False}, {"tekst": "{tm} s", "poprawna": False}],
        "uzasadnienie": "T = t / N = {tm} s / {N} = {T} s. Odpowiedź „{inv} s” to wartość N/t (czyli częstotliwość w hercach), pomylona z okresem.",
        "zrodlo": "autorskie, w stylu skanów (s. 22)",
    })

    # --- Rozdział 3 ---
    z.append({
        "id": "3-otw-przemiany", "rozdzial": 3, "typ": "otwarte", "pkt": 2, "rysunek": "miska",
        "warianty": [
            {"polecenie": "Niewielka kulka porusza się ruchem drgającym na dnie kulistej miski. Opisz, jakie przemiany energii występują podczas ruchu kulki od punktu B do punktu A, a następnie od punktu C do punktu B.",
             "strzalka1": "B→A", "strzalka2": "C→B"},
            {"polecenie": "Niewielka kulka porusza się ruchem drgającym na dnie kulistej miski. Opisz, jakie przemiany energii występują podczas ruchu kulki od punktu B do punktu C, a następnie od punktu A do punktu B.",
             "strzalka1": "B→C", "strzalka2": "A→B"},
        ],
        "klucz": ["1 pkt — od B w górę (do skrajnego punktu): energia kinetyczna zamienia się w energię potencjalną (grawitacji).",
                  "1 pkt — od skrajnego punktu do B: energia potencjalna zamienia się w energię kinetyczną."],
        "odpowiedz": ["B→A (lub B→C): energia kinetyczna → energia potencjalna.", "C→B (lub A→B): energia potencjalna → energia kinetyczna.",
                      "Uznajemy też wzmiankę, że suma obu energii (energia mechaniczna) jest stała."],
        "zrodlo": S + " 28 zad.2",
    })
    z.append({
        "id": "3-obl-h", "rozdzial": 3, "typ": "obliczenia", "pkt": 2,
        "param": {"v": [0.5, 0.6, 0.7, 0.8, 1.2, 1.5, 1.8, 2.0, 2.4, 2.5]},
        "pochodne": [["h", "v**2/(2*9.8)"]],
        "tekst": "Gdy kulka wahadła przechodzi przez położenie równowagi, jej prędkość jest równa {v} m/s. Oblicz, na jaką maksymalną wysokość (ponad położenie równowagi) wzniesie się ta kulka. Przyjmij, że przyspieszenie ziemskie ma wartość 9,8 m/s². Pomiń opory ruchu. Wynik podaj z dokładnością do dwóch cyfr znaczących.",
        "wynik": "h", "jednostka": "m", "cyfry": 2,
        "rozwiazanie": ["Z zasady zachowania energii mechanicznej: E_k = E_p, czyli mv²/2 = mgh, stąd h = v²/(2g).",
                        "h = ({v} m/s)² / (2 · 9,8 m/s²) ≈ {h} m."],
        "punktacja": ["1 pkt — zapis zasady zachowania energii i wzór na h", "1 pkt — poprawny wynik (2 cyfry znaczące) z jednostką (uznajemy też w cm)"],
        "zrodlo": S + " 28 zad.3",
    })
    z.append({
        "id": "3-obl-v", "rozdzial": 3, "typ": "obliczenia", "pkt": 2,
        "param": {"hc": [10, 15, 20, 30, 35, 40, 45, 50]},
        "pochodne": [["v", "(2*9.8*hc/100)**0.5"], ["hm", "hc/100"]],
        "tekst": "Oblicz, jaką prędkość początkową należy nadać siedzisku huśtawki, znajdującemu się w położeniu równowagi, aby wychyliło się tak, że jego maksymalna wysokość wyniesie {hc} cm. Przyjmij, że przyspieszenie ziemskie ma wartość 9,8 m/s². Pomiń opory ruchu. Wynik podaj z dokładnością do dwóch cyfr znaczących.",
        "wynik": "v", "jednostka": "m/s", "cyfry": 2,
        "rozwiazanie": ["Z zasady zachowania energii: mv²/2 = mgh, stąd v = √(2gh); h = {hc} cm = {hm} m.",
                        "v = √(2 · 9,8 m/s² · {hm} m) ≈ {v} m/s."],
        "punktacja": ["1 pkt — wzór v = √(2gh) i zamiana cm na m", "1 pkt — poprawny wynik (2 cyfry znaczące) z jednostką"],
        "zrodlo": S + " 28 zad.4",
    })
    z.append({
        "id": "3-quiz-wozek", "rozdzial": 3, "typ": "quiz_dwa", "pkt": 2,
        "wstep": "Wózek przymocowany do sprężyny porusza się w poziomie ruchem drgającym. Wybierz właściwe dokończenie zdania spośród wariantów <b>A</b> i <b>B</b> oraz jego poprawne uzasadnienie spośród wariantów <b>1</b> i <b>2</b>.",
        "warianty": [
            {"zdanie": "Gdy wózek przechodzi przez położenie, w którym jego odległość od położenia równowagi jest największa, energia sprężystości sprężyny jest",
             "wybor": ["największa,", "najmniejsza,"], "poprawny_wybor": 0,
             "powody": ["zmiana długości sprężyny jest największa.", "prędkość wózka jest największa."], "poprawny_powod": 0},
            {"zdanie": "Gdy wózek przechodzi przez położenie, w którym jego prędkość jest największa, energia sprężystości sprężyny jest",
             "wybor": ["najmniejsza,", "największa,"], "poprawny_wybor": 0,
             "powody": ["sprężyna nie jest wtedy ani rozciągnięta, ani ściśnięta.", "zmiana długości sprężyny jest największa."], "poprawny_powod": 0},
        ],
        "zrodlo": S + " 28 zad.5",
    })
    return z


def baza():
    return {"wersja": 1,
            "opis": "Baza zadań z działu Drgania zbudowana na podstawie skanów podręcznika (fizyka/drgania/IMG_2395–2398.jpeg).",
            "rozdzialy": ROZDZIALY, "zadania": zadania()}
