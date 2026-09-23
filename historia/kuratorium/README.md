# Testy treningowe — Wojewódzki Konkurs Przedmiotowy z Historii

Autorskie arkusze treningowe dla uczniów klas IV–VIII przygotowujących się do Wojewódzkiego
Konkursu Przedmiotowego z Historii organizowanego przez Kujawsko-Pomorskiego Kuratora Oświaty,
wraz z narzędziami, które pomagają je składać i sprawdzać.

Wygenerowane arkusze są **nieoficjalne** — nie pochodzą od kuratorium i nie są jego kluczami.
Odwzorowują natomiast strukturę, punktację i poziom trudności arkuszy archiwalnych: etap szkolny,
19 zadań, dokładnie 100 punktów, 60 minut pracy, zakres materiału zamknięty III rozbiorem (1795 r.).

Komplet zasad — zakres każdego etapu, parametry arkusza, typy zadań, wymagania wobec map,
kluczy i PDF-ów — opisuje [`SPECYFIKACJA_GENEROWANIA_TESTOW_HISTORYCZNYCH.md`](SPECYFIKACJA_GENEROWANIA_TESTOW_HISTORYCZNYCH.md).
To jest dokument nadrzędny; README tylko wprowadza w strukturę repozytorium.

## Gotowe warianty

Każdy wariant to para plików: arkusz dla ucznia (z kartą odpowiedzi) i osobny klucz.
Wszystko, co wygenerowane, leży w `output/` — HTML jako format roboczy, PDF jako docelowy,
pod tą samą nazwą. Wariant G to więc `output/test_szkolny_wariant_G.html`
i `output/test_szkolny_wariant_G.pdf`, a do nich `output/klucz_odpowiedzi_wariant_G.*`.

| Wariant | Pliki w `output/` | Uwagi |
| --- | --- | --- |
| A | `test_szkolny_wariant_A.pdf` | mapa poprawiona po tym, jak pierwsza wersja okazała się nieczytelna — jest wzorcem jakości map |
| B | `test_szkolny_wariant_B.pdf` | |
| C–F | `test_szkolny_wariant_{C,D,E,F}.pdf` | E jako pierwszy świadomie wykorzystał limit powtórzeń |
| G | `test_szkolny_wariant_G.pdf` | mapa portów hanzeatyckich, „Batory pod Pskowem” Matejki |
| H | `test_szkolny_wariant_H.pdf` | mapa wojny trzynastoletniej, „Kazanie Skargi” Matejki — pierwszy obraz spoza puli sześciu dotąd używanych reprodukcji |
| I | `test_szkolny_wariant_I.pdf` | mapa potopu szwedzkiego (cała Polska, nie tylko region), „Stańczyk” Matejki — ósmy wykorzystany obraz; pula siedmiu lokalnych reprodukcji jest już wyczerpana |
| J | `test_szkolny_wariant_J.pdf` | mapa trzech unii polsko-litewskich, pierwsze źródło ikonograficzne spoza twórczości Matejki — widok Warszawy Bernarda Bellotta; tylko 3 z 19 zadań to powtórzenia (16%), najniższy wynik dotychczas, dzięki trybowi `--rg` w `tools/baza_pytan.py` |
| K | `test_szkolny_wariant_K.pdf` | pierwszy wariant korzystający z `output/bank_pytan_zewnetrznych.json` — 9 z 19 zadań (47%) zaczerpnięto wprost z arkuszy mazowieckich, resztę napisano od nowa; mapa czterech bitew Rzeczpospolitej XVII w. (Kłuszyn, Chocim, Kircholm, Zbaraż), obraz „Bitwa pod Grunwaldem” Matejki jako źródło ikonograficzne (dziewiąte użycie, po raz pierwszy pod kątem krytyki źródła, nie samych faktów) |
| L | `test_szkolny_wariant_L.pdf` | pierwszy wariant korzystający jednocześnie ze wszystkich trzech zewnętrznych źródeł — 8 z 19 zadań (42%) zaczerpnięto z arkuszy mazowieckich (3), pomorskich (2) i zachodniopomorskich (3) łącznie, resztę napisano od nowa; mapa trzech bitew wojen grecko-perskich (Maraton, Termopile, Salamina), obraz „Hołd pruski” Matejki jako źródło ikonograficzne (ponowne użycie, pod kątem krytyki źródła jak w K) |
| M | `test_szkolny_wariant_M.pdf` | wszystkie 19 zadań napisane od nowa (bank zewnętrzny nieużyty); 4 powtórzenia tematu (21%); mapa sześciu średniowiecznych uniwersytetów (Bolonia, Paryż, Oksford, Praga, Kraków, Salamanka); pierwsze źródło ikonograficzne spoza malarstwa — tkanina z Bayeux (śmierć Harolda, `assets/bayeux_smierc_harolda.jpg`); źródła w kluczu instytucjonalne (ZPE, MHP, muzea, archiwa), nie tylko Wikipedia |

