
# Python String Methods: Deep Dive Notes
This document covers the following important **string methods** in Python:  
- `split()`
- `join()`
- `replace()`
- `find()`
- `format()`


## 1. `split()`

### Theory
- Breaks a string into a **list of substrings** based on a delimiter (default is whitespace).

### Syntax:  

```python
string.split(separator, maxsplit)
```

### Real-World Analogy

Like cutting a **cake into slices**. Each slice = one word/part of the string.

### Example

```python
sentence = "Python is fun to learn"
words = sentence.split()  
print(words)  # ['Python', 'is', 'fun', 'to', 'learn']

csv_data = "John,Doe,25,New York"
fields = csv_data.split(",")
print(fields)  # ['John', 'Doe', '25', 'New York']
```

---

## 2. `join()`

### Theory

* Combines elements of a list/iterable into a **single string** using a separator.
* Syntax:

  ```python
  separator.join(iterable)
  ```

### Real-World Analogy

Like threading **beads on a string**. Beads = list items, thread = separator.

### Example

```python
words = ['Python', 'is', 'awesome']
sentence = " ".join(words)
print(sentence)  # Python is awesome

paths = ["home", "user", "documents"]
full_path = "/".join(paths)
print(full_path)  # home/user/documents
```

---

## 3. `replace()`

### Theory

* Substitutes parts of a string with another string.
* Syntax:

  ```python
  string.replace(old, new, count)
  ```

### Real-World Analogy

Like using **Find and Replace** in a text editor.

### Example

```python
text = "I like Java. Java is powerful."
new_text = text.replace("Java", "Python")
print(new_text)  # I like Python. Python is powerful.

limited = text.replace("Java", "Python", 1)
print(limited)  # I like Python. Java is powerful.
```

---

## 4. `find()`

### Theory

* Returns the **lowest index** of a substring in a string. If not found → `-1`.
* Syntax:

  ```python
  string.find(substring, start, end)
  ```

### Real-World Analogy

Like **looking for a book** on a shelf. If it’s there, you know the position; else you return empty-handed (`-1`).

### Example

```python
quote = "Knowledge is power"
index = quote.find("power")
print(index)  # 13

missing = quote.find("money")
print(missing)  # -1
```

---

## 5. `format()`

### Theory

* Inserts values into placeholders `{}` inside a string.
* Syntax:

  ```python
  string.format(value1, value2, ...)
  ```

### Real-World Analogy

Like filling **blanks in a form** with actual details.

### Example

```python
name = "Alice"
age = 25
intro = "My name is {} and I am {} years old.".format(name, age)
print(intro)  # My name is Alice and I am 25 years old.

print("Hello {0}, you scored {1}%".format("Bob", 92))
print("Hello {name}, you scored {score}%".format(name="Charlie", score=88))
```

---

# Assignment Section

These assignments combine **functions, loops, and conditionals** with the covered string methods.
Avoid OOP (classes, inheritance).

---

### 1. Sentence Analyzer

Write a function that:

* Takes a sentence as input.
* Splits it into words.
* Counts how many words start with a vowel and how many with a consonant.
* Returns the counts in a formatted string.

---

### 2. CSV Cleaner

You have a CSV string of names:
`"Alice, Bob ,Charlie,  David, Eve "`

* Write a function that:

  1. Splits the string into names.
  2. Removes extra spaces.
  3. Joins them back with `;`.
  4. Prints the cleaned CSV string.

---

### 3. Word Replacer Game

Write a program that:

* Asks the user for a paragraph.
* If the word `"boring"` is found, replace **all occurrences** with `"exciting"`.
* Print the modified paragraph.
* If `"boring"` is not found, print `"No changes made."`

---

### 4. Find First Vowel Position

Write a function that:

* Takes a string.
* Finds the **first vowel position** using `.find()` in a loop over vowels `"aeiou"`.
* Returns the vowel and its index.
* If no vowel is found, return `"No vowels"`.

---

### 5. Employee Report Generator

Write a program that:

1. Takes employee records as a list of strings:
   `["John,25,Developer,New York", "Alice,30,Designer,London", ...]`
2. For each record:

   * Split into fields.
   * Replace `"Developer"` with `"Data Scientist"`.
   * Format and print:
     `"Employee John (25 years old) works as a Data Scientist in New York."`

---

### 6. Password Strength Checker

Write a function that:

* Takes a password string.
* Checks:

  * Length ≥ 8
  * Contains at least one number
  * Contains at least one special character (`!@#$%^&*`)
* Use `.find()` and `.replace()` where needed.
* Return `"Strong Password"` or `"Weak Password"`.

---

### 7. Palindrome Sentence Checker

Write a function that:

* Takes a sentence.
* Removes spaces using `.replace()`.
* Checks (using loop + condition) if it reads the same forwards and backwards.
* Return `"Palindrome"` or `"Not Palindrome"`.


