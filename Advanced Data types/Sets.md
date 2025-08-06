

# Python Sets – Complete Notes

##  What is a Set?

A **set** in Python is an unordered collection of **unique** and **immutable** elements.

- Defined using curly braces `{}` or the `set()` constructor.
- Automatically removes duplicates.
- Elements must be hashable (e.g., no lists inside a set).

```python
my_set = {1, 2, 3}
````

##  Real-World Analogy

Imagine a **guest list for a private event**:

* Every person can only appear **once**.
* The order in which names are added doesn’t matter.
* You can check if someone is invited, but not their position on the list.

---

##  Key Characteristics

| Property      | Description                                  |
| ------------- | -------------------------------------------- |
| Unordered     | No indexing or slicing (`set[0]` is invalid) |
| Unique values | Duplicate items are removed automatically    |
| Mutable       | Can add or remove elements                   |


---

##  Common Set Methods

| Method             | Description                                 | Example            |
| ------------------ | ------------------------------------------- | ------------------ |
| `add(x)`           | Adds element `x`                            | `s.add(5)`         |
| `update(iterable)` | Adds multiple elements                      | `s.update([6, 7])` |
| `remove(x)`        | Removes element `x` (KeyError if not found) | `s.remove(2)`      |
| `discard(x)`       | Removes element `x` (no error if not found) | `s.discard(10)`    |
| `pop()`            | Removes and returns a random element        | `s.pop()`          |
| `clear()`          | Removes all elements                        | `s.clear()`        |
| `copy()`           | Returns a shallow copy                      | `t = s.copy()`     |

---

##  Set Operations (Math-Style)

| Operation            | Symbol/Method                            | Description                      |                             |
| -------------------- | ---------------------------------------- | -------------------------------- | --------------------------- |
| Union                | \`                                       | `or`set1.union(set2)\`           | All elements from both sets |
| Intersection         | `&` or `set1.intersection(set2)`         | Common elements                  |                             |
| Difference           | `-` or `set1.difference(set2)`           | Elements in set1 but not in set2 |                             |
| Symmetric Difference | `^` or `set1.symmetric_difference(set2)` | Elements in either, not both     |                             |
| Subset check         | `set1 <= set2`                           | True if set1 is subset of set2   |                             |
| Superset check       | `set1 >= set2`                           | True if set1 is superset of set2 |                             |
| Disjoint check       | `set1.isdisjoint(set2)`                  | True if no elements in common    |                             |

---

##  What You Can’t Do with Sets

* No indexing: `s[0]` will raise `TypeError`
* No slicing
* Cannot contain unhashable types (like lists, dictionaries)

---

##  Looping Over a Set

```python
my_set = {"apple", "banana", "cherry"}
for item in my_set:
    print(item)  # Order not guaranteed
```

---

##  When to Use Sets

* Removing duplicates from a list
* Fast membership testing (`x in s`)
* Performing set operations like union, intersection, difference
* Representing items that must be **unique**

---

##  <center>Set Exercises (Practice Only – No Answers)</center>
---
---

### 1. Basic Set Creation

* Create a set with integers from 1 to 5.
* Add the number 6 to the set.

---

### 2. Duplicate Removal

* Convert the list `[1, 2, 2, 3, 4, 4, 4, 5]` into a set to remove duplicates.

---

### 3. Membership Testing

* Check if the number 3 exists in the set `{1, 2, 3, 4}`.

---

### 4. Set Operations

* Given: `a = {1, 2, 3}`, `b = {3, 4, 5}`
* Find:

  * Union
  * Intersection
  * Difference (a - b)
  * Symmetric difference

---

### 5. Subset and Superset

* Check if `{1, 2}` is a subset of `{1, 2, 3, 4}`.
* Check if `{1, 2, 3, 4}` is a superset of `{2, 3}`.

---

### 6. Removing Elements

* Try removing an element that **exists** using `remove()`.
* Try removing one that **doesn’t exist** using both `remove()` and `discard()` — what happens?

---

### 7. Set from String

* Convert the string `"banana"` into a set.
* What is the result?

---

---

##  Summary

* Sets are used to store **unique**, unordered items.
* Great for **fast lookup**, **de-duplication**, and **set math operations**.
* No indexing or duplicates allowed.
