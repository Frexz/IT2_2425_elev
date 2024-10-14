# Øvingsoppgaver 2.1

### 2.1.1
Ta for deg oppgave 1.7.2 (og 1.3.2) som oversetter vanlige tall (titallssystemet) til binære tall. Løs oppgaven med GUI. Ta gjerne utgangspunkt i løsningsforslaget til oppgave 1.7.2.

### 2.1.2
Ta for deg oppgave 1.2.1 om beregning av flytid og løs oppgaven med GUI. Ta gjerne utgangspunkt i løsningsforslaget til oggaven og sett inn bilde av en hastighetsmåler hvis du ønsker.

### 2.1.3 - Eksamensoppgave Høsten 2019
Du skal lage en applikasjon som beregner kaloriforbruk for en gitt aktivitet - en slags treningskalkulator. Beregningen skal basere seg på valgt **aktivitet** i kombinasjon med valgt **intensitet** og **varighet** på treningen.

#### Krav
- Brukeren skal kunne velge mellom disse fem aktivitetene:
    - Aerobic (814 kcal/time)
    - Bordtennis (236 kcal/time)
    - Fotball (510 kcal/time)
    - Golf (244 kcal/time)
    - Jogging (666 kcal/time)
- Brukeren skal kunne velge mellom disse intensitetsnivåene:
    - Lavt (Du kan gange kaloriforbruket med 0,8 for å trekke fra 20%)
    - Middels (Kaloriforbruket som er oppgitt)
    - Høyt (Du kan gange kaloriforbruket med 1,2 for å legge til 20%)
- Brukeren skal kunne oppgi varighet i minutter.

*Tips: Én time er 60 minutter. Du må dele oppgitt varighet i minutter på 60 for å få antall timer.*

- Løsningen skal implementeres etter denne grensesnittskissen:
    - Brukeren skal velge aktivitet fra en nedtrekksliste.
    - Brukeren skal velge intensitet på treningen ved å velge én av tre radiobuttons.
    - Brukeren skal oppgi varighet på treningen i minutter i et tekstfelt.
    - Ved klikk på knappen skal kaloriforbruket for valgt aktivitet, intensitet og angitt varighet beregnes og vises.

![treningskalkulator wireframe](/img/kaloriforbruk.png)
