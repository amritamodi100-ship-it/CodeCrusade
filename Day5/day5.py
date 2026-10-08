#  i = itrate 

# for i in range(0,5,2) :
#     print(i)

# a = int(input("Enter the number : "))
# for i in range(0,a+1) :
#     print(i)
#     if i % 2 == 2

# count = int(input("Enter the natural number : "))
# sum = 0
# for i in range(-8,count,-1):#(-10,count,)
#     if count > 0 :
#         sum += i
#         print(sum)
#     else :
#         print("Not a natural number : ")    

  

# count = int(input("Enter the natural number : "))
# sum = 0
# for i in range(0,count):
#       sum += i
# print(sum)


# for i in range(1,4):
#     for j in range(1,4):
#         print(j)
#     print(i)    

'''
1
2
3
# 1
1
2
3
# 2
1
2
3
# 3
'''

# the below ranges is of left alliged triangle

# in star
n = 5   
for i in range(1,n+1): #(n,0,-1):
    for j in range(i):
        print("*", end = " ")
    print()   



# column wise row
n = 5   
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end = " ")
    print()  


# in cont. num
n = 5   
a = 1
for i in range(1,n+1):
    for j in range(i):
        print(a, end = " ")
        a +=1
    print()      


# row wise column
n = 5   
a = 1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i, end = " ")
        a +=1
    print()  



