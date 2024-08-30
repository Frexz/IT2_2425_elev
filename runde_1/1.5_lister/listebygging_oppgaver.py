# Listebygging
# Lag en liste som
import random
import math

def egenskapsverdi():
    resultater = [random.randint(1,6) for x in range(4)]
    resultater.sort(reverse=True)
    return sum(resultater[:3])

# 1. Inneholder alle tall fra 80 til og med 100
l1 = [x for x in range(80, 101)]
# 2. Inneholder alle partall mellom 100 og 200
l2 = [x for x in range(100, 201) if x % 2 == 0]
# 3. Inneholder de 10 første kvadrattallene
l3 = [x**2 for x in range(1, 11)]
# 4. Inneholder første og siste bokstav i navnet ditt
navn = 'Fredrik'
l4 = [b for b in navn if navn.index(b) == 0 or navn.index(b) == len(navn) - 1]
# 5. Inneholder 6 tilfeldige terningkast
l5 = [egenskapsverdi() for x in range(6)]
print(l5)
# 6. Inneholder kvadratroten av tallene mellom 20 og 30
l6 = [math.sqrt(x) for x in range(20, 31)]