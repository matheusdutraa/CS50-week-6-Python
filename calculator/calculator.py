try:
    x = int(input("x: "))
except ValueError:
    print("That is not an int!")
try:
    y = int(input("y: "))
except ValueError:
    print("That is not an int!")

print(x + y)


"""
from cs50 import get_int

x = get_int("x: ")
y = get_int("y: ")
print(x + y)
"""
"""
from cs50

x = cs50.get_int("x: ")
y = cs50.get_int("y: ")
print(x + y)
"""
