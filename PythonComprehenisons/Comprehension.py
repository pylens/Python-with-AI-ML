
squares = []
for i in range(1, 6):
    if i %2==0:
        squares.append(i * i)
print(squares)


squares = [i*i for i in range(1,6) if i%2==0]
print(squares)


# Squares of even numbers from 1–10
squares = [x**3 for x in range(1, 11) if x % 2 == 0]
print(squares)  # [4, 16, 36, 64, 100]


# Flatten a nested list
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [num for row in matrix for num in row if num >5]
print(flattened)  # [1, 2, 3, 4, 5, 6]

emp = []
for row in matrix:
    for num in row:
        if num>5:
            emp.append(num)
print(emp)        


# set comprehenssion 
nums = [1, 2, 2, 3, 4, 4, 5 ,5]
unique_squares = {x**2 for x in nums}
print(unique_squares)  # {1, 4, 9, 16, 25}



# dict comprehensions
# Create dictionary of number and its cube
cubes = {x: x**3 for x in range(1, 6)}
print(cubes)  # {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}

empdict = {}
for i in range(1,6):
    empdict[i] = i**3
print(empdict)    


# Invert key-value pairs
original = {'a': 1, 'b': 2, 'c': 3}

inverted = {v: k for k, v in original.items()}
print(inverted)  # {1: 'a', 2: 'b', 3: 'c'}

#nested
# Multiplication table (1 to 3)
table = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(table)  # [[1, 2, 3], [2, 4, 6], [3, 6, 9]]