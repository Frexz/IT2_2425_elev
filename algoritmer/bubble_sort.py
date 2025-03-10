def bubble_sort(liste):
    for _ in range(len(liste)):
        for i in range(len(liste) - 1):
            if liste[i] > liste[i + 1]:
                liste[i], liste[i + 1] = liste[i + 1], liste[i]

liste = [6, 3, 0, 1, 5]
bubble_sort(liste)

assert liste == [0, 1, 3, 5, 6]
print(liste)
