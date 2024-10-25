#!/usr/bin/python2.7

# print statement
print "Hello from Python2!"

# divivsion (int to floor)
print 5 / 2

# string (ASCII)
print type("Some text")
print type(u"Some text")

# xrange
for x in xrange(0, 3):
    print x

# error handling
try:
    error_here
except NameError, error:
    print "Error msg: ", error

# raw_input
inp = raw_input("Enter: ")
print "Echo: ", inp

# type annotation
# not available in python2

# different types comparison
print [1,2] > "str"

# rounding (float)
print round(9.5)

# raise
raise NameError, "Custom exception"