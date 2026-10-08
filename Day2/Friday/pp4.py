'''Minutes to Hours: Ask the user for a large number of minutes 
(for example, 135). Using floor division (//) and modulo (%),figure 
out how many whole hours that is, and how many minutes are left over.
Print it like: "Hours: X, Minutes: Y".'''

min = int(input("Enter large number of mins : "))
temp = min 
leftMin=temp%60
hour = min // 60
print(f"{hour} {leftMin} ")

