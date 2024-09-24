numerator = 10**3
denominator = int(input("Enter a number for denominator"))

try:
    result = float(numerator/denominator)
    print(result)
except ZeroDivisionError:
    print("Denominator cannot be Zero")