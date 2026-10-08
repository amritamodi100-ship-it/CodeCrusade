member = int(input("Enter the no of member : "))

for i in range(1 ,member+1):
    print("--- customer", i ,"---")
    print("1. Standard Room = RS.1500/day ")
    print("2. Deluxe Room = RS.3000/day ")
    print("3. Luxury Room = RS.5000/day")

    room = int(input("\n Choose room : "))
    days = int(input("Enter no of days : "))

    if room == 1:
        rate = 1500
    elif room == 2:
         rate =3000
    elif room == 3:
        rate = 5000
    else :
        print("Invalid room choice : ")
        continue

    room_charge = rate * days 

    if days > 5:
        discount = room_charge * 0.20
    elif days >= 3 :
        discount = room_charge * 0.10
    else :
        discount = 0

    food_charge = 0
    food = input("Did customer ordered food ! (yes / no ):")
    if food == "yes":

        items = int(input("Enter no of food item : "))
        for i in range(items):
            price = float(input("Enter food item price : "))
            food_charge += price

    subtotal = room_charge + food_charge
    after_discount = subtotal - discount

    gst = after_discount*0.18
    final_bill = after_discount + gst  



    print("\n----HOTEL BILL-----") 
    print("ROOM CHARGES = ",room_charge )
    print("FOOD CHARGES = ",food_charge )
    print("DISCOUNT = ",discount )
    print("GST = ", gst)
    print("Final Bill = ", final_bill )