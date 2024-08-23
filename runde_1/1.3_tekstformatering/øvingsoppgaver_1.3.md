# Øvingsoppgaver 1.3
Her er noen tips som er greie å vite før dere løser disse oppgavene:
- Når man skriver ut tekst, kan man sette inn en tab/innrykk med ``\t`` og linjeskift/ny linje med ``\n``. Eks. ``print('Første linje\nAndre linje')`` vil skrives ut på to linjer.
- Når brukeren skriver inn et tall kan man sjekke om teksten også er et heltall med metoden ``str.isnumeric()``.

## 1.3.1
Bruk kun ``print``-setninger og skriv teksten 'Vertikal' med én bokstav på hver linje.

Gjør det samme med en løkke.
**Hint:** en tekst/streng er en liste med tegn som kan brukes likt som lister i ``for``-setninger. Funksjonen ``list()`` gjør også at ``list('Tekst')`` blir ``['T','e', 'k', 's', 't']``

Gjør det samme med kun én ``print``-setning og bruken av ``\n``.

Gjør det samme med metoden ``str.join()``.
**Eksempel:** ``'+'.join(['a', 'b', 'c'])`` gir ``'a + b + c'``

## 1.3.2
Skriv et program som oversetter vanlige tall (titallssystemet) til binære tall. Dersom brukeren skriver inn noe som ikke er et heltall, skal de gis en tilbakemelding. Du kan bruke ``str.isnumeric()`` til å sjekke om teksten danner et heltall.

Eksempel på kjøring:
```
Skriv inn et heltall: 5
5 i titallssystemet er 101 binært.

Skriv inn et tall: fem
fem er ikke et tall.
```

Utvid programmet ved å la det gå i løkke helt til brukeren skriver ``'slutt'``.

## 1.3.3
Skriv ut listen nedenfor slik at tallene kommer under hverandre med komme på samme plass og med 1 desimal.

```
[1, 2.3, 4.56, 7.890, 12.34, 567.890]
```
Utskrift:
```
  1.0
  2.3
  4.6
  7.9
 12.3
567.9
```