### Utsnitt, henter ut deler av listen
venner = ['Ole', 'Dole', 'Doffen', 'Donald']

print(venner)       # Hele listen
print(venner[1:3])  # Fra og med element på indeks 1 opp til elementet, men ikke inkludert, på indeks
                    # 3: ['Dole', 'Doffen']
print(venner[:2])   # Fra og med begynnelsen av listen opp til, men ikke inkludert, elementet på
                    # indeks 2: ['Ole', 'Dole']
print(venner[2:])   # Fra og med elementet på indeks 2 og resten av listen: ['Doffen', 'Donald']
print(venner[1::2]) # Fra og med elementet på indeks 1 og resten av listen, men med steg lik 2,
                    # altså annenhvert element: ['Dole', 'Donald']
print(venner[:])    # Fra og med begynnelsen til og med slutten av listen, altså hele listen.