chang=0
while True:
    if chang<0:
        
        qty = int(input("Enter number product : "))
        price = float(input("Price per unit : "))

        total = price*qty
        print("Total money :",total)

        pay = float(input("Enter pay money : "))
        change = pay - total
        print ("Money change :",change)

        print("Breaking")
        break
print("Finished")
