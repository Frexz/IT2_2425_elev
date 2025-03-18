"""
selection-sort: for hver indeks i listen sjekker vi alle tallene etter indeksen
om det er det minste tallet. Deretter bytter man plass slik at det minste tallet 
kommer først. Består av to for-løkker uten mulighet til å bryte ut tidlig. Hvilket
betyr at til og med en sortert liste må gås gjennom.

insertion-sort: ett og ett element velges og puttes på riktig plass ved å jobbe seg 
bakover fra plassene elementen fantes. Består også av to løkker, men hvis listen allerede
er sortert vil den indre løkken aldri kjøre i insertion-sort. 
"""

def insertion_sort(liste, n):
    for i in range(1, n):
        element = liste[i]
        j = i - 1
        while j >= 0 and liste[j] > element:
            liste[j + 1] = liste[j]
            j -= 1
        liste[j + 1] = element

liste = [64, 25, 12, 22, 11]
insertion_sort(liste, len(liste))
assert liste == [11, 12, 22, 25, 64]