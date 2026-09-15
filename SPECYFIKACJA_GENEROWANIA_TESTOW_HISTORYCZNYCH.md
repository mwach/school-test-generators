# Specyfikacja generowania testów konkursowych z historii

## 1. Cel

Generowanie autorskich testów treningowych dla uczniów klas IV–VIII przygotowujących się
do Wojewódzkiego Konkursu Przedmiotowego z Historii organizowanego przez
Kujawsko-Pomorskiego Kuratora Oświaty.

Testy powinny:

- odpowiadać strukturze i trudności arkuszy z poprzednich lat;
- obejmować wyłącznie zakres właściwy dla wskazanego etapu;
- zawierać pytania autorskie, a nie kopie pytań archiwalnych;
- korzystać z wiarygodnych materiałów internetowych i podręczników szkolnych;
- mieć zweryfikowane odpowiedzi oraz jednoznaczną punktację;
- **być zawsze dostarczane jako PDF** — osobny plik z testem (wraz z kartą odpowiedzi)
  i osobny plik z kluczem odpowiedzi. HTML jest tylko formatem roboczym; oddanie samego
  HTML-a nie jest wykonaniem zadania.

### Powtarzalność zagadnień między wariantami

Unikatowość tematów **nie jest wymaganiem krytycznym**. Zagadnienia mogą powtarzać się
między testami, ale powtórzenia nie mogą przekroczyć **30% zadań** w arkuszu — przy 19 zadaniach
oznacza to najwyżej 5 zadań o temacie użytym już wcześniej.

Zasady stosowania limitu:

- powtórzeniem jest zadanie o tym samym zagadnieniu co zadanie we wcześniejszym wariancie,
  nawet jeśli treść pytań jest inna;
- pojedyncze nazwy własne (data, postać, bitwa) występujące jako element listy w innym
  zadaniu nie liczą się jako powtórzenie tematu;
- zadanie powtarzające temat musi mieć **inną formę** (np. wcześniej dopasowanie, teraz
  prawda/fałsz) oraz inne konkretne pozycje;
- pozostałe 70% zadań ma dotyczyć zagadnień nowych względem wcześniejszych wariantów;
- liczbę powtórzeń podaj w kluczu, w sekcji kontroli rozkładu treści.

Priorytet mają: zgodność z zakresem etapu, poprawność merytoryczna, suma 100 punktów
i równowaga historia powszechna/historia Polski. Jeżeli trzymanie się nowych tematów
wymuszałoby zadania spoza zakresu albo naciągane merytorycznie, wybierz powtórzenie
mieszczące się w limicie.

### Baza potencjalnych pytań (zacznij od niej)

Wszystkie wydarzenia mieszczące się w zakresie konkursu (do III rozbioru, 1795 r.) są zebrane
w bazie generowanej przez `tools/baza_pytan.py` — 129 pozycji z podziałem na obszar
(historia Polski / powszechna), typ zagadnienia i oceną **ryzyka powtórzenia** względem
arkuszy A–F:

| ryzyko | co znaczy | jak używać |
| --- | --- | --- |
| `brak` | zagadnienie nie wystąpiło dotąd nigdzie | bierz swobodnie |
| `niskie` | tylko wzmianka w komentarzu klucza, uczeń jej nie widział | bierz swobodnie |
| `średnie` | nazwa własna była w arkuszu, ale bez daty | można użyć, pytając o inny aspekt |
| `wysokie` | data była w treści arkusza | liczy się do limitu 30% |

Stan po wariancie F: `brak` 2, `niskie` 5, `średnie` 49, `wysokie` 73. **Pula samych dat jest
praktycznie wyczerpana** — świeżości kolejnych wariantów nie da się już budować na
nieużywanych datach, tylko na nowym ujęciu znanych wydarzeń: innym źródle, innej formie
zadania, innym aspekcie tego samego faktu. Naturalnym zapleczem są pozycje `średnie`:
nazwa pojawiła się w arkuszu, ale pytanie o samą datę jest wciąż nowe.

Ryzyko wyliczane jest automatycznie — skrypt szuka w arkuszach roku wydarzenia oraz rdzeni
jego nazw własnych. Przy zagadnieniach opisanych w arkuszu bardzo omownie ocena może być
zaniżona, dlatego przed użyciem pozycji zajrzyj do wskazanego wariantu. Jeśli trafisz na
takie pudło, dopisz brakujące hasło do `HASLA_DODATKOWE` w skrypcie.

Użycie:

```bash
python3 tools/baza_pytan.py           # podsumowanie i lista pozycji do wzięcia
python3 tools/baza_pytan.py --json    # output/baza_pytan.json do dalszego przetwarzania
python3 tools/baza_pytan.py --html    # widok do PDF (output/Baza_potencjalnych_pytan.pdf)
```

Po dodaniu nowego wariantu nie trzeba nic aktualizować ręcznie — skrypt czyta arkusze
i klucze z `output/`, więc wystarczy uruchomić go ponownie.

## 2. Zakres materiału według etapu

Konkurs ma trzy etapy o różnym zakresie i różnym czasie pracy. Przed generowaniem
czegokolwiek trzeba ustalić etap, bo pomyłka na tym poziomie unieważnia cały arkusz.
Zapisy regulaminu szczegółowego na rok 2025/2026 (rozdz. IV):

| Etap | Zakres podstawy programowej dla klas 5–8 | Czas pracy |
| --- | --- | --- |
| I — szkolny | działy I–XVII, do walki o niepodległość w ostatnich latach XVIII w. | 60 minut |
| II — rejonowy | działy I–XXI, do powstania styczniowego włącznie | 60 minut |
| III — wojewódzki | działy I–XLI, do miejsca Polski w świecie współczesnym | 90 minut |

Etap wojewódzki 2025/2026 ma dodatkowy zakres: „Czerwiec — miesiąc ważnych rocznic.
Krok ku wolności — protesty w 1956 i 1976 roku”.

Etap szkolny obejmuje działy I–XVII podstawy programowej historii dla klas 5–8:

1. Cywilizacje starożytne.
2. Bizancjum i świat islamu.
3. Średniowieczna Europa.
4. Społeczeństwo i kultura średniowiecznej Europy.
5. Polska w okresie wczesnopiastowskim.
6. Polska w okresie rozbicia dzielnicowego.
7. Polska w XIV i XV wieku.
8. Wielkie odkrycia geograficzne.
9. „Złoty wiek” w Polsce na tle europejskim.
10. Początki Rzeczypospolitej Obojga Narodów.
11. Rzeczpospolita Obojga Narodów i jej sąsiedzi w XVII wieku.
12. Europa w XVII i XVIII wieku.
13. Rzeczpospolita Obojga Narodów w I połowie XVIII wieku.
14. Powstanie Stanów Zjednoczonych.
15. Wielka rewolucja we Francji.
16. Rzeczpospolita w dobie stanisławowskiej.
17. Walka o utrzymanie niepodległości w ostatnich latach XVIII wieku.

