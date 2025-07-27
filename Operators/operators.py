## comparission operators
# it is used to compare the two oparends using an operator

a = 10
b = 200

# print(a==b) # it will return the False
# print(a!=b) # it returns True
# print(a>=b) 
# print(a<=b) 
print("****************String comparission***********")
## String comparsion
# Note python is type senstive 
name1 = "Hemanth is an ml engineer"
name2 = name1
# value= 123

# print(id(name1))
# name2 = "hemanth"
# print(id(name2)) # it will return the different id
# print(name1==name2)

# print(10 <= a < 100 > b)

# print(f" {' ' in name1}")
# print(f" {'z' in name1}")
# # print(f" { 123 in value}")

# print(f" {'z' not in name1}")

x = 10
y = x
z = y
print(f"id of x is: {id(x)}\nid of y is: {id(y)}")
print(x is y)
print( x is z)



# a = [1, 2, 3]
# b = a
# c = [1, 2, 3]

# print(a is b)   # True: b refers to the same object as a
# print(a is c)   # False: a and c have the same content, but different objects

# print(name1 is name2)