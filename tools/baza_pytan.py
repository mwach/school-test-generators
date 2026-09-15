#!/usr/bin/env python3
"""Baza potencjalnych pytań — wydarzenia mieszczące się w zakresie konkursu (do III rozbioru, 1795 r.).

Źródłem dat jest `tools/generuj_tabele_daty.py`; tutaj dochodzi klasyfikacja potrzebna przy
komponowaniu arkusza: obszar (historia Polski / powszechna) oraz typ zagadnienia. Wydarzenia
po 1795 r. są poza zakresem Wojewódzkiego Konkursu Przedmiotowego i do bazy nie wchodzą.

Status „wolne” oznacza, że zagadnienie nie wystąpiło jeszcze w żadnym arkuszu A–G, czyli można
je wykorzystać bez naruszania limitu 30% powtórzeń. Arkusze i klucze czytane są z `output/`.

Użycie:
    python3 tools/baza_pytan.py                 # podsumowanie w terminalu
    python3 tools/baza_pytan.py --json          # zapis output/baza_pytan.json
    python3 tools/baza_pytan.py --html          # widok HTML na stdout
"""
import html
import importlib.util
import json
import pathlib
import sys
from collections import Counter, defaultdict

GRANICA_ZAKRESU = 1795  # III rozbiór Polski — koniec zakresu konkursu

# Arkusze, klucze i wyniki tego skryptu leżą w output/ — patrz sekcja 9 specyfikacji.
KATALOG_WYJSCIA = pathlib.Path(__file__).parent.parent / 'output'

TYPY = ["cywilizacje i państwa", "władcy i dynastie", "ustrój i prawo", "wojny i bitwy",
        "dyplomacja i traktaty", "religia i Kościół", "kultura i nauka",
        "odkrycia i gospodarka"]

