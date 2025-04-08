with open('currencyData.txt') as f:
    lines=f.readlines()
# print((lines))
currencydict={}
for line in lines:
    parsed = line.split("\t")
    currencydict[parsed[0]] = parsed[2]
    print(parsed)
print("Starts from here: ")
# print(currencydict)
amount = float(input("Enter Amount:\n"))
print("In which currency do you want to change?: \n", currencydict.keys())
[print(item)for item in currencydict.keys()]

currency=input("Enter one of these currency names: ")
print(f"Rs.{amount} = {amount*float(currencydict[currency])} {currency}")