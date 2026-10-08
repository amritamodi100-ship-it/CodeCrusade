unit = int(input("Enter the unit of bill : "))
if unit <= 100 :
    bill = unit * 5
elif unit <= 200 :
    bill = unit * 7
else :
    bill = unit * 10

print("Electricity bill : ",bill)             