# klucz sortowania -> (obszar, typ zagadnienia)
KLASYFIKACJA = {
    # --- starożytność (cała historia powszechna) ---
    -3000: ("powszechna", "cywilizacje i państwa"),
    -2700: ("powszechna", "cywilizacje i państwa"),
    -1792: ("powszechna", "ustrój i prawo"),
    -776: ("powszechna", "kultura i nauka"),
    -753: ("powszechna", "cywilizacje i państwa"),
    -490: ("powszechna", "wojny i bitwy"),
    -480: ("powszechna", "wojny i bitwy"),
    -431: ("powszechna", "wojny i bitwy"),
    -334: ("powszechna", "wojny i bitwy"),
    -264: ("powszechna", "wojny i bitwy"),
    -218: ("powszechna", "wojny i bitwy"),
    -217: ("powszechna", "wojny i bitwy"),
    -216: ("powszechna", "wojny i bitwy"),
    -202: ("powszechna", "wojny i bitwy"),
    -149: ("powszechna", "wojny i bitwy"),
    -146: ("powszechna", "wojny i bitwy"),
    -44: ("powszechna", "władcy i dynastie"),
    -31: ("powszechna", "cywilizacje i państwa"),
    313: ("powszechna", "religia i Kościół"),
    395: ("powszechna", "cywilizacje i państwa"),
    476: ("powszechna", "cywilizacje i państwa"),
    # --- średniowiecze ---
    496: ("powszechna", "religia i Kościół"),
    622: ("powszechna", "religia i Kościół"),
    732: ("powszechna", "wojny i bitwy"),
    800: ("powszechna", "władcy i dynastie"),
    843: ("powszechna", "dyplomacja i traktaty"),
    911: ("powszechna", "dyplomacja i traktaty"),
    962: ("powszechna", "władcy i dynastie"),
    965: ("Polska", "władcy i dynastie"),
    966: ("Polska", "religia i Kościół"),
    972: ("Polska", "wojny i bitwy"),
    1000: ("Polska", "dyplomacja i traktaty"),
    1025: ("Polska", "władcy i dynastie"),
    1054: ("powszechna", "religia i Kościół"),
    1066: ("powszechna", "wojny i bitwy"),
    1076: ("Polska", "władcy i dynastie"),
    1077: ("powszechna", "religia i Kościół"),
    1095: ("powszechna", "religia i Kościół"),
    1096: ("powszechna", "wojny i bitwy"),
    1099: ("powszechna", "wojny i bitwy"),
    1138: ("Polska", "ustrój i prawo"),
    1204: ("powszechna", "wojny i bitwy"),
    1215: ("powszechna", "ustrój i prawo"),
    1226: ("Polska", "dyplomacja i traktaty"),
    1236: ("powszechna", "wojny i bitwy"),
    1241: ("Polska", "wojny i bitwy"),
    1295: ("Polska", "władcy i dynastie"),
    1308: ("Polska", "wojny i bitwy"),
    1309: ("Polska", "cywilizacje i państwa"),
    1320: ("Polska", "władcy i dynastie"),
    1333: ("Polska", "władcy i dynastie"),
    1337: ("powszechna", "wojny i bitwy"),
    1343: ("Polska", "dyplomacja i traktaty"),
    1356: ("Polska", "odkrycia i gospodarka"),
    1364: ("Polska", "kultura i nauka"),
    1374: ("Polska", "ustrój i prawo"),
    1384: ("Polska", "władcy i dynastie"),
    1385: ("Polska", "dyplomacja i traktaty"),
    1387: ("Polska", "religia i Kościół"),
    1400: ("Polska", "kultura i nauka"),
    1410: ("Polska", "wojny i bitwy"),
    1411: ("Polska", "dyplomacja i traktaty"),
    1440: ("Polska", "ustrój i prawo"),
    1444: ("Polska", "wojny i bitwy"),
    1447: ("Polska", "władcy i dynastie"),
    1450: ("powszechna", "kultura i nauka"),
    1453: ("powszechna", "wojny i bitwy"),
    1454: ("Polska", "wojny i bitwy"),
    1463: ("Polska", "wojny i bitwy"),
    1466: ("Polska", "dyplomacja i traktaty"),
    1469: ("powszechna", "władcy i dynastie"),
    1477: ("Polska", "kultura i nauka"),
    1488: ("powszechna", "odkrycia i gospodarka"),
    # --- nowożytność ---
    1492: ("powszechna", "odkrycia i gospodarka"),
    1498: ("powszechna", "odkrycia i gospodarka"),
    1501: ("Polska", "władcy i dynastie"),
    1505: ("Polska", "ustrój i prawo"),
    1517: ("powszechna", "religia i Kościół"),
    1521: ("powszechna", "religia i Kościół"),
    1525: ("Polska", "dyplomacja i traktaty"),
    1526: ("powszechna", "wojny i bitwy"),
    1529: ("powszechna", "wojny i bitwy"),
    1534: ("powszechna", "religia i Kościół"),
    1543: ("Polska", "kultura i nauka"),
    1545: ("powszechna", "religia i Kościół"),
    1555: ("powszechna", "religia i Kościół"),
    1569: ("Polska", "ustrój i prawo"),
    1573: ("Polska", "ustrój i prawo"),
    1596: ("Polska", "religia i Kościół"),
    1605: ("Polska", "wojny i bitwy"),
    1606: ("Polska", "ustrój i prawo"),
    1610: ("Polska", "wojny i bitwy"),
    1618: ("powszechna", "wojny i bitwy"),
    1619: ("Polska", "dyplomacja i traktaty"),
    1648: ("Polska", "wojny i bitwy"),
    1649: ("powszechna", "władcy i dynastie"),
    1654: ("Polska", "dyplomacja i traktaty"),
    1655: ("Polska", "wojny i bitwy"),
    1656: ("Polska", "religia i Kościół"),
    1658: ("Polska", "religia i Kościół"),
    1665: ("Polska", "ustrój i prawo"),
    1667: ("Polska", "dyplomacja i traktaty"),
    1672: ("Polska", "dyplomacja i traktaty"),
    1683: ("Polska", "wojny i bitwy"),
    1688: ("powszechna", "ustrój i prawo"),
    1699: ("Polska", "dyplomacja i traktaty"),
    1700: ("powszechna", "wojny i bitwy"),
    1703: ("powszechna", "cywilizacje i państwa"),
    1709: ("powszechna", "wojny i bitwy"),
    1712: ("powszechna", "cywilizacje i państwa"),
    1717: ("Polska", "ustrój i prawo"),
    1721: ("powszechna", "władcy i dynastie"),
    1748: ("powszechna", "kultura i nauka"),
    1751: ("powszechna", "kultura i nauka"),
    1762: ("powszechna", "kultura i nauka"),
    1764: ("Polska", "władcy i dynastie"),
    1765: ("Polska", "kultura i nauka"),
    1768: ("Polska", "ustrój i prawo"),
    1772: ("Polska", "dyplomacja i traktaty"),
    1773: ("Polska", "kultura i nauka"),
    1776: ("powszechna", "ustrój i prawo"),
    1787: ("powszechna", "ustrój i prawo"),
    1788: ("Polska", "ustrój i prawo"),
    1789: ("powszechna", "cywilizacje i państwa"),
    1791: ("Polska", "ustrój i prawo"),
    1792: ("Polska", "ustrój i prawo"),
    1793: ("Polska", "dyplomacja i traktaty"),
    1794: ("Polska", "wojny i bitwy"),
    1795: ("Polska", "dyplomacja i traktaty"),
}


