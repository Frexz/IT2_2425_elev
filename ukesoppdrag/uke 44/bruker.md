# Oppgave til selvstudie uke 44

## 1.  Gjør ferdig Bankkonto-programmet
Fullfør Bankkonto-programmet ved å legge til metoder som håndterer både oppdatering av Bankkonto-objektet og oppdatering av GUI. Legg også til en Label som gir beskjed når man tar ut mer penger enn det man har på konto.

## 2. Bruker-klasse
I denne oppgaven skal du skrive en klasse som heter Bruker.

Klassen skal ha følgende attributter som får verdier via parametere:
- brukernavn: str
- passord: str

Klassen skal ha følgende metode:
- bytt_passord(gammelt: str, nytt: str): void

Altså skal metoden ta gammelt passord som parameter og et nytt passord som parameter. Passordet skal kun byttes hvis gammelt passord matcher passordet til brukeren. Hvis ikke skal det skrive ut feilmelding.

Opprett følgende brukere som du legger til en ordbok med brukernavnet som nøkkel og et objekt fra Bruker-klassen som verdi:
- brukernavn: "bruker123", passord: "passord"
- brukernavn: "kiwi_lover_93", "123456789"
- brukernavn: "admin", "admin"

Test at du får til å bytte passord til brukeren med navn "admin".