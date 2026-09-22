#!/usr/bin/env python3
"""Buduje chronologiczną tabelę dat: wydarzenia z arkuszy A–F scalone z listą przekazaną przez autora.

Kolumna „Arkusze” podaje warianty, w których data wystąpiła (w zadaniu lub w komentarzu klucza).
Kreska oznacza datę wyłącznie z listy dodatkowej, jeszcze nieużytą w żadnym arkuszu.

Użycie:
    python3 tools/generuj_tabele_daty.py > output/tabela_dat_i_wydarzen.html
    python3 tools/generuj_tabele_daty.py --do-nauki > output/tabela_dat_do_nauki.html

Przełącznik --do-nauki pomija kolumnę „Arkusze” i notkę o wariantach: zostaje sama chronologia
do powtarzania przez ucznia.
"""
import html
import re
import sys

# (klucz sortowania, etykieta daty, wydarzenie, warianty arkuszy, czy z listy autora)
DANE = [
    # ---------------- STAROŻYTNOŚĆ ----------------
    (-3000, "ok. 3000 p.n.e.", "Zjednoczenie Egiptu; powstanie pisma klinowego w Mezopotamii", "", True),
    (-2700, "ok. 2700–1400 p.n.e.", "Cywilizacja minojska na Krecie – najstarsza cywilizacja Europy", "F", False),
    (-1792, "1792–1750 p.n.e.", "Panowanie Hammurabiego w Babilonie; kodeks Hammurabiego", "B", False),
    (-776, "776 p.n.e.", "Pierwsze udokumentowane igrzyska olimpijskie w Grecji", "B", True),
    (-753, "753 p.n.e.", "Tradycyjna data założenia Rzymu", "B D", True),
    (-490, "490 p.n.e.", "Bitwa pod Maratonem (wojny grecko-perskie)", "C", True),
    (-480, "480 p.n.e.", "Bitwy pod Termopilami i pod Salaminą", "", True),
    (-431, "431–404 p.n.e.", "Wojna peloponeska; zwycięstwo Sparty nad Atenami", "E", False),
    (-334, "334 p.n.e.", "Początek wyprawy Aleksandra Wielkiego przeciw Persji", "", True),
    (-264, "264–241 p.n.e.", "Pierwsza wojna punicka", "F", False),
    (-218, "218 p.n.e.", "Przeprawa Hannibala przez Alpy", "F", False),
    (-217, "218–201 p.n.e.", "Druga wojna punicka", "F", False),
    (-216, "216 p.n.e.", "Bitwa pod Kannami – największa klęska Rzymian", "F", False),
    (-202, "202 p.n.e.", "Bitwa pod Zamą; zwycięstwo Scypiona Afrykańskiego nad Hannibalem", "F", False),
    (-149, "149–146 p.n.e.", "Trzecia wojna punicka", "F", False),
    (-146, "146 p.n.e.", "Zburzenie Kartaginy", "F", False),
    (-44, "44 p.n.e.", "Zabójstwo Juliusza Cezara (Idy marcowe)", "", True),
    (-31, "31 p.n.e.", "Bitwa pod Akcjum – początek cesarstwa rzymskiego", "", True),
    (313, "313", "Edykt mediolański – koniec prześladowań chrześcijan", "C E", True),
    (395, "395", "Podział cesarstwa rzymskiego na wschodnie i zachodnie", "E", True),
    (476, "476", "Upadek cesarstwa zachodniorzymskiego – koniec starożytności", "A B D E", True),
    # ---------------- ŚREDNIOWIECZE ----------------
    (496, "496", "Chrzest Chlodwiga – początek chrześcijańskiego państwa Franków", "E", True),
    (622, "622", "Hidżra – ucieczka Mahometa z Mekki do Medyny, początek ery muzułmańskiej", "A", True),
    (732, "732", "Bitwa pod Poitiers – Karol Młot zatrzymuje ekspansję arabską", "B C E", False),
    (800, "800", "Koronacja cesarska Karola Wielkiego", "A B C E", True),
    (843, "843", "Traktat w Verdun – podział państwa Franków na trzy części", "E", True),
    (911, "911", "Nadanie Normandii wodzowi Normanów Rollonowi", "E", False),
    (962, "962", "Koronacja Ottona I – powstanie Świętego Cesarstwa Rzymskiego", "B", True),
    (965, "965", "Małżeństwo Mieszka I z czeską księżniczką Dobrawą", "F", False),
    (966, "966", "Chrzest Polski (Mieszko I)", "A C E F", True),
    (972, "972", "Bitwa pod Cedynią – Mieszko I pokonuje margrabiego Hodona", "A B C F", False),
    (1000, "1000", "Zjazd gnieźnieński", "B E", True),
    (1025, "1025", "Koronacja i śmierć Bolesława Chrobrego – pierwsza koronacja w Polsce", "A B C", True),
    (1054, "1054", "Wielka schizma wschodnia – podział na katolicyzm i prawosławie", "A D", True),
    (1066, "1066", "Bitwa pod Hastings – podbój Anglii przez Normanów", "E", True),
    (1076, "1076", "Koronacja Bolesława Śmiałego", "B C", False),
    (1077, "1077", "Upokorzenie Henryka IV w Canossie (spór o inwestyturę)", "C", False),
    (1095, "1095", "Wezwanie papieża Urbana II do krucjaty na synodzie w Clermont", "C", False),
    (1096, "1096", "Początek pierwszej krucjaty", "C", True),
    (1099, "1099", "Zdobycie Jerozolimy przez krzyżowców", "C", False),
    (1138, "1138", "Ustawa sukcesyjna Bolesława Krzywoustego – początek rozbicia dzielnicowego", "A C", True),
    (1204, "1204", "Zdobycie i splądrowanie Konstantynopola przez krzyżowców (IV krucjata)", "C", False),
    (1215, "1215", "Wielka Karta Swobód w Anglii", "D", False),
    (1226, "1226", "Sprowadzenie Krzyżaków do Polski przez Konrada Mazowieckiego", "C F", True),
    (1236, "1236", "Zdobycie Kordoby przez chrześcijan (rekonkwista)", "F", False),
    (1241, "1241", "Najazd mongolski na Polskę i bitwa pod Legnicą", "C", True),
    (1295, "1295", "Koronacja Przemysła II", "B", False),
    (1308, "1308", "Zajęcie Gdańska i Pomorza Gdańskiego przez Krzyżaków", "C", False),
    (1309, "1309", "Malbork siedzibą wielkiego mistrza zakonu krzyżackiego", "F", False),
    (1320, "1320", "Koronacja Władysława Łokietka – koniec rozbicia dzielnicowego", "A B C", True),
    (1333, "1333–1370", "Panowanie Kazimierza Wielkiego", "B", True),
    (1337, "1337–1453", "Wojna stuletnia między Anglią a Francją", "D", False),
    (1343, "1343", "Pokój w Kaliszu z zakonem krzyżackim", "C", False),
    (1356, "1356", "Nadanie Lwowowi praw miejskich na wzór magdeburski", "E", False),
    (1364, "1364", "Założenie Akademii Krakowskiej przez Kazimierza Wielkiego", "C F", True),
    (1374, "1374", "Przywilej koszycki – pierwszy wielki przywilej szlachecki", "C", False),
    (1384, "1384", "Koronacja Jadwigi Andegaweńskiej", "D", False),
    (1385, "1385", "Unia w Krewie – początek związku Polski z Litwą", "D", True),
    (1387, "1387", "Chrzest Litwy", "D", False),
    (1400, "1400", "Odnowienie Akademii Krakowskiej przez Władysława Jagiełłę", "F", False),
    (1410, "1410", "Bitwa pod Grunwaldem (15 lipca)", "B D E", True),
    (1411, "1411", "Pierwszy pokój toruński", "D", False),
    (1440, "1440", "Powstanie Związku Pruskiego przeciw zakonowi krzyżackiemu", "F", False),
    (1444, "1444", "Bitwa pod Warną – śmierć Władysława III Warneńczyka", "F", False),
    (1447, "1447", "Koronacja Kazimierza Jagiellończyka", "F", False),
    (1450, "ok. 1450", "Prasa drukarska Jana Gutenberga", "F", False),
    (1453, "1453", "Upadek Konstantynopola – koniec cesarstwa bizantyjskiego; koniec wojny stuletniej", "D F", True),
    (1454, "1454", "Wybuch wojny trzynastoletniej; klęska pod Chojnicami", "F", False),
    (1463, "1463", "Zwycięstwo flotylli kaperskiej w Zatoce Świeżej", "F", False),
    (1466, "1466", "Drugi pokój toruński – odzyskanie Pomorza Gdańskiego", "D F", True),
    (1469, "1469", "Małżeństwo Izabeli Kastylijskiej i Ferdynanda Aragońskiego", "F", False),
    (1477, "1477–1489", "Ołtarz Wita Stwosza w kościele Mariackim w Krakowie", "F", False),
    (1488, "1488", "Opłynięcie Przylądka Dobrej Nadziei przez Bartolomeu Diasa", "A", False),
    (1492, "1492", "Odkrycie Ameryki przez Kolumba; zdobycie Granady – koniec rekonkwisty", "A C F", True),
    (1498, "1498", "Vasco da Gama dopływa do Indii", "A", False),
    # ---------------- NOWOŻYTNOŚĆ ----------------
    (1501, "1501–1506", "Panowanie Aleksandra Jagiellończyka", "F", False),
    (1505, "1505", "Konstytucja Nihil novi – początek demokracji szlacheckiej", "F", False),
    (1517, "1517", "Wystąpienie Marcina Lutra w Wittenberdze – początek reformacji", "A B C D", True),
    (1521, "1521", "Sejm Rzeszy w Wormacji; zdobycie Belgradu przez Turków", "D F", False),
    (1525, "1525", "Hołd pruski (10 kwietnia)", "D", True),
    (1526, "1526", "Bitwa pod Mohaczem – Turcy opanowują większość Węgier", "F", False),
    (1529, "1529", "Pierwsze oblężenie Wiednia przez Turków", "F", False),
    (1534, "1534", "Akt supremacji Henryka VIII – powstanie Kościoła anglikańskiego", "D", False),
    (1543, "1543", "Wydanie „O obrotach sfer niebieskich” Mikołaja Kopernika", "C", False),
    (1545, "1545–1563", "Sobór trydencki – początek kontrreformacji", "C", False),
    (1555, "1555", "Pokój augsburski – zasada „czyja władza, tego religia”", "C D", False),
    (1569, "1569", "Unia lubelska – powstanie Rzeczypospolitej Obojga Narodów", "A B", True),
    (1573, "1573", "Konfederacja warszawska i pierwsza wolna elekcja (Henryk Walezy)", "A C D", True),
    (1596, "1596", "Unia brzeska – powstanie Kościoła greckokatolickiego", "D", False),
    (1605, "1605", "Bitwa pod Kircholmem", "A", False),
    (1606, "1606–1609", "Rokosz Zebrzydowskiego", "E", False),
    (1610, "1610", "Bitwa pod Kłuszynem", "A", False),
    (1618, "1618–1648", "Wojna trzydziestoletnia", "D", True),
    (1619, "1619", "Rozejm w Dywilinie z Rosją", "C", False),
    (1648, "1648", "Wybuch powstania Chmielnickiego (Żółte Wody, Korsuń); pokój westfalski", "A D E F", True),
    (1649, "1649", "Ścięcie króla Anglii Karola I", "D", False),
    (1654, "1654", "Ugoda perejasławska – uzależnienie Ukrainy od Rosji", "C F", False),
    (1655, "1655–1660", "Potop szwedzki (Ujście, obrona Jasnej Góry; pokój w Oliwie 1660)", "C E", True),
    (1656, "1656", "Śluby lwowskie Jana Kazimierza (1 kwietnia)", "E", False),
    (1658, "1658", "Wygnanie braci polskich z Rzeczypospolitej", "D", False),
    (1665, "1665–1666", "Rokosz Lubomirskiego", "E", False),
    (1667, "1667", "Rozejm w Andruszowie z Rosją", "C E", False),
    (1672, "1672", "Pokój w Buczaczu z Turcją", "C", False),
    (1683, "1683", "Odsiecz wiedeńska Jana III Sobieskiego (12 września)", "A D E F", True),
    (1688, "1688", "Chwalebna rewolucja w Anglii", "", True),
    (1699, "1699", "Pokój w Karłowicach", "C", False),
    (1700, "1700–1721", "Wielka wojna północna", "F", False),
    (1703, "1703", "Założenie Petersburga przez Piotra I", "F", False),
    (1709, "1709", "Bitwa pod Połtawą – zwycięstwo Rosji nad Szwecją", "F", False),
    (1712, "1712", "Petersburg stolicą Rosji", "F", False),
    (1717, "1717", "Sejm niemy", "D", False),
    (1721, "1721", "Piotr I przyjmuje tytuł imperatora", "F", False),
    (1748, "1748", "„O duchu praw” Monteskiusza", "F", False),
    (1751, "1751", "Początek wydawania Wielkiej Encyklopedii Francuskiej", "F", False),
    (1762, "1762", "„Umowa społeczna” Jana Jakuba Rousseau", "F", False),
    (1764, "1764–1795", "Panowanie Stanisława Augusta Poniatowskiego", "", True),
    (1765, "1765", "Powstanie Teatru Narodowego w Warszawie", "B", False),
    (1768, "1768–1772", "Konfederacja barska", "D", False),
    (1772, "1772", "Pierwszy rozbiór Polski", "B C D E F", True),
    (1773, "1773", "Sejm rozbiorowy (protest Rejtana); powstanie Komisji Edukacji Narodowej", "B C D", False),
    (1776, "1776", "Deklaracja niepodległości USA (4 lipca)", "A C", True),
    (1787, "1787", "Uchwalenie konstytucji Stanów Zjednoczonych", "E", False),
    (1788, "1788–1792", "Obrady Sejmu Wielkiego (Czteroletniego)", "C E F", False),
    (1789, "1789", "Wybuch rewolucji francuskiej – zburzenie Bastylii (14 lipca)", "A C", True),
    (1791, "1791", "Uchwalenie Konstytucji 3 maja", "A B E F", True),
    (1792, "1792", "Konfederacja targowicka i wojna w obronie konstytucji", "A B C E F", False),
    (1793, "1793", "Drugi rozbiór Polski; sejm grodzieński", "B C E F", True),
    (1794, "1794", "Powstanie kościuszkowskie (Racławice, Maciejowice)", "B C E F", True),
    (1795, "1795", "Trzeci rozbiór Polski – Polska znika z map na 123 lata", "A B C D E F", True),
    # ---------------- WIEK XIX ----------------
    (1797, "1797", "Powstanie Legionów Polskich we Włoszech", "", True),
    (1807, "1807", "Utworzenie Księstwa Warszawskiego (pokój w Tylży)", "", True),
    (1815, "1815", "Kongres wiedeński – utworzenie Królestwa Polskiego", "", True),
    (1830, "1830", "Wybuch powstania listopadowego (noc z 29 na 30 listopada)", "", True),
    (1848, "1848", "Wiosna Ludów w Europie", "", True),
    (1861, "1861–1865", "Wojna secesyjna w USA", "", True),
    (1863, "1863", "Wybuch powstania styczniowego (22 stycznia)", "", True),
    (1871, "1871", "Zjednoczenie Niemiec – powstanie II Rzeszy", "", True),
    # ---------------- WIEK XX ----------------
    (1914, "1914–1918", "Pierwsza wojna światowa", "", True),
    (1917, "1917", "Rewolucje w Rosji – lutowa i październikowa", "", True),
    (1918, "1918", "Odzyskanie niepodległości przez Polskę (11 listopada)", "D", True),
    (1919, "1919–1921", "Wojna polsko-bolszewicka (Bitwa Warszawska 15 sierpnia 1920, pokój ryski 1921)", "", True),
    (1921, "1921", "Uchwalenie konstytucji marcowej", "", True),
    (1926, "1926", "Przewrót majowy Józefa Piłsudskiego", "", True),
    (1939, "1939", "Wybuch II wojny światowej (1 września atak Niemiec, 17 września atak ZSRR)", "", True),
    (1941, "1941", "Atak Niemiec na ZSRR (operacja Barbarossa); atak na Pearl Harbor", "", True),
    (1943, "1943", "Powstanie w getcie warszawskim; odkrycie grobów katyńskich", "", True),
    (1944, "1944", "Wybuch powstania warszawskiego (1 sierpnia)", "", True),
    (1945, "1945", "Koniec II wojny światowej (kapitulacja Niemiec 8 maja, Japonii 2 września); konferencja w Jałcie", "", True),
    (1956, "1956", "Poznański Czerwiec – pierwszy masowy protest robotniczy w PRL", "", True),
    (1970, "1970", "Tragedia na Wybrzeżu (Grudzień ’70)", "", True),
    (1978, "1978", "Wybór Karola Wojtyły na papieża Jana Pawła II (16 października)", "", True),
    (1980, "1980", "Strajki sierpniowe; powstanie NSZZ „Solidarność”", "", True),
    (1981, "1981", "Wprowadzenie stanu wojennego w Polsce (13 grudnia)", "", True),
    (1989, "1989", "Obrady Okrągłego Stołu i wybory czerwcowe (4 czerwca) – początek III RP", "", True),
    (1999, "1999", "Wstąpienie Polski do NATO", "", True),
    (2004, "2004", "Wejście Polski do Unii Europejskiej (1 maja)", "", True),
]

