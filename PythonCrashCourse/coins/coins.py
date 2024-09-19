# Write a program that asks the user for a (integer) number of cents, from 0 to 99, and outputs how many of each type of coin would represent that amount with the fewest total number of coins. When you run your program, it should match the following format:

# Please enter an amount in cents less than a dollar.
# 87
# Your change will be:
# Q: 3
# D: 1
# N: 0
# P: 2

quarter= 25
dime=10
nickle=5
penny=1

numberOfDimes=0
numberOfNickles=0
numberOfPennies=0
numberOfQuarters=0
amount = float(input( " Please enter an amount in cents, less than a dollar."))
if amount >= quarter:
    numberOfQuarters= amount //quarter;
    amount -= (numberOfQuarters * quarter)
if amount >= dime:
    numberOfDimes = amount // dime
    amount -=(numberOfDimes * dime)
if amount >= nickle:
    numberOfNickles = amount // nickle
    amount -= (numberOfNickles * nickle)
if amount >= penny:
    numberOfPennies = amount // penny
    amount -= (numberOfPennies * penny)

print(f"Quarters: {numberOfQuarters}, Nickles: {numberOfNickles}, Dimes: {numberOfDimes}, Pennies: {numberOfPennies}")

