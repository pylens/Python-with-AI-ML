# Arithmetic Operators

Arithmetic operators are used to perform mathematical operations on numeric values. These operators are fundamental in most programming languages and are used for everything from simple calculations to complex expressions.

## Common Arithmetic Operators

| Operator | Symbol | Description                            | Example         | Result |
|----------|--------|----------------------------------------|-----------------|--------|
| Addition | `+`    | Adds two operands                      | `5 + 3`         | `8`    |
| Subtraction | `-` | Subtracts right operand from left      | `10 - 4`        | `6`    |
| Multiplication | `*` | Multiplies two operands              | `6 * 7`         | `42`   |
| Division | `/`    | Divides left operand by right          | `15 / 3`        | `5.0`  |
| Floor Division | `//` | Divides and returns integer part    | `17 // 4`       | `4`    |
| Modulus | `%`     | Returns the remainder of a division    | `10 % 3`        | `1`    |
| Exponentiation | `**` | Raises to the power                 | `2 ** 3`        | `8`    |

## Detailed Explanation

### Addition (`+`)
- Adds two numbers.
- In some languages, can concatenate strings.
  - Example: `'Hello' + ' World'` gives `'Hello World'`.

### Subtraction (`-`)
- Subtracts right operand from the left.
  - Example: `9 - 4 = 5`

### Multiplication (`*`)
- Multiplies two numbers.
- In Python: `'Hi' * 3` = `'HiHiHi'`.

### Division (`/`)
- Divides and returns float (even if divisible).
  - Example: `10 / 2 = 5.0`, `5 / 2 = 2.5`

### Floor Division (`//`)
- Returns integer quotient, discards remainder.
  - Example: `17 // 4 = 4`

### Modulus (`%`)
- Returns remainder of division.
  - Example: `10 % 3 = 1`
- Often used to check for even/odd numbers:
  - `if x % 2 == 0`: even number.

### Exponentiation (`**`)
- Raises to the power.
  - Example: `2 ** 4 = 16`

## Operator Precedence

When multiple operators appear, precedence determines which are evaluated first.

Order (highest to lowest):
1. `**`
2. `*`, `/`, `//`, `%`
3. `+`, `-`

Associativity:
- `**`: right-to-left
- others: left-to-right

Examples:
- `5 + 2 * 3 = 5 + 6 = 11`
- `2 ** 3 ** 2 = 2 ** 9 = 512`

## Type Mixing

Mixing int and float:
- `5 + 2.0 = 7.0`
- `/` always returns float, even if whole number.

## Summary

Arithmetic operators include:
- `+`, `-`, `*`, `/`, `//`, `%`, `**`

They're essential for:
- Math
- Loop logic
- Conditions
- Algorithms

Use parentheses `()` to control precedence and improve readability:
- `(5 + 2) * 3 = 21`

Be careful with integer division, especially in loops or index-based logic.

# Logical Operators

Logical operators are used to combine conditional statements and return boolean values (`True` or `False`). These are essential for controlling flow in conditions (`if`, `while`, etc.).

## Common Logical Operators

| Operator | Keyword | Description                                  | Example              | Result |
|----------|---------|----------------------------------------------|----------------------|--------|
| AND      | `and`   | Returns `True` if both operands are true     | `True and True`      | `True` |
| OR       | `or`    | Returns `True` if at least one is true       | `True or False`      | `True` |
| NOT      | `not`   | Reverses the result                          | `not False`          | `True` |

## Detailed Explanation

### AND (`and`)
- Both conditions must be `True` for the result to be `True`.
- If any condition is `False`, the result is `False`.
```python
True and True   # True
True and False  # False
False and True  # False
False and False # False
```
- Example:
```python
age = 25
has_id = True
if age > 18 and has_id:
    print("Allowed")
```

### OR (`or`)
- At least one condition must be `True` for the result to be `True`.
- Only if both are `False`, the result is `False`.
```python
True or True    # True
True or False   # True
False or True   # True
False or False  # False
```
- Example:
```python
is_admin = False
is_editor = True
if is_admin or is_editor:
    print("Access granted")
```

### NOT (`not`)
- Reverses the boolean value.
```python
not True   # False
not False  # True
```
- Example:
```python
is_logged_in = False
if not is_logged_in:
    print("Please log in")
```

## Operator Precedence

Order of evaluation:
1. `not`
2. `and`
3. `or`

Examples:
```python
True or True and False    # evaluates to True
# Because: True or (True and False) => True or False => True

not True or False         # evaluates to False
# Because: (not True) or False => False or False => False
```

