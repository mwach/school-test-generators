# Testy z fizyki — Drgania (szkoła podstawowa)

Notatka ustaleń dla serii testów z działu „Drgania”. Każdy nowy test (2, 3, …) ma się
trzymać tych zasad — przeczytaj całość przed generowaniem. Nadrzędne zasady wspólne
całemu repo: [`../../AGENTS.md`](../../AGENTS.md). Format notatki wzorowany na
[`../../chemia/wodorotlenki/WYMAGANIA.md`](../../chemia/wodorotlenki/WYMAGANIA.md)
i [`../../matematyka/trojkaty2/WYMAGANIA.md`](../../matematyka/trojkaty2/WYMAGANIA.md).

## Pochodzenie i zasada tworzenia

- Zamawiający dodał 4 zdjęcia stron podręcznika z sekcji „Sprawdź się!” (rozdział
  „I. Drgania”): `IMG_2395.jpeg` (s. 13, rozdz. 1), `IMG_2396.jpeg` (s. 14, rozdz. 1),
  `IMG_2397.jpeg` (s. 22, rozdz. 2), `IMG_2398.jpeg` (s. 28, rozdz. 3). Leżą lokalnie w tym
  katalogu; to materiał chroniony prawem autorskim — **wzorzec formy, nie bank pytań**, i
  (jak w `matematyka/trojkaty2`) **nie są w repo** (decyzja zamawiającego 2026-10-09: skanów nie dodawać; wpis w `.gitignore`).
  Baza pytań `baza_pytan.json` jest już samodzielna — skany nie są potrzebne do generowania.
- **Seria 2** (2026-10-10): 4 kolejne zdjęcia „Sprawdź się!”. `IMG_2402.jpeg` (s. 34) i `IMG_2403.jpeg` (s. 35)
  pochodzą z **rozdziału 4 „Ruch drgający na wykresach”** (P/F o wykresie, odczyt A i T, ślad piasku na linijce,
  wykres z punktami = klatki filmu). `IMG_2404.jpeg` (s. 44) i `IMG_2405.jpeg` (s. 45) to **podsumowanie
  (Powtórzenie)** całego działu (P/F, quiz A/B+1/2 o energii kinetycznej ciężarka, pół okresu, młot 18 uderzeń/min,
  dwa wykresy K i L). Tak samo lokalnie, poza repo. Zadania dopisane w `tools/baza_seria2.py` (pole `seria: 2`;
  generator przy każdym uruchomieniu odtwarza je idempotentnie w `baza_pytan.json`).
- Tytuły rozdziałów 2 i 3 wywnioskowane z treści (na skanach ich nie widać):
  1. Drgania wokół nas, 2. Okres i częstotliwość drgań, 3. Energia w ruchu drgającym.
- **Baza pytań** `baza_pytan.json` jest tworzona przy pierwszym uruchomieniu
  `tools/generuj_test.py` (z `tools/baza_poczatkowa.py`, opartej na skanach) i od tego
  momentu jest źródłem zadań dla wszystkich kolejnych testów. Nowe zadania dopisuj do
  `baza_pytan.json` (zadania autorskie oznacz w polu `zrodlo` jako „autorskie, w stylu skanów”).
- Prośba: **podobne zadania ze zmienionymi danymi liczbowymi** — typ i forma jak na skanach,
  liczby i treść przeformułowane. Nie kopiuj danych liczbowych ze skanów 1:1.

## Wykresy x(t) i rysunki w serii 2

- Wykresy rysuje generator (SVG, `svg_wykres`): oś pionowa x (cm) co 0,5 cm (podpisy całkowite), oś pozioma t (s)
  z 8 równymi podziałami (podpisy na dole ramki) — okres/ okresy są zawsze wielokrotnością podziału, więc da się je
  odczytać dokładnie. Krzywa startuje z 0 (sin) albo ze skrajnego położenia (−cos).
- Wykres z kropkami (klatki filmu): kropki w chwilach (k+½)/fps — w jednym okresie jest dokładnie N = T·fps kropek
  (żadna nie leży na granicy okresu, więc zliczenie jest jednoznaczne).
- Dwa wykresy (K, L): amplitudy i okresy tak dobrane, żeby częstotliwości były „okrągłe” (okresy 0,5; 1; 2; 4 s);
  AK ≠ AL. Zadanie obliczeniowe i quiz z dwoma wykresami mają `kolizja: wykresy2` — nie wchodzą razem do testu.
