def aldersgruppe(alder):
    if alder < 17:
        gruppe = 'barn'
    elif alder < 67:
        gruppe = 'voksen'
    else:
        gruppe = 'pensjonist'
    
    return gruppe

# assert - assert må etterfølges av et uttrykk som enten er True eller False. Hvis betingelsen
# er True skjer det ingenting. Er betingelsen derimot False oppstår det en kjøretidsfeil og 
# programmet avsluttes. På den måten kan man teste programmet for logiske feil på en effektiv
# måte. Hvis man debugger programmet starter debuggeren på den linjen med assert som feiler slik
# at det er svært enkelt å se programmets tilstand øyeblikke før det feiler.
# Alle assert-setninger sier noe om hvordan vi på forhånd forventer at programmet skal oppføre seg.

assert aldersgruppe(10) == 'barn'
assert aldersgruppe(15) == 'barn'
# Denne linjen får en AssertionError. Alder på 16 gir altså ikke gruppen 'vosken'
# som forventet
assert aldersgruppe(16) == 'voksen' 
assert aldersgruppe(50) == 'voksen'
assert aldersgruppe(66) == 'voksen'
assert aldersgruppe(67) == 'pensjonist'
assert aldersgruppe(80) == 'pensjonist'