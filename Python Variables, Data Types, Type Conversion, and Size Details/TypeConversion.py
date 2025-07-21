# please go through the .md file in the repo for more informtion.

# this is sample code for the above problem

name = "hemanth" # string
age = 26 # integer
height = 5.9 # float
IsMarried = False # 0 True = 1 or any non zero value

print("age is :", age, "and the type of age is:", type(age))
print("height is :", height, "and the type of height is:", type(height))
print("name is :", name, "and the type of name is:", type(name))
print("IsMarried is :", IsMarried, "and the type of IsMarried is:", type(IsMarried))
print("******************************************")
# 1. we can convert int into string or float
converteAgeToString = float(age)
print("Converted age is :", converteAgeToString, "and the type of Converted age is:", type(converteAgeToString))

#2. we can convert float into string and integer
convertedHeight = str(height)
print("Converted height is :", convertedHeight, "and the type of Converted height is:", type(convertedHeight))

#3. we cannot convert non numeric strings into a integrrs or float or Bool (hemanth, 876q78)
# convertedName = int(name)
# print(" Converted name is :", convertedName, "and the type of Converted name is:", type(convertedName))
# print("Converted IsMarried is :", IsMarried, "and the type of Converted IsMarried is:", type(IsMarried))

convertedIsMarried = int(IsMarried)
print("converted IsMarried is :", convertedIsMarried, "and the type of converted IsMarried is:", type(convertedIsMarried))

num = 826734
print(type(str(num)))