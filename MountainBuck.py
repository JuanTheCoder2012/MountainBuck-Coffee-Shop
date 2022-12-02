# this is a Python project that i want to make for my portfolio, this is a project about coffee ordering. The way its going to work is the customer 
# is going to input what kind of coffee they want.

print("Hello, Welcome to MountainBuck coffee shop!!")

name = input("What is your name?\n")
print("Hello " + name + ", Thank you for coming in today!\n\n\n")

menu = "Black Coffee, Expresso, Latte, Cappucino"

snacks = "Croissants, Chips, Danish, Tarts, Cannoli"

print(name + ", what would you like from our menu today? Here is what we are serving.\n" + menu)

order = input()

price = 9

quantity = input("\nHow many coffees would you like?\n")

total = price * int(quantity)

print("Thank you. Your total is: $" + str(total))


print("\nNo problem " + name + ", we'll have your " + order + " ready for you in a couple of minutes.\n\n\n")


print("Did you also want to buy some snacks or pastries?\n" + snacks)

order2 = input()

price = 10

quantity = input("\nHow many snacks would you like?\n")

total2 = price * int(quantity)

print("\nOk, your total is: $" + str(total2))

grand_total = total + total2 

print("\nSo, your grand total is going to be: $" + str(grand_total))


print("\n\nNo worries " + name + ", your " + order + " and " + order2 + " will be ready soon.")

print("\n\nYour order is ready " + name + " Thank you for coming in please come back soon!")





