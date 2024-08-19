# Med addisjon
totalt = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
print(totalt)

# Med løkke
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
totalt = 0

for tall in liste:
    totalt += tall

print(totalt)

# Med range
totalt = 0

for tall in range(1, 11):
    totalt += tall

print(totalt)

# Med totalt
liste = range(1, 11)
totalt = sum(liste)
print(totalt)

# Hvis man kombinerer range- og totalt- funksjonene kan koden skrives på 2-3 linjer
# uavhengig av hvor mange tall som skal totaltmeres.

# Med rekke
totalt = 10*(10 + 1) / 2 # Sum av aritmetisk rekke der n = 10, a_1 = 1, og a_n = 10
print(totalt)