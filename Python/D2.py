# Day 02 - Python Practice
# Topics: input, print, strings, len(), indexing, concatenation, repetition


# 1. Print the input and ###
word = input()
print(word)
print("###")

# Takes one word and prints it, then prints ### on the next line.


# 2. Print two inputs on two lines
word1 = input()
word2 = input()
print(word1)
print(word2)

# Takes two words and prints each word on a separate line.


# 3. Join two words
first = input()
second = input()
print(first + second)

# Joins two strings without space.


# 4. Print name and age
name = input()
age = input()
print(name + " is " + age + " years old")

# Combines name and age in sentence format.


# 5. Full name
first_name = input()
last_name = input()
print(first_name + " " + last_name)

# Joins first name and last name with a space.


# 6. Simple square pattern
print("* *")
print("* *")

# Prints a simple 2x2 square pattern.


# 7. Simple triangle pattern
print("*")
print("* *")

# Prints a simple triangle pattern.


# 8. Stars format
word = input()
print("* * * " + word + " * * *")

# Prints the word between stars.


# 9. Length of string
word = input()
print(len(word))

# len() counts total characters in the string.


# 10. String repetition
word = input()
print((word + " ") * 3)

# Repeats the word three times with spaces.


# 11. First character
word = input()
print(word[0])

# Index 0 gives the first character of a string.


# 12. Reverse two-digit number
number = input()
first_digit = number[0]
second_digit = number[1]
print(second_digit + first_digit)

# Treats number as string and reverses two characters.


# 13. Index of last character
word = input()
last_index = len(word) - 1
print(last_index)

# Last index is always length - 1.


# 14. Last character
word = input()
last_index = len(word) - 1
print(word[last_index])

# Uses last index to print the last character.


# 15. First letter with stars
word = input()
first_letter = word[0]
stars = "*" * (len(word) - 1)
print(first_letter + stars)

# Keeps first letter and replaces remaining letters with stars.
