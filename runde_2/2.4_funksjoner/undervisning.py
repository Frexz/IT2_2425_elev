def get_initials(name):
    return name[0]

first_name = input("What is your name? ")
initials = get_initials(first_name)

print(f"Your name is {first_name} and your initials are {initials}.")