def linear_search(liste, tall):
    count = 0
    for element in liste:
        if element == tall:
            return count
        count += 1
    return count
    
liste = [x for x in range(1, 1000001)]


print(linear_search(liste, 2000000))