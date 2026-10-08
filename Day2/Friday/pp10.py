age = int(input("Enter your age : "))
memb_card = input("do you have mambershop card True or False  : ")
has_card = (memb_card == "True")

get_discount =(age < 18 or age > 65) and has_card

print("Eligible for discount : ",get_discount)