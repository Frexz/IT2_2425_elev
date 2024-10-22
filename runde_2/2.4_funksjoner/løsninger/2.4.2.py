def fjern_over_10(tall: list[float]) -> list[float]:
    return [x for x in tall if x <= 10]

# Test
tall = [4, 12, 3, 8, 23, 5, 11, 9]

assert fjern_over_10(tall) == [4, 3, 8, 5, 9]

print("Testen er bestått!")