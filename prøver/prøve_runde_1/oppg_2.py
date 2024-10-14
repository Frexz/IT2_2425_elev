vokaler = "aeiouyæøå"
ord = input('Skriv inn et ord: ').lower()
antall_vokaler = 0

for bokstav in ord:
    if bokstav in vokaler:
        antall_vokaler += 1

print(f"Ordet har {antall_vokaler} vokaler.")
