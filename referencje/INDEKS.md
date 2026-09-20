# Archiwum referencyjne — Wojewódzki Konkurs Przedmiotowy z Historii

Zbiór oryginalnych arkuszy i kluczy z czterech kuratoriów: Bydgoszcz, lata 2017/2018–2025/2026
(`arkusze/`, płasko), Warszawa, etap szkolny, lata 2019/2020–2025/2026 (`arkusze/mazowieckie/`,
od 2026-09-20), Gdańsk, etap szkolny, lata 2018/2019–2025/2026 (`arkusze/pomorskie/`, od
2026-09-20) i Szczecin, etap szkolny, lata 2018/2019–2025/2026 (`arkusze/zachodniopomorskie/`,
od 2026-09-20). Główny zestaw (kujawsko-pomorski) służy wyłącznie do **kalibracji**: pokazuje
realną strukturę, punktację, formy zadań i poziom trudności, i nie wolno z niego kopiować pytań.
Pozostałe trzy zestawy mają **inny status** — zob. niżej.

## Zawartość katalogu

| Ścieżka | Opis |
| --- | --- |
| `arkusze/` | Oryginalne PDF-y kujawsko-pomorskie (24 pliki, 12 kompletnych par arkusz + klucz) |
| `arkusze/mazowieckie/` | Oryginalne PDF-y mazowieckie, etap szkolny 2019/2020–2025/2026 (14 plików, 7 par) |
| `arkusze/pomorskie/` | Oryginalne PDF-y pomorskie (Gdańsk), etap szkolny 2018/2019–2025/2026 (16 plików, 8 par) |
| `arkusze/zachodniopomorskie/` | Oryginalne PDF-y zachodniopomorskie (Szczecin), etap szkolny 2018/2019–2025/2026 (16 plików, 8 par; brak historii dla SP w paczce 2017/2018) |
| `tekst/` | Warstwa tekstowa arkuszy kujawsko-pomorskich, do przeszukiwania przez `rg` |
| `tekst/mazowieckie/` | Warstwa tekstowa arkuszy mazowieckich |
| `tekst/pomorskie/` | Warstwa tekstowa arkuszy pomorskich (klucz 2021/2022 ma pustą warstwę tekstową — to skan; treść odczytana ręcznie z PDF-u) |
| `tekst/zachodniopomorskie/` | Warstwa tekstowa arkuszy zachodniopomorskich |
| `regulamin-2025-2026-historia.pdf` / `.txt` | Regulamin szczegółowy na rok 2025/2026 (kujawsko-pomorski) |
| `PARAMETRY_ARKUSZY.txt` | Automatyczne zestawienie parametrów arkuszy kujawsko-pomorskich |
| `PARAMETRY_ARKUSZY_MAZOWIECKIE.txt` | To samo dla arkuszy mazowieckich (z zastrzeżeniami — inny format klucza) |

## Źródła mazowieckie, pomorskie i zachodniopomorskie — inny status niż główne archiwum

Mazowieckie pobrane z `https://konkursy.kuratorium.waw.pl/ko/form/907,Bank-zadan-konkursowych.html`,
pomorskie z `https://sp2.edu.gdansk.pl/pl/page/konkursy-1/wojewodzki-konkurs-historyczny-dla-szkol-podstawowych/testy-i-modele-odpowiedzi`,
zachodniopomorskie z `https://www.gov.pl/web/kuratorium-oswiaty-w-szczecinie/konkursy-przedmiotowe-zachodniopomorskiego-kuratora-oswiaty---archiwum`
(wszystkie trzy: etap szkolny, szkoła podstawowa; zachodniopomorskie publikuje materiały jako
paczki zip ze wszystkimi przedmiotami naraz — historię trzeba było z nich wypakować). W odróżnieniu
od archiwum kujawsko-pomorskiego, **decyzją zamawiającego z 2026-09-20 wolno z nich dosłownie
zapożyczać zadania**: do 30–50% zadań w nowym wariancie testu może pochodzić z tych źródeł
łącznie (ewentualnie z drobną redakcją), reszta musi być napisana od nowa — tak jak dotychczas.
Katalog wszystkich zadań z trzech źródeł, z klasyfikacją tematu, typu, punktacji i statusem
wykorzystania, jest w `output/bank_pytan_zewnetrznych.json` (536 pozycji: 190 mazowieckich,
106 pomorskich, 240 zachodniopomorskich). Ten plik jest źródłem prawdy o tym, co już zużyto —
przed wyborem zadania do nowego wariantu sprawdź w nim `status`, a po wykorzystaniu ustaw je na
`"uzyte"` i dopisz literę wariantu do `uzyte_w_wariantach`.

