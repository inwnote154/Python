def Check_Rate(sales):
    Rates=[0.30,0.25,0.20,0.15,0.10,0.05,0.0]
    TotalSales=[1000000.0,750000.0,500000.0,250000,100000.0,1.0,0]
    for n in range(len(TotalSales)):
        if sales>TotalSales[n]:
            return(Rates[n])

Sales=[]
count=1
Done=True
while Done:
    sale=float(input(f"Enter sale {count} (-1 to exit) : "))
    if sale>-1.0:
        Sales+=(sale,)
        count+=1
    elif sale==-1:
        break

Totals=sum(Sales)
print(f"Total sales : {Totals}")
Rate=Check_Rate(Totals)
print(f"Commission Rate : {Rate*100}%")
Commision=Totals*Rate
print(f"Total Commision : {Commision}")
