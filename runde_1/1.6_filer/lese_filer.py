### Lese filer - for å åpen en fil bruker man funksjonen open() med filbanen som argument.
# Hvis filen man leser er i samme mappe som Python-programmet er det tilstrekkelig å oppgi navnet 
# på filen med filtype, som en streng. Bruker man open() burde man også bruke close() når filen er lest.
# Om man bruker en with-setning, derimot, lukkes filen automatisk når blokken fullføres.

# Åpne med with setning. Variabelen fil peker på fil-objektet som åpnes.
with open('navn.txt') as fil:
    # read() - leser alt innholdet i filen
    data = fil.read()
    print('read():')
    print(data)

    # seek() - flytter filmarkøren til oppgitt posisjon/indeks
    fil.seek(1)
    data = fil.read(2)  # Leser bare to tegn fra der filmarkøren er
    print('\nseek(1), read(2): ')
    print(data)

    # readlines() - leser hver linje og samler dem som elementer i en liste. Legg merke til at hver
    # linje avsluttes med \n
    fil.seek(0)
    linjer = fil.readlines()
    print('\nreadlines(): ')
    print(linjer)

    # readline() - leser en og en linjer
    fil.seek(0)
    print('\nreadline(): ')
    print(fil.readline().lower(), end='')
    print(fil.readline().lower())

    # for-løkke - man kan også iterere gjennom en fil linje for linje med en for-løkke
    fil.seek(0)
    print('\nfor-løkke')
    for linje in fil:
        print(linje.upper(), end='')
