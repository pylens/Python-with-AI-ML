
# Python Comprehensions — Complete Notes

## 1. Introduction
Comprehensions in Python provide a **concise way** to create new lists, sets, or dictionaries from existing iterables (like lists, tuples, strings, or ranges).

Instead of writing **multiple lines of loops + conditionals**, you can achieve the same result in **a single line**.

---

## 2. Why Use Comprehensions Instead of Loops?

### Advantages
- **Shorter code** (more readable & elegant).
- **Faster execution** (optimized at the C level).
- **Cleaner logic** (one-liner instead of multiple lines).
- **Easy transformations** (map + filter in one step).

**Without comprehension:**
```python
squares = []
for i in range(1, 6):
    squares.append(i * i)
print(squares)
````

**With comprehension:**

```python
squares = [i * i for i in range(1, 6)]
print(squares)
```

---

## 3. Real-world Analogy

Imagine **filtering fruits in a basket**:

* Without comprehension: You take each fruit, check it, and then put it in another basket manually.
* With comprehension: You use a **sorting machine** that automatically checks and puts the right fruits in the basket in one go.

---

## 4. Types of Comprehensions

### 4.1 List Comprehension

Creates a list in a single line.

**Basic form:**

```python
[expression for item in iterable if condition]
```

**Examples:**

```python
# Squares of even numbers from 1–10
squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(squares)  # [4, 16, 36, 64, 100]

# Flatten a nested list
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [num for row in matrix for num in row]
print(flattened)  # [1, 2, 3, 4, 5, 6]
```

---

### 4.2 Set Comprehension

Creates a set (unique elements, unordered).

```python
nums = [1, 2, 2, 3, 4, 4, 5]
unique_squares = {x**2 for x in nums}
print(unique_squares)  # {1, 4, 9, 16, 25}
```

---

### 4.3 Dictionary Comprehension

Creates a dictionary in one line.

```python
# Create dictionary of number and its cube
cubes = {x: x**3 for x in range(1, 6)}
print(cubes)  # {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}

# Invert key-value pairs
original = {'a': 1, 'b': 2, 'c': 3}
inverted = {v: k for k, v in original.items()}
print(inverted)  # {1: 'a', 2: 'b', 3: 'c'}
```

---

### 4.4 Nested Comprehensions

Comprehensions inside comprehensions.

```python
# Multiplication table (1 to 3)
table = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(table)  # [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# Extract vowels from list of words
words = ["apple", "banana", "grape"]
vowels = [ch for word in words for ch in word if ch in "aeiou"]
print(vowels)  # ['a', 'e', 'a', 'a', 'a', 'a', 'e']
```

---

## 5. Medium-to-Complex Examples

### 5.1 Filtering with Conditions

```python
# Students who passed
students = {"Alice": 85, "Bob": 42, "Charlie": 77, "Diana": 35}
passed = {name: score for name, score in students.items() if score >= 50}
print(passed)  # {'Alice': 85, 'Charlie': 77}
```

---

### 5.2 Matrix Transpose

```python
matrix = [[1, 2, 3], [4, 5, 6]]
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transpose)  # [[1, 4], [2, 5], [3, 6]]
```

---

### 5.3 Cartesian Product

```python
colors = ["red", "blue"]
objects = ["car", "ball"]

pairs = [(c, o) for c in colors for o in objects]
print(pairs)  # [('red', 'car'), ('red', 'ball'), ('blue', 'car'), ('blue', 'ball')]
```

---

### 5.4 Flattening + Filtering Together

```python
nested = [[1, -2, 3], [-4, 5, -6]]
positive_nums = [num for row in nested for num in row if num > 0]
print(positive_nums)  # [1, 3, 5]
```

---

### 5.5 Complex Transformation

```python
# Dictionary with word lengths (ignoring short words)
words = ["python", "is", "awesome", "to", "learn"]
word_lengths = {word: len(word) for word in words if len(word) > 2}
print(word_lengths)  # {'python': 6, 'awesome': 7, 'learn': 5}
```

---

## 6. When NOT to Use Comprehensions

* If logic is too **complex to read in one line** → normal loops are better.
* If it involves **multiple nested conditions** → loops improve clarity.

---

## Assignment — Python Comprehensions

1. Create a list comprehension that stores the squares of numbers from 1 to 20 but only if the number is divisible by 3.
2. Given a string, use comprehension to remove all vowels from it.
3. Flatten the following nested list using list comprehension: `[[1,2,3],[4,5],[6,7,8]]`.
4. Create a set comprehension to find unique consonants in the word `"comprehension"`.
5. Use dictionary comprehension to map each character in `"PYTHON"` to its ASCII value.
6. From a dictionary of students and scores, build a new dictionary containing only students who scored **above average**.
7. Generate a list of all `(x, y)` coordinate pairs where `x` and `y` are from 1–5 but only if `x + y` is even.
8. Transpose a 3x3 matrix using nested list comprehensions.
9. Given a list of words, create a dictionary where the key is the word and the value is the count of vowels in that word.
10. Build a dictionary comprehension to invert a nested dictionary:

```python
data = {"a": {"x": 1}, "b": {"y": 2}}
# Expected output: {1: ("a","x"), 2: ("b","y")}

```
