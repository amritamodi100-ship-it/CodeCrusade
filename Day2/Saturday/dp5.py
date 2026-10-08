bill_amt = float(input("Enter the amount of the bill : "))
AddTip = float(input("Give the tip : "))

tip_percent = ( AddTip / 100 )* bill_amt
bill_amt += tip_percent

print("The total amount of the bill : ",bill_amt) 