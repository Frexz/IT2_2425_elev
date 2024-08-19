class Person:                           # Opprett en klasse
    fornavn = 'N'                       # Attributt/egenskap
    etternavn = 'N'

person = Person()                       # Opprett et objekt
person.etternavn = 'Nilsen'             # Punktnotasjon
print(person.fornavn, person.etternavn) # N Nilsen