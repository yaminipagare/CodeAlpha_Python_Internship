import random

words = ["apple", "python", "india", "mobile", "computer"]

word = random.choice(words)
guessed = []

print("Welcome to Hangman Game!")

for chance in range(6):
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print(display)

    if "_" not in display:
        print("Congratulations! You guessed the word.")
        break

    guess = input("Enter a letter: ").lower()

    if guess in word:
        guessed.append(guess)
    else:
        print("Wrong guess!")

else:
    print("Game Over!")
    print("The word was:", word)
