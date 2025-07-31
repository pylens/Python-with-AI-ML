
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

```

---

You can copy this entire block into your markdown notes — it will render perfectly.

Let me know the next topic you want: **tuples**, **sets**, **dicts**, or maybe even **NumPy arrays vs lists**?
```
