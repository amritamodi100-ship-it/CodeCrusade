''' The Boolean Illusion: A junior developer wrote the code below to convert 
user input into a Boolean. However, if you run this and type the word "False", 
the terminal prints True! Debug this type casting trap. Write a corrected version 
that actually prints False when the user types the exact word "False". 
(Hint: Do not wrap the input in bool(); compare the raw string instead).'''

# answer = input("Type False: ")
# print(bool(answer))

get = input("Enter the value : ")
get_bool = (get == "True")
print(get_bool)
