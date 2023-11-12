import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr)
print(arr.shape)

# Random numbers with random module
np.random.seed(5)
print(np.random.rand(5))
arr = np.random.randint(low=1, high=10, size=10)
print(arr)
# Removing repeated elements
print('Array without repeated elements:',np.unique(arr))
# Getting number of repetition for each element
print('Array without repeated elements and the number of repetitions for each element:',np.unique(arr, return_counts=True))

# Random numbers with random module
np.random.seed(5)
arr1 = np.random.randint(low=1, high=10, size=10)
# Random numbers with random module
np.random.seed(10)
arr2 = np.random.randint(low=1, high=10, size=10)
# Showing arrays
print(arr1)
print(arr2)
# Adding two arrays
print(arr1 + arr2)
# Multiplying two arrays
print(arr1 * arr2)

# Mean of array
print(np.mean(arr1))
# Median of array
print(np.median(arr1))
# Sum of array elements
print(np.sum(arr1))

# Creating an numpy array
arr = np.array([
        [1 , 2, 3],
        [4 , 5, 6],
        [7 , 8, 9]
    ])
print(arr)
# Sum of elements of second column
print(arr.sum(axis=0)[1]) # axis 0: columns
# Sum of elements of first row
print(arr.sum(axis=1)[0]) # axis 1: rows
# Division
print(arr/10)

# Conditional slicing
# Slicing odd elements
print(arr % 2 == 1) # Returns an array like arr, but boolean
print(arr[arr % 2 == 1])