def _dane_dat():
    sciezka = pathlib.Path(__file__).with_name('generuj_tabele_daty.py')
    spec = importlib.util.spec_from_file_location('tabela_daty', sciezka)
    modul = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modul)
    return modul.DANE, modul.EPOKI


def _tekst_bez_stylu(sciezka):
    """Zwraca czysty tekst pliku HTML, bez bloku <style> (żeby nie łapać font-weight itp.)."""
    import re
    tresc = sciezka.read_text(encoding='utf-8')
    tresc = re.sub(r'<style.*?</style>', ' ', tresc, flags=re.S)
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', tresc)))


def _wystepuje(rok, przed_nasza_era, tekst):
    """Czy dany rok występuje w tekście. Rozstrzyga kolizje typu 1792 p.n.e. vs 1792 r."""
    import re
    for m in re.finditer(rf'(?<![\d–-]){rok}(?![\d])', tekst):
        ogon = tekst[m.end():m.end() + 24]
        czy_pne = bool(re.match(r'[\s–-]*(?:\d{1,4}\s*)?(?:r\.\s*)?p\.n\.e\.', ogon))
        if czy_pne == przed_nasza_era:
            return True
    return False


# Słowa pisane wielką literą, które nie identyfikują wydarzenia (początki zdań, nazwy
# powtarzające się w wielu wydarzeniach). Bez tej listy „Początek” czy „Polski” dawałyby
# trafienie w każdym arkuszu.
STOPLISTA = {
    'początek', 'powstanie', 'koronacja', 'zwycięstwo', 'panowanie', 'uchwalenie', 'wybuch',
    'zdobycie', 'zajęcie', 'wygnanie', 'założenie', 'małżeństwo', 'zjednoczenie', 'cywilizacja',
    'bitwa', 'bitwy', 'pokój', 'pokoju', 'rozejm', 'ugoda', 'unia', 'chrzest', 'wojna', 'wojny',
    'pierwsza', 'pierwszy', 'pierwszej', 'drugi', 'drugiej', 'trzecia', 'trzeci', 'wielka',
    'wielkiej', 'wielkiego', 'wielkim', 'najazd', 'wezwanie', 'chwalebna', 'prasa', 'ołtarz',
    'nadanie', 'wydanie', 'przyjmuje', 'przeprawa', 'zburzenie', 'ustawa', 'przywilej',
    'konstytucja', 'konstytucji', 'deklaracja', 'sejm', 'sejmu', 'rokosz', 'konfederacja',
    'oblężenie', 'odsiecz', 'potop', 'akademia', 'teatr', 'edykt', 'sobór', 'schizma',
    'polski', 'polska', 'polskę', 'polskiego', 'europy', 'europie', 'kościoła', 'kościół',
    'kościoły', 'rzeczypospolitej', 'rzeczpospolita', 'rosją', 'rosji', 'rosja', 'turcją',
    'turcji', 'szwecją', 'szwecji', 'litwy', 'litwą', 'anglii', 'francji', 'niemiec',
    'cesarstwa', 'cesarstwo', 'papieża', 'papież', 'zakonu', 'zakonem', 'krzyżaków',
    'krzyżackim', 'krzyżackiego', 'stanów', 'zjednoczonych', 'ukrainy', 'prus', 'pruskiego',
    'gdańskiego', 'pomorza', 'krakowie', 'krakowa', 'mezopotamii', 'egiptu',
    # przymiotniki odmiejscowe i pokrewne, które nie wyróżniają wydarzenia
    'szwedzki', 'szwedzkiego', 'krzyżacki', 'rzymski', 'rzymskiego', 'miejskich',
    'miejskie', 'francuski', 'francuskiej', 'mongolski', 'olimpijskie', 'niebieskich',
    'królewski', 'chrześcijan', 'zachodniorzymskiego', 'wschodnia', 'społeczna',
}
POZIOMY = {'wysokie': 3, 'średnie': 2, 'niskie': 1, 'brak': 0}

