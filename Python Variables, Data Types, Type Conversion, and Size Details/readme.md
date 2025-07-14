## Python Variables, Data Types, Type Conversion, and Size Details

### 1. Variables in Python
* A variable stores data in memory.
* You do not need to declare its type.
* Use = to assign values.
Example:
```python
name = "Alice"

age = 25

height = 5.7
```
* Variables are case-sensitive
* Names should not start with a number

### 2. Common Data Types and Their Size (in Python)
| ** Data Type ** | Example        | Description                   | Typical Size (64-bit)              |
|-----------|----------------|-------------------------------|------------------------------------|
| int       | x = 10000      | Whole numbers                 | At least 24–28 bytes               |
| float     | y = 3.14       | Decimal numbers (floating point) | 24 bytes                        |
| bool      | flag = True    | Boolean (True or False)       | 28 bytes                           |
| str       | name = "Bob"   | Text / sequence of characters | 49 + length in bytes               |
| list      | [1, 2, 3]      | Ordered mutable collection    | 64 bytes (base) + items            |
| tuple     | (1, 2)         | Ordered immutable collection  | 48 bytes (base) + items            |
| dict      | {"a": 1}       | Key-value pairs               | ~240+ bytes (depends)              |
| set       | {1, 2}         | Unordered unique items        | ~232+ bytes                        |


#### To check the size of an object in Python:
```python
import sys
print(sys.getsizeof(10))      # size of int
print(sys.getsizeof(3.14))    # size of float
print(sys.getsizeof("text"))  # size of str
```
Note: Sizes include Python's object overhead and are approximate for 64-bit systems.

### 3. Platform and Architecture Differences (32-bit vs 64-bit)
* On 64-bit systems, Python has a larger memory overhead due to pointer size (8 bytes instead of 4).
* On 32-bit systems, objects like int, list, and dict take less space in memory.
* In low-level languages like C/C++, data types have fixed sizes (e.g., int = 4 bytes), but:
    * In Python, data types are objects, so their size is not fixed and may grow dynamically.
* Example: Python int can store very large numbers (no overflow), unlike C/C++.

### 4. Type Conversion (Casting)
Convert data from one type to another using built-in functions:

| Function   | Description             |
|------------|-------------------------|
| int(x)     | Converts to integer     |
| float(x)   | Converts to float       |
| str(x)     | Converts to string      |
| bool(x)    | Converts to boolean     |


Examples:
``` python
a = "123"
b = int(a)     # "123" → 123

x = 5

y = float(x)   # 5 → 5.0

z = str(x)     # 5 → "5"

Note: Not all conversions are valid:

int("abc")  # Error
```
### 5. Check Type and Size in Python
```python
x = 100
print(type(x))            # <class 'int'>
print(sys.getsizeof(x))   # Memory size in bytes
```
Summary:
* Python is dynamically typed, so size depends on the value and system.
* On 64-bit machines, memory use is slightly higher.
* Use sys.getsizeof() for actual memory usage.
* Unlike C/C++, Python int and float do not have strict size limits.
