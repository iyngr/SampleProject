# Building a calculator using Python
def sum(num1, num2):
    result = num1 + num2


def diff(num1, num2):
    result = num1 - num2


def mul(num1, num2):
    result = num1 * num2


def div(num1, num2):
    result = num1 / num2


print("Press 1 to add two numbers")
print("Press 2 to subtract two numbers")
print("Press 3 to find product of two numbers")
print("Press 4 to find quotient of two numbers")
print("To exit press 5")
choice = input("Enter your choice 1 to 4")

num1 = input("First number")
num2 = input("Second number")

if choice == 1:
    print(sum(num1, num2))
elif choice == 2:
    print(diff(num1, num2))
elif choice == 3:
    print(mul(num1, num2))
elif choice == 4:
    print(diff(num1, num2))
elif choice == 5:
    exit()
else:
    print("Enter a valid number to perform calculation")
