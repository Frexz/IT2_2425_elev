def finn_maks(liste):
    maks = liste[0]     # Det første
                        # tallet i lista
    for tall in liste:
        if tall > maks:
            maks = tall

    return maks

liste1 = [3, 8, 5, 11, 7]
print(liste1)
print(finn_maks(liste1))    # Skriver ut 11

liste2 = [1, 13, 4, 5, 3, 3, 8, 5, 11, 7]
print(liste2)
print(finn_maks(liste2))    # Skrive ut 13