"""A Simple Program for Guessing The correct Number"""
import random

# Prompt the user to Enter the Lower and Upper bounds
try:
    low = int(input("Please Enter the Lower Bound: "))
    upper = int(input("Please Enter the High Bound: "))

    if low >= upper:
        print("Invalid Input!, Lower Bound must be less than High Bound.")

except ValueError:
    print("Invalid input: Please enter valid integers.")

# Generate the random number within the given range
else:
    num_to_guess = random.randint(low, upper)

    # Allow the user up to 5 attempts to guess
    u_try = 1
    while u_try <= 5:

        try :
            Guess = int(input(f"Guess {u_try}: "))
            if Guess < low or Guess > upper:
                print(f"Out of Range! Please enter a number between {low} and {upper}.")

        except ValueError:
                print("Invalid input: Please enter valid integers.")

        else:
            if Guess == num_to_guess:
                print("Correct! You guessed it!")
                break

            elif Guess > num_to_guess:
                print("Too High!")

            else:
                print("Too Low!")

        finally:
            u_try += 1
            if u_try > 5:
                print(f"Better Luck Next Time! The correct number was {num_to_guess}.")

print("Play With Me Again.")