Materiały dodatkowe do nauki: `output/Daty_i_wydarzenia_do_nauki.pdf` (chronologia dla ucznia),
`output/Daty_i_wydarzenia_zestawienie.pdf` (pełne zestawienie)
oraz `output/Baza_potencjalnych_pytan.pdf`.

## Struktura repozytorium

W katalogu głównym są tylko dwa dokumenty i cztery katalogi — wszystko, co powstaje
z generowania, trafia do `output/`.

```
output/
  test_szkolny_wariant_*.html      arkusze robocze (źródło PDF-ów)
  klucz_odpowiedzi_wariant_*.html  klucze robocze
  *.pdf                            wersje docelowe arkuszy, kluczy i materiałów do nauki
  baza_pytan.json                  baza zagadnień z oceną ryzyka powtórzenia
  bank_pytan_zewnetrznych.json     katalog zadań z arkuszy mazowieckich, pomorskich i zachodniopomorskich (wolno je cytować wprost)
  previews/                        podglądy PNG stron — poza repozytorium (.gitignore)
assets/                            mapy SVG, bazowe mapy CC0, reprodukcje obrazów Matejki
tools/                             skrypty pomocnicze (python3 + Swift)
referencje/arkusze/                archiwalne arkusze i klucze kuratorium bydgoskiego (2017/2018–2025/2026)
referencje/arkusze/mazowieckie/    arkusze kuratorium warszawskiego, etap szkolny (2019/2020–2025/2026)
referencje/arkusze/pomorskie/      arkusze kuratorium gdańskiego, etap szkolny (2018/2019–2025/2026)
referencje/arkusze/zachodniopomorskie/  arkusze kuratorium szczecińskiego, etap szkolny (2018/2019–2025/2026)
referencje/tekst/                  warstwa tekstowa wszystkich czterech archiwów do przeszukiwania
```

Arkusze odwołują się do grafik ścieżką `../assets/…`, więc HTML-a nie należy przenosić
poza `output/` — inaczej mapy i reprodukcje przestaną się wyświetlać.

## Jak powstaje nowy wariant

1. **Dobór tematów.** Punktem wyjścia jest baza zagadnień, która dla każdego wydarzenia
   w zakresie konkursu podaje obszar (historia Polski / powszechna), typ zagadnienia
   i ryzyko powtórzenia względem wcześniejszych arkuszy:

   ```bash
   python3 tools/baza_pytan.py
   ```

   Skrypt czyta arkusze i klucze z `output/`, więc po dodaniu wariantu wystarczy
   uruchomić go ponownie — nic nie trzeba aktualizować ręcznie. Powtórzenia tematów są
   dopuszczalne do 30% zadań (przy 19 zadaniach: najwyżej 5), zawsze w innej formie zadania.

   Od wariantu K dochodzi drugie źródło: `output/bank_pytan_zewnetrznych.json` katalogujący
   536 zadań z arkuszy mazowieckich (`referencje/arkusze/mazowieckie/`, 190 pozycji), pomorskich
   (`referencje/arkusze/pomorskie/`, 106 pozycji) i zachodniopomorskich
   (`referencje/arkusze/zachodniopomorskie/`, 240 pozycji). Decyzją zamawiającego z 2026-09-20
   do 30–50% zadań nowego wariantu może pochodzić wprost stamtąd łącznie (z ewentualną drobną
   redakcją i przeliczeniem punktacji z pierwotnej skali 50 na skalę 100-punktową), reszta jak
   dotychczas musi być napisana od nowa. Źródła pomorskie i zachodniopomorskie sięgają też
   XIX–XX w. — wybieraj z nich wyłącznie pozycje z polem `w_zakresie_1795: true`. Po wybraniu
   zadania do wariantu ustaw jego `status` na `"uzyte"` i dopisz literę wariantu do
   `uzyte_w_wariantach`, żeby uniknąć powtórnego zapożyczenia tego samego zadania w kolejnym
   arkuszu.

2. **Mapa, jeśli zadanie jej wymaga.** `tools/zbuduj_mape.py` składa mapę z bazowej mapy Europy:
   wypełnia morze i ląd kontrastowo, wycisza granice państw, nanosi ponumerowane punkty
   wyliczone rachunkowo ze współrzędnych geograficznych. Kadr i punkty ustawia się w sekcji
   `__main__`; skrypt przerywa pracę, jeśli punkt wypada poza kadrem.

3. **Arkusz i klucz w HTML** — zapisane w `output/`, zgodnie ze specyfikacją, z rozliczeniem
   limitu powtórzeń w sekcji „Kontrola limitu powtórzeń (30%)” klucza.

