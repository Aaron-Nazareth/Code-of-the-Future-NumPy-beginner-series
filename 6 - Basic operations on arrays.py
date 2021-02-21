# Tutorial 6

# Importing relevant modules
import numpy as np

# We can create an array between numbers like we can do with lists and the 'range' command.
# When using arrays, we use the 'arange' command.
a = np.arange(0, 5)  # Creates an array from 0 up to 5 - [0 1 2 3 4]
print(a)

# Basic math operations on arrays
b = np.array([4, 6, 19, 23, 45])
print(b)

# Addition
print(a + b)
# Subtraction
print(b - a)
# Square all the elements in a
print(a**2)

# NumPy actually has it's own functions built in
print(np.square(a))

# Testing whether values in an array are less than a given value
c = np.array([1, 2, 3, 4])
print(c < 2)  # This prints an array of booleans showing whether values are less than 2.
