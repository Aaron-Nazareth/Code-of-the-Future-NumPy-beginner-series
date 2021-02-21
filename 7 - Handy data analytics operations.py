# Tutorial 7

# Importing relevant modules
import numpy as np

# Operations that come in handy for data analysis
one_dim = np.array([1, 2, 3, 4, 5])
two_dim = np.array([[1, 2, 3], [4, 5, 6]])

# Summations
print(sum(one_dim))  # Produces sum of values within 'one_dim'
print(sum(two_dim))  # Produces sum of arrays
print(one_dim.sum())  # Produces sum of values within 'one_dim'
print(two_dim.sum())  # Produces sum of values within 'two_dim'

# Maximum and minimum
print(one_dim.min())
print(one_dim.max())
print(two_dim.min())
print(two_dim.max())

# We can add elements in each row and column
two_dim2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(two_dim2)

# Summing elements within each column
print(two_dim2.sum(axis=0))

# Summing elements within each row
print(two_dim2.sum(axis=1))
