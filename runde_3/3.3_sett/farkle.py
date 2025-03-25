from random import randint
from collections import Counter

teller = 0

def roll():
    return [randint(1, 6) for _ in range(6)]

def get_score(result):
    global teller
    score = 0
    counter = Counter(result)

    if 6 in counter.values():
        # 6 like
        score += 3000
        teller += 1
    elif all(x == 3 for x in counter.values()):
        # 2 x 3 like
        score += 2500
    elif all(x == 2 for x in counter.values()):
        # 3 par
        score += 1500
    elif all(x == 1 for x in counter.values()):
        # Straight
        score += 1500
    else:
        # 5 like
        if 5 in counter.values():
            score += 2000
            for key, value in counter.items():
                if value == 5:
                    counter.pop(key)
                    break
        
        # 4 like
        if 4 in counter.values():
            score += 1000
            for key, value in counter.items():
                if value == 4:
                    counter.pop(key)
                    break
        
        # 3 like
        if 3 in counter.values():
            for key, value in counter.items():
                if value == 3:
                    score += 1000 if key == 1 else 100*key
                    counter.pop(key)
                    break
        
        # Enere og femmere
        for key, value in counter.items():
            if key == 1:
                score += 100 * value
            elif key == 5:
                score += 50 * value

    
    return score

for _ in range(10000):
    res = roll()
    get_score(res)
print(f"Fikk 6 like {teller} ganger")

