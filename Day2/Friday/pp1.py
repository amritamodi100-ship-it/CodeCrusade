bill= input("Enter the the total bill : ")
people = input("Number of person splitting the bill : ")

Total_bill = int(bill)
cost_per_person = int(people)

cal = Total_bill / cost_per_person
print("Each person has to give : ",cal)

