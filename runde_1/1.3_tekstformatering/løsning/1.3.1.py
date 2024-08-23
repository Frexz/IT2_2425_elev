# Med print-setninger
print('Med print-setninger'.center(50, '-'))
print('V')
print('e')
print('r')
print('t')
print('i')
print('k')
print('a')
print('l')

# Med for-løkke med omgjøring til liste
print('Med for-løkke med omgjøring til liste'.center(60, '-'))
for bokstav in list('Vertikal'):
    print(bokstav)

# Med for-løkke uten omgjøring til liste
print('Med for-løkke uten omgjøring til liste'.center(60, '-'))
for bokstav in 'Vertikal':
    print(bokstav)

# Med kun én print-setning
print('Med kun én print-setning'.center(60, '-'))
print('V\ne\nr\nt\ni\nk\na\nl')

# Med str.join()
print('Med str.join()'.center(60, '-'))
print('\n'.join(list('Vertikal')))