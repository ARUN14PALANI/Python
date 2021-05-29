#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
pass_letters=""
for letter in range(0,nr_letters):
  #random_no = random.randint(0, len(letters))
  #pass_letters += letters[random_no-1]
  pass_letters += random.choice(letters)

pass_symbols=""
for letter in range(0,nr_symbols):
  #random_no = random.randint(0, len(symbols))
  #pass_symbols += symbols[random_no-1]
  pass_symbols += random.choice(symbols)
  
pass_num=""
for letter in range(0,nr_numbers):
  #random_no = random.randint(0, len(numbers))
  #pass_num += numbers[random_no-1]
  pass_num += random.choice(numbers) #without random number

easy_password = pass_letters+pass_symbols+pass_num
print(easy_password)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
list_easy_pwd = list(easy_password)
random.shuffle(list_easy_pwd)
#passs =''.join(list_easy_pwd) **list to string without for loop
password = ""
for values in list_easy_pwd:
  password += values
print(password)