# Wydarzenia, przy których warto znać dokładny dzień, nie tylko rok.
DOKLADNE_DATY = [
    ("15 lipca 1410", "bitwa pod Grunwaldem"),
    ("10 kwietnia 1525", "hołd pruski"),
    ("12 września 1683", "odsiecz wiedeńska"),
    ("4 lipca 1776", "Deklaracja niepodległości USA"),
    ("14 lipca 1789", "zburzenie Bastylii"),
    ("3 maja 1791", "uchwalenie Konstytucji 3 maja"),
    ("29/30 listopada 1830", "wybuch powstania listopadowego"),
    ("22 stycznia 1863", "wybuch powstania styczniowego"),
    ("11 listopada 1918", "odzyskanie niepodległości"),
    ("15 sierpnia 1920", "Bitwa Warszawska"),
    ("1 września 1939", "wybuch II wojny światowej"),
    ("1 sierpnia 1944", "wybuch powstania warszawskiego"),
    ("8 maja 1945", "kapitulacja Niemiec"),
    ("13 grudnia 1981", "wprowadzenie stanu wojennego"),
    ("4 czerwca 1989", "wybory czerwcowe"),
    ("1 maja 2004", "wejście Polski do Unii Europejskiej"),
]

EPOKI = [
    ("Starożytność", -10 ** 6, 476),
    ("Średniowiecze", 477, 1491),
    ("Nowożytność", 1492, 1795),
    ("Wiek XIX", 1796, 1913),
    ("Wiek XX i historia współczesna", 1914, 10 ** 6),
]

