#calculator
import art

print(art.logo)

#Add
def add(n1,n2):
  return n1+n2
#subtract
def subtract(n1,n2):
  return n1-n2
#Multiply
def multiply(n1,n2):
  return n1*n2
#Division
def divide(n1,n2):
  return n1/n2

operation = {"-":subtract,"+":add,"*":multiply,"/":divide}

num1 = int(input("Enter the first number: "))
for symbol in operation:
  print(symbol)
recalc = "y"
while recalc == "y":
  symbol = input("Enter the operator symbol: ")
  cal_fun= operation[symbol]
  num2 = int(input("Enter the second number: "))
  result = cal_fun(num1,num2)
  print(f"{num1} {symbol} {num2} = {result}")
  num1 = result
  recalc = input("Enter the if continue calculation y/n : ")


