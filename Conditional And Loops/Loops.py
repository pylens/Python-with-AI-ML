fruits = ["apple", "banana", "cherry"]


print(f"After looping...")

for fruit in fruits: # 1st, 2nd, 3rd,.... end of the element(unless u mentioned a stop case or condtion)
    if fruit == "bana":
        break
    else: 
        print(fruit)
       




# indexing
fruits = ["apple", "banana", "cherry", "raspberry", "mango", "strawberry"]

# listLen = len(fruits)

# print(f"lenght of the list is {listLen}")
# print(f"first is {fruits[0]}")
print("********************************")
for i in range(0,len(fruits)):
    if fruits[i] == 'mango' or fruits[i] == 'raspberry':
        continue # it will skip the current loop
    else:
        print(fruits[i])


## pass
print("pass ")

# fututre purpose
for i in range(10):
    pass # it will do nothing, just a placeholder


# nested loops

colors = ["red", "green"]
fruits = ["apple", "banana"]

for color in colors: # 1 --> red 2 --> green
    for fruit in fruits: 
        print(color, fruit) # 1 --> color = red, fruit = apple 2--> color = red, fruit = banana 
       
                            # 1 --> color = green, fruit = apple 2--> color = green, fruit = banana


## examples
print("printing a simple mul table")  


number = int(input("what is the number you want to see the table of: "))
tablerange = int(input("what is the range of the table you want to print upto: "))
for i in range(1, tablerange):
    print(f"{number} * {i} = {number * i}")


# gussing even odd

print("gussing even or odd")

number = int(input("enter a number: "))
if number % 2 == 0:
    print("even")
else:
    print("odd")