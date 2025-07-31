
# Python Lists – Complete Notes
---
## What is a List?

A **list** in Python is an ordered, mutable (changeable) collection of items.

- Lists can hold elements of any type (integers, strings, other lists, etc.).
- They allow duplicate values.
- Lists are defined using square brackets `[]`.

```python
my_list = [1, 2, 3, "apple", [5, 6]]
````

---

## Real-World Analogy

Think of a Python list like a **shopping list**:

* You can add or remove items.
* You care about the **order**.
* You can check what items are inside and how many times they appear.

---

## Common List Methods

| Method                | Description                                             | Example                |
| --------------------- | ------------------------------------------------------- | ---------------------- |
| `append(x)`           | Adds item `x` to the end                                | `lst.append(10)`       |
| `extend(iterable)`    | Appends all elements from another iterable              | `lst.extend([4, 5])`   |
| `insert(i, x)`        | Inserts item `x` at index `i`                           | `lst.insert(1, 99)`    |
| `remove(x)`           | Removes first occurrence of `x`                         | `lst.remove(2)`        |
| `pop(i=-1)`           | Removes and returns item at index `i` (default is last) | `lst.pop()`            |
| `clear()`             | Removes all items from the list                         | `lst.clear()`          |
| `index(x)`            | Returns index of first occurrence of `x`                | `lst.index("apple")`   |
| `count(x)`            | Counts number of times `x` appears                      | `lst.count(1)`         |
| `sort(reverse=False)` | Sorts the list in-place (ascending by default)          | `lst.sort()`           |
| `reverse()`           | Reverses the list in-place                              | `lst.reverse()`        |
| `copy()`              | Returns a shallow copy of the list                      | `new_lst = lst.copy()` |

---

## Other Useful Operations

| Operation      | Description       | Example          |
| -------------- | ----------------- | ---------------- |
| `len(lst)`     | Length of list    | `len(lst)`       |
| `x in lst`     | Membership test   | `"apple" in lst` |
| `lst + [a, b]` | Concatenate lists | `lst + [4, 5]`   |
| `lst * 2`      | Repeat list       | `lst * 2`        |
| `lst[i]`       | Indexing          | `lst[0]`         |
| `lst[i:j]`     | Slicing           | `lst[1:4]`       |

---

## Looping Over a List

```python
# Basic loop
for item in lst:
    print(item)

# With index
for i, item in enumerate(lst):
    print(i, item)
```

---

## List Comprehensions (Bonus)

Quickly create new lists using concise syntax.

```python
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
```

Add condition:

```python
evens = [x for x in range(10) if x % 2 == 0]
```

---

## Summary

* Lists are powerful, flexible, and widely used in Python.
* You can store, modify, and manipulate any type of data.
* Methods like `append`, `extend`, `sort`, and `pop` make lists highly functional.


---
---
---


## <center> List Exercises (Practice Only – No Answers)</center>

### 1. Create and Access
- Create a list with at least 6 different elements (mix of int, str, and float).
- Access and print the 2nd and 5th elements using indexing.

---

### 2. List Slicing
- Slice the list to get a sublist of the middle 3 elements.
- Reverse the list using slicing.

---

### 3. Add and Remove Elements
- Add an element to the end of the list using `append()`.
- Insert an element at the second position.
- Remove a specific element by value.
- Remove the last element using `pop()`.

---

### 4. Sorting and Reversing
- Sort a list of numbers in ascending order.
- Reverse the sorted list.

---

### 5. Counting and Indexing
- Count how many times a specific item appears in the list.
- Find the index of the first occurrence of a given item.

---

### 6. Extend vs Append
- Use `append()` to add a list to another list.
- Use `extend()` to merge two lists.
- What’s the difference in the result?

---

### 7. List Comprehension
- Use list comprehension to create a list of squares from 1 to 10.
- Use list comprehension to filter out odd numbers from a list.

---

### 8. Copying Lists
- Create a shallow copy of a list using `copy()`.
- Prove that modifying the new list does not affect the original.

---

### 9. Nested Lists
- Create a 2D list (a list of lists) representing a 3x3 matrix.
- Access the middle element of the matrix.
- Change the value of the bottom-right element.

---

### 10. Looping
- Loop through a list and print each item with its index.
- Sum all numeric values in a list using a loop.


```
Create a github repo with the above exercises and commit the code with a meaningful commit message and share the url of the repo on the form that will be send saturday.
```