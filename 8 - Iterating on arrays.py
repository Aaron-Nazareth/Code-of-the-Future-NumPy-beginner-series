# Tutorial 8

# Importing relevant modules
import numpy as np

# Iterating over a 1 dimensional array
one_dim = np.array([1, 2, 3, 4, 5])

for element in one_dim:
    print(element)

# Iterating over a 2 dimensional array
two_dim = np.array([[1, 2, 3], [4, 5, 6]])

for element in two_dim:
    for number in element:  # For loop in a for loop is required due to 2nd dimension
        print(number)

# Using 'nditer' to iterate over multiple dimensions without needing loads of for loops!
for element in np.nditer(two_dim):
    print(element)

# Figuring out the index using 'ndenumerate'
for index, element in np.ndenumerate(two_dim):
    print(index, element)


# Expanding on Ellie's tutorial
# Testing out 'nditer' with a 3 dimensional array
three_dim = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for element in np.nditer(three_dim):
    print(element)
