from math import floor

bokstaver = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

print(f'a) {bokstaver[:3]}')

# For denne listen kunne man også bare ha skrevet ut bokstaver[2:5]
midterste_indeks = floor(len(bokstaver) / 2)
print(f'b) {bokstaver[midterste_indeks - 1:midterste_indeks + 2]}')

print(f'c) {bokstaver[2:]}')