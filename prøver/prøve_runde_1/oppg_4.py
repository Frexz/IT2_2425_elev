def midterste(tall):
    sortert = sorted(tall)
    indeks = tall.index(sortert[1])
    return indeks

assert midterste([2, 3, 1]) == 0
assert midterste([5, 10, 14]) == 1
assert midterste([3, 5, 4]) == 2

print("Programmer kjørte uten problemer.")