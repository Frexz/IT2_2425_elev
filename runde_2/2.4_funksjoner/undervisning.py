def regn_ut(a: float, b: float) -> tuple[float, float, float, float]:
    sum_ = a + b
    diff = a - b
    prod = a * b
    try:
        kvot = round(a / b, 3)
    except ZeroDivisionError:
        kvot = 'ugyldig'
    return sum_, diff, prod, kvot

assert regn_ut(2, 3) == (5, -1, 6, 0.667), f"Feil, fikk {regn_ut(2, 3)} i stedet."
assert regn_ut(5, 0) == (5, 5, 0, 'ugyldig')
assert regn_ut(-4, -3) == (-7, -1, 12, 1.333)

print("Funksjonen bestod testen!")