## Logical Operators with Non-Boolean Values (Python Specific)

Python allows logical operators to be used with non-boolean values, returning actual operands:

```python
a = 0
b = 5
a and b   # 0 (because a is falsy)
b and a   # 0 (because a is falsy)
a or b    # 5 (because a is falsy, returns b)
b or a    # 5 (because b is truthy)
```

- `and` returns the first falsy value or the last value if all are truthy.
- `or` returns the first truthy value.

This is used in Python idioms:
```python
name = input("Enter name: ") or "Guest"
```

## Summary

Logical operators are used to evaluate combinations of conditions:
- `and` → All must be `True`
- `or` → At least one must be `True`
- `not` → Inverts the boolean value

They are essential for:
- Conditional logic
- Filtering
- Flow control

Use parentheses `()` for clarity in complex expressions:
```python
if (is_active and is_verified) or is_admin:
    print("Access granted")
```

# Comparison Operators

Comparison operators are used to compare two values or expressions. They return a Boolean value: `True` or `False`.

## List of Comparison Operators

| Operator | Description                    | Example           | Result    |
|----------|--------------------------------|-------------------|-----------|
| `==`     | Equal to                       | `5 == 5`          | `True`    |
| `!=`     | Not equal to                   | `5 != 3`          | `True`    |
| `>`      | Greater than                   | `7 > 4`           | `True`    |
| `<`      | Less than                      | `2 < 6`           | `True`    |
| `>=`     | Greater than or equal to       | `8 >= 8`          | `True`    |
| `<=`     | Less than or equal to          | `3 <= 5`          | `True`    |

## Explanation and Examples

### Equal to (`==`)
Returns `True` if the operands are equal.
```python
5 == 5    # True
'a' == 'a'  # True
```

### Not equal to (`!=`)
Returns `True` if operands are not equal.
```python
5 != 3    # True
5 != 5    # False
```

### Greater than (`>`)
Returns `True` if the left operand is greater than the right.
```python
7 > 4     # True
3 > 9     # False
```

### Less than (`<`)
Returns `True` if the left operand is less than the right.
```python
2 < 6     # True
9 < 1     # False
```

### Greater than or equal to (`>=`)
Returns `True` if the left operand is greater than or equal to the right.
```python
8 >= 8    # True
9 >= 3    # True
```

### Less than or equal to (`<=`)
Returns `True` if the left operand is less than or equal to the right.
```python
3 <= 5    # True
10 <= 2   # False
```

## Comparison with Strings

Python compares strings using their Unicode values.
```python
'apple' == 'apple'   # True
'apple' < 'banana'   # True
'abc' > 'ABC'        # True (lowercase > uppercase)
```

## Chained Comparisons

Python supports chaining of comparison operators:
```python
x = 5
print(1 < x < 10)    # True
print(x == 5 == True)  # False, because 5 == True is False
```

## Comparing Different Types

Comparing different types can return `False` or raise an error:
```python
5 == '5'     # False (int vs str)
5 < '7'      # TypeError in Python 3
```

## Use in Conditions

Comparison operators are most commonly used in `if` statements and loops:
```python
age = 18
if age >= 18:
    print("Eligible")
```

## Summary

Comparison operators help you evaluate relationships between values:
- `==` checks equality
- `!=` checks inequality
- `>` and `<` compare magnitude
- `>=` and `<=` check inclusive conditions

Use them to build conditional logic and filters throughout your code.

# Bitwise Operators in Python

Bitwise operators operate on integers at the **bit level**. They perform operations on the binary representations of numbers.

## List of Bitwise Operators

