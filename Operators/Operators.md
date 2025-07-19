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

