'''. Bouncer Logic (Logical Operators): A club requires guests
to be over 18 AND have a VIP pass, OR they must be over 21. 
Create variables for age and is_vip. Write a
single print statementusing "and" and "or"
to determine if they can enter (True or False).''' 

# age = int(input("Enter the number : "))
age = 22
is_vip = True
check = (age >18 and is_vip) or (age > 21)
print("can enter in club = ",check)
