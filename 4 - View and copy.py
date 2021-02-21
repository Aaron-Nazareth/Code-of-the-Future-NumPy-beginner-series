# Tutorial 4

# Importing relevant modules
import numpy as np

# Copy
array = np.array([1, 2, 3, 4, 5])  # One dimensional array
copy = array.copy()  # Creates copy of the original array
array[0] = 10  # This changes the 1 to a 10
print(array)  # This prints the edited array
print(copy)  # This prints the backup copy of the original array

# View
array2 = np.array([1, 2, 3, 4, 5])  # One dimensional array
view = array2.view()  # Creates a view of the original array
array2[0] = 10  # This changes the 1 to a 10
print(array2)  # This prints the edited array
print(view)  # This prints the edited array

# Python to recall whether it is a copy or a view
print(view.base)
print(copy.base)