- Ślad piasku: linijka 2–12 cm, ślad od x_min do x_max (kroki 0,5 cm), tolerancja odczytu ±0,1 cm.
- Okres wahadła **nie zależy od amplitudy** (zdanie P/F `2p14`, przy niewielkich wychyleniach).

## Struktura testu (od testu 4; testy 1–3 miały 3 rozdziały × 2 = 6 zadań)

- **4 rozdziały × 2 zadania = 8 zadań**, w kolejności rozdziałów: 1. Drgania wokół nas, 2. Okres i częstotliwość drgań,
  3. Energia w ruchu drgającym, 4. Ruch drgający na wykresach (tytuł rozdziału 4 wg skanu s. 34–35). Czas pracy: 60 minut.
- **Zadania z podsumowania (s. 44–45; pole `powtorzenie: true`, poza pulami rozdziałów) wchodzą do testu losowo
  zamiast jednego z zadań** — generator wstawia **jedno** takie zadanie na test, w miejsce losowego zadania w parze
  swojego rozdziału (P/F z powtórzenia — dowolnego rozdziału; zadania o dwóch wykresach — rozdz. 4, młot i pół
  okresu — rozdz. 2, ciężarek na sprężynie — rozdz. 3). Zadania z powtórzenia nie powtarzają się, dopóki są
  niewykorzystane; w kluczu mają dopisek „(powtórzenie)” przy źródle.
- Dwa zadania z jednego rozdziału mają **różne typy**; w całym teście występuje co najmniej po jednym zadaniu
  typu: **obliczenia** (min. 2), **P/F** (max. 2), **quiz** (wybór jednokrotny lub dwuczęściowy, także z rysunkiem).
  Zadania otwarte (krótka odpowiedź) są dopuszczalne.
- Kolejne testy nie powtarzają zadań z banku, dopóki w rozdziale są nieużyte
  (`historia_testow.json`); po wyczerpaniu rozdział startuje od nowa — wtedy zmieniają się
  dane liczbowe i kolejność odpowiedzi.
- Jedna wersja testu (bez grup A/B). Arkusz i **osobna karta odpowiedzi** to dwa pliki.
- Zadania, które nie mogą być razem w teście (ten sam odczyt z wykresu), mają wspólne pole `kolizja`.

| Typ | Zasada punktacji |
|---|---|
| P/F (4 zdania) | 4 poprawne = 2 pkt, 3 = 1 pkt, ≤ 2 = 0 |
| quiz (wybór jednokrotny) | 1 pkt |
| quiz dwuczęściowy (A/B + 1/2) | 1 pkt za wybór A/B + 1 pkt za uzasadnienie 1/2 |
| obliczenia | wg zadania (2–3 pkt): wzór/odczyt, podstawienie, wynik z jednostką |
| otwarte | 2 pkt (po 1 za każdy element odpowiedzi) |
| obliczenia z wykresem (klatki, dwa wykresy) | 3 pkt (odczyt / pośredni krok / wynik z jednostką) |

## Zasady merytoryczne (rozstrzygnięte)

- Fakty zgodne z podręcznikiem ze skanów; sprawdzone też w źródłach z klucza (Wikipedia pl).
- Ruch drgający analizujemy **bez oporów**, chyba że zdanie wprost mówi o oporach.
- Przyspieszenie ziemskie **g = 9,8 m/s²**; wyniki „do dwóch cyfr znaczących” liczone
  z zaokrągleniem half-up; generator odrzuca dane, dla których zaokrąglenie jest graniczne
  (np. …5 na drugiej cyfrze).
- Okres huśtawki „mija położenie równowagi co t” → T = 2t (dwa przejścia na okres).
- Nie używamy zdań o energii potencjalnej ciężarka na **pionowej** sprężynie
  (grawitacyjna + sprężysta — niejednoznaczne); dla sprężyny stosujemy wózek poziomy.
- Odczyt z linijki: dolna krawędź ciężarka, dokładność 0,1 cm; uznajemy ±0,1 cm.
- Dystraktory w quizach odpowiadają typowym błędom (odwrócenie f i T, pomylenie liczby
  drgań z czasem, mylenie amplitudy z rozmachem 2A, pomylenie prędkości z energią sprężystości).
