"""A Simple Program Simulate 21 Number Game"""
import random
import sys

# Get Players Details
def get_players():
    players = []

    while True:
        try:
            num_players = int(input("\nHow Many Players? "))

            if num_players == 1:
                first_player = input("Player 1 's Name is : ")
                players.append(first_player)
                players.append("Computer")

            elif num_players > 1 :
                for i in range(num_players):
                    player = input(f"Player {i+1} 's Name is : ").strip().capitalize()
                    players.append(player)

            else:
                print("This Game Needs At Least 1 Player.")
                continue

        except ValueError:
            print("Invalid Input. Enter a Number.")
            continue

        else:
            break

    return players


# Game Starts
def start_play(players):
    current_number = 0
    turn = 0

    print(f'_____Game Starts_____')

    while current_number < 21:
        # To loop over players list
        player = players[turn % len(players)]

        print(f"Current Number is {current_number}, {player}'s turn.")

        if player == "Computer":
            moves = random.randint(1,3)
            print(f"Computer chooses: {moves}.")

        else:
            try:
                moves = int(input("Choose a number [1,2,3]: "))

                if moves not in [1,2,3]:
                    print("Invalid Move!. You must choose 1, 2 or 3")
                    continue

            except ValueError:
                print("Invalid Input. Enter a Number. ")
                continue

        current_number += moves

        if current_number >= 21:
            print(f"{player} reached 21, {player} loses.")
            break

        turn += 1


def main():
    print("Welcome in 21 Number Game!")
    print("\nRules:\nPlayers take turns adding 1, 2, or 3 to a total starting at 0."
          "\nThe player who reaches or exceeds 21 loses.")

    while True:
        players = get_players()
        start_play(players)

        again = input("Do you want to play again? ( y / n ): ").strip().lower()

        if again != "y":
            print("Thanks For Playing. Good Bye!")
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Game Interrupted. Good Bye")
        sys.exit(0)