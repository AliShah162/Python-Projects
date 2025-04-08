sum=0
print("Welcome to Ali General Store!")
while True:
    Userinput=input("Enter price of the product or press q to quit: ")
    if Userinput.isnumeric():
     sum=sum+int(Userinput)
     print(f"Your Order so far is {sum}")
    elif Userinput=="q":
        print(f"Thank you for shopping here your total bill is: {sum}")
        break
    else:
        print("Error!")