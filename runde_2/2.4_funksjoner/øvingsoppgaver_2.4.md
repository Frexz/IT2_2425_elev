# Øvingsoppgaver 2.4 - Funksjoner

## 2.4.1
Lag en funksjon som tar inn to tall og returnerer summen, differansen, produktet og kvotienten av de to tallene som en tuppel. I denne oppgaven kreves ikke feilhåndtering dersom der andre tallet er null.

```
~ Eksempel ~

Input: 2, 3
Output: (5, -1, 6, 0.666666)
```

## 2.4.2
Lag en funksjon som fjerner alle tall over 10 fra en liste med tall. Funksjonen skal returnere en ny liste.

```
~ Eksempel ~

Input: [4, 12, 3, 8, 23, 5, 11, 9]
Output: [4, 3, 8, 5, 9]
```

## 2.4.3
Lag en funksjon som skriver ut hvor mange vokaler det er i en tekststreng.

```
~ Eksempel ~

Input: "Vil du være med på turen i høst?"
Output: 10
```

## 2.4.4
Lag en funksjon som skriver ut hvor mange forksjellige bokstaver det er i en tekststreng. Når vi telle, skal vi ikke skille mellom store og små bokstaver. **Hint:** Du kan sjekke om en karakter er en bokstav med ``karakter.isalpha()``.

```
~ Eksempel ~

Input: "Sesam, seasam, lukk deg opp!"
Output: 11
```

## 2.4.5
a) Lag en funksjon som skriver ut en pyramide som vist nedenfor til venstre. Prøve å gjøre det med ``for``-løkke med bare én setning. **Tips:** ``4*" "`` er ``"    "``.

b) Lag en funksjon som skriver ut en liten (S), medium (M) eller stor (L) pyramidel Funksjonen skal altså defineres med en parameter og kalles opp med et argument. Tillatt både store og små bokstaver.

```
Liten pyramide (S):

  *  
 *** 
*****

Medium pyramide (M):

    *    
   ***   
  *****  
 *******
*********

Stor pyramide (L):

      *     
     ***
    *****
   *******
  *********
 ***********
*************
```

## 2.4.6
Anta det er 50 km mellom Askim og Oslo. Det er kø, og vi har en gjennomsnittshastighet på 50 km/t til Oslo. Hjem igjen er det ingen trafikk på motorveien og gjennomsnittshastigheten er 100 km/t. Gjennomsnittshastigheten tur/retur Oslo er ikke 75 km/t (aritmetisk gjennomsnitt), men 67 km/t (harmonisk gjennomsnitt). Det innser vi lett når vi har kjørt 100 km på 1,5 timer. Formelen for harmonisk gjennomsnitt er:

```
n / (1/x_1 + 1/x_2 + 1/x_3 + ... + 1/x_n)
```

Lag en funksjon, ``harm_gjsn``, som tar som argument en liste med verdier og returnerer det harmoniske gjennomsnittet av verdiene.

```
~ Eksempel ~

Input: [50, 100]
Output: 66,7

Input: [5, 15, 25]
Output: 9,8
```

## 2.4.7
Lag en funksjon, ``tall_med_siffer``, som tar som argument et siffer (0-9), og returnerer en liste med alle tall fra 0 til 00 som inneholder det angitte sifferet.

```
~ Eksempel ~

Input: 5
Output: [5, 15, 25, 35, 45, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 65, 75, 85, 95]

Input: 7
Output: [7, 17, 27, 37, 47, 57, 67, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 87, 97]
```