Granicą chronologiczną etapu szkolnego jest III rozbiór Polski w 1795 r. Nie należy
wprowadzać zagadnień z epoki napoleońskiej ani XIX wieku. Dla etapu rejonowego granicą
jest powstanie styczniowe, a etap wojewódzki obejmuje całą podstawę programową.

## 3. Parametry arkusza

Wzorzec potwierdzony pomiarem oryginalnych arkuszy z `referencje/arkusze/`
(etap szkolny, roczniki 2018/2019–2025/2026):

- czas pracy: **60 minut**;
- maksymalna liczba punktów: **100** — bez wyjątku we wszystkich zmierzonych rocznikach;
- typowa liczba zadań: **18–21**, przy czym od 2023/2024 konsekwentnie **18–19**;
- zalecana liczba zadań dla nowych wariantów: **18 lub 19**;
- wartość pojedynczego zadania: najczęściej 3–6 punktów, maksymalnie 10;
- objętość arkusza: 8–14 stron, nowsze są dłuższe z powodu materiałów źródłowych;
- numeracja zadań rzymska, punktacja zapisywana jako `Zadanie VII (0 – 5 p.)`;
- orientacyjny podział punktów:
  - 48–53 pkt – historia powszechna;
  - 47–52 pkt – historia Polski;
- wszystkie odpowiedzi powinny być możliwe do zapisania w osobnej karcie odpowiedzi.

Każdy wariant powinien mieć własne oznaczenie i ziarno, np.:

```text
Wariant C
Ziarno wariantu: 2026-09-08-C
```

## 4. Zalecane typy zadań

Arkusz powinien być hybrydowy i zawierać przynajmniej sześć różnych form.

Najczęściej występujące formy:

- prawda/fałsz;
- dopasowanie postaci do wydarzeń;
- dopasowanie przyczyn i skutków;
- uzupełnianie luk;
- wybór jednej odpowiedzi;
- zadania chronologiczne i osie czasu;
- rozpoznawanie pojęć na podstawie definicji;
- analiza tekstu źródłowego;
- analiza dokładnej mapy; schemat kartograficzny stosuj tylko wtedy, gdy zadanie nie
  wymaga rozpoznawania rzeczywistego położenia miejsc, granic ani przebiegu wybrzeży;
- analiza obrazu, budowli, portretu lub innego źródła ikonograficznego;
- odczytywanie drzewa genealogicznego;
- tabela dotycząca wojen, bitew, dowódców i traktatów;
- krzyżówka lub zadanie z hasłem i wyjaśnieniem rozwiązania.

W jednym arkuszu należy uwzględnić:

- co najmniej jedno źródło pisane;
- co najmniej jedną mapę;
- co najmniej jedno źródło ikonograficzne;
- co najmniej jedno zadanie chronologiczne;
- co najmniej jedno zadanie dotyczące przyczyn i skutków;
- zadania z historii powszechnej oraz historii Polski.

### Losowanie kolejności odpowiedzi (obowiązkowe)

Klucz nie może dać się odgadnąć bez znajomości materiału. Najczęstszy błąd polega na tym, że
bank odpowiedzi układa się w tej samej kolejności co opisy, więc klucz wychodzi rosnący
(1 – A, 2 – B, 3 – C, …). Uczeń wpisujący alfabet z góry na dół zdobywa wtedy pełną punktację.
Ten sam błąd w zadaniu chronologicznym oznacza, że wydarzenia są już wypisane w kolejności
chronologicznej, a klucz to 1, 2, 3, 4, 5, 6.

Zasady dla każdej formy zadania:

- **dopasowanie (A–F)** — po napisaniu opisów przetasuj bank odpowiedzi. Klucz nie może być
  ciągiem rosnącym, najwyżej **jedna** pozycja może trafić na swoje miejsce (pozycja *n*
  z *n*-tą literą), a rosnący fragment nie może być dłuższy niż **dwie** pozycje;
- **odpowiedź zbędna** — nie umieszczaj jej zawsze na końcu banku. Rotuj ją między wariantami:
  raz w środku, raz na drugiej pozycji. Zbędna litera stale na końcu sama podpowiada, że
  pozostałe idą po kolei;
- **chronologia** — wypisz wydarzenia w kolejności innej niż chronologiczna. Klucz nie może być
  ani rosnący, ani malejący, i najwyżej jedno wydarzenie może stać na swojej właściwej pozycji;
- **mapa** — numery na mapie przypisz niezależnie od kolejności opisów A–E, tak aby klucz
  nie brzmiał „A – 1, B – 2, C – 3”;
- **prawda/fałsz** — obie wartości muszą wystąpić, a seria tej samej wartości nie może być
  dłuższa niż trzy pozycje. Nie grupuj wszystkich zdań prawdziwych na początku, a fałszywych
  na końcu; przeplataj je. To samo dotyczy klasyfikacji przyczyna/skutek;
- **wybór jednej odpowiedzi** — rozłóż poprawne odpowiedzi po wszystkich pozycjach; żadna
  pozycja nie może zbierać więcej niż około 40% poprawnych odpowiedzi w arkuszu.

Przetasowanie wykonuj przez zmianę przypisania liter do haseł w banku (albo kolejności
wypisania pozycji), a nie przez zmianę treści opisów — wtedy wystarczy zaktualizować jedną
linię w kluczu. Po każdej takiej zmianie **sprawdź merytorycznie**, czy litera z klucza wskazuje
nadal właściwe hasło; najprościej wypisać skryptem pary „opis → hasło z banku” i przeczytać je.

Kontrolę wykonuje `tools/sprawdz_losowosc_klucza.py` (opis w § 13). Uruchom je na kluczu przed
wygenerowaniem PDF-ów; narzędzie kończy się kodem błędu, jeżeli którykolwiek klucz jest
przewidywalny.

## 5. Poziom trudności

Poziom powinien być wyższy niż typowy sprawdzian szkolny, ale nie powinien wymagać
wiedzy akademickiej ani treści wykraczających poza podstawę programową.

Zalecany rozkład:

- 25–30% punktów – zadania podstawowe;
- 45–50% punktów – zadania średnio trudne;
- 20–25% punktów – zadania trudniejsze, wymagające analizy źródła, chronologii,
  rozróżnienia podobnych pojęć albo połączenia kilku informacji.

Typowe pułapki konkursowe:

- Karol Wielki został koronowany w 800 r., czyli jeszcze w VIII wieku;
- w 1025 r. koronowali się Bolesław Chrobry i Mieszko II – pytanie musi wskazywać,
  o którą koronację chodzi;
