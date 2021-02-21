# Tutorial 3

# Importing relevant modules
import numpy as np

# Slicing one dimensional arrays
one_dim = np.array([1, 2, 3, 4, 5])  # One dimensional array
print(one_dim[0:4])  # Prints from 1st element up to (but not including) 5th element
print(one_dim[2:])  # Prints from the 3rd element to the last element
# We can recall elements in steps
print(one_dim[:4:2])  # Uses increment of 2

# Considering two dimensional array slicing
two_dim = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(two_dim[1, 0:2])  # This prints from the 1st element up to the 3rd element,
# within the 2nd dimension

print(two_dim[0:3, 0])  # This prints the 1st element within the 2nd dimension, from each of
# the 1st element up to the 4th element within the 1st dimension.

print(two_dim[0:, 0:2])  # From all elements, slice from index 0 to index 2
