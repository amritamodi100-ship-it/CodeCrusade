w = input("Enter your weight in kg : ")
h = input("Enter your height in meter : ")

weight = int(w)
height = int(h)

BodyMassIndex = (weight / ((height) ** 2))

print(BodyMassIndex)