with open('navn.txt', encoding='utf-8') as fil:
    linje = fil.readline()
    print(linje.strip().split(' '))
        