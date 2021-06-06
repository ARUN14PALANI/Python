#Number Guessing Game Objectives:
import art
import random


# Include an ASCII art logo.
print(art.logo)
random_value = int((random.choice(list(range(1,101)))))
print(random_value)

def check_greater(bot_value,player_value):
  if player_value == bot_value:
    return "Congrats, your guess is correct!"
  elif player_value > bot_value:
    return "Your prediction is higher than the actual value"
  elif player_value < bot_value:
    return "Your prediction is lower than the actual value"


def game_predict(tries):
  user_value = int(input("Guess the number between 1 and 100 :"))
  for i in range (0,tries):
    print(check_greater(random_value,user_value))
    if check_greater(random_value,user_value) == "Congrats, your guess is correct!":
      print("won")
      break
    else:
        tries -= 1
        print(f"left chances: {tries}")
        user_value = int(input("Guess again :"))
    
  if tries == 0:
    print("You lost the game")





# Allow the player to submit a guess for a number between 1 and 100.
game_level = input("Enter the difficulty level, hard or easy:")


if game_level == "hard":
  chances = 5
  game_predict(chances)
elif game_level == "easy":
  chances = 10
  game_predict(chances)

# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

