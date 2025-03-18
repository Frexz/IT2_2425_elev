import random

antall_terninger = 5
antall_kast = 100

for n in range(antall_kast):
    res = []
    for i in range(antall_terninger):
        res.append(random.randint(1, 6))
    
    res_set = set(res)
    # Yatzy
    if len(res_set) == 1:
        print(f"Yatzy: {res}")
    elif len(res_set) == 2:
        count = res.count(res[0])
        # Fire like
        if count == 1 or count == 4:
            print(f"Fire like: {res}")
        # Hus
        else:
            print(f"Hus: {res}")
    elif len(res_set) == 5:
        # Stor straight
        if res_set.issubset({2, 3, 4, 5, 6}):
            print(f"Stor straight: {res}")
        # Liten straight
        elif res_set.issubset({1, 2, 3, 4, 5}):
            print(f"Liten straight: {res}")