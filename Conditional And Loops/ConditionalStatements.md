
# Python Conditional Statements — Complete Note
## 1. What are Conditional Statements?

Conditional statements allow you to **control the flow** of your program based on certain conditions (True/False).

**Real-world analogy:**
Think of them like **traffic lights**:

* Green → Go (do something)
* Red → Stop (do something else)
* Yellow → Prepare (maybe do a different action)

---

## 2. The `if` Statement

**Syntax:**

```python
if condition:
    # code to execute if condition is True
```

**Example:**

```python
temperature = 35
if temperature > 30:
    print("It's hot outside!")
```

**Real-world analogy:**
“If it’s raining, take an umbrella.”

---

## 3. The `if...else` Statement

**Syntax:**

```python
if condition:
    # runs if True
else:
    # runs if False
```

**Example:**

```python
balance = 500
if balance >= 100:
    print("Purchase approved.")
else:
    print("Insufficient funds.")
```

**Real-world analogy:**
“If the shop is open, buy milk. Otherwise, wait until tomorrow.”

---

## 4. The `if...elif...else` Statement

**Syntax:**

```python
if condition1:
    # runs if condition1 is True
elif condition2:
    # runs if condition1 is False and condition2 is True
else:
    # runs if none are True
```

**Example:**

```python
marks = 85
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
else:
    print("Grade: C")
```

**Real-world analogy:**
Choosing clothes based on weather:

* If it’s sunny → Wear sunglasses
* Else if it’s cloudy → Take a light jacket
* Else → Carry an umbrella

---

## 5. Nested `if` Statements

**Syntax:**

```python
if condition1:
    if condition2:
        # runs if both are True
```

**Example:**

```python
age = 20
citizen = True
if age >= 18:
    if citizen:
        print("Eligible to vote.")
```

**Real-world analogy:**
“If the store is open AND you have money, then buy groceries.”

---

## 6. The `pass` Statement

`pass` is used as a placeholder when no action is needed.

**Example:**

```python
age = 17
if age < 18:
    pass  # Do nothing for now
```

**Real-world analogy:**
Like saying “No comment” when you have nothing to say.

---

## 7. Short-hand Conditional Expressions (Ternary Operator)

**Syntax:**

```python
value_if_true if condition else value_if_false
```

**Example:**

```python
age = 18
status = "Adult" if age >= 18 else "Minor"
```

**Real-world analogy:**
“If you have a ticket, enter. Else, stay outside.”

---

## 8. Multiple Conditions with `and` / `or` / `not`

### `and`

```python
if age >= 18 and citizen:
    print("Eligible to vote.")
```
 Runs if **both** conditions are True.

**Real-world analogy:** “You can drive if you’re 18 AND have a license.”

---

### `or`

```python
if day == "Saturday" or day == "Sunday":
    print("Weekend!")
```
 Runs if **at least one** condition is True.

**Real-world analogy:** “You can enter with a ticket OR a VIP pass.”

---

### `not`

```python
if not raining:
    print("Go for a walk.")
```
 Runs if the condition is False.

**Real-world analogy:** “If NOT hungry, don’t order food.”

---

## 9. `in` and `not in` in Conditionals

```python
fruits = ["apple", "banana", "cherry"]

if "banana" in fruits:
    print("We have bananas!")

if "mango" not in fruits:
    print("No mangoes available.")
```

**Real-world analogy:**
Checking if a book is in a library’s catalog.

---

## 10. Common Pitfalls

* Using `=` instead of `==` in conditions. (`=` assigns, `==` compares)
* Forgetting colons (`:`) after `if`, `elif`, `else`.
* Indentation errors.

---

## Assignment — Conditional Statements (No Loops)


1. **Simple `if`**:  
   Store your age in a variable. If it’s 18 or above, print "Adult".

2. **`if...else`**:  
   Store your bank balance in a variable. If it’s greater than 1000, print "Sufficient funds", else print "Low balance".

3. **`if...elif...else`**:  
   Store a number in a variable.  
   - If it’s positive, print "Positive".  
   - If it’s zero, print "Zero".  
   - Else, print "Negative".

4. **Nested `if`**:  
   Store your age and a boolean `has_license`. If age is 18 or above and `has_license` is True, print "Can drive".

5. **Ternary Operator**:  
   Store your score in a variable. Print `"Pass"` if it’s 50 or above, otherwise print `"Fail"`.

6. **`and` / `or`**:  
   Store two boolean variables `is_weekend` and `is_holiday`. If it’s weekend or holiday, print `"Day off"`.

7. **`in` / `not in`**:  
   Create a list of three colors. If `"red"` is in the list, print `"Red available"`. If `"green"` is not in the list, print `"Green not available"`.


