


#  Python Functions — Complete Notes

## 1. What is a Function?
A **function** is a reusable block of code that performs a specific task.  
Instead of writing the same code again and again, you can **define it once and call it many times**.

**Real-world analogy:**  
- Think of a **coffee machine**: you press a button, it performs a set of steps internally, and gives you coffee.  
- You don’t care about how it works inside (implementation), you just use it by **calling** it.

---

## 2. Defining a Function
In Python, we use the `def` keyword.

**Syntax:**
```python
def function_name(parameters):
    # code block
    return value
````

---

## 3. Types of Functions in Python

### 3.1 Built-in Functions

Python already provides many ready-to-use functions.

**Examples:**

```python
print(len("hello"))   # length of string
print(max([1, 2, 3])) # maximum value
print(type(5))        # type of object
```

---

### 3.2 User-defined Functions

You can create your own functions.

**Example:**

```python
def greet():
    print("Hello, welcome to Python!")

greet()  # calling the function
```

**Real-world analogy:**

* Like creating your own **recipe** in cooking. Once defined, you can reuse it anytime.

---

### 3.3 Functions with Parameters

Parameters (inputs) allow passing values to a function.

```python
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Alice")
```

---

### 3.4 Functions with Multiple Parameters

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)
```

---

### 3.5 Default Parameters

If no value is passed, a **default value** is used.

```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()          # Hello, Guest!
greet("Alice")   # Hello, Alice!
```

---

### 3.6 Keyword Arguments

You can specify arguments by name.

```python
def book_ticket(name, seat):
    print(f"Booking confirmed for {name} in seat {seat}")

book_ticket(seat=12, name="John")
```

---

### 3.7 Arbitrary Arguments (`*args`)

Allows passing multiple values without knowing the exact number.

```python
def show_numbers(*args):
    for num in args:
        print(num)

show_numbers(1, 2, 3, 4, 5)
```

---

### 3.8 Arbitrary Keyword Arguments (`**kwargs`)

Accepts multiple **key-value pairs**.

```python
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

show_info(name="Alice", age=25, city="New York")
```

---

### 3.9 Return Statement

Functions can return values back to the caller.

```python
def multiply(a, b):
    return a * b

result = multiply(4, 5)
print(result)  # 20
```

**Real-world analogy:**
A **vending machine** takes money + button press (input), and returns a snack (output).

---

### 3.10 Nested Functions

A function defined inside another function.

```python
def outer():
    def inner():
        print("This is inner function")
    inner()

outer()
```

---

### 3.11 Lambda Functions (Anonymous Functions)

Short, one-line functions using `lambda`.

```python
square = lambda x: x * x
print(square(5))  # 25
```

**Real-world analogy:**
Quick sticky notes vs. a full notebook — use lambdas for **short, quick tasks**.

---

## 4. Scope of Variables

* **Local variable:** Defined inside a function, accessible only inside.
* **Global variable:** Defined outside, accessible anywhere.

```python
x = 10  # global

def func():
    y = 5  # local
    print("Inside:", x, y)

func()
print("Outside:", x)  # y not accessible here
```

---

## 5. Why Use Functions?
 Code reusability Easier debugging Organized structure Avoid repetition

**Real-world analogy:**
Imagine writing your name 100 times in a notebook. Instead of rewriting each time, you create a **stamp** (function) and reuse it.

---

## Assignment — Functions

1. Write a function to calculate the square of a number.
2. Create a function that takes two numbers and returns their sum.
3. Write a function that takes a list and prints all its elements.
4. Create a function with default parameter that greets `"Guest"` if no name is passed.
5. Write a function that accepts arbitrary arguments (`*args`) and prints the largest number.
6. Write a function that accepts keyword arguments (`**kwargs`) and prints them in key-value format.
7. Create a function to check if a number is even or odd (use return statement).
8. Write a lambda function to find cube of a number.
9. Define a nested function where the inner function returns the square of a number and the outer function doubles it.
10. Create a function that takes a dictionary of students and marks, and returns the names of students who scored above 50.

---