- Zdania P/F, które nawzajem podpowiadają odpowiedź, są w bazie w jednej `grupa` —
  w teście wchodzi najwyżej jedno z grupy. Zadanie nie może podpowiadać innego zadania.

## Losowość klucza

- P/F: w zadaniu co najmniej jedno P i jedno F, wzór nie może być `PFPF`/`FPFP`.
- Quizy: kolejność opcji tasowana; litery poprawnych odpowiedzi nie mogą być wszystkie takie same.
- Kontrola działa automatycznie w generatorze (przed PDF) i przerywa generowanie przy błędzie.
- Po każdym tasowaniu klucz jest wyliczany z danych (nie ręcznie) — litera zawsze wskazuje
  właściwą opcję; mimo to przejrzyj klucz wzrokowo.

## Pliki i nazewnictwo

```
IMG_2395–2398.jpeg, IMG_2402–2405.jpeg   skany podręcznika (wzorzec formy; tylko lokalnie, w .gitignore)
WYMAGANIA.md                       ta notatka
drgania.css                        wspólny styl arkuszy i kart odpowiedzi
baza_pytan.json                    baza zadań (tworzona przy 1. uruchomieniu)
historia_testow.json               które zadania i z jakimi danymi poszły do testów
tools/baza_poczatkowa.py           definicja bazy zbudowana ze skanów
tools/baza_seria2.py               zadania i zdania P/F dopisane ze skanów IMG_2402–2405 (seria 2)
tools/generuj_test.py              generator: wybór zadań, dane, HTML, kontrola klucza, PDF
testy/test_drgania_N_arkusz.html/.pdf
testy/test_drgania_N_karta_odpowiedzi.html/.pdf
```

## Proces generowania

```bash
# nowy test (numer = kolejny wolny), z PDF
python3 fizyka/drgania/tools/generuj_test.py --pdf
# opcjonalnie: --wymus id,id (zadania, które mają wejść do testu), --numer N
# podgląd stron (poza repo) i obejrzenie każdej
swift historia/kuratorium/tools/pdf_to_png.swift fizyka/drgania/testy/<plik>.pdf <tmp>/podglad 0.9
```

Przed oddaniem: obejrzyj podgląd każdej strony (rysunki: linijka ze sprężyną i miska
z kulkami — czytelne etykiety, bez przycięć), sprawdź że karta odpowiedzi jest osobnym PDF-em.
Po wygenerowaniu i weryfikacji — commit + push (pamięć użytkownika: bez pytania).

## Historia testów

| Test | Data | Zadania (rozdział: id) | Klucz zamknięty |
|---|---|---|---|
| 1 | 2026-10-09 | 1: P/F (amplituda, ruch okresowy), quiz miska (najmniejsza prędkość); 2: obliczenia T→f (0,75 s), quiz okres (30 drgań/60 s); 3: obliczenia h z v (2,4 m/s), quiz wózek na sprężynie (B2) | P/F `PFFP`, 2 C, 4 C, 6 B2 |
| 2 | 2026-10-09 | 1: quiz bombka, obliczenia amplituda z linijki (2,0 cm); 2: P/F (okres, częstotliwość), obliczenia metronom (20 drgań/40 s); 3: P/F (energia), obliczenia v z h (45 cm) | P/F `PFPP`, `FPPP`; 1 A |
| 3 | 2026-10-10 | (jeszcze w układzie 3 rozdziały × 2) seria 2: 1: P/F (osie wykresu, amplituda z wykresu), obliczenia ślad piasku (3–8 cm); 2: obliczenia klatki filmu (T = 1,6 s, 16 kropek → 10 kl./s), quiz dwa wykresy K/L; 3: P/F (energia), quiz A/B+1/2 ciężarek w skrajnym położeniu | P/F `FPPF`, piasek 5,5 cm / 2,5 cm, 10 kl./s, quiz C, P/F `FPPP`, B1 |
| 4 | 2026-10-10 | **pierwszy test 4×2 = 8 zadań**, 15 pkt. 1: P/F z powtórzenia (zamiast zadania rozdz. 1), obliczenia amplituda z linijek (2,7 cm); 2: obliczenia huśtawka (3 s → 6 s), quiz kHz; 3: otwarte (miska), quiz wózek; 4: P/F (wykresy, klatki), quiz odczyt A i T z wykresu | P/F `PFFF`, 6 s, C, B2, P/F `PPFP`, A |