- seniorat określał sposób wyłaniania seniora, a pryncypat jego władzę zwierzchnią;
- I rozbiór nastąpił w 1772 r., ale sejm rozbiorowy obradował w 1773 r.;
- konfederacja targowicka poprzedziła II rozbiór;
- Magellan rozpoczął pierwszą wyprawę dookoła świata, lecz ukończył ją Juan Sebastián Elcano;
- w pytaniach genealogicznych trzeba odróżniać wuja od stryja oraz wnuka od siostrzeńca;
- należy odróżniać pokój w Oliwie, rozejm w Andruszowie lub Dywilinie, ugodę
  w Perejasławiu i pokój w Karłowicach.

## 6. Źródła

### Lokalne archiwum referencyjne (sprawdzaj je najpierw)

Katalog `referencje/` zawiera oryginalne arkusze i klucze Kuratorium Oświaty w Bydgoszczy
z lat 2017/2018–2025/2026 wraz z regulaminem. To najbliższy dostępny wzorzec, bliższy niż
materiały innych kuratoriów, więc kalibrację nowego wariantu zaczynaj właśnie od niego.

- `referencje/INDEKS.md` — opis zbioru, parametry arkuszy, wykryte rozbieżności;
- `referencje/arkusze/` — PDF-y w nazewnictwie `<rok>-<etap>-historia-<a|k>.pdf`;
- `referencje/tekst/` — warstwa tekstowa do przeszukiwania poleceniem `rg`;
- `referencje/regulamin-2025-2026-historia.pdf` — obowiązujący regulamin szczegółowy.

**Nazwa pliku koduje etap** (`szkolny`, `rejonowy`, `wojewodzki`). Do kalibracji zakresu
używaj wyłącznie plików z tego etapu, który generujesz; arkusze z innych etapów służą
najwyżej jako wzorzec formy zadań. Pliki z oznaczeniem `gim` (2017/2018) dotyczą gimnazjum
sprzed reformy i nie opisują obowiązującego zakresu materiału.

Archiwum jest wzorcem formy i trudności, nie bankiem pytań — treści zadań nie wolno kopiować.

### Źródła nadrzędne

1. Regulamin szczegółowy Konkursu Przedmiotowego z Historii:
   <https://sp-8.pl/pliki/2025-2026/konkursy/historia.pdf>
2. Katalog materiałów ZPE dla historii w klasach IV–VIII:
   <https://zpe.gov.pl/szukaj-ksztalcenie-ogolne?query=&stage=E2&subject=Historia+Szko%C5%82a+podstawowa+4-8>
3. Elektroniczne podręczniki i materiały dydaktyczne wskazane przez MEN:
   <https://www.gov.pl/web/edukacja/elektroniczne-wersje-podrecznikow-i-materialow-dydaktycznych>

### Archiwa konkursowe

- Kuratorium Oświaty w Bydgoszczy:
  <https://kuratorium.bydgoszcz.pl/konkursy-kuratora_archiwum/>
- Kuratorium Oświaty w Krakowie:
  <https://kuratorium.krakow.pl/category/rodzice-i-uczniowie/konkursy-przedmiotowe/>
- Kuratorium Oświaty w Łodzi:
  <https://www.kuratorium.lodz.pl/konkurs/materialy-konkursowe-7/>
- Kuratorium Oświaty w Opolu:
  <https://www.kuratorium.opole.pl/category/konkursy/konkursy-przedmiotowe/>
- Kuratorium Oświaty w Poznaniu — pakiet arkuszy i schematów 2024/2025:
  <https://ko.poznan.pl/wp-content/uploads/2025/06/wojewodzki-konkurs-historyczny.pdf>
- Kuratorium Oświaty w Warszawie — bank zadań konkursowych:
  <https://konkursy.kuratorium.waw.pl/ko/form/907,Bank-zadan-konkursowych.html>
- Kuratorium Oświaty w Olsztynie — arkusz i klucz 2025/2026:
  <https://www.ko.olsztyn.pl/wp-content/uploads/2025/12/historia-arkusz.pdf>
  oraz
  <https://www.ko.olsztyn.pl/wp-content/uploads/2025/12/historia-klucz.pdf>

Arkusze innych kuratoriów mogą służyć jako wzorzec formy i poziomu trudności.
Ich zakres nie może automatycznie zastępować zakresu konkursu kujawsko-pomorskiego.

Różnice, które należy uwzględnić:

- arkusze małopolskie zwykle trwają 90 minut i mogą obejmować całą podstawę programową;
- arkusze wielkopolskie zawierają dużo zadań wymagających uzasadnienia odpowiedzi
  konkretnym dowodem ze źródła, ale również treści regionalne;
- mazowiecki etap szkolny 2025/2026 kończy się na I połowie XVIII wieku, dlatego sam
  nie pokrywa działów XIV–XVII;
- warmińsko-mazurski arkusz 2025/2026 ma 24 zadania i 40 punktów na 60 minut,
  dzięki czemu jest dobrym wzorcem tempa, ale nie punktacji;
- zakres i punktację należy zawsze przeliczyć na wymagania kujawsko-pomorskie:
  60 minut, 100 punktów i cezura 1795 r.

### Przydatne źródła szczegółowe

- prawo rzymskie:
  <https://zpe.gov.pl/a/prawo-rzymskie/DfNBG4pvi>
- feudalizm:
  <https://zpe.gov.pl/watek/LPnuJIeI9D/1/b/system-feudalny-i-spoleczenstwo-stanowe/P1LSBJ8eY>
- pierwsi Piastowie:
  <https://zpe.gov.pl/watek/LP190LTbYE/46/b/wladcy-i-mieszkancy-polski-pierwszych-piastow/PCkgenqAe>
- wielkie odkrycia geograficzne:
  <https://zpe.gov.pl/watek/LP190LTbYE/58/a/skutki-odkryc-geograficznych/D1DOIUxUs>
- renesansowa Rzeczpospolita:
  <https://zpe.gov.pl/a/renesansowa-rzeczpospolita/DhUWg8Yms>
- unia lubelska:
  <https://zpe.gov.pl/watek/LP190LTbYE/62/a/powstanie-rzeczypospolitej-obojga-narodow-unia-lubelska-1569/D4FJvvhYP>
- akt unii lubelskiej w AGAD:
  <https://www.agad.gov.pl/Unia%20Lubelska/Unia%20lubelska%201569%20r.pdf>
- Konstytucja 3 maja:
  <https://zpe.gov.pl/a/konstytucja-3-maja/D14citlTB>
- tekst Ustawy Rządowej w Bibliotece Sejmowej:
  <https://libr.sejm.gov.pl/tek01/txt/kpol/1791.html>