# Hasła, których nie da się wyprowadzić z opisu wydarzenia — bo są to słowa z listy ogólnej
# (Gdańsk, Litwa) albo terminy w opisie niewystępujące (pismo klinowe, arianie). Podawane
# jako gotowe rdzenie w mianowniku małą literą; dopuszczalne wyrażenia wielowyrazowe.
HASLA_DODATKOWE = {
    -3000: ['klinow', 'hieroglif'],
    -264: ['punick'], -218: ['punick'], -217: ['punick'], -216: ['punick'],
    -202: ['punick'], -149: ['punick'], -146: ['punick'],
    1308: ['gdańsk'], 1387: ['litw'], 1466: ['gdańsk'],
    1525: ['hołd'], 1658: ['arianie', 'arianizm', 'bracia polscy', 'braci polskich'],
    1776: ['zjednoczonych'], 1787: ['zjednoczonych'],
}
DL_RDZENIA = 6  # dopasowanie po rdzeniu, bo polska odmiana zmienia końcówki


def _rdzen(slowo):
    return slowo.lower()[:DL_RDZENIA]


STOP_RDZENIE = {_rdzen(w) for w in STOPLISTA}


def _hasla(wydarzenie):
    """Rdzenie nazw odróżniających wydarzenie od innych. Bierzemy nazwy własne oraz
    przymiotniki odmiejscowe pisane małą literą („toruński”, „perejasławska”), bo często
    to one identyfikują wydarzenie w treści zadania."""
    import re
    slowa = re.findall(r'[A-ZĄĆĘŁŃÓŚŹŻ][\wąćęłńóśźż-]{4,}', wydarzenie)
    slowa += re.findall(r'\b[a-ząćęłńóśźż]{5,}(?:ski|skie|skiego|ska|cki|ckie|cka|nski|ński)\b',
                        wydarzenie)
    rdzenie = {_rdzen(s) for s in slowa} - STOP_RDZENIE
    return sorted(rdzenie)


def _uzycie_w_arkuszach(rekordy, katalog):
    """Szacuje ryzyko powtórzenia z trzech sygnałów: rok w treści arkusza (najmocniejszy),
    nazwa własna w treści arkusza, wzmianka wyłącznie w komentarzu klucza."""
    warianty = 'ABCDEFG'
    teksty = {}
    for w in warianty:
        for rodzaj, wzor in (('arkusz', 'test_szkolny_wariant_%s.html'),
                             ('klucz', 'klucz_odpowiedzi_wariant_%s.html')):
            p = katalog / (wzor % w)
            teksty[(w, rodzaj)] = _tekst_bez_stylu(p) if p.exists() else ''
    for r in rekordy:
        rok, pne = abs(r['sort']), r['sort'] < 0
        hasla = _hasla(r['wydarzenie']) + HASLA_DODATKOWE.get(r['sort'], [])
        r['hasla'] = hasla
        r['rok_w_arkuszu'] = [w for w in warianty
                             if _wystepuje(rok, pne, teksty[(w, 'arkusz')])]
        r['nazwa_w_arkuszu'] = [w for w in warianty
                                if w not in r['rok_w_arkuszu']
                                and any(h in teksty[(w, 'arkusz')].lower() for h in hasla)]
        uzyte = set(r['rok_w_arkuszu']) | set(r['nazwa_w_arkuszu'])
        r['tylko_w_kluczu'] = [w for w in warianty if w not in uzyte
                               and _wystepuje(rok, pne, teksty[(w, 'klucz')])]
        if r['rok_w_arkuszu']:
            r['ryzyko'] = 'wysokie'
        elif r['nazwa_w_arkuszu']:
            r['ryzyko'] = 'średnie'
        elif r['tylko_w_kluczu']:
            r['ryzyko'] = 'niskie'
        else:
            r['ryzyko'] = 'brak'
        r['status'] = 'wolne' if POZIOMY[r['ryzyko']] <= 1 else 'wykorzystane'
    return rekordy