CSS = """
    @page { size: A4; margin: 13mm 12mm 15mm; }
    * { box-sizing: border-box; }
    body { margin: 0; color: #172033; font-family: "Arial","Helvetica",sans-serif;
      font-size: 9.6pt; line-height: 1.25; }
    h1 { font-size: 19pt; color: #163a63; margin: 0 0 2mm; }
    h2 { font-size: 12.4pt; color: #163a63; margin: 5mm 0 1.5mm; break-after: avoid; }
    p { margin: 0 0 2mm; }
    .eyebrow { color: #9a5a00; font-weight: 700; letter-spacing: .7px;
      text-transform: uppercase; font-size: 8.6pt; }
    .intro { padding: 3mm 4mm; background: #eef5fb; border-left: 5px solid #1f5a91;
      margin-bottom: 4mm; font-size: 9pt; }
    table { width: 100%; border-collapse: collapse; }
    th, td { border: 1px solid #8090a2; padding: 1.1mm 1.8mm; vertical-align: top; }
    th { background: #eaf1f7; color: #163a63; text-align: left; font-size: 9pt; }
    thead { display: table-header-group; }
    tr { break-inside: avoid; }
    .data { width: 26mm; white-space: nowrap; font-weight: 700; color: #163a63; }
    .war { width: 22mm; white-space: nowrap; text-align: center; font-size: 8.6pt;
      letter-spacing: .6px; color: #9a5a00; font-weight: 700; }
    .brak { color: #9aa5b3; font-weight: 400; }
    .lista { font-size: 8.4pt; color: #5c6878; }
    .dni { padding: 3mm 4mm; background: #f6f3ed; border: 1px solid #d8cdb9;
      font-size: 8.8pt; line-height: 1.5; }
    .stopka { margin-top: 4mm; font-size: 8.4pt; color: #606b79;
      border-top: 1px solid #c7cfd8; padding-top: 2mm; }
"""


