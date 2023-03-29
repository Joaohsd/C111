# Importing numpy
import numpy as np

# Creating a numpy array of 1-D
arr = np.array([1,2,3])
print(arr)
# Verifying type of array created
print(type(arr))

# Creating a numpy array of 2-D
arr = np.array([
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
    ])
print(arr)
# Slicing to get 3,4,7 and 8 elements
# The second element (end) is exclusive
print(arr[:2,2:])

# Creating an array of zeros
arr = np.zeros(10)
print(arr)

# Creating an array of ones
arr = np.ones((3,3))
print(arr)

# Creating a sequential array
arr = np.arange(start=1, stop=13, step=1)
print(arr)

# Reshaping an array
# In this case, the array should be compatible with desired shape.
arr = np.arange(start=1, stop=13, step=1).reshape((3,4))
print(arr)

# Creating an array with linearly spaced
arr = np.linspace(start=0, stop=100, num=11)
print(arr)

# Concatenating Arrays
arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])

print(np.concatenate((arr1,arr2)))

# Attributes of array
arr = np.array([
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
    ])
print(arr.size)
print(arr.ndim)
print(arr.shape)