def zbuduj():
    dane, epoki = _dane_dat()
    w_zakresie = [d for d in dane if d[0] <= GRANICA_ZAKRESU]
    brak = [d[1] for d in w_zakresie if d[0] not in KLASYFIKACJA]
    if brak:
        raise SystemExit('Brak klasyfikacji dla pozycji: ' + ', '.join(brak))
    rekordy = []
    for sort, etykieta, wydarzenie, warianty, _z_listy in w_zakresie:
        obszar, typ = KLASYFIKACJA[sort]
        epoka = next(n for n, od, do in epoki if od <= sort <= do)
        rekordy.append({
            'sort': sort,
            'data': etykieta,
            'wydarzenie': wydarzenie,
            'epoka': epoka,
            'obszar': obszar,
            'typ': typ,
            'warianty': warianty.split() if warianty else [],
        })
    return _uzycie_w_arkuszach(rekordy, KATALOG_WYJSCIA)


def podsumowanie(rek):
    wolne = [r for r in rek if r['status'] == 'wolne']
    print(f'Baza potencjalnych pytań — zakres do {GRANICA_ZAKRESU} r.')
    print(f'  pozycji razem: {len(rek)}')
    print('\nRyzyko powtórzenia (na podstawie arkuszy A–G):')
    for poz in ('brak', 'niskie', 'średnie', 'wysokie'):
        n = sum(1 for r in rek if r['ryzyko'] == poz)
        print(f'  {poz:9s} {n:3d}')
    print(f'\nDo wykorzystania w kolejnym wariancie (ryzyko brak lub niskie): {len(wolne)}')
    print('\nWg obszaru — to wąskie gardło przy bilansie 50/50:')
    for obszar in ('Polska', 'powszechna'):
        w = [r for r in wolne if r['obszar'] == obszar]
        wsz = [r for r in rek if r['obszar'] == obszar]
        print(f'  {obszar:11s} dostępnych {len(w):3d} z {len(wsz):3d}')
    print('\nWg epoki:')
    for epoka in dict.fromkeys(r['epoka'] for r in rek):
        print(f'  {epoka:16s} {sum(1 for r in wolne if r["epoka"] == epoka):3d}')
    print('\nWg typu zagadnienia:')
    for typ, n in Counter(r['typ'] for r in wolne).most_common():
        print(f'  {typ:24s} {n:3d}')
    print('\nWykaz pozycji do wykorzystania:')
    for r in wolne:
        znacznik = '·' if r['ryzyko'] == 'brak' else '~'
        print(f'  {znacznik} {r["data"]:18s} {r["obszar"]:11s} {r["typ"]:24s} '
              f'{r["wydarzenie"][:56]}')
    print('\n  · nie wystąpiło nigdzie   ~ tylko wzmianka w komentarzu klucza')


