def regn(a: float, b: float) -> tuple[float, float, float, float]:
    return a + b, a - b, a * b,  a / b


# Test
sum_, diff, prod, kvot = regn(2, 3)


assert sum_ == 5
assert diff == -1
assert prod == 6
assert kvot == 2 / 3

print("Testen er bestått!")