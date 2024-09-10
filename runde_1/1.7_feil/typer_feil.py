print('Hallo!')      # Syntaksfeil: mangler sluttparentes
      
total = str(3) + 'feil'  # Semantisk feil: meningsløst å addere et tall med en tekst.

alder = 4
if alder >= 18:
    print('Umyndig')
else:
    print('Myndig') # Logisk feil: fireåringer er ikke myndige