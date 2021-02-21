# Tutorial 2

# Import relevant modules
import numpy as np

# Let's start indexing (returning specific values) arrays
array = np.array([1, 2, 3, 4, 5])  # One dimensional array
print(array[0])  # This prints the 1st element
print(array[3])  # This prints the 4th element

# Two dimension indexing
two_dim = np.array([[1, 2, 3], [4, 5, 6]])  # Two dimensional array
print(two_dim[0])  # This prints the 1st element of the 1st dimension
print(two_dim[1, 0])  # This selects the 2nd element of the 1st dimension, then prints the
# 1st element of the 2nd dimension

# Three dimensional indexing
three_dim = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(three_dim[0, 1, 2])
# This selects the 1st element of the 1st dimension to give [[1, 2, 3], [4, 5, 6]],
# then the 2nd element of the 2nd dimension to give [4, 5, 6],
# then prints the 3rd element of the 3rd dimension to give 6.

