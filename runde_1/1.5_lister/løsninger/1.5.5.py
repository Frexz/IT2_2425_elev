tall = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

tall = [tall[i] for i in range(len(tall)) if i % 2 == 0]
print(tall)