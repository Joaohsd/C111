import numpy as np

# Resetting seed in order to always generate the same random numbers
np.random.seed(5)

# Create an array with 10 elements
arr = np.random.uniform(low=-1, high=1, size=10).astype(np.float32)

# Multiplying by 100 and discarding decimal values
arrInt = np.int32(arr * 100)

print(arrInt)
