import numpy as np

# Resetting seed in order to always generate the same random numbers
np.random.seed(10)

# Create an array with 16 random elements and reshaping it
arr = np.random.randint(low=1, high=50, size=16).reshape((4,4))

values = np.unique(arr, return_counts=True)[0]
numTimes = np.unique(arr, return_counts=True)[1]

# Show number of times for each value
for i in range(len(values)):
    print(f'Number of times for value {values[i]} is {numTimes[i]}')

# Show numbers that appear just 2 times
print(f'Numbers that appear just 2 times are: {values[numTimes==2]}')