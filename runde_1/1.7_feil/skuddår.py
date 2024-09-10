def skuddår(år):
    if år % 4 == 0:
        if år % 100 == 0:
            if år % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

assert skuddår(4) == True
assert skuddår(5) == False
assert skuddår(100) == False
assert skuddår(400) == True