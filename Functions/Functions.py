# def greet():
#     print("Hello, welcome to Python!")
#     # greet()
# greet()

# Functions with parameters(positional)
def greet_user(name, age):
    print(f"Hello, {name}! your age is {age}")


# greet_user(input("Enter your name: "), input("Enter your age: "))

# adding two values

# Default parameters
def sum(a=10, b=20):
    print(a+b)

# sum(100, 100)

# NAmed arguments(keyword arguments)
def book_ticket(name, seat):
    print(f"Booking confirmed for {name} in seat {seat}")

# book_ticket(seat=12, name="John")


# arbitary arguments

def show_numbers(*args):
    print(*args)
    for num in args:
        print(num)

# show_numbers(1, 2, 3, 4, 5)


def sum(*nums):
    res = 0
    for num in nums:
        res = res + num
    return res

# print(sum(100, 100, 500))

# def show_info(**kwargs):

#     for key, value in kwargs.items():
#         # print(key, ":", value)
#         return key, value

lis1 = []
def takeInputs():
    for i in range(5):
        value = int(input("Enter a VAlue: "))
        lis1.append(value)

    return sum(*lis1)    

# print(takeInputs())

# print(show_info(name="Alice", age=25, city="New York"))


def outer():
    def inner():
        print("This is inner function")
    inner()

outer()