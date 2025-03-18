"""
Oppgave 1
a) 1.
b) 4.

Oppgave 2
a)

FUNCTION max(liste)
    SET max TO liste[0]
    FOR hvert element i liste
        IF element GREATER THAN max
            SET max TO element
        ENDIF
    ENDFOR
    RETURN max
ENDFUNCTION
"""

def max(liste):
    max = liste[0]
    for element in liste:
        if element > max:
            max = element
    return max

liste = [3, 1, 7, 9, 2]
assert max(liste) == 9