**Źródła pomorskie i zachodniopomorskie mają istotnie szerszy zakres materiału niż etap
szkolny w tym projekcie** — sięgają XIX i XX wieku (powstania narodowe, dwudziestolecie
międzywojenne, obie wojny światowe, PRL, a zachodniopomorskie nawet po Unię Europejską),
podczas gdy ten projekt generuje wyłącznie etap szkolny do 1795 r. Dlatego każda pozycja z tych
dwóch źródeł w banku ma dodatkowe pole `w_zakresie_1795` (true/false) — tylko pozycje `true`
wolno wykorzystać wprost; `false` są skatalogowane wyłącznie informacyjnie. Z 106 pozycji
pomorskich 80 mieści się w zakresie, z 240 zachodniopomorskich — 138. Uwaga: jedna pozycja
zachodniopomorska (2025/2026, zadanie 20, Legiony Polskie we Włoszech 1797) jest oznaczona jako
`false` mimo pozornej bliskości zakresu — 1797 przekracza twardą granicę `GRANICA_ZAKRESU = 1795`
z `tools/baza_pytan.py`, gdzie dokładnie to samo wydarzenie jest jedyną pozycją dopuszczonego
rozszerzenia rejonowego (z limitem 2 zadań/arkusz). Źródło mazowieckie w całości mieści się do
1795 r. (zweryfikowano ręcznie), więc nie ma tego pola.

Wszystkie trzy źródła liczą się w skali **50 punktów** (nie 100 jak kujawsko-pomorskie) — przy
zapożyczaniu zadania do własnego arkusza punktację trzeba przeliczyć na skalę 100-punktową,
a nie kopiować wprost z klucza. Numeracja zadań jest arabska (nie rzymska). Arkusze mazowieckie
deklarują 90 minut pracy, pomorskie i zachodniopomorskie 45–60 minut — żadne z nich nie
kalibruje czasu pracy dla tego projektu, tylko archiwum kujawsko-pomorskie (60 minut na etapie
szkolnym).

Zestawienie odtwarza polecenie:

```bash
python3 tools/analizuj_arkusze.py referencje/tekst
```

## Konwencja nazw — etap jest zakodowany w nazwie pliku

```
<rok>-<etap>-historia-<a|k>.pdf
   |      |               |
   |      |               +-- a = arkusz, k = klucz odpowiedzi
   |      +------------------ szkolny | rejonowy | wojewodzki
   +------------------------- rok szkolny
```

**Etap jest najważniejszym filtrem.** Zakres materiału, czas pracy i punktacja różnią się
między etapami, więc arkusza rejonowego nie wolno używać jako wzorca zakresu dla szkolnego.

Pliki z przedrostkiem `gim` (2017/2018) pochodzą sprzed reformy i dotyczą **gimnazjum**.
Nadają się wyłącznie jako wzorzec formy zadań, nigdy jako źródło zakresu materiału.

## Zakres materiału według etapu (regulamin 2025/2026, rozdz. IV)

| Etap | Zakres podstawy programowej dla klas 5–8 | Czas pracy |
| --- | --- | --- |
| I — szkolny | działy I–XVII, od cywilizacji starożytnych do walki o niepodległość w ostatnich latach XVIII w. | 60 minut |
| II — rejonowy | działy I–XXI, do powstania styczniowego włącznie | 60 minut |
| III — wojewódzki | działy I–XLI, do miejsca Polski w świecie współczesnym | 90 minut |

