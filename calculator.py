# Simple Calculator Program

def add(x, y):
  return x + y

def sub(x, y):
  return x - y

def mul(x, y):
  return x * y

def div(x, y):
  if y == 0:
    return "Error: Division by zero!"
  return x / y

print("Simple Calculator")
print("----------------")

# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

op_choice = int(input("Enter your choice (1/2/3/4): "))

# Perform the calculation
if op_choice == 1:
  result = add(num1, num2)
elif op_choice == 2:
  result = sub(num1, num2)
elif op_choice == 3:
  result = mul(num1, num2)
elif op_choice == 4:
  result = div(num1, num2)
else:
  result = "Error: Invalid operation choice!"

# Display the result
print("Result:", result)
