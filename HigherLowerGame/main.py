import game_data
import art
import random

print(art.logo)




def check_greater(input_value,value_a,value_b):
  a = int(value_a)
  b = int(value_b)
  if a > b and input_value == "a":
    print("correct")
    return True
  elif b > a and input_value == "b":
    print("correct")
    return True
  else: 
    print("worng")
    return False


in_game = True
user_score = 0
while in_game == True: 
  value_a = random.choice(game_data.data)
  value_b = random.choice(game_data.data)
  if value_b == value_a:
    value_b = random.choice(game_data.data)
  print(f'(a) Name :{value_a["name"]},description : {value_a["description"]}, country :{value_a["country"]}' )
  print(art.vs)
  print(f'(b) Name :{value_b["name"]},description : {value_b["description"]}, country :{value_b["country"]}' ) 
  val = input("enter a is greater or b is greater: ")
  first_val = int(value_a["follower_count"])
  second_val = int(value_b["follower_count"])
  in_game = check_greater(val,first_val,second_val)
  if in_game == False:
    print("Game over")
  else:
    user_score += 1
    print(user_score)
    in_game == True


print(f"Total score :{user_score}")