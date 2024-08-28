venner = ['Ole', 'Donald', 'Doffen']    # Oppretter en liste med 3 elementer

print(type(venner)) # Typen til venner, som er 'list'
print(len(venner))  # Antall elementer i listen
print(venner)       # Utskrift av listen: ['Ole', 'Donald', 'Doffen']

print(venner[0])    # Det første elementet i listen: Ole
print(venner[1])    # Det andre elementet i listen: Donald
print(venner[len(venner) - 1])  # Det siste elementet i listen: Doffen
print(venner[-1], '\n')   # Det siste elementet i listen + linjeskift: Doffen

venner[1] = 'Dole'  # Gir en ny verdi til listens andre element
print(venner)       # Ny liste er nå: ['Ole', 'Dole', 'Doffen']




