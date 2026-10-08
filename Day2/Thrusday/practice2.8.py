'''The Digit Extractor: Create a variable with the integer 85.
Using ONLY floor division (//) and modulo (%),figure out a way 
to extract the "8" and save it in a tens_digit variable, and extract the
"5" and save it in a units_digit variable. Print both variables.'''

a = 85 
b = 10
tens_digit = (a // b)
units_digit = (a % b)
print("The number : ", a)
print("The value extract in the tens digit is : ",tens_digit)
print("The value extract in the units digit is : ",units_digit)