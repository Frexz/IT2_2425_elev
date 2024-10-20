def antall_vokaler(tekst):
    vokaler = "aeiouyæøå"
    antall = 0
    for bokstav in tekst:
        if bokstav in vokaler:
            antall += 1
    return antall

tekst = "Vil du være med på turen i høst?"

assert antall_vokaler(tekst) == 10