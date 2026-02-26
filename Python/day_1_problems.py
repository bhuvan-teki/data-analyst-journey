# Question 1: Basic String Input
# Sample Input: Bhuvan, 18
# Sample Output: Hello Bhuvan, you are 18 years old.

name = input()
age = input()
statement = ("Hello " + name + ", you are " + age + " years old.")
print(statement)

# --------------------------------------------------

# Question 2: Numbers + Thinking (Sum & Product)
# Sample Input: 10, 5
# Sample Output: Sum: 15, Product: 50

num1 = int(input())
num2 = int(input())

sum = num1 + num2
product = num1 * num2

print("Sum:", sum)
print("Product:", product)

# --------------------------------------------------

# Question 3: Input + Type + Logic (Future Age)
# Sample Input: 18
# Sample Output: After 5 years, you will be 23 years old.

age = int(input())
new_age = age + 5
statement = "After 5 years, you will be " + str(new_age) + " years old."
print(statement)

# --------------------------------------------------

# Question 4: Money + Real Life Logic (GST Calculation)
# Sample Input: 100
# Sample Output: Final Price: 118.0

price = float(input())
final_price = price + (price * 18 / 100)
print("Final Price:", final_price)
