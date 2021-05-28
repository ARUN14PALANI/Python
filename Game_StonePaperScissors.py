rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
action_image = [rock,paper,scissors]
action_list = ["rock","paper","scissors"]
player_option = input("enter your opyion 1 as 'rock', 2 as 'paper' or 3 as 'scissors' :")

player_option = int(player_option)-1
random_num = random.randint(0,2)

print(f"your action: {action_image[player_option]}")
print(f"Bot action: {action_image[random_num]}")

if action_list[player_option] == "rock" and action_list[random_num] == "scissors":
    print("you won the match!")
elif action_list[player_option] == "scissors" and action_list[random_num] == "paper":
    print("you won the match!")
elif action_list[player_option] == "paper" and action_list[random_num] == "rock":
    print("you won the match!")
elif (action_list[player_option] == "paper" and action_list[random_num] == "paper") or (action_list[player_option] == "rock" and action_list[random_num] == "rock") or (action_list[player_option] == "scissors" and action_list[random_num] == "scissors") :
    print("Match is Draw!")  
else:
    print("You lose the match!")