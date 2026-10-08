'''The ATM Dispenser: A user wants to withdraw some money
(ask them for an amount, like 80). The ATM only has $50 bills and
$10 bills. Using floor division and modulo, figure out 
how many $50 bills to give them, and then how many $10 bills
to give them from what is leftover. Print the counts of both bills.'''

money = int(input("Enter the money to withdraw : "))

print("ATM only has $50 and $80 bill ")

fifty_bill = money // 50 
left_over = money % 50
ten_bill = left_over // 50

print(fifty_bill)
print(ten_bill)



