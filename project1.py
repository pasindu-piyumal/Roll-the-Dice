import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    player = input("Enter the number of plyer(2-4) : ")
    if player.isdigit():
        player = int(player)
        if 2<=player<=4:
            break
        else:
            print("Must be 2-4 players")
    else:
        print("Invalid, try again")


max_score = 50
player_score = [0 for _ in range(player)]

while max(player_score) < max_score:

    for  i in range(player):
        print("\nPlayer number", i+1, "turn has just started!\n")
        print("Your total score is:", player_score[i], "\n")

        current_score = 0

        while True:

            should_roll  = input("Would you like to roll (y) ? ")
            if should_roll.lower() == "y":
                value = roll()
                if value == 1:
                    print("You rolled a 1! Turn done!")
                    current_score = 0
                    break
                else:
                    current_score += value
                    print("You rolled a: ", value)

                print("Your score is: ", current_score)

            else:
                break

        player_score[i] += current_score
        print("Your current score is: ", player_score[i])

    max_score =max(player_score)
    winning_idx = player_score.index(max_score)
    print("Player number ", winning_idx + 1, " is the winner with  score of: ",max_score)

