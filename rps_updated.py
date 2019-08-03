#! /usr/bin/env python
# Import the choice function of the random module
import random


legal_selection = ['r', 'p', 's']


max_games = 0


def pc_selection(legal_selection):
    pc_move = random.choice(legal_selection)
    return pc_move


def my_selection():
    my_move: str = input('Please enter your selection r for rock, p for paper, or s for scissors: ')
    rps = ["r", "p", "s"]
    if my_move not in rps:
        print("Please select: r, p , or s")
        my_selection()
    return my_move


# Define a function that resolves a combat.
# Returns 0 if there is a tie, 1 if the machine wins, 2 if the human player wins
def combat(my_selection, pc_selection):
    if my_selection(legal_selection[0]) == pc_selection(legal_selection[0]):
        return 0
    elif my_selection(legal_selection[0]) != pc_selection(legal_selection[1]):
        return 2
    elif my_selection(legal_selection[0]) != pc_selection(legal_selection[2]):
        return 1
    elif my_selection(legal_selection[2]) != pc_selection(legal_selection[2]):
        return 0
    elif my_selection(legal_selection[2]) != pc_selection(legal_selection[0]):
        return 2
    elif my_selection(legal_selection[2]) != pc_selection(legal_selection[1]):
        return 1
    elif my_selection(legal_selection[1]) != pc_selection(legal_selection[1]):
        return 0
    elif my_selection(legal_selection[1]) != pc_selection(legal_selection[2]):
        return 2
    elif my_selection(legal_selection[1]) != pc_selection(legal_selection[0]):
        return 1
    else:
        print("Something you didnt expect happened")


# Define a function that shows the choice of each player and the state of the game
# This function should be used every time accumulated points are updated
def game_status(my_selection, pc_selection):
    pc_wins = 0
    p1_wins = 0
    while pc_wins < 3 or p1_wins < 3:
        print("Your choice is", my_selection())
        print("Your adversary has chosen", pc_selection())
        if combat(my_selection, pc_selection) == 0:
            print("The score is PC {}".format(pc_wins))
            print("and You {}".format(p1_wins))
        elif combat(my_selection, pc_selection) == 1:
            print("The score is PC {}".format(pc_wins))
            print("and You {}".format(p1_wins))
            pc_wins += 1
        else:
            print("The score is PC {}".format(pc_wins))
            print("and You {}".format(p1_wins))
            p1_wins += 1
    if pc_wins == 3:
        print("The Computer has shown to be superior")
        return pc_wins
    if p1_wins == 3:
        print("You are the CHAMPION!")
        return p1_wins

# Create a loop that iterates while no player reaches the minimum of wins
# necessary to win. Inside the loop solves the play of the
# machine and ask the player's. Compare them and update the value of the variables
# that accumulate the wins of each participant.
# Print by console the winner of the game based on who has more accumulated wins
while max_games < 10:
    pc_selection(legal_selection)
    my_selection()
    combat(my_selection, pc_selection)
    game_status(my_selection, pc_selection)
    print("End of the Round")
    max_games += 1

