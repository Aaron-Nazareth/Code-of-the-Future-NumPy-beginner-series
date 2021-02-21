# Tutorial 1

# Importing relevant modules
import numpy as np

# Creating a simple array
array = np.array([1, 2, 3, 4, 5])
print(array)

# Let's explore the different size dimensions

# Zero dimensional array
zero_dim = np.array(3617940738)
print(zero_dim)

# One dimensional array
one_dim = np.array([1, 2, 3])
print(one_dim)

# Two dimensional array
two_dim = np.array([[1, 2, 3], [4, 5, 6]])
print(two_dim)

# Three dimensional array
three_dim = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(three_dim)

# Finding the dimension of a given array
print(three_dim.ndim)
print(two_dim.ndim)

# Give an array any dimension you want
new_array = np.array([1, 2], ndmin=5)
print(new_array)
