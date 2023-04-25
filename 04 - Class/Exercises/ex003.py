import numpy as np

# Resetting seed in order to always generate the same random numbers
np.random.seed(10)

# Create an array with 16 random elements and reshaping it
arr = np.random.randint(low=1, high=50, size=16).reshape((4,4))

for i in range(arr.shape[0]):
    print(f'Mean of row {i} is:\t{np.mean(arr, axis=1)[i]}')
    print(f'Mean of column {i} is:\t{np.mean(arr, axis=0)[i]}')