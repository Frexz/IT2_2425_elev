# Øvingsoppgaver 1.4

# 1.4.1
Forklar hva som skjer i koden nedenfor:
```
for i in range(1, 4):
    print('i: ' + str(i))
    for j in range(1, 3):
        print('i: ' + str(i) + ' og j:' + str(j))
```

# 1.4.2
Lag et program som skriver ut partallene fra 100 og ned til og med 80.
```
100 98 96 94 92 90 88 86 84 82 80
```

# 1.4.3
Lag et program som skriver ut de 10 første kubikktallene på én linje (1, 8, 27 osv.)
```
   1   8   27   64   125   216   343   512   729   1000
```

# 1.4.4
Utvid gangetabell-eksempel til å inkludere kolonne- og rad-overskrifter
```
   |   1   2   3   4   5   6   7   8   9  10
--------------------------------------------
1  |   1   2   3   4   5   6   7   8   9  10
2  |   2   4   6   8  10  12  14  16  18  20
3  |   3   6   9  12  15  18  21  24  27  30
4  |   4   8  12  16  20  24  28  32  36  40
5  |   5  10  15  20  25  30  35  40  45  50
6  |   6  12  18  24  30  36  42  48  54  60
7  |   7  14  21  28  35  42  49  56  63  70
8  |   8  16  24  32  40  48  56  64  72  80
9  |   9  18  27  36  45  54  63  72  81  90
10 |  10  20  30  40  50  60  70  80  90 100
```

# 1.4.5
Lag et program som skriver ut alle Fibonacci-tallene under 1000 i fem kolonner. Det første taller er 0. Det andre tallet
er 1. Det tredje er summe av de to foregående, ``0 + 1 = 1``. Det fjerde er summen av de to foregående tallene ``1 + 1 = 2``, 
og slik fortsetter det: ``1 + 2 = 3``, ``2 + 3 = 5``, ``3 + 5 = 8``, osv: ``0, 1, 1, 2, 3, 5, 8, 13, 21 ...``
```
------Fibonaccitallene under 1000-------
       0       1       1       2       3
       5       8      13      21      34
      55      89     144     233     377
     610     987
```