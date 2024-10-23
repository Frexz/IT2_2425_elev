def tall_med_siffer(siffer):
    tall_liste = []
    for tall in range(100):
        if str(siffer) in str(tall):
            tall_liste.append(tall)
    return tall_liste

# Test
assert tall_med_siffer(5) == [5, 15, 25, 35, 45, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 65, 75, 85, 95]
assert tall_med_siffer(7) == [7, 17, 27, 37, 47, 57, 67, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 87, 97]

print("Testen er bestått!")