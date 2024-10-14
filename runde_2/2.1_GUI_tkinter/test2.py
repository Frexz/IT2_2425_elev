is_playing = True
number_of_guesses = 0
secret_word = "cake"

print("Welcome to the word guessing game!\n")
print("Your hint is: ", end="")
for letter in secret_word:
    print('_', end=' ')
print()

while is_playing:
    guess = input("What is your guess? ")
    number_of_guesses += 1

    while len(guess) != len(secret_word):
        print("\nSorry, the guess must have the same number of letter as the secret word.")
        guess = input("What is your guess? ")
    
    if guess == secret_word:
        is_playing = False
        print("Congratulations! You guess it!")
        print(f"You used {number_of_guesses} amount of guesses")
        continue
    else:
        print("Your hint is: ", end="")
        for i in range(len(secret_word)):
            if guess[i] == secret_word[i]:
                print(guess[i].upper(), end="")
            elif guess[i] in secret_word:
                print(guess[i].lower(), end="")
            else:
                print("_", end="")
        print()