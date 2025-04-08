# import math
# from math import factorial

def factorial(number):
    if number == 1 or number == 0:
        return 1
    else:
        return number * factorial(number-1)

if __name__ == ' __main__ ':

    number = int(input("Enter the number you want factorial of: "))
    fac = factorial(number)
    print(f"Factorial is {fac}" )