Na rok 2025/2026 etap wojewódzki ma dodatkowo zakres: „Czerwiec — miesiąc ważnych rocznic.
Krok ku wolności — protesty w 1956 i 1976 roku”.

Regulamin wymaga, aby arkusz na **każdym** etapie zawierał zadania hybrydowe (prawda/fałsz,
uzupełnianie luk, wybór, dopasowanie, podpis ilustracji, mapa) oraz analizę źródeł pisanych,
ikonograficznych, kartograficznych i statystycznych.

## Parametry archiwalnych arkuszy

| Rok | Etap | Zadań | Punktów | Czas |
| --- | --- | --- | --- | --- |
| 2017/2018 (gim) | rejonowy | 18 | 100 | 90 min |
| 2017/2018 (gim) | wojewódzki | 18 | 120 | 90 min |
| 2018/2019 | szkolny | 20 | 100 | 60 min |
| 2018/2019 | rejonowy | 17 | 100 | 90 min |
| 2019/2020 | szkolny | 21 | 100 | 60 min |
| 2019/2020 | rejonowy | 19 | 100 | 90 min |
| 2022/2023 | szkolny | 21 | 100 | 60 min |
| 2022/2023 | rejonowy | 20 | 100 | 60 min |
| 2023/2024 | szkolny | 19 | 100 | 60 min |
| 2023/2024 | rejonowy | 19 | 100 | 60 min |
| 2024/2025 | szkolny | 19 | 100 | 60 min |
| 2025/2026 | szkolny | 18 | 100 | 60 min |

Wnioski kalibracyjne dla etapu szkolnego:

- punktacja to **zawsze 100 punktów**, a czas pracy **zawsze 60 minut**;
- liczba zadań spada w kolejnych latach: 20–21 do 2022/2023, potem 18–19;
- pojedyncze zadanie jest warte najczęściej 3–6 punktów, maksymalnie 10;
- arkusze mają 8–14 stron, przy czym nowsze są dłuższe, bo zawierają więcej materiałów źródłowych;
- numeracja zadań jest rzymska, a punktacja zapisywana jako `Zadanie VII (0 – 5 p.)`.

Etap rejonowy skrócono z 90 do 60 minut począwszy od 2022/2023, mimo szerszego zakresu materiału.

## Rozbieżności wykryte w oryginałach

Materiały kuratoryjne zawierają błędy — poniższe wykryto porównując arkusz z kluczem:

| Rok, etap | Rozbieżność |
| --- | --- |
| 2019/2020, szkolny | zadanie XVIII: 7 p. w arkuszu, 6 p. w kluczu (klucz sumuje się do 99) |
| 2025/2026, szkolny | zadanie IV: 9 p. w arkuszu, 8 p. w kluczu (klucz sumuje się do 99) |

W kluczu 2024/2025 warstwa tekstowa PDF jest pofragmentowana i automatyczne parowanie numerów
z punktacją jest niewiarygodne. Ten plik należy sprawdzać wzrokowo w PDF, nie w `tekst/`.

Wniosek: archiwalnego klucza nie wolno przepisywać bez weryfikacji.

## Jak korzystać przy generowaniu nowego testu

1. Ustal etap, a następnie zawęź materiał do zakresu z tabeli powyżej.
2. Przejrzyj arkusze z tego samego etapu z 2–3 ostatnich lat, aby dobrać proporcje form zadań:

   ```bash
   rg -i 'zadanie [ivx]+ \(0' referencje/tekst/2025-2026-szkolny-historia-a.txt
   ```

3. Sprawdź, czy planowany temat nie powtarza się zbyt blisko poprzedniego roku:

   ```bash
   rg -i -l 'unia lubelska' referencje/tekst/*szkolny*
   ```

4. Zachowaj rozkład punktów typowy dla etapu i sumę 100 punktów.
5. Pytania formułuj od nowa. Archiwum jest wzorcem formy i trudności, nie bankiem pytań.
