
# Python Dictionaries — Complete Notes

## 1. What is a Dictionary in Python?

A **dictionary** in Python is a **collection of key-value pairs**.
## Properties of Python Dictionaries

- **Ordered** *(Python 3.7+)*: Maintains insertion order of keys.  
- **Indexed by keys**: Access elements using keys, not numeric positions.  
- **Keys are immutable**: Keys can be strings, numbers, or tuples (no lists or other dicts).  
- **Values are mutable**: You can change the value of a key after creation.  
- **Keys must be unique**: Adding the same key again overwrites the old value.  
- **Values can be duplicated**: Different keys can store the same value.  
- **Dynamic size**: Can grow or shrink in size at runtime.  
- **Heterogeneous values**: Values can be of any data type.  
- **Nested**: Can contain other dictionaries or lists as values.  

Think of it as a **real-world phonebook**:

* The **name** is the **key**.
* The **phone number** is the **value**.
 Keys must be **unique** and **immutable** (e.g., strings, numbers, tuples). Values can be **anything** — strings, numbers, lists, even other dictionaries.

```python
phonebook = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9999"
}
```

---

## 2. Creating Dictionaries

### Method 1: Curly Braces `{}` (Most Common)

```python
user = {"name": "John", "age": 25, "city": "New York"}
```

### Method 2: Using `dict()` Constructor

```python
user = dict(name="John", age=25, city="New York")
```

### Method 3: From List of Tuples

```python
pairs = [("name", "John"), ("age", 25)]
user = dict(pairs)
```

**Analogy**:
Creating a dictionary is like **filling out a contact form** — you specify what information each label (key) should hold.

---

## 3. Accessing Dictionary Elements

### Using Square Brackets `[]`

```python
print(user["name"])  # Output: John
```
 Throws `KeyError` if key doesn’t exist.

### Using `.get()` (Safer)

```python
print(user.get("email", "Not Available"))  # Output: Not Available
```
 **When to use:** If you’re not sure the key exists and want to avoid errors.

**Real-world analogy**:
Like **asking a librarian** for a book:

* `[]` is like demanding “Give me book X now!” — and getting upset if it’s not there.
* `.get()` is like politely asking “Do you have book X? If not, just tell me.”

---

## 4. Adding & Updating Elements

```python
user["email"] = "john@example.com"  # Add new
user["age"] = 26  # Update existing
```

**Real-world analogy**:
Like adding or updating a contact in your phone.

---

## 5. Removing Elements

### `pop(key[, default])`

Removes a key and returns its value.

```python
age = user.pop("age", None)
```
 Use when you need the value after removing it.

### `popitem()`

Removes **last inserted** key-value pair (Python 3.7+).

```python
last_item = user.popitem()
```
 Use for stack-like behavior.

### `del`

```python
del user["email"]
```
 Use when you don’t need the value.

### `clear()`

```python
user.clear()  # Empty dictionary
```
 Use to reset completely.

---

## 6. Looping Through Dictionaries

### Looping over Keys

```python
for key in user:
    print(key)
```

### Looping over Values

```python
for value in user.values():
    print(value)
```

### Looping over Key-Value Pairs

```python
for key, value in user.items():
    print(key, value)
```

**Analogy**:
Imagine you’re reading **a menu**:

* Keys = dish names
* Values = prices
* `.items()` = looking at dish + price together.

---

## 7. Dictionary Functions & Methods with Real-World Uses

| Function    | Description             | Real-World Example                          |
| ----------- | ----------------------- | ------------------------------------------- |
| `get()`     | Get value safely        | Checking if a contact exists before calling |
| `keys()`    | Get all keys            | Listing all usernames in a system           |
| `values()`  | Get all values          | Getting all product prices                  |
| `items()`   | Get all key-value pairs | Printing invoice with item name & price     |
| `update()`  | Merge or overwrite keys | Updating user profile with new details      |
| `pop()`     | Remove & return value   | Removing an order from active list          |
| `popitem()` | Remove last inserted    | Processing tasks in reverse order           |
| `clear()`   | Remove all items        | Resetting game state                        |

---

## 8. Dictionary Comprehensions

Quick way to create dictionaries.

```python
squares = {x: x**2 for x in range(5)}
```

**Analogy**:
Like creating a table where each row is automatically filled with a formula.

---

## 9. Nested Dictionaries

A dictionary inside another dictionary.

```python
company = {
    "emp1": {"name": "Alice", "role": "Engineer"},
    "emp2": {"name": "Bob", "role": "Manager"}
}
```
 Use for hierarchical data, like organization structures.

---

## 10. Common Pitfalls

* **Mutable keys**: Lists can’t be keys.
* **Overwriting keys**: Adding a key that already exists will replace the old value.
* **Unhashable types as keys**: Tuples are fine, lists are not.

---

## 11. When to Use Dictionaries in Real Life

* **Phonebook** (name → number)
* **Product Catalog** (product ID → details)
* **Configuration settings** (setting name → value)
* **Game inventory** (item name → quantity)

---

## 12. Full Example — Student Grade Tracker

```python
grades = {
    "Alice": [85, 90, 78],
    "Bob": [72, 88, 91],
}

# Add new student
grades["Charlie"] = [95, 85, 87]

# Update grades
grades["Alice"].append(92)

# Get average grades
for student, scores in grades.items():
    avg = sum(scores) / len(scores)
    print(f"{student}'s average: {avg:.2f}")
```

---

## 13. Summary Table

| Operation  | Syntax                         | Use Case               |
| ---------- | ------------------------------ | ---------------------- |
| Create     | `{}` / `dict()`                | Start a new collection |
| Access     | `dict[key]` / `.get()`         | Get values             |
| Add/Update | `dict[key] = value`            | Insert or modify       |
| Remove     | `pop()` / `del` / `clear()`    | Delete data            |
| Iterate    | `for key, val in dict.items()` | Looping                |


---
---
---

# <center> Assignment — Python Dictionaries

1. **Create a dictionary** called `student` with the following key-value pairs:
   - `"name"` → `"Alice"`
   - `"age"` → `22`
   - `"courses"` → `["Math", "Physics", "Chemistry"]`

2. **Add** a new key `"email"` with value `"alice@example.com"`.

3. **Update** the `"age"` to `23`.

4. **Remove** the `"email"` key using `pop()` and store the removed value in a variable.

5. **Access** the `"name"` value using `[]`.

6. **Access** the `"phone"` value using `.get()` with a default message `"Not available"`.

7. **Create** a dictionary comprehension that maps numbers from `1` to `5` to their squares.

8. **Nested Dictionary Task**:  
   Create a dictionary called `company` where each key is an employee ID (e.g., `"emp1"`, `"emp2"`) and the value is another dictionary with keys `"name"` and `"role"`.  
   Add at least two employees.

9. **Convert** the dictionary’s `.items()` view into a list of tuples.

10. **Convert** the list of tuples back into a dictionary.

---
