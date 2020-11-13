import sys

x = float(input("x: "))
y = float(input("y: "))

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    sys.exit(1)
except ValueError:
    print("Strings can not be divided, it must be an integer or a floating point number")
    sys.exit(1)


print(f"{x} divided by {y} is {result}")
