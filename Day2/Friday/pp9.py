'''Number Reversal: Ask the user to enter a 2-digit integer (like 45).
Using floor division and modulo, extract the tens digit (4) and the
units digit (5). Now, using math, flip them around to create the
number 54 and print it! 
(Hint: Multiply the units digit by 10 and add the tens digit).'''

n = int(input("Enter two digit no : "))

tens_digit = n // 10
units_digit = n % 10

print(tens_digit)
print(units_digit)

new = units_digit * 10 + tens_digit
print(new)