- insurekcja kościuszkowska i III rozbiór:
  <https://zpe.gov.pl/a/przeczytaj/DyVjT4BRW>
- obraz „Rejtan. Upadek Polski”:
  <https://digitalizacja.zamek-krolewski.pl/obiekt-693-rejtan-upadek-polski>
- wektorowa mapa bazowa basenu Morza Śródziemnego, TheDastanMR, Wikimedia Commons,
  CC0 1.0:
  <https://commons.wikimedia.org/wiki/File:Blank_Map_of_Mediterranean_Sea_region.svg>

## 7. Zasady korzystania ze źródeł

1. Najpierw ustal zakres na podstawie obowiązującego regulaminu.
2. Arkusze archiwalne wykorzystuj do analizy struktury, nie do kopiowania pytań.
3. Każdą odpowiedź sprawdź przynajmniej w jednym źródle instytucjonalnym lub
   zatwierdzonym podręczniku.
4. Fakty potencjalnie niejednoznaczne sprawdź w dwóch niezależnych źródłach.
5. Cytaty skracaj wyłącznie z zaznaczeniem pominięć za pomocą `[...]`.
6. Przy uwspółcześnieniu pisowni źródła zaznacz to w podpisie.
7. Dla ilustracji podaj autora, tytuł, instytucję lub repozytorium oraz licencję.
8. Preferuj domenę publiczną, materiały instytucji publicznych i licencje Creative Commons.
9. Nie traktuj Wikipedii jako jedynego źródła weryfikacyjnego.

### Standard map konkursowych

Za wzorzec jakości przyjmij mapę Hanzy z wariantu G (`assets/hanza_wariant_G.svg`). Przy
zadaniach wymagających rozpoznawania miast, państw, granic lub wydarzeń przestrzennych:

0. **Wypełnij morze i ląd różnymi kolorami.** To najważniejszy pojedynczy zabieg. Mapa
   wariantu F miała ląd i morze białe, a granice państw tak samo grube jak linię brzegową,
   przez co nie czytała się jako mapa, tylko jako plątanina wielokątów — uczeń nie widział,
   gdzie jest woda. Hierarchia, która działa: morze wypełnione (`#cfe2ee`), ląd jasny
   (`#f7f3e8`), linia brzegowa gruba i ciemna, granice państw cienkie i jasnoszare.
   Realizuje to `tools/zbuduj_mape.py`.

1. Nie rysuj umownej linii brzegowej odręcznie. Użyj geograficznie poprawnej mapy
   bazowej, najlepiej w formacie wektorowym SVG.
2. Preferuj mapy z domeny publicznej albo na licencji CC0/Creative Commons,
   pochodzące z wiarygodnego repozytorium, np. Wikimedia Commons.
3. Na mapę bazową nanoś własną, edytowalną warstwę oznaczeń. Punkty powinny mieć
   wysoki kontrast, obwódkę i numery czytelne również w wydruku czarno-białym.
4. Dodaj strzałkę północy i krótką legendę, jeśli poprawiają orientację. Nie dodawaj
   nazw ani symboli, które zdradzają odpowiedź.
5. Pokaż cały obszar potrzebny do rozwiązania zadania. Nie używaj współczesnych granic
   politycznych, jeżeli nie są potrzebne albo mogłyby wprowadzać w błąd historyczny.
6. Każdy punkt, granicę i trasę sprawdź według atlasu lub współrzędnych geograficznych.
   Zgodność numerów z odpowiedziami w kluczu sprawdź osobno.
7. Pod mapą podaj autora mapy bazowej, repozytorium i licencję, a w wykazie źródeł
   zamieść aktywny adres strony pliku.
8. Po wygenerowaniu PDF obejrzyj rzeczywistą stronę arkusza, nie tylko plik źródłowy.
   Sprawdź ostrość konturów, położenie punktów, legendę, brak obcięć oraz czytelność
   przy typowym wydruku A4.
9. **Dobierz kadr o charakterystycznym zarysie.** Obszar z rozbudowaną linią brzegową
   (Bałtyk, Skandynawia, Półwysep Apeniński) uczeń rozpoznaje od razu; wycinek samego
   wnętrza kontynentu wygląda jak przypadkowa plama, nawet gdy jest geograficznie poprawny.
   Kadr Bałtyku z wariantu G to `viewBox="440 880 890 555"`.
10. Mapę wstawiaj szeroko — `max-width: 152mm`. Mapa o szerokości 88–96 mm (warianty E i F)
    jest za mała, by odczytać położenie punktów względem wybrzeża.

## 8. Klucz odpowiedzi

Klucz powinien być osobnym dokumentem i zawierać:

- odpowiedź do każdego elementu zadania;
- maksymalną liczbę punktów;
- sposób przyznawania punktów;
- dopuszczalne warianty nazw i pisowni;
- zasady oceniania odpowiedzi otwartych;
- ostrzeżenia dotyczące odpowiedzi pozornie poprawnych;
- sumę kontrolną 100 punktów;
- tabelę rozkładu tematycznego;
- wykaz źródeł z aktywnymi adresami URL;
- mapę przypisującą zadania do źródeł weryfikacyjnych.

Nie należy przyznawać połówek punktów, chyba że regulamin konkretnej edycji stanowi inaczej.

## 9. Wymagania dotyczące PDF

### Gdzie zapisywać pliki

Wszystko, co powstaje z generowania, trafia do `output/` — zarówno robocze HTML-e, jak i PDF-y,
a także `baza_pytan.json` i tabele dat. W katalogu głównym nie zapisujemy niczego; zostają tam
wyłącznie `README.md`, specyfikacja i katalogi `assets/`, `tools/`, `referencje/`, `output/`.

PDF powtarza nazwę źródłowego HTML-a, więc `output/test_szkolny_wariant_G.html` daje
`output/test_szkolny_wariant_G.pdf`. Dzięki temu nie powstają dwie kopie tego samego arkusza
pod różnymi nazwami; wcześniej takie duplikaty trzeba było sprzątać ręcznie.

Arkusze leżą o poziom niżej niż grafiki, więc odwołania do nich mają postać `../assets/…`.
Nowy arkusz musi trzymać tę konwencję, inaczej mapy i reprodukcje nie wyrenderują się w PDF.
Podglądy PNG idą do `output/previews/<wariant>/` i są wyłączone z repozytorium.

Test:

- format A4;
- czytelna strona tytułowa;
- pole na kod ucznia;
- instrukcja;
- czas pracy i maksymalna punktacja;
- punktacja przy każdym zadaniu;
- miejsce na odpowiedzi;
- osobna karta odpowiedzi;
- numer wariantu;
- informacja, że materiał jest nieoficjalnym arkuszem treningowym.

Klucz:

- format A4;
- odpowiedzi w kolejności zadań;
- czytelne wyróżnienie odpowiedzi;
- tabela źródeł;
- data sprawdzenia źródeł;
- informacja, że dokument nie jest oficjalnym kluczem kuratorium.

Przed przekazaniem plików należy sprawdzić:

- czy PDF otwiera się poprawnie;
- czy zawiera wszystkie strony i ilustracje;
- czy suma punktów wynosi dokładnie 100;
- czy liczba zadań zgadza się z instrukcją;
- czy każde zadanie ma odpowiedź w kluczu;
- czy zakres nie wykracza poza 1795 r.;
- czy mapy mają poprawne kontury i oznaczenia oraz są czytelne po wydrukowaniu;
- czy położenie każdego punktu na mapie zgadza się z odpowiedzią w kluczu;
- czy pytania nie zawierają niezamierzonych podpowiedzi.

## 10. Uwagi wynikające z analizy archiwalnych kluczy

Archiwalne dokumenty również mogą zawierać błędy. W lokalnym archiwum potwierdzono
konkretne przypadki:

| Rok, etap | Rozbieżność |
| --- | --- |
| 2019/2020, szkolny | zadanie XVIII: 7 p. w arkuszu, 6 p. w kluczu — klucz sumuje się do 99 |
| 2025/2026, szkolny | zadanie IV: 9 p. w arkuszu, 8 p. w kluczu — klucz sumuje się do 99 |

W kluczu 2024/2025 warstwa tekstowa PDF jest pofragmentowana, więc automatyczne parowanie
numerów zadań z punktacją daje błędne wyniki. Ten plik sprawdzaj wzrokowo w PDF.

Ogólne problemy obejmują:

- rozbieżności jednego punktu między arkuszem i kluczem;
- niepełne lub źle zeskanowane klucze;
- błędy redakcyjne w instrukcjach P/F;
- odpowiedzi alternatywne niewymienione w pierwotnym kluczu;
- zadania, w których pytanie nie rozstrzyga jednoznacznie między dwiema poprawnymi odpowiedziami.

Dlatego model nie może bezkrytycznie przepisywać klucza archiwalnego. Powinien niezależnie
sprawdzić odpowiedzi i usunąć niejednoznaczności przed wygenerowaniem PDF.

## 11. Gotowy prompt dla innego modelu

```text
Przygotuj autorski test treningowy dla etapu szkolnego Wojewódzkiego Konkursu
Przedmiotowego z Historii dla uczniów klas IV–VIII, zgodny z wymaganiami
Kujawsko-Pomorskiego Kuratora Oświaty.

Najpierw skalibruj się na lokalnym archiwum w katalogu `referencje/`:
- przeczytaj `referencje/INDEKS.md`;
- nazwa pliku koduje etap (`szkolny`, `rejonowy`, `wojewodzki`) — korzystaj z arkuszy
  tego etapu, który generujesz, bo zakres materiału i czas pracy różnią się między etapami;
- pomiń pliki `gim` z 2017/2018, bo dotyczą gimnazjum sprzed reformy;
- przeszukuj `referencje/tekst/` przez `rg`, żeby sprawdzić formy zadań z ostatnich lat
  i sprawdzić, które tematy już wystąpiły;
- traktuj archiwum jako wzorzec formy i trudności, nigdy jako bank pytań do skopiowania.

Zakres (etap szkolny):
- działy I–XVII podstawy programowej historii dla klas 5–8;
- od cywilizacji starożytnych do III rozbioru Polski w 1795 r.;
- bez epoki napoleońskiej i XIX wieku.

Gdyby polecenie dotyczyło innego etapu, zmień zakres: rejonowy obejmuje działy I–XXI
(do powstania styczniowego, 60 minut), a wojewódzki działy I–XLI (90 minut).

Parametry:
- 60 minut;
- 18–19 zadań;
- dokładnie 100 punktów;
- około połowy punktów z historii powszechnej i połowy z historii Polski;
- poziom i struktura zbliżone do arkuszy kuratoryjnych z poprzednich lat.

Zastosuj co najmniej sześć typów zadań, w tym obowiązkowo:
- analizę tekstu źródłowego;
- analizę mapy;
- analizę źródła ikonograficznego;
- chronologię;
- przyczyny i skutki;
- zadania pojęciowe;
- zadania prawda/fałsz lub dopasowanie.

Pytania muszą być nowe i nie mogą być kopiami z arkuszy archiwalnych. Arkusze
kuratoriów wykorzystaj jedynie jako wzorzec formy i trudności.

Losuj kolejność odpowiedzi. Klucz nie może dać się odgadnąć bez znajomości materiału:
- w zadaniach na dopasowanie przetasuj bank haseł, żeby klucz nie był ciągiem rosnącym
  (1 – A, 2 – B, 3 – C…); najwyżej jedna pozycja może trafić na swoje miejsce, a rosnący
  fragment nie może być dłuższy niż dwie pozycje;
- odpowiedzi zbędnej nie umieszczaj zawsze na końcu banku — rotuj jej pozycję;
- w zadaniu chronologicznym wypisz wydarzenia w kolejności innej niż chronologiczna,
  tak aby klucz nie brzmiał 1, 2, 3, 4, 5, 6;
- numery na mapie przypisz niezależnie od kolejności opisów A–E;
- w zadaniach prawda/fałsz przeplataj obie wartości i nie twórz serii dłuższych niż trzy;
- po każdym przetasowaniu sprawdź, czy litera z klucza wskazuje nadal właściwe hasło.

Unikatowość zagadnień nie jest wymaganiem krytycznym. Tematy mogą powtarzać się
z wcześniejszymi wariantami, ale najwyżej w 30% zadań (przy 19 zadaniach: maksymalnie 5).
Zadanie powtarzające temat musi mieć inną formę i inne konkretne pozycje. Jeśli trzymanie
się wyłącznie nowych tematów wymuszałoby zadania spoza zakresu etapu albo naciągane
merytorycznie, wybierz powtórzenie mieszczące się w limicie.

Wymagania dotyczące map:
- przy zadaniach lokalizacyjnych używaj geograficznie poprawnej mapy bazowej SVG,
  a nie odręcznego lub umownego schematu wybrzeży;
- preferuj domenę publiczną, CC0 lub Creative Commons i podaj autora, repozytorium,
  licencję oraz aktywny URL;
- dodaj własną warstwę numerowanych oznaczeń o wysokim kontraście, strzałkę północy
  i legendę, o ile nie zdradzają odpowiedzi;
- sprawdź położenie wszystkich punktów na podstawie atlasu lub współrzędnych oraz
  porównaj ich numery z kluczem;
- nie używaj współczesnych granic politycznych, jeśli nie są potrzebne;
- po wygenerowaniu obejrzyj właściwą stronę PDF w skali odpowiadającej wydrukowi A4
  i sprawdź ostrość, brak obcięć oraz czytelność w kolorze i skali szarości.

Korzystaj przede wszystkim z:
1. regulaminu konkursu kujawsko-pomorskiego;
2. katalogu ZPE dla historii w klasach IV–VIII:
   https://zpe.gov.pl/szukaj-ksztalcenie-ogolne?query=&stage=E2&subject=Historia+Szko%C5%82a+podstawowa+4-8
3. materiałów wskazanych przez MEN:
   https://www.gov.pl/web/edukacja/elektroniczne-wersje-podrecznikow-i-materialow-dydaktycznych
4. oficjalnych archiwów kuratoriów w Bydgoszczy, Krakowie, Łodzi, Opolu,
   Poznaniu, Warszawie i Olsztynie;
5. źródeł instytucjonalnych, np. ZPE, AGAD, Biblioteki Sejmowej i muzeów.

Każdą odpowiedź zweryfikuj. Fakty niejednoznaczne sprawdź w co najmniej dwóch
źródłach. Usuń pytania, które dopuszczają więcej odpowiedzi, niż przewiduje polecenie.

Wygeneruj obowiązkowo dwa pliki PDF (HTML traktuj wyłącznie jako format roboczy):
1. test w formacie PDF, zawierający na końcu kartę odpowiedzi;
2. osobny PDF z kluczem odpowiedzi i punktacją;
3. w kluczu zamieść dopuszczalne warianty odpowiedzi, wykaz wykorzystanych źródeł
   z adresami URL, przypisanie zadań do źródeł oraz liczbę zadań powtarzających temat;
4. podaj oznaczenie wariantu i ziarno losowania.

Przed zakończeniem automatycznie sprawdź:
- sumę 100 punktów;
- zgodność liczby zadań z instrukcją;
- kompletność klucza;
- zakres chronologiczny;
- udział zadań powtarzających temat (limit 30%);
- czy żaden klucz nie jest przewidywalny — brak ciągów rosnących typu A, B, C, D
  oraz 1, 2, 3, 4 i brak długich serii w zadaniach prawda/fałsz;
- poprawność położenia punktów oraz czytelność map i ilustracji na stronach PDF;
- że oba pliki PDF powstały, otwierają się i mają oczekiwaną liczbę stron.
```

