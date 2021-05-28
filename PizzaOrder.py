print("Welcome to AKS Pizza Stall!")
pizza_size = input(str("Please mention your pizza size 'S/M/L': "))
add_peproni = input("Do you need add peproni in your pizza? Mention (y/n): ")
add_cheese = input("Do you need add extra cheese in your pizza? Mention (y/n): ")
bill_value = 0
print(add_peproni.lower())
print(pizza_size.lower())
if (pizza_size.lower() == "s"):
    bill_value = 15 
elif pizza_size.lower() == "m":
        bill_value = 20
elif pizza_size.lower() == "l":
    bill_value = 25
else:
    print("Error Occured : Please mention correctly")

if (add_peproni.lower() == "y") and pizza_size.lower() == "s":
    bill_value += 2
elif (add_peproni.lower() == "y") and (pizza_size.lower() == "m" or pizza_size.lower() == "l"):
    bill_value += 3

if add_cheese == "y" and (pizza_size.lower() == "m" or pizza_size.lower() == "l"  or pizza_size.lower() == "s"):
    bill_value += 1

print(f"You Ordered size :({pizza_size}), Added Peproni ({add_peproni}), Added Extra Cheese ({add_cheese})")
print(f"Your total bill value is Rs.{bill_value}/-")
