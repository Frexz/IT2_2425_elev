def binary_search(liste: list, tall: int):
    liste.sort()
    count = 0
    while liste:
        i = int(len(liste) / 2)
        m = liste[i]
        if m == tall:
            return count
        elif tall > m:
            liste = liste[i + 1:]
        else:
            liste = liste[:i]
        count += 1
    return count

liste = [x for x in range(1, 1000001)]

print(binary_search(liste, 2000000))