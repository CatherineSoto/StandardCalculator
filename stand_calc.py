# In this version, we give the user the option to decide whether they want to add, subtract, multiply, or divide.
# This decision ends up changing the entire format of the program.
# As of now, this program still takes it only 2 float numbers.


# Adding Function
def add(num1, num2):
    print("Adding: ")
    return num1 + num2

# Subtracting Function
def subtract(num1, num2):
    print("Subtracting: ")
    return num1 - num2

# Multiplying Function
def multiply(num1, num2):
    print("Multiplying: ")
    return num1 * num2

# Dividing Function
def divide(num1, num2):
    print("Dividing: ")
    return num1 / num2

# Taking input from the user
print("Would you like to add, subtract, multiply, or divide two numbers?")
choose = input("Type 'add' to add, 'sub' to subtract, 'mult' to multiply, and 'div' to divide: ")

num1 = float(input("First number: "))
num2 = float(input("Second number: "))

if choose == 'add':
    print(add(num1, num2))
elif choose == 'sub':
    print(subtract(num1, num2))
elif choose == 'mult':
    print(multiply(num1, num2))
elif choose == 'div':
    print(divide(num1, num2))
else:
    print("Invalid Input")