4. **Kontrola losowości klucza** przed generowaniem PDF-ów. Narzędzie wykrywa przewidywalne
   klucze (ciągi A, B, C, D oraz 1, 2, 3, 4, pozycje stojące na swoim miejscu, długie serie
   w prawda/fałsz) i kończy się kodem błędu, gdy znajdzie problem:

   ```bash
   python3 tools/sprawdz_losowosc_klucza.py output/klucz_odpowiedzi_wariant_G.html
   ```

   Sprawdzany jest wyłącznie rozkład odpowiedzi, nie ich poprawność — po przetasowaniu banku
   trzeba osobno potwierdzić, że litera z klucza wskazuje właściwe hasło.

5. **PDF** — druk z Chrome w trybie headless:

   ```bash
   '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' \
     --headless --disable-gpu --no-pdf-header-footer \
     --print-to-pdf='output/test_szkolny_wariant_G.pdf' \
     "file://$PWD/output/test_szkolny_wariant_G.html"
   ```

6. **Przegląd składu** — render stron do PNG i obejrzenie ich, zwłaszcza map:

   ```bash
   swift tools/pdf_to_png.swift output/test_szkolny_wariant_G.pdf output/previews/G 0.72
   ```

   Podglądy PNG są celowo wyłączone z repozytorium (`.gitignore`) — odtwarza się je z HTML-a.

Przed oddaniem plików trzeba jeszcze potwierdzić, że suma punktów to dokładnie 100, każde
zadanie ma odpowiedź w kluczu, zakres nie wykracza poza 1795 r., a położenie każdego punktu
na mapie zgadza się z kluczem. Pełna lista kontrolna jest w specyfikacji, w sekcji
„Wymagania dotyczące PDF”.

## Narzędzia

| Skrypt | Do czego służy |
| --- | --- |
| `tools/baza_pytan.py` | baza zagadnień w zakresie konkursu z oceną ryzyka powtórzenia (`--json`, `--html`) |
| `tools/generuj_tabele_daty.py` | chronologiczne zestawienie dat i wydarzeń (`--do-nauki` dla wersji uczniowskiej) |
| `tools/zbuduj_mape.py` | składanie mapy zadania z bazowej mapy Europy |
| `tools/sprawdz_losowosc_klucza.py` | wykrywanie przewidywalnych kluczy odpowiedzi |
| `tools/analizuj_arkusze.py` | zestawienie etapu, liczby zadań, punktacji i czasu pracy arkuszy archiwalnych |
| `tools/extract_pdf_text.swift` | wyciąganie warstwy tekstowej z PDF-ów do przeszukiwania |
| `tools/pdf_to_png.swift` | render stron PDF do PNG, do przeglądu składu |

Skrypty korzystają wyłącznie z narzędzi dostępnych w systemie — `python3` oraz Swift z PDFKit —
bez instalowania dodatkowych zależności. Zakładają macOS (PDFKit, Chrome pod ścieżką `/Applications`).

## Źródła zadań (linki do banku pytań)

Strony, z których pobrano archiwalne arkusze wykorzystywane jako baza pytań
(`output/bank_pytan_zewnetrznych.json`) — zapisane tu, żeby przy kolejnym uzupełnianiu bazy
nie trzeba było ich szukać od nowa:

| Województwo | Strona | Zakres pobrany |
| --- | --- | --- |
| Mazowieckie | `https://konkursy.kuratorium.waw.pl/ko/form/907,Bank-zadan-konkursowych.html` | etap szkolny, historia, 2019/2020–2025/2026 |
| Pomorskie | `https://sp2.edu.gdansk.pl/pl/page/konkursy-1/wojewodzki-konkurs-historyczny-dla-szkol-podstawowych/testy-i-modele-odpowiedzi` | etap szkolny, 2018/2019–2025/2026 |
| Zachodniopomorskie | `https://www.gov.pl/web/kuratorium-oswiaty-w-szczecinie/konkursy-przedmiotowe-zachodniopomorskiego-kuratora-oswiaty---archiwum` | etap szkolny, paczki zip ze wszystkimi przedmiotami, 2018/2019–2025/2026 (2017/2018 bez historii dla SP) |

Kujawsko-pomorskie archiwum kalibracyjne w `referencje/arkusze/` (bez podkatalogu) nie ma
jednego źródła strony — pliki zebrano wcześniej, przed wprowadzeniem tej konwencji.

## Prawa do materiałów

Arkusze i klucze kujawsko-pomorskie w `referencje/arkusze/` są dokumentami Kujawsko-Pomorskiego
Kuratorium Oświaty i służą tu wyłącznie jako materiał referencyjny (kalibracja formy, nie
źródło pytań). Arkusze mazowieckie, pomorskie i zachodniopomorskie są dokumentami odpowiednich
kuratoriów (Warszawa, Gdańsk, Szczecin) i — decyzją zamawiającego z 2026-09-20 — służą też jako
bezpośrednie źródło części zadań w nowych wariantach (zob. „Jak powstaje nowy wariant” i
`referencje/INDEKS.md`). Bazowe mapy w `assets/` pochodzą z zasobów CC0 (Natural Earth),
reprodukcje obrazów Jana Matejki są w domenie publicznej.
