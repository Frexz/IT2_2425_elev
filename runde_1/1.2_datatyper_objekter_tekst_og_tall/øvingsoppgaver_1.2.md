# Øvingsoppgaver 1.2
I oppgavene under brukes også operatorene for heltallsdivisjon (``//``) og modulo (``%``). Heltallsdivisjon gir oss hvor mange hele ganger et tall går opp i et annet. Modulo gir resten i en heltallsdivisjon.

F.eks
```
13 // 5 = 2
```
```
13 % 5 = 3 fordi 13 = 2*5 + 3
```

## 1.2.1
Bruk eksempelet om flytid og regn ut tiden i timer, minutter og sekunder. I denne oppgaven skal du kunne bruke ``*``, ``/``, ``+`` og ``-`` samt ``int()``.

Gjør om flytiden til sekunder og bruk ``//`` (heltallsdivisjon) og ``%`` modulo for å gjøre det samme.

Bruk ``divmod`` til å gjøre det samme. ``divmod`` utfører både heltallsdivisjon og modulo. Eksempel: ``kvotient, rest = divmod(13, 5)`` gir ``kvotient = 2`` og ``rest = 3``.

Bruke ``datetime.timedelta`` klassen til å gjøre det samme. Den tillater at du oppgir antall timer som desimaltall og når vi gjør om objektet om til tekst med ``str()``, får vi teksten på formatet ``tt:mm:ss``. Sekundene vises med desimaler som kan fjernes. Huske å ha med ``import datetime``.

## 1.2.2
Lag en variabel som referer til teksten 'jeg bor i Norge.'. Bruk IntelliSense til å utforske metodene til tekstobjektet. Beskriv spesifikt forskjellen mellom metodene ``capitalize()``, ``title()`` og ``lower()``. Bruk ``print()`` til å vise resultatene.