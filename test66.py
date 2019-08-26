
import random

options2 = ['r', 'p', 's']
max_games = 3
games_played = 0
player_score = 0
my_choice = ""

def pc():
  return random.choice(options2)

def myoption():
  rps = str(input("rock, paper or scissors?")).lower()
  if rps in options2:
    return rps
  else:
    print("invalid, try again")
    myoption()

# Define a function that resolves a combat.
# Returns 0 if there is a tie, 1 if the machine wins, 2 if the human player wins
def combat(): # the core of the game
  global my_choice
  my_choice = myoption()
  if my_choice == pc():
    print("0, it is a tie")
  elif my_choice == 'p' and pc() == 'r':
    print("2, you win")
  elif my_choice == 'p' and pc() == 's':
    print("1, you lose")
  elif my_choice == 'r' and pc() == 'p':
    print("2, you win")
  elif my_choice == 'r' and pc() == 's':
    print("1, you lose")
  elif my_choice == 's' and pc() == 'p':
    print("2, you win")
  elif my_choice == 's' and pc() == 'r':
    print("1, you lose")
# Define a function that shows the choice of each player and the state of the game
# This function should be used every time accumulated points are updated
# Create a loop that iterates while no player reaches the minimum of wins
# necessary to win. Inside the loop solves the play of the
# machine and ask the player's. Compare them and update the value of the variables
# that accumulate the wins of each participant.
# Print by console the winner of the game based on who has more accumulated wins

def updateScore(): # keep track of W and L
  global player_score # Access the global variable "player_score"
  player_score += 1 # ...and add 1 to its current value

while games_played < max_games:
  games_played += 1 # Add 1 to current value of games_played
  if combat() == True: # Play a game. If player wins...
    updateScore() # ...add 1 to player_score
  print("You've won", str(player_score), "out of", str(games_played) + ".")

print("Game over.")
