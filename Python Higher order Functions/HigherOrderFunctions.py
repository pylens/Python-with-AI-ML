numbers = [1, 2, 3, 4, 5]

# Loop way
squares = []
for n in numbers:
    squares.append(n**2)
print(squares)    

def getsquares(num):
    return num**2

squares_map = list(map(getsquares, numbers))
print(squares_map)


numbers = [10, 15, 20, 25, 30]

# Loop way
evens = []
for n in numbers:
    if n % 2 == 0:
        evens.append(n)
print(evens)        


evens_filter = list(filter(lambda x: x % 2 == 0, numbers))
print(evens_filter)


from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Loop way
total = 0
for n in numbers:
    total += n
print(total)

total_reduce = reduce(lambda a, b: a * b, numbers)
print(total_reduce)


names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]
ages = [25, 23, 26]

combined = list(zip(names, scores, ages))
print(combined)  # [('Alice', 85), ('Bob', 90), ('Charlie', 95)]

fruits = ["apple", "banana", "cherry"]

for enm, ele in enumerate(fruits, start=3):
    print(enm, ele)


print(list(enumerate(fruits, start=0))) 