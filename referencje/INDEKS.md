# Archiwum referencyjne — Wojewódzki Konkurs Przedmiotowy z Historii

Zbiór oryginalnych arkuszy i kluczy Kuratorium Oświaty w Bydgoszczy z lat 2017/2018–2025/2026.
Służy do **kalibracji** nowych wariantów testów: pokazuje realną strukturę, punktację, formy zadań
i poziom trudności. Nie wolno kopiować z niego pytań — wyłącznie wzorować się na formie.

## Zawartość katalogu

| Ścieżka | Opis |
| --- | --- |
| `arkusze/` | Oryginalne PDF-y (24 pliki, 12 kompletnych par arkusz + klucz) |
| `tekst/` | Warstwa tekstowa każdego PDF-u, do przeszukiwania przez `rg` |
| `regulamin-2025-2026-historia.pdf` / `.txt` | Regulamin szczegółowy na rok 2025/2026 |
| `PARAMETRY_ARKUSZY.txt` | Automatyczne zestawienie parametrów wszystkich arkuszy |

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
