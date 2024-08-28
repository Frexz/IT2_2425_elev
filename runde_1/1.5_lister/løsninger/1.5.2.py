frukt = ['eple', 'appelsin', 'banan']

frukt.append('kiwi')
print(f'a) {frukt}')

indeks = frukt.index('appelsin')
frukt[indeks] = 'plomme'
print(f'b) {frukt}')

frukt.remove('banan')
print(f'c) {frukt}')