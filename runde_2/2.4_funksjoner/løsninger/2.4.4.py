def unike_bokstaver(tekst):
    unike = []
    for bokstav in tekst.lower():
        if bokstav not in unike and bokstav.isalpha():
            unike.append(bokstav)
    return len(unike)

tekst = "Sesam, sesam, lukk deg opp!"

assert unike_bokstaver(tekst) == 11