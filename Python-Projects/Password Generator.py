import string
import random
if __name__=="__main__":
    s1=string.ascii_lowercase
    print(s1)
    s2=string.ascii_uppercase
    print(s2)
    s3=string.digits
    print(s3)
    s4=string.punctuation
    print(s4)
    plen=int(input("Enter the length of password you want: \n"))
    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    # s.extend(list(s3))   
    print("Your Password is: ")
    random.shuffle(s)
    print("".join(s[0:plen]))
    