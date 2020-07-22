cash = int(input("Enter number money withdraw : "))

a = float(cash//1000)
cash = float(cash - 1000*a)

b = float(cash//500)
cash = float(cash - 500*b)

c = float(cash//100)
cash = float(cash - 100*c)

print("Cash B1000 :",a)
print("Cash B500 :",b)
print("Cash B100 :",c)