| Operator | Name           | Description                                                        | Example           | Result     |
|----------|----------------|--------------------------------------------------------------------|-------------------|------------|
| `&`      | AND            | Sets each bit to 1 if both bits are 1                              | `5 & 3`           | `1`        |
|  |      | OR             | Sets each bit to 1 if one of two bits is 1                         | 5 | 3           | `7`        |
| `^`      | XOR            | Sets each bit to 1 if only one of two bits is 1                    | `5 ^ 3`           | `6`        |
| `~`      | NOT            | Inverts all the bits (1's complement)                              | `~5`              | `-6`       |
| `<<`     | Left Shift     | Shifts bits to the left and adds 0s on the right                   | `5 << 1`          | `10`       |
| `>>`     | Right Shift    | Shifts bits to the right and drops bits on the right               | `5 >> 1`          | `2`        |

## Explanation and Examples

### Bitwise AND (`&`)
```python
a = 5    # 0101
b = 3    # 0011
print(a & b)  # 0001 => 1
```

### Bitwise OR (`|`)
```python
a = 5    # 0101
b = 3    # 0011
print(a | b)  # 0111 => 7
```

### Bitwise XOR (`^`)
```python
a = 5    # 0101
b = 3    # 0011
print(a ^ b)  # 0110 => 6
```

### Bitwise NOT (`~`)
```python
a = 5    # 00000101
print(~a)  # 11111010 => -6 (in 2's complement)
```

### Left Shift (`<<`)
```python
a = 5    # 00000101
print(a << 1)  # 00001010 => 10
print(a << 2)  # 00010100 => 20
```

### Right Shift (`>>`)
```python
a = 5    # 00000101
print(a >> 1)  # 00000010 => 2
print(a >> 2)  # 00000001 => 1
```

## Binary Format Helper
You can use `bin()` to see the binary form of integers:
```python
print(bin(5))  # '0b101'
print(bin(3))  # '0b11'
```

## Use Cases

- **Bit masking** – Turning specific bits on/off
- **Permission handling** – e.g., `read`, `write`, `execute` flags
- **Compression** – Compact data into smaller representations
- **Performance optimization** – Bitwise ops are extremely fast

## Summary

Bitwise operators allow you to manipulate data at the binary level:

| Symbol | Operation        |
|--------|------------------|
| `&`    | AND              |
| `|`    | OR               |
| `^`    | XOR              |
| `~`    | NOT (1’s complement) |
| `<<`   | Left Shift       |
| `>>`   | Right Shift      |

Use them carefully, and only when working with **integers** and **binary-level logic**.

# Python Membership Operators

Membership operators in Python are used to test whether a value exists within a sequence, such as a list, tuple, set, string, or dictionary.

Python provides two membership operators:

---

## 1. `in`

### Description:
Returns `True` if the specified value exists in the sequence.

### Syntax:
```python
value in sequence
```

### Example:
```python
my_list = [1, 2, 3, 4]
print(3 in my_list)      # True
print(5 in my_list)      # False

word = "python"
print("y" in word)       # True
print("z" in word)       # False
```

---

## 2. `not in`

### Description:
Returns `True` if the specified value does not exist in the sequence.

### Syntax:
```python
value not in sequence
```

### Example:
```python
my_list = [1, 2, 3, 4]
print(5 not in my_list)    # True
print(2 not in my_list)    # False

word = "python"
print("a" not in word)     # True
print("p" not in word)     # False
```

---

## Works With:
- Strings: checks characters or substrings
- Lists, Tuples, Sets: checks if element exists
- Dictionaries: checks for keys only, not values

### Dictionary Example:
```python
my_dict = {"name": "Alice", "age": 25}
print("name" in my_dict)        # True (checks key)
print("Alice" in my_dict)       # False (value, not key)
```

---

## Summary Table

| Operator   | Description                         | Example             | Result |
|------------|-------------------------------------|----------------------|--------|
| `in`       | True if value exists in sequence    | `"a" in "apple"`     | True   |
| `not in`   | True if value not in sequence       | `"z" not in "apple"` | True   |

---

# End of Membership Operators Notes

# Python Identity Operators

Identity operators are used to compare the memory locations of two objects. In Python, everything is an object, and each object has a unique identity (memory address).

Python provides two identity operators:

---

## 1. `is`

### Description:
Returns `True` if both variables point to the same object in memory.

### Syntax:
```python
x is y
```

### Example:
```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)   # True: b refers to the same object as a
print(a is c)   # False: a and c have the same content, but different objects
```

---

## 2. `is not`

### Description:
Returns `True` if both variables do **not** point to the same object in memory.

### Syntax:
```python
x is not y
```

### Example:
```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is not b)  # False
print(a is not c)  # True
```

---

## Note:
- `is` checks for **object identity** (memory address).
- `==` checks for **value equality** (do contents match?).

### Example of Difference:
```python
x = [10, 20]
y = [10, 20]
print(x == y)   # True: same values
print(x is y)   # False: different objects
```

---

## Summary Table

| Operator   | Description                             | Example        | Result |
|------------|-----------------------------------------|----------------|--------|
| `is`       | True if same object in memory           | `x is y`       | True/False |
| `is not`   | True if not same object in memory       | `x is not y`   | True/False |

---

# End of Identity Operators Notes