## 12. Dotychczas wygenerowane przykłady

- `output/test_szkolny_wariant_A.pdf`
- `output/klucz_odpowiedzi_wariant_A.pdf`
- `output/test_szkolny_wariant_B.pdf`
- `output/klucz_odpowiedzi_wariant_B.pdf`
- `output/test_szkolny_wariant_A_poprawiona_mapa.pdf` — wzorzec jakości mapy;
- `output/klucz_odpowiedzi_wariant_A_poprawiona_mapa.pdf`;
- `output/test_szkolny_wariant_C.pdf` — 19 zadań, 100 p., ziarno `2026-09-09-C`;
- `output/klucz_odpowiedzi_wariant_C.pdf`.

Tematy wykorzystane w wariancie C (użyte ponownie liczą się do limitu 30% powtórzeń): tabela cywilizacji
starożytnych, Grecja w wyborze jednokrotnym, urzędy republiki rzymskiej, edykt mediolański,
mapa Bizancjum–islam–krucjaty, spór o inwestyturę, prawo magdeburskie i dziesięcina,
pierwsi Piastowie w tekście z wyborem wariantu, chronologia rozbicia dzielnicowego,
Kazimierz Wielki i Andegawenowie, krzyżówka z hasłem KOMPAS, przyczyny i skutki reformacji,
obraz Matejki „Astronom Kopernik”, artykuły henrykowskie jako tekst źródłowy,
traktaty i rozejmy XVII w., powstanie Stanów Zjednoczonych, rewolucja francuska,
Sejm Wielki i Konstytucja 3 maja, daty rozbiorów i insurekcji.

- `output/test_szkolny_wariant_D.pdf` — 19 zadań, 100 p., ziarno `2026-09-10-D`;
- `output/klucz_odpowiedzi_wariant_D.pdf`.

Tematy wykorzystane w wariancie D (użyte ponownie liczą się do limitu 30% powtórzeń): osiągnięcia cywilizacji
starożytnych, wojny grecko-perskie i Aleksander Wielki, Rzym od republiki do cesarstwa, twórcy kultury
antycznej, monarchia stanowa w Anglii i Francji, wojna stuletnia i kryzys XIV w., unia w Krewie i wojny
z zakonem krzyżackim, mapa ośrodków reformacji, „Hołd pruski” Matejki, złoty wiek kultury polskiej,
wielowyznaniowość Rzeczypospolitej, krzyżówka z hasłem SEJMIK, wojna trzydziestoletnia, list Jana III
Sobieskiego spod Wiednia, absolutyzm i monarchia parlamentarna, czasy saskie, rewolucja naukowa
i oświecenie, konfederacja barska i I rozbiór, przyczyny i skutki upadku Rzeczypospolitej.

- `output/test_szkolny_wariant_E.pdf` — 19 zadań, 100 p., ziarno `2026-09-11-E`;
- `output/klucz_odpowiedzi_wariant_E.pdf`.

Tematy wykorzystane w wariancie E (użyte ponownie liczą się do limitu 30% powtórzeń): starożytny Egipt,
Ateny i Sparta, życie codzienne w Rzymie, upadek cesarstwa zachodniorzymskiego i wędrówka ludów,
wikingowie i Normanowie, państwo Franków, Słowianie i sąsiedzi Polski, „Bitwa pod Grunwaldem” Matejki,
przyczyny i skutki wielkich odkryć, mapa miast Rzeczypospolitej, wieś i gospodarka folwarczna,
krzyżówka z hasłem ROKOSZ, chronologia Rzeczypospolitej w XVII w., śluby lwowskie jako tekst źródłowy,
kultura baroku w Europie, kolonializm i gospodarka nowożytna, oświecony absolutyzm, Sejm Wielki
i Konstytucja 3 maja, rozbiory i upadek Rzeczypospolitej.

Wariant E jest pierwszym, który świadomie wykorzystał limit powtórzeń: 5 z 19 zadań (26%) dotyczy
zagadnień obecnych w wariantach A–D (IX, XIII, XIV, XVIII, XIX), za każdym razem w innej formie
i z innymi pozycjami szczegółowymi. Rozliczenie limitu zapisano w kluczu, w sekcji
„Kontrola limitu powtórzeń (30%)” — powtarzaj ten układ w kolejnych wariantach.

