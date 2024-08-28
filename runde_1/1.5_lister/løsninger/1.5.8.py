from math import sqrt

tall = [x for x in range(2, 101)]   # Lager liste med tall fra 2 til og med 100

for i in range(2, round(sqrt(100))):                    # Gjentas fra 2 opp til 10
    tall = [x for x in tall if x % i != 0 or x == i]    # Fjerner alle tall delelig med i, bortsett
                                                        # fra tall lik i

print('Primtall under 100:')
for i in range(len(tall)):

    if i % 5 == 0 and i != 0:   # Legger til et linjeskift for hvert femte element
        print()                 # hopper over første gang

    print(f'{tall[i]:4}', end='')

    