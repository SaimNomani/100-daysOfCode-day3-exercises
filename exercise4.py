# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.
#
# Based on a user's order, work out their final bill.
#
# Small Pizza: $15
#
# Medium Pizza: $20
#
# Large Pizza: $25
#
# Pepperoni for Small Pizza: +$2
#
# Pepperoni for Medium or Large Pizza: +$3
#
# Extra cheese for any size pizza: + $1
#
# Example Input
# size = "L"
# add_pepperoni = "Y"
# extra_cheese = "N"
# Example Output
# Your final bill is: $28.
print("Welcome to Python Pizza Deliveries!\n")
print("Small Pizza(s): $15\n")
print("Medium Pizza(m): $20\n")
print("Large Pizza(l): $25\n")
size = input("what size pizza do you want? ")
print("pepperoni for small pizza: +$2")
print("pepperoni for medium and large pizza: +$3")
addPepperoni = input("Do you want pepperoni?\nEnter 'y': yes\nEnter 'n': no\n")
print("extra cheese for any pizza: +$1")
addExtraCheese = input("Do you want extra cheese?\nEnter 'y': yes\nEnter 'n': no\n")
bill = 0
if size == 's' or size == 'S':
    bill += 15
    if addPepperoni == 'y' or addPepperoni == 'Y':
        bill += 2
    else:
        print("wrong key\n")
    if addExtraCheese == 'y' or addExtraCheese == 'Y':
        bill += 1
    else:
        print("wrong key\n")
elif size == 'm' or size == 'M':
    bill += 20
    if addPepperoni == 'y' or addPepperoni == 'Y':
        bill += 3
    else:
        print("wrong key\n")
    if addExtraCheese == 'y' or addExtraCheese == 'Y':
        bill += 1
    else:
        print("wrong key\n")
elif size == 'l' or size == 'L':
    bill += 25
    if addPepperoni == 'y' or addPepperoni == 'Y':
        bill += 3
    else:
        print("wrong key\n")
    if addExtraCheese == 'y' or addExtraCheese == 'Y':
        bill += 1
    else:
        print("wrong key\n")
print(f"final bill: ${bill}")
