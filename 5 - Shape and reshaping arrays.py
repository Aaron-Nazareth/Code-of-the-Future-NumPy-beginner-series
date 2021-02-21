# Tutorial 5

# Importing relevant modules
import numpy as np

# Shape of an array
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(array.shape)  # This will print (3, 3) because we have 3 elements and inside
# each of those elements are 3 more elements

# Notice what happens when we have different numbers of elements
# array2 = np.array([[1, 2, 3], [4, 5, 6, 7]])
# print(array.shape)  # Error as the elements are different sizes

# Reshaping arrays
# Let's suppose we have an array of student's ages and we have 3 students of each age.
students_ages = np.array([19, 19, 19, 20, 20, 20, 21, 21, 21])
# We also have their average exam score over the year
exam_score = np.array([57, 60, 65, 59, 63, 70, 65, 72, 75])
# Splitting up the exam score
exam_split = exam_score.reshape(3, 3)
print(exam_split)

# We can't reshape every single array!
# The 2 numbers we input into the reshape command must multiply together to create
# the number of elements within the original array.

# exam_split = exam_score.reshape(2, 4)
# print(exam_split)  # This wouldn't work as 9 elements cannot be split into a (2, 4) format

# Reshape into 3 dimensional
one_dim = np.array([1, 2, 3, 4, 5, 6])
three_dim = one_dim.reshape(2, 3, 1)
print(three_dim)
# This will take [1 2 3 4 5 6] and break it into 2 arrays, then inside those 2 arrays it will
# have 3 arrays of 1 element.
