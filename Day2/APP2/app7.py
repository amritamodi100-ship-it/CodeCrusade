s_maths = float(input("Enter the marks of Maths : "))
s_eng = float(input("Enter the marks of English : "))
s_che = float(input("Enter the marks of Chemistry : "))
s_pps = float(input("Enter the marks of pps : "))
s_cons = float(input("Enter the mark of constitution : "))

TotalMarks = s_maths + s_eng + s_che + s_pps + s_cons
avg = TotalMarks / 5
percent = ((TotalMarks / 120)*100)

print("Total Marks of all the subjects are : ",TotalMarks)
print("Average Marks of all the subject is : ",avg)
print("Your percentage is : ",percent)
print((percent )>= 75)