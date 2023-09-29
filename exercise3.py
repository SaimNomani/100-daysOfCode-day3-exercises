# Write a program that works out whether if a given year is a leap year.
# Example Input 1
# 2400
# Example Output 1
# Leap year.
# Example Input 2
# 1989
# Example Output 2
# Not leap year.
year = int(input("Enter year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("leap year")
        else:
            print("Not a leap year")
    else:
        print("leap year")

else:
    print("Not a leap year")
