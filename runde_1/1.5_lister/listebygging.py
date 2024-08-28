### Listebygging - Listebygging, eller list comprehension, lar oss lage lister på en 
# effektiv og kompakt måte basert på innholdet i ulike Iterables (lister, strenger og sekvenser).

# Kvadrattallene - de 10 første kvadrattallene.
kvadrater = [x**2 for x in range(1, 11)]
print(f'Kvadrater:\n{kvadrater}')

# Tall som inneholder sifferet 2 - alle tall fra 1 til 100 som inneholder sifferet 2
tall = [x for x in range(1, 101) if '2' in str(x)]
print(f'Tall med siffer 2:\n{tall}')

# Gjøre en matrise flat - Gjør en flerdimensjonal liste om til en endimensjonal liste
flerdimensjonal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print('Flerdimensjonal:')
for rad in flerdimensjonal:
    print(rad)

endimensjonal = [tall for rad in flerdimensjonal for tall in rad]
print(f'Endimensjonal:\n{endimensjonal}')