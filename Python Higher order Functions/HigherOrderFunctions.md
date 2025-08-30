

# Python Built-in Functions — `map`, `filter`, `reduce`, `zip`, `enumerate`

## 1. Why Use Them Instead of Loops?

* Loops can solve the same problems, but they often require **more code**.
* These functions allow **declarative programming** — you tell Python **what to do**, not **how to do it**.
* Often **faster and cleaner** because they’re implemented in C internally.

**Real-world analogy:**

* Think of them as **shortcuts in Excel** (like applying a formula to a whole column) instead of manually calculating each cell with a calculator.

---

## 2. `map()`

Applies a function to **each item** in an iterable and returns a new iterable.

**Syntax:**

```python
map(function, iterable)
```

**Example (with loop vs map):**

```python
numbers = [1, 2, 3, 4, 5]

# Loop way
squares = []
for n in numbers:
    squares.append(n**2)

# map way
squares_map = list(map(lambda x: x**2, numbers))

print(squares)      # [1, 4, 9, 16, 25]
print(squares_map)  # [1, 4, 9, 16, 25]
```

---

## 3. `filter()`

Filters elements from an iterable based on a **condition**.

**Syntax:**

```python
filter(function, iterable)
```

**Example:**

```python
numbers = [10, 15, 20, 25, 30]

# Loop way
evens = []
for n in numbers:
    if n % 2 == 0:
        evens.append(n)

# filter way
evens_filter = list(filter(lambda x: x % 2 == 0, numbers))

print(evens)        # [10, 20, 30]
print(evens_filter) # [10, 20, 30]
```

---

## 4. `reduce()`

Applies a function **cumulatively** to items of an iterable (requires `functools`).

**Syntax:**

```python
from functools import reduce
reduce(function, iterable)
```

**Example:**

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Loop way
total = 0
for n in numbers:
    total += n

# reduce way
total_reduce = reduce(lambda a, b: a + b, numbers)

print(total)        # 15
print(total_reduce) # 15
```

**Analogy:**
Like adding bills one by one in a wallet until you get the **final total**.

---

## 5. `zip()`

Combines two or more iterables element-wise.

**Syntax:**

```python
zip(iterable1, iterable2, ...)
```

**Example:**

```python
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]

combined = list(zip(names, scores))
print(combined)  # [('Alice', 85), ('Bob', 90), ('Charlie', 95)]
```

**Analogy:**
Like zipping two sides of a zipper together — pairs elements side by side.

---

## 6. `enumerate()`

Adds an **index counter** to an iterable.

**Syntax:**

```python
enumerate(iterable, start=0)
```

**Example:**

```python
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

# Output:
# 1 apple
# 2 banana
# 3 cherry
```

**Analogy:**
Like giving students **roll numbers** in a classroom.

---

## Assignment — Built-in Functions

1. Use `map()` to convert a list of temperatures in Celsius to Fahrenheit.
2. Use `filter()` to extract names longer than 5 characters from a list of names.
3. Use `reduce()` to find the product of all numbers in a list.
4. Use `zip()` to pair a list of countries with their capitals.
5. Use `enumerate()` to print items in a shopping list along with their position.
6. Combine `map()` and `filter()` to square only the even numbers in a list.
7. Use `zip()` and `map()` together to add two lists element-wise.

