m1 = int(input("Enter the marks of math : "))
m2 = int(input("Enter the marks of english : "))
m3 = int(input("Enter the marks of pps : "))
sum = (m1 + m2 + m3)
percentage = (( sum / 72 ) * 100)
print(percentage)

if m1 >= 20 and m2 >= 20 and m3 >= 20 :
    if percentage >= 90 :
        print("GRADE : A")
    elif percentage >= 70 :
        print("GRADE : B")
    elif percentage >= 50 :
        print("GRADE : C")        
    else :
       print("GRADE : E")
else :        
     print("Fail")