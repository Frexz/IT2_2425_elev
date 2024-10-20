# Funksjoner har også egenskapen at de kan returnere en verdi.
# Dette gjør man med 'return'.

# den matematiske funksjonen f(x) = x^2 + 4x - 1
def f(x: float) -> float:
    return x**2 + 4*x - 1

# Funksjonskallet byttes ut med returverdien til funksjonen.
for i in range(6):
    print(f'f({i}) = {f(i)}')

# Ofte må man 'fange' returverdier i en variabel.
y = f(5)


# Man kan også ha flere enn én returverdi. Da returneres verdiene som en tuppel.
def kvadrat_kubikk(x: float) -> tuple[float, float]:
    return x**2, x**3

# Da må man bruke flere varibler for å 'fange' returverdiene
kvadrat, kubikk = kvadrat_kubikk(4)
print(kvadrat, kubikk)