def buduj(do_nauki: bool = False) -> str:
    tytul = ('Daty i wydarzenia – tabela do nauki' if do_nauki
             else 'Daty i wydarzenia – zestawienie zbiorcze')
    out = ['<!doctype html>', '<html lang="pl">', '<head>', '<meta charset="utf-8">',
           f'<title>{tytul}</title>', f'<style>{CSS}</style>', '</head>', '<body>',
           '<div class="eyebrow">Materiał pomocniczy • powtórka chronologii</div>',
           f'<h1>{tytul}</h1>']

    z_arkuszy = sum(1 for *_, w, _ in DANE if w)
    tylko_lista = len(DANE) - z_arkuszy
    if do_nauki:
        out.append(
            f'<div class="intro">{len(DANE)} dat i wydarzeń w porządku chronologicznym, '
            'od zjednoczenia Egiptu do wejścia Polski do Unii Europejskiej. '
            'Zestawienie obejmuje daty wykorzystane w arkuszach treningowych oraz pełną listę '
            'dat do opanowania. Na końcu wyróżniono wydarzenia, przy których trzeba znać '
            'nie tylko rok, ale i dokładny dzień.</div>')
    else:
        out.append(
            '<div class="intro">Zestawienie łączy wszystkie daty użyte w arkuszach treningowych '
            f'<strong>A–F</strong> ({z_arkuszy} pozycji) z listą dat do opanowania '
            f'({tylko_lista} pozycji, które w arkuszach jeszcze nie wystąpiły). '
            'Kolumna <strong>Arkusze</strong> wskazuje warianty, w których data pojawiła się '
            'w zadaniu albo w komentarzu klucza. Kreska oznacza datę spoza arkuszy – to materiał '
            'na kolejne warianty. Arkusze obejmują program do III rozbioru Polski, dlatego '
            'wiek XIX i XX pochodzą wyłącznie z listy dodatkowej.</div>')

    for nazwa, od, do in EPOKI:
        poz = [d for d in DANE if od <= d[0] <= do]
        if not poz:
            continue
        if do_nauki:
            naglowek = f'<h2>{html.escape(nazwa)} <span class="lista">({len(poz)} pozycji)</span></h2>'
            wiersz_th = '<tr><th class="data">Data</th><th>Wydarzenie</th></tr>'
        else:
            w_ark = sum(1 for *_, w, _ in poz if w)
            naglowek = (f'<h2>{html.escape(nazwa)} <span class="lista">'
                        f'({len(poz)} pozycji, z arkuszy: {w_ark})</span></h2>')
            wiersz_th = ('<tr><th class="data">Data</th><th>Wydarzenie</th>'
                         '<th class="war">Arkusze</th></tr>')
        out += [naglowek, f'<table><thead>{wiersz_th}</thead><tbody>']
        for _, etykieta, wydarzenie, warianty, _z_listy in poz:
            komorki = (f'<td class="data">{html.escape(etykieta)}</td>'
                       f'<td>{html.escape(wydarzenie)}</td>')
            if not do_nauki:
                wk = (html.escape(warianty) if warianty
                      else '<span class="brak">&mdash;</span>')
                komorki += f'<td class="war">{wk}</td>'
            out.append(f'<tr>{komorki}</tr>')
        out.append('</tbody></table>')

    out += ['<h2>Wydarzenia, przy których warto znać dokładny dzień</h2>',
            '<p class="dni">' + ' &nbsp;•&nbsp; '.join(
                f'<strong>{html.escape(d)}</strong> – {html.escape(o)}'
                for d, o in DOKLADNE_DATY) + '</p>']
    if do_nauki:
        out.append(f'<p class="stopka">Łącznie pozycji: <strong>{len(DANE)}</strong>. '
                   'Zakres Wojewódzkiego Konkursu Przedmiotowego kończy się na III rozbiorze '
                   'Polski (1795 r.) – dalsze epoki przydają się na olimpiadzie.</p>')
    else:
        out.append('<p class="stopka">Zestawienie wygenerowane na podstawie arkuszy treningowych '
                   'wariantów A–F oraz listy dat przekazanej przez autora. Łącznie pozycji: '
                   f'<strong>{len(DANE)}</strong>, z tego z arkuszy {z_arkuszy}.</p>')
    out += ['</body>', '</html>']
    return '\n'.join(out)


if __name__ == '__main__':
    sys.stdout.write(buduj(do_nauki='--do-nauki' in sys.argv))
