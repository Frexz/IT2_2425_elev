# Øvingsoppgaver 2.6 - Objektorientert programmering

## 2.6.1
Legemidler deles ofte inn i tre kategorier: vanlige, vanedannende og narkotiske legemidler. Et legemiddel skal ha følgende attributter:
- navn: str
- pris: int
- virkestoff: float

I tillegg må alle legemidler ha en egen ID (klassevariabel) som er unik for hvert legemiddel. F.eks kan man ha et system slik at første opprettede legemiddel har ID = 1, mens neste har ID = 2 osv.

Et legmiddel tilhører én av de tre kategoriene nevnt ovenfor og objekter skal da kun opprettes som én av tre subklasser: Vanlig, Narkotisk eller Vanedannende. Disse subklassene har alle attributter og metoder som Legemiddel, men har i tillegg:

- Narkotisk har et attributt med et heltall som sier hvor sterkt narkotisk det er
- Vanedannende har et attributt med et heltall som sier hvor vanedannende det er
- Vanlig har ingen øvrige egenskaper enn Legemiddel

#### Oppgaven
Skriv klassene **Legemiddel, Narkotisk, Vanedannende og Vanlig**. De tre sistnevnte skal arve fra den første. Konstruktøren til **Legemiddel** (og dermed også **Vanlig**) skal ta inn et navn, pris og virkestoff. Kontruktørene til **Narkotisk** og **Vanedannende** skal i tillegg ta inn styrke.

**Legemiddel** skal ha metodene ``hent_id``, ``hent_navn``, ``hent_pris`` og ``hent_virkestoff`` som returnerer de relevante verdiene. I tillegg skal klassen ha metoden ``sett_ny_pris`` som skal ved hjelp av en parameter sette en ny pris.

** Narkotisk** har i tillegg metoden ``hent_narkotisk_styrke`` og **Vanedannende** har metoden ``hent_vanedannende_styrke``.

Alle klassene bør har en ``__str__``-metode som man kan bruke til å skrive ut all relevant informasjon om klassen.

## 2.6.2
I denne oppgaven skal du skrive to klasser: ``Lege`` og ``Spesialist``.

#### Lege
Klassen ``Lege`` har kun attributtet navn: str som den får fra konstruktøren.

#### Spesialist
Klassen ``Spesialist`` arver fra klassen lege og har i tillegg attributtet kontroll_id: int.
Den har også metodene ``hent_kontroll_id`` som returnerer kontroll-id'en og ``sjekk_kontroll_id`` som sjekker legens kontroll-id mot en parameter. Metoden skal returnere true/false ut fra om id'en matcher parameteren.