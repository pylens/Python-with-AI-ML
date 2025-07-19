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
