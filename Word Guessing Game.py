"""A Simple Program To Guess the Correct Characters"""
import random

# Create a list of German Words
WORDS = ["Hund", "Haus", "Baum", "Milch", "Mond", "Auto", "Ball", "Sonne", "Tisch", "Tasche"]

# Choose a random word from the constant list
secret_word = random.choice(WORDS).strip().lower()
guessed_position = [False] * len(secret_word)
attempt_counter = 0
MAX_ATTEMPT = 2 * len(secret_word)

print(f"Guess the characters of a word with {len(secret_word)} letters!")

# Attempts
while attempt_counter < MAX_ATTEMPT and not all(guessed_position):

    try:
        guess = input(f'Turn {attempt_counter + 1}. Enter a Character: ').strip().lower()

        if len(guess) != 1:
            print("Enter Only One Character")
            continue

    except ValueError:
        print("Invalid Input. You must Enter a Valid Character.")

    else:

        if len(guess) != 1:
            print("Enter only one character!")
            continue

        if guess in secret_word:
            print("Correct!")
            for idx, char in enumerate(secret_word):
                if char == guess:
                    guessed_position[idx] = True

        else:
            print("Nope. Try Again.")

    finally:
        attempt_counter += 1
        display_word = "".join([char if guessed else "_" for char, guessed in zip(secret_word, guessed_position)])
        print(f"Word: {display_word}")


if all(guessed_position):
    print(f"\nYou WON! The word was {secret_word}.")

else:
    print(f"\nBetter Luck Next Time! The correct number was {secret_word}.")

