def selection_sort(liste, n):
    for i in range(0, n - 1):
        min = i
        for j in range(i + 1, n):
            if liste[j] < liste[min]:
                min = j
    
        if min != i:
            liste[i], liste[min] = liste[min], liste[i]

liste = [64, 25, 12, 22, 11]
selection_sort(liste, len(liste))
assert liste == [11, 12, 22, 25, 64], f"Fikk {liste}"