# Sequence of Instructions & Input/Output Basics

**Date:** June 4, 2026  
**Module:** Python Fundamentals

````md

A program is a sequence of instructions given to a computer.

Python executes code line by line from top to bottom.

## Variables

A variable is created when we assign a value to it for the first time.

Example:

```python
age = 10
print(age)
````

Output:

```text
10
```

If the variable name is inside quotes, Python prints the text, not the value.

```python
age = 10
print("age")
```

Output:

```text
age
```

## Order of Instructions

Python reads code line by line.

Wrong example:

```python
print(age)
age = 10
```

Output:

```text
NameError
```

Reason:

The variable `age` was not created before printing.

## Spacing in Python

Unwanted spaces at the beginning of a line can cause errors.

Example error:

```text
IndentationError
```

This happens when Python finds unexpected spacing.

## Variable Reassignment

Values stored in variables can be changed.

```python
a = 1
print(a)

a = 2
print(a)
```

Output:

```text
1
2
```

## Updating a Variable

```python
a = 2
print(a)

a = a + 1
print(a)
```

Output:

```text
2
3
```

## Expression

An expression is a valid combination of values, variables, and operators.

Examples:

```python
a * b
a + 2
5 * 2 + 3 * 4
```

## BODMAS

Python follows the normal order of operations.

Order:

1. Brackets
2. Orders
3. Division
4. Multiplication
5. Addition
6. Subtraction

Example:

```python
print(10 / 2 + 3)
print(10 / (2 + 3))
```

Output:

```text
8.0
2.0
```

---

# Input and Output Basics

## String Concatenation

Joining strings together is called string concatenation.

```python
a = "Hello" + " " + "World"
print(a)
```

Output:

```text
Hello World
```

## Concatenation Error

String concatenation works only with strings.

Wrong example:

```python
a = "*" + 10
print(a)
```

Output:

```text
TypeError
```

Reason:

Python cannot directly add a string and an integer.

## String Repetition

The `*` operator can repeat a string.

```python
a = "*" * 10
print(a)
```

Output:

```text
**********
```

## Formatting with Repetition

```python
s = "Python"
s = ("* " * 3) + s + (" *" * 3)
print(s)
```

Output:

```text
* * * Python * * *
```

## Length of String

`len()` returns the number of characters in a string.

```python
username = input()
length = len(username)
print(length)
```

Input:

```text
Ravi
```

Output:

```text
4
```

## input()

`input()` is used to take input from the user.

Important:

`input()` always reads the entered value as a string.

Example:

```python
username = input()
print(username)
```

Input:

```text
Ajay
```

Output:

```text
Ajay
```

## Joining Input Values

```python
username = input()
age = input()
print(username + " is " + age + " years old")
```

Input:

```text
Ravi
10
```

Output:

```text
Ravi is 10 years old
```

This works because `input()` stores `10` as a string `"10"`.

## String Indexing

We can access characters in a string using index numbers.

Index starts from `0`.

Example:

```python
username = "Ravi"
first_letter = username[0]
print(first_letter)
```

Output:

```text
R
```

## IndexError

Using an index that does not exist causes an error.

```python
username = "Ravi"
print(username[4])
```

Output:

```text
IndexError
```

Reason:

`Ravi` has indexes:

```text
R = 0
a = 1
v = 2
i = 3
```

There is no index `4`.

## 🎯 Key Concepts Mastered Today

* Program
* Sequence of instructions
* Variables
* Variable reassignment
* Expressions
* BODMAS
* input()
* print()
* Strings
* String concatenation
* String repetition
* len()
* String indexing
* NameError
* TypeError
* IndentationError
* IndexError

## 👨‍💻 Repository Owner
Bhuvan Teki

GitHub: https://github.com/bhuvan-teki/

LinkedIn: https://www.linkedin.com/in/bhuvanteki/

Data Analyst Journey - Documenting my learning progress, logic implementation, and technical growth step-by-step.