Wariant E przeszedł też korektę losowości klucza. W pierwszej wersji sześć zadań miało klucz
rosnący (I, V, VI, XV, XVII — dopasowania — oraz XIII, gdzie wydarzenia były wypisane
w kolejności chronologicznej, więc klucz brzmiał 1, 2, 3, 4, 5, 6). Banki odpowiedzi
przetasowano, kolejność wydarzeń zmieniono, a zdania prawda/fałsz w zadaniach II, VII i XVI
przeplatano, żeby rozbić serie typu P, P, P, F, F. Ten sam defekt ma **wariant D**
(zadania I, IV, X, XV, XVII oraz mapa VIII z kluczem 1, 2, 3, 4, 5) i **wariant C**
(mapa V) — jeżeli będą używane, wymagają analogicznej poprawki.

- `output/test_szkolny_wariant_F.pdf` — 19 zadań, 100 p., ziarno `2026-09-12-F`, 11 stron;
- `output/klucz_odpowiedzi_wariant_F.pdf` — 5 stron.

Tematy wykorzystane w wariancie F (użyte ponownie liczą się do limitu 30% powtórzeń): Mezopotamia,
Fenicjanie i Kreta, starożytne Chiny i Indie, wojny punickie, Mieszko I i początki państwa polskiego,
krzyżówka z hasłem RYCERZ (zakony i rycerstwo), zakon krzyżacki w Prusach, wynalazki i technika
średniowiecza, kultura polskiego średniowiecza, rekonkwista i zjednoczenie Hiszpanii,
Kazimierz Jagiellończyk i wojna trzynastoletnia, konstytucja *Nihil novi* jako tekst źródłowy,
miasta i mieszczaństwo w Rzeczypospolitej, mapa ekspansji Imperium Osmańskiego, powstanie
Chmielnickiego, Rosja Piotra I, oświecenie w Europie, „Konstytucja 3 maja 1791” Matejki,
rozbiory i upadek Rzeczypospolitej.

Wariant F jest pierwszym powstałym już pod nowymi regułami losowania kolejności odpowiedzi — kontrolę
`tools/sprawdz_losowosc_klucza.py` uruchomiono **przed** wygenerowaniem PDF-ów i przeszła bez uwag.
Powtórzeń jest tu tylko 4 na 19 zadań (21%), z zapasem poniżej limitu. Przy komponowaniu wariantu
ujawniła się jednak ważna prawidłowość: **zagadnienia z historii Polski wyczerpują się szybciej niż
powszechne**, bo jest ich w podstawie programowej mniej. Utrzymanie bilansu 48–53 / 47–52 punktów
wymaga więc zużywania limitu powtórzeń przede wszystkim na zadania polskie (w wariancie F wszystkie
cztery powtórki oprócz oświecenia dotyczą historii Polski). Planując wariant G, najpierw ustal listę
zadań polskich, a dopiero potem dobierz powszechne — odwrotna kolejność prowadzi do arkusza
przeciążonego historią powszechną.

Przy tej okazji poprawiono też **klucz wariantu E**: krzyżówka w zadaniu XII rozliczała się na 8 p.
(6 haseł + hasło + wyjaśnienie) przy zapowiedzianych w arkuszu 7 p. Obowiązujący schemat to
**6 p. za hasła krzyżówki + 1 p. za odczytane hasło razem z wyjaśnieniem**.

- `output/test_szkolny_wariant_G.pdf` — 19 zadań, 100 p., ziarno `2026-09-14-G`, 11 stron;
- `output/klucz_odpowiedzi_wariant_G.pdf` — 6 stron.

Tematy wykorzystane w wariancie G (użyte ponownie liczą się do limitu 30% powtórzeń): kultura
starożytnej Grecji, armia i podboje rzymskie, reguła świętego Benedykta jako tekst źródłowy,
wyprawy krzyżowe, mapa portów i kantorów Hanzy, chronologia Europy XIV–XV w., akt unii
lubelskiej, kontrreformacja, „Batory pod Pskowem” Matejki, Anglia Elżbiety I, wojsko
Rzeczypospolitej, rokosze szlacheckie, Gdańsk i handel zbożem, sarmatyzm, krzyżówka z hasłem
HETMAN, sejm i liberum veto, manufaktury i merkantylizm, Komisja Edukacji Narodowej,
rozbiory i insurekcja.

Wariant G powstał już z użyciem bazy pytań i pokazał, co znaczy wyczerpanie puli tematów
w praktyce. Przy doborze zadań trzeba było zejść na **poziom podtematu**: „armia rzymska”
zamiast „Rzym”, „kontrreformacja” zamiast „reformacja”, „Anglia Elżbiety I” zamiast
„monarchia parlamentarna”. Przy grubszej granulacji wszystkie 19 zadań byłoby powtórzeniami.
Taka granulacja jest zgodna z praktyką wariantów C–F (osobno „urzędy republiki rzymskiej”,
„Rzym od republiki do cesarstwa”, „życie codzienne w Rzymie”) i tylko ona pozwala utrzymać
limit — w wariancie G wyszło dokładnie 5 powtórzeń na 19 zadań (26%).

Druga obserwacja: sprawdzanie świeżości tematu **wyszukiwaniem po nazwach własnych w arkuszach
A–F** jest szybsze i pewniejsze niż przeglądanie list tematów w tej specyfikacji, bo warianty A
i B nigdy nie zostały tu rozpisane. Wystarczy pętla `rg -qi "<hasło>" test_szkolny_wariant_?.html`
po kandydatach — tak wyszło na jaw, że krucjaty, Komisja Edukacji Narodowej i chwalebna
rewolucja były już zajęte, a husaria, rokosze, Hanza i sarmatyzm wolne.

### Liczenie stron PDF — tylko przez PDFKit

Zliczanie wystąpień `/Type /Page` w surowych bajtach PDF **jest zawodne** i zaniża wynik, gdy Chrome
upakuje obiekty w strumienie (dla wariantu F dało 8 stron przy faktycznych 11). `mdls` z kolei zwraca
wartości nieaktualne. Liczbę stron ustalaj wyłącznie przez PDFKit:

```bash
cat > /tmp/licz_strony.swift <<'SWIFT'
import PDFKit
for p in CommandLine.arguments.dropFirst() {
    if let d = PDFDocument(url: URL(fileURLWithPath: p)) { print("\(p): \(d.pageCount) stron") }
}
SWIFT
swift /tmp/licz_strony.swift output/test_szkolny_wariant_F.pdf
```

### Zagęszczenie składu a liczba stron

Przy `break-inside: avoid` na `.task` o liczbie stron decyduje średnia wysokość zadania, a nie
sumaryczna objętość treści. Zadania o wysokości ok. 100 mm mieszczą się po dwa na stronie i marnują
ok. 70 mm; po zejściu do ok. 85 mm wchodzą po trzy. W wariancie E te ustawienia skróciły arkusz
z 13 do 10 stron bez usuwania treści:

- `font-size: 10.4pt`, `line-height: 1.28`;
- `.compact th, .compact td { padding: 1.1mm 1.7mm; }`;
- `.task { padding: 3mm 4mm; margin: 0 0 4mm; }`;
- `.choices { columns: 3; column-gap: 6mm; }`;
- `.answer-space { min-height: 7mm; }`.

Grupowanie zadań w kolejne znaczniki `<section>` **nie** wpływa na podział na strony — nie próbuj
sterować łamaniem w ten sposób. Wysokość zadań mierz w przeglądarce (klon węzła `.task` wstawiony
do kontenera o szerokości 182 mm), bo szacowanie „na oko” zaniża wyniki o kilkadziesiąt procent.

Zabiegi zagęszczające działają jednak **skokowo, nie liniowo**: w wariancie F skrócenie odstępów
między zadaniami, zmniejszenie `.answer-space` oraz mapy do 88 mm i obrazu do 140 mm nie zmieniło
liczby stron (nadal 11), bo oszczędność ok. 35 mm nie wystarczyła, by w wolne miejsce weszło kolejne
zadanie. Zmiany wycofano, bo pogarszały czytelność grafik, nie dając nic w zamian. Wniosek: zanim
zmniejszysz ilustracje, sprawdź, ile milimetrów brakuje do wciśnięcia następnego zadania — jeśli
więcej niż kilkanaście, drobne korekty nie pomogą i lepiej zaakceptować dodatkową stronę.
Zakres 10–11 stron arkusza przy 19 zadaniach jest normą, a nie defektem.

### Mapy bazowe dostępne lokalnie

- `assets/mediterranean_blank_cc0.svg` — basen Morza Śródziemnego, CC0 (warianty A i C);
- `assets/europe_blank_cc0.svg` — Europa, dane Natural Earth 1:50 mln, CC0 (warianty D–G).

Mapa Europy ma wygodną strukturę: 49 ścieżek o `stroke-width="0.6"` to granice państw,
a jedna o `stroke-width="0.9"` (164 podścieżki) to linia brzegowa całego lądu. Wypełnienie
tej jednej ścieżki kolorem z `fill-rule="evenodd"` daje poprawny ląd z wyspami i morzami
wewnętrznymi jako otworami — na tym opiera się `tools/zbuduj_mape.py`.

Mapy śródziemnomorskiej **nie da się na razie używać do precyzyjnych punktów**: próba odtworzenia jej
odwzorowania z pięciu znaczników wariantu C dała maksymalny błąd ok. 11 px (≈0,8° długości
geograficznej), zarówno przy założeniu Mercatora, jak i odwzorowania równoodległościowego. Dopóki
parametry nie zostaną wyznaczone rzetelnie, zadania mapowe opieraj na mapie Europy — jej kadr sięga
na południe do Krety i na wschód do Bosforu, co pokrywa Bałkany, Anatolię zachodnią i Europę Środkową
(w wariancie F wykorzystano kadr `viewBox="855 1455 370 357"`).

Mapa Europy jest w odwzorowaniu Mercatora o parametrach `x = 1374,20·lon[rad] + 496,33`
oraz `y = −1374,18·ln(tg(45° + lat/2)) + 2809,24`, dopasowanych do siedemnastu stolic o znanych
współrzędnych z maksymalnym błędem 0,13 piksela. Dzięki temu położenie dowolnego miasta można wyliczyć
rachunkowo, zamiast szacować je na oko. Po naniesieniu punktów zawsze wykonaj render kontrolny —
punkt położony blisko granicy państwa bywa dla ucznia niejednoznaczny i lepiej zastąpić go innym
miastem (tak Trydent zastąpiono Wormacją).

Pliki HTML użyte do generowania PDF pozostawiono w katalogu projektu, dzięki czemu można
zmieniać treść, styl oraz tworzyć kolejne warianty.

## 13. Narzędzia pomocnicze

- `tools/extract_pdf_text.swift` — wyciąga warstwę tekstową z PDF-ów do katalogu z tekstem:

  ```bash
  swift tools/extract_pdf_text.swift referencje/arkusze referencje/tekst
  ```

- `tools/analizuj_arkusze.py` — zestawia etap, liczbę zadań, punktację i czas pracy:

  ```bash
  python3 tools/analizuj_arkusze.py referencje/tekst
  ```

- `tools/pdf_to_png.swift` — renderuje strony PDF do plików PNG, do przeglądu składu:

  ```bash
  swift tools/pdf_to_png.swift output/test_szkolny_wariant_E.pdf output/previews/E 0.72
  ```

- `tools/sprawdz_losowosc_klucza.py` — wykrywa przewidywalne klucze: ciągi rosnące
  A, B, C, D oraz 1, 2, 3, 4, pozycje stojące na swoim miejscu i długie serie
  w zadaniach prawda/fałsz. Kończy się kodem błędu, gdy znajdzie problem, więc nadaje się
  do uruchamiania przed generowaniem PDF-ów:

  ```bash
  python3 tools/sprawdz_losowosc_klucza.py output/klucz_odpowiedzi_wariant_*.html
  ```

  Narzędzie sprawdza wyłącznie rozkład odpowiedzi, nie ich poprawność. Po przetasowaniu banku
  trzeba osobno potwierdzić, że litera z klucza wskazuje właściwe hasło.

- `tools/generuj_tabele_daty.py` — chronologiczne zestawienie dat i wydarzeń (pełne oraz
  uczniowskie, bez kolumn roboczych):

  ```bash
  python3 tools/generuj_tabele_daty.py > output/tabela_dat_i_wydarzen.html
  python3 tools/generuj_tabele_daty.py --do-nauki > output/tabela_dat_do_nauki.html
  ```

- `tools/zbuduj_mape.py` — składa mapę zadania z bazowej mapy Europy: wypełnia morze i ląd,
  wycisza granice państw, nanosi ponumerowane punkty wyliczone rachunkowo ze współrzędnych
  geograficznych, dodaje strzałkę północy i legendę. Kadr, punkty i numerację ustawia się
  w sekcji `__main__`; skrypt przerywa pracę, jeśli któryś punkt wypada poza kadrem:

  ```bash
  python3 tools/zbuduj_mape.py
  ```

- `tools/baza_pytan.py` — baza potencjalnych pytań: wydarzenia w zakresie konkursu
  (do 1795 r.) z obszarem, typem zagadnienia i oceną ryzyka powtórzenia względem arkuszy A–F.
  Punkt wyjścia przy doborze tematów do nowego wariantu — patrz sekcja
  „Baza potencjalnych pytań”:

  ```bash
  python3 tools/baza_pytan.py
  ```

Skrypty korzystają wyłącznie z narzędzi dostępnych w systemie (Swift z PDFKit, python3),
bez instalowania dodatkowych zależności.
