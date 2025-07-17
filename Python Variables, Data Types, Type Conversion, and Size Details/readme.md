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
| **Data Type** | Example        | Description                   | Typical Size (64-bit)              |
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


## Python Type Conversion – Rules and Limitations

### 1. Implicit Type Conversion
Python automatically converts a variable from one data type to another during operations when needed.
It only happens between compatible types to prevent data loss.

Usually converts from lower precision to higher precision types (e.g., int to float).
Rules:

int + float results in float

int + complex results in complex

float + complex results in complex

Limitations:

Cannot implicitly convert between incompatible types (e.g., str and int)
May result in unintended data types if not handled carefully

2. Explicit Type Conversion (Type Casting)
Done manually using built-in functions such as int(), float(), str(), bool(), list(), tuple(), etc.

Useful when converting between types that do not automatically convert

**Common Conversions:**

int("123") → converts numeric string to integer
float("3.14") → converts string to float
str(100) → converts number to string
bool(0) → converts to False, non-zero numbers convert to True
list("abc") → converts string to list of characters

**Rules:**

- The value must be in a format that the target type can interpret

- Strings must contain only valid numeric characters when converting to int or float
- Converting from float to int truncates the decimal part
  
**Limitations:**

- int("abc") raises ValueError because the string is not numeric
- int(3.9) returns 3, not 4 (it truncates, not rounds)
- float("3.14.15") raises ValueError due to invalid format
- int(3+4j) raises TypeError because complex numbers cannot be converted to int or float
- bool() may return False for values like 0, None, '', [], {}, even though they are not literally False
  
3. Data Type Sizes and Limits (on a 64-bit system)
   
- int: Arbitrary size, limited only by available memory
- float: 64-bit (IEEE 754), approximately ±1.8 × 10³⁰⁸
- bool: Uses 1 byte, represents True or False
- str, list, dict, etc.: Dynamically sized, limited by system memory
  
5. Key Limitations and Caveats
- Precision loss when converting large integers to float
- Float to int conversion discards fractional part
- No direct conversion from complex to int or float
- Always ensure proper format before converting from string
- Implicit conversions can sometimes lead to unexpected data types in operations
