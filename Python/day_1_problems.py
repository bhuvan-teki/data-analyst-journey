# Question 1: Basic String Input
# input = Bhuvan
# input = 18

name = input()
age = input()
statement = ("Hello " + name + ", you are " + age + " years old.")
print(statement)

# output: Hello Bhuvan, you are 18 years old.

# --------------------------------------------------

# Question 2: Numbers + Thinking (Sum & Product)
# input = 10
# input = 5

num1 = int(input())
num2 = int(input())

sum = num1 + num2
product = num1 * num2

print("Sum:", sum)
print("Product:", product)

# output:
# Sum: 15
# Product: 50

# --------------------------------------------------

# Question 3: Input + Type + Logic (Future Age)
# input = 18

age = int(input())
new_age = age + 5
statement = "After 5 years, you will be " + str(new_age) + " years old."
print(statement)

# output: After 5 years, you will be 23 years old.

# --------------------------------------------------

# Question 4: Money + Real Life Logic (GST Calculation)
# input = 100

price = float(input())
final_price = price + (price * 18 / 100)
print("Final Price:", final_price)

# output: Final Price: 118.0
