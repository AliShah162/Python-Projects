def runrate(target,overs):
    rr=target/overs
    print(rr)
    print(f"The team can easily win at the runrate of  {rr}")
    
print("The RunRate Calculator :")
a=int(input("Enter target to chase: "))
b=int(input("Enter total number of overs: "))
runrate(a,b)