
# Python Loops — Complete Notes

## 1. Introduction
Loops are used to **repeat a block of code** multiple times until a condition is met or a sequence is exhausted.

**Real-world analogy:**  
- **For loop:** Like checking each book on a shelf one by one.  
- **While loop:** Like watering plants until the soil is moist — you don’t know exactly how many times you’ll pour water, you stop when the condition is met.

---

## 2. Types of Loops in Python

### 2.1 `for` Loop
Iterates over a sequence (like a list, tuple, string, or dictionary).

**Syntax:**
```python
for variable in sequence:
    # code block
````

**Example:**

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

**Real-world analogy:**
You call each friend in your contact list — you know exactly how many friends there are.

---

### 2.2 Using `range()` with `for`

`range()` generates a sequence of numbers.

**Example:**

```python
for i in range(5):
    print(i)  # 0 to 4
```

**Start & step values:**

```python
for i in range(2, 10, 2):
    print(i)  # 2, 4, 6, 8
```

---

### 2.3 `while` Loop

Repeats **while** a condition is `True`.

**Syntax:**

```python
while condition:
    # code block
```

**Example:**

```python
count = 1
while count <= 5:
    print(count)
    count += 1
```

**Real-world analogy:**
You keep eating until you feel full — you don’t know beforehand how many bites it will take.

---

### 2.4 Loop Control Statements

#### 1. `break`

Ends the loop immediately.

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

#### 2. `continue`

Skips the current iteration.

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

#### 3. `pass`

Does nothing (placeholder for future code).

```python
for i in range(3):
    pass
```

---

### 2.5 Nested Loops

A loop inside another loop.

```python
colors = ["red", "green"]
fruits = ["apple", "banana"]

for color in colors:
    for fruit in fruits:
        print(color, fruit)
```

---

### 2.6 `else` with Loops

Runs after the loop finishes naturally (not by `break`).

```python
for i in range(3):
    print(i)
else:
    print("Loop finished!")
```

---

## 3. Using Loops with Conditional Statements

Loops and conditionals are often combined to **repeat actions** but make **decisions inside each iteration**.

**Example:**

```python
for num in range(1, 11):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
```

**Real-world analogy:**
Checking each customer in a queue and deciding whether they have the correct documents before allowing entry.

---

## Assignment — Loops + Conditional Statements

1. Print all numbers from 1 to 20, but print `"Even"` if the number is even and `"Odd"` if the number is odd.
2. Loop through a list of names and print only those that start with the letter `"A"`.
3. For numbers from 1 to 50, print `"Fizz"` if divisible by 3, `"Buzz"` if divisible by 5, and `"FizzBuzz"` if divisible by both.
4. Given a dictionary of students and marks, print only the names of students who scored more than 75.
5. Print all prime numbers between 1 and 30.
6. Given a list of words, print those with length greater than 5 characters.
7. Using nested loops, print a multiplication table from 1 to 5, but skip printing results that are greater than 15.

