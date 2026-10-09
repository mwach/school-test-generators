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
- Tytuły rozdziałów 2 i 3 wywnioskowane z treści (na skanach ich nie widać):
  1. Drgania wokół nas, 2. Okres i częstotliwość drgań, 3. Energia w ruchu drgającym.
- **Baza pytań** `baza_pytan.json` jest tworzona przy pierwszym uruchomieniu
  `tools/generuj_test.py` (z `tools/baza_poczatkowa.py`, opartej na skanach) i od tego
  momentu jest źródłem zadań dla wszystkich kolejnych testów. Nowe zadania dopisuj do
  `baza_pytan.json` (zadania autorskie oznacz w polu `zrodlo` jako „autorskie, w stylu skanów”).
- Prośba: **podobne zadania ze zmienionymi danymi liczbowymi** — typ i forma jak na skanach,
  liczby i treść przeformułowane. Nie kopiuj danych liczbowych ze skanów 1:1.

## Struktura testu (ustalona z zamawiającym)

- **3 rozdziały × 2 zadania = 6 zadań** w teście, w kolejności rozdziałów.
- Dwa zadania z jednego rozdziału mają **różne typy**; w całym teście występuje co najmniej
  po jednym zadaniu typu: **obliczenia**, **P/F**, **quiz** (wybór jednokrotny lub
  dwuczęściowy, także z rysunkiem). Zadania otwarte (krótka odpowiedź) są dopuszczalne.
- Kolejne testy nie powtarzają zadań z banku, dopóki w rozdziale są nieużyte
  (`historia_testow.json`); po wyczerpaniu rozdział startuje od nowa — wtedy zmieniają się
  dane liczbowe i kolejność odpowiedzi.
- Jedna wersja testu (bez grup A/B). Arkusz i **osobna karta odpowiedzi** to dwa pliki.

| Typ | Zasada punktacji |
|---|---|
| P/F (4 zdania) | 4 poprawne = 2 pkt, 3 = 1 pkt, ≤ 2 = 0 |
| quiz (wybór jednokrotny) | 1 pkt |
| quiz dwuczęściowy (A/B + 1/2) | 1 pkt za wybór A/B + 1 pkt za uzasadnienie 1/2 |
| obliczenia | wg zadania (2–3 pkt): wzór/odczyt, podstawienie, wynik z jednostką |
| otwarte | 2 pkt (po 1 za każdy element odpowiedzi) |

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
IMG_2395–2398.jpeg                 skany podręcznika (wzorzec formy; tylko lokalnie, w .gitignore)
WYMAGANIA.md                       ta notatka
drgania.css                        wspólny styl arkuszy i kart odpowiedzi
baza_pytan.json                    baza zadań (tworzona przy 1. uruchomieniu)
historia_testow.json               które zadania i z jakimi danymi poszły do testów
tools/baza_poczatkowa.py           definicja bazy zbudowana ze skanów
tools/generuj_test.py              generator: wybór zadań, dane, HTML, kontrola klucza, PDF
testy/test_drgania_N_arkusz.html/.pdf
testy/test_drgania_N_karta_odpowiedzi.html/.pdf
```

## Proces generowania

```bash
# nowy test (numer = kolejny wolny), z PDF
python3 fizyka/drgania/tools/generuj_test.py --pdf
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
