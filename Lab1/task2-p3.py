#!/usr/bin/python3.12

# print function
print("Hello from Python3!")

# division (float)
print(5/2)

# string (unicode)
print(type("Some text"))
print(type(u"Some text"))

# range
print([x for x in range(0, 3)])

# error handling
try:
    error_here
except NameError as error:
    print(f"Error msg: {error}")


#input
inp = input("Enter: ")
print(f"Echo: {inp}")

#type annotation
x: int = 10

# different types comparison
try:
    print([1,2] > "str")
except TypeError as e:
    print("Can't compare this :(")

# rounding (int)
print(round(9.5))

# raise
raise NameError("SCustom exception")