def pyramide(n):
    for i in range(n):
        print((n - 1 - i)*" " + (2*i + 1)*"*" + (n - 1 - i)*" ")

størrelse = input("Hvor stor skal pyramiden være? (S, M eller L) ").upper()

if størrelse == "S":
    pyramide(3)
elif størrelse == "M":
    pyramide(5)
elif størrelse == "L":
    pyramide(7)
else:
    print("Størrelsen du oppga er ikke gyldig.")
