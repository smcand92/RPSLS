import random

# helper functions

# convert name to number
def name_to_number(name):

    if name == 'rock':
        return 0
    elif name == "spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print("Error Name")

# convert number to name
def number_to_name(number):

    if number == 0:
        return "rock"
    elif number == 1:
        return "spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print("Error Number")


def rpsls(player_pick):

    # print a blank line to separate each game
    print("\n")

    # print message for the player pick
    print("Player chose " + player_pick)

    # convert player pick to number using name_to_number
    player_number = name_to_number(player_pick)

    # computer selects random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)

    # compute random guess for comp_number using number_to_name
    comp_pick = number_to_name(comp_number)

    # print out message to show computer choice
    print("Computer chose " + comp_pick)

    # calculate difference between comp and player number
    difference = (comp_number - player_number) % 5

    # if/else statement to determine winner
    if difference == 1 or difference == 2:
        print("Computer wins!")
    elif difference == 4 or difference == 3:
        print("Player wins!")
    elif difference == 0:
        print("It's a tie!")


# tests
rpsls("rock")
rpsls("paper")
rpsls("scissors")
rpsls("lizard")
rpsls("spock")

