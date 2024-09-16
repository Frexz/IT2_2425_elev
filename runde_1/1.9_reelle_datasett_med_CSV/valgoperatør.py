# Det er mulig å ha en if-setning på én linje. Da kalles den en valgoperatør.
# Syntaksen er slik: <verdi hvis True> if <betingelse> else <verdi hvis False>
# Slik kan man gi variabler ulike verdier avhengig av betingelsen. Man kan selvsagt gjøre det samme med en
# if-else-blokk, men denne måten er litt mer kompakt og spesielt egnet for enkle valg.
for i in range(4):
    tidsenhet = 'timer' if i != 1 else 'time'
    print(f'{i} {tidsenhet}')