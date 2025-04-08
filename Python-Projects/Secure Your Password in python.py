
SECURE=(('a','@'),('e','£'),('1','|'),('o','0'),('and','&'))
def Securedpassword(password):
    for a,b in SECURE:
        password=password.replace(a,b)
    return password    

if __name__ =="__main__":
    password=input("Enter your password:\n")
    password=Securedpassword(password)
    print(f"your secure password is {password}") 