CSS = """
    @page { size: A4; margin: 13mm 12mm 15mm; }
    * { box-sizing: border-box; }
    body { margin: 0; color: #172033; font-family: "Arial","Helvetica",sans-serif;
      font-size: 9.2pt; line-height: 1.24; }
    h1 { font-size: 19pt; color: #163a63; margin: 0 0 2mm; }
    h2 { font-size: 12.4pt; color: #163a63; margin: 5mm 0 1.5mm; break-after: avoid; }
    .eyebrow { color: #9a5a00; font-weight: 700; letter-spacing: .7px;
      text-transform: uppercase; font-size: 8.6pt; }
    .intro { padding: 3mm 4mm; background: #eef5fb; border-left: 5px solid #1f5a91;
      margin-bottom: 4mm; font-size: 8.8pt; }
    table { width: 100%; border-collapse: collapse; }
    th, td { border: 1px solid #8090a2; padding: 1mm 1.7mm; vertical-align: top; }
    th { background: #eaf1f7; color: #163a63; text-align: left; font-size: 8.8pt; }
    thead { display: table-header-group; }
    tr { break-inside: avoid; }
    .data { width: 25mm; white-space: nowrap; font-weight: 700; color: #163a63; }
    .obszar { width: 21mm; white-space: nowrap; font-size: 8.4pt; }
    .typ { width: 34mm; font-size: 8.4pt; color: #4c596b; }
    .st { width: 27mm; white-space: nowrap; text-align: center; font-size: 8.2pt;
      font-weight: 700; }
    .wolne { color: #1f7a3d; }
    .uzyte { color: #9a5a00; }
    .blok { color: #a12a2a; }
    .legenda { margin: 2mm 0 0; font-size: 8.2pt; color: #4c596b; }
    .legenda li { margin-bottom: .6mm; }
    .zbiorcza td, .zbiorcza th { text-align: center; }
    .zbiorcza td:first-child, .zbiorcza th:first-child { text-align: left; }
    .stopka { margin-top: 4mm; font-size: 8.2pt; color: #606b79;
      border-top: 1px solid #c7cfd8; padding-top: 2mm; }
"""


def widok_html(rek):
    wolne = [r for r in rek if r['status'] == 'wolne']
    out = ['<!doctype html>', '<html lang="pl">', '<head>', '<meta charset="utf-8">',
           '<title>Baza potencjalnych pytań</title>', f'<style>{CSS}</style>', '</head>',
           '<body>', '<div class="eyebrow">Materiał roboczy • planowanie wariantów</div>',
           '<h1>Baza potencjalnych pytań</h1>',
           f'<div class="intro">Wydarzenia mieszczące się w zakresie Wojewódzkiego Konkursu '
           f'Przedmiotowego, czyli do III rozbioru Polski ({GRANICA_ZAKRESU} r.) — razem '
           f'<strong>{len(rek)}</strong> pozycji. Wydarzenia późniejsze są poza zakresem '
           f'i do bazy nie wchodzą.<br>Kolumna <em>Ryzyko</em> mówi, na ile dane zagadnienie '
           f'jest już zużyte przez warianty A–G. Zupełnie nietkniętych pozycji zostało tylko '
           f'<strong>{len(wolne)}</strong>, więc pula samych dat jest praktycznie wyczerpana: '
           f'świeżość kolejnego arkusza trzeba budować nie na nowych datach, ale na nowym '
           f'ujęciu znanych wydarzeń — innym źródle, innej formie zadania, innym aspekcie. '
           f'Praktycznym zapleczem są pozycje <span class="uzyte">ŚREDNIE</span> '
           f'(<strong>{sum(1 for r in rek if r["ryzyko"] == "średnie")}</strong>): wystąpiły '
           f'w arkuszu bez daty, więc pytanie o samą datę jest wciąż nowe.</div>',
           '<ul class="legenda">',
           '<li><span class="wolne">BRAK</span> — zagadnienie nie wystąpiło dotąd nigdzie.</li>',
           '<li><span class="wolne">NISKIE</span> — pojawiło się wyłącznie we komentarzu '
           'klucza, nie w treści zadania; uczeń go nie widział.</li>',
           '<li><span class="uzyte">ŚREDNIE</span> — nazwa własna wystąpiła w treści arkusza, '
           'ale bez daty. Można wrócić do zagadnienia w innej formie zadania.</li>',
           '<li><span class="blok">WYSOKIE</span> — data wystąpiła w treści arkusza. '
           'Powtórzenie liczy się do limitu 30%.</li>', '</ul>']

    # zbiorcza tabela dostępnych zasobów
    out += ['<h2>Ile zagadnień zostało do wykorzystania</h2>',
            '<table class="zbiorcza"><thead><tr><th>Obszar</th><th>Brak</th><th>Niskie</th>'
            '<th>Do wzięcia</th><th>Średnie</th><th>Wysokie</th><th>Razem</th></tr></thead>'
            '<tbody>']
    for obszar in ('Polska', 'powszechna', None):
        wsz = [r for r in rek if obszar is None or r['obszar'] == obszar]
        licz = Counter(r['ryzyko'] for r in wsz)
        dost = licz['brak'] + licz['niskie']
        nazwa = ('<strong>razem</strong>' if obszar is None
                 else 'historia ' + ('powszechna' if obszar == 'powszechna' else 'Polski'))
        out.append(f'<tr><td>{nazwa}</td><td>{licz["brak"]}</td><td>{licz["niskie"]}</td>'
                   f'<td class="wolne"><strong>{dost}</strong></td>'
                   f'<td>{licz["średnie"]}</td><td>{licz["wysokie"]}</td>'
                   f'<td>{len(wsz)}</td></tr>')
    out.append('</tbody></table>')

    klasy = {'brak': 'wolne', 'niskie': 'wolne', 'średnie': 'uzyte', 'wysokie': 'blok'}
    for epoka in dict.fromkeys(r['epoka'] for r in rek):
        poz = [r for r in rek if r['epoka'] == epoka]
        w = sum(1 for r in poz if r['status'] == 'wolne')
        out += [f'<h2>{html.escape(epoka)} <span style="font-size:8.4pt;color:#5c6878">'
                f'({len(poz)} pozycji, do wzięcia {w})</span></h2>',
                '<table><thead><tr><th class="data">Data</th><th>Wydarzenie</th>'
                '<th class="obszar">Obszar</th><th class="typ">Typ zagadnienia</th>'
                '<th class="st">Ryzyko</th></tr></thead><tbody>']
        for r in poz:
            gdzie = r['rok_w_arkuszu'] or r['nazwa_w_arkuszu'] or r['tylko_w_kluczu']
            opis = r['ryzyko'].upper() + (f' ({"".join(gdzie)})' if gdzie else '')
            out.append(f'<tr><td class="data">{html.escape(r["data"])}</td>'
                       f'<td>{html.escape(r["wydarzenie"])}</td>'
                       f'<td class="obszar">{html.escape(r["obszar"])}</td>'
                       f'<td class="typ">{html.escape(r["typ"])}</td>'
                       f'<td class="st"><span class="{klasy[r["ryzyko"]]}">'
                       f'{html.escape(opis)}</span></td></tr>')
        out.append('</tbody></table>')

    out += ['<p class="stopka">Baza generowana z <code>tools/baza_pytan.py</code> na podstawie '
            'dat z <code>tools/generuj_tabele_daty.py</code> oraz treści arkuszy i kluczy '
            'A–G. Ryzyko wyliczane automatycznie: skrypt szuka w arkuszach roku wydarzenia '
            'oraz jego nazw własnych, dlatego przy zagadnieniach opisanych w arkuszu bardzo '
            'omownie ocena może być zaniżona — przed użyciem pozycji warto zajrzeć do '
            'wskazanego wariantu. Po dodaniu nowego arkusza wystarczy uruchomić skrypt '
            'ponownie.</p>', '</body>', '</html>']
    return '\n'.join(out)


if __name__ == '__main__':
    rekordy = zbuduj()
    if '--json' in sys.argv:
        cel = KATALOG_WYJSCIA / 'baza_pytan.json'
        cel.write_text(
            json.dumps({'granica_zakresu': GRANICA_ZAKRESU, 'typy': TYPY,
                        'pozycje': rekordy}, ensure_ascii=False, indent=2),
            encoding='utf-8')
        print(f'Zapisano {cel} — {len(rekordy)} pozycji')
    elif '--html' in sys.argv:
        sys.stdout.write(widok_html(rekordy))
    else:
        podsumowanie(rekordy)
