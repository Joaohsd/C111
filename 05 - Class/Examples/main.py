import numpy as np

np.random.seed(10)

# Generate 16 elements in range [1,10)
arr = np.random.randint(low=1, high=10, size=16).reshape((4,4))

# Show array
print(arr)

# Show odd elements of the array
print(arr[arr%2==1])

# Working with text in numpy
names = np.array(['Dudu', 'Paulo', 'Pedro', 'Leticia', 'Daniela'])

# Return index of positions in each element that constains 'e', return -1 if does not contain
print(np.char.find(names, 'e'))

# Using condition to get elements that contains 'e'
print(names[np.char.find(names, 'e') > 0])

# Loading dataset
dataset = np.loadtxt('space.csv', delimiter=';', encoding='utf-8', dtype=str)

# Show the first line of the dataset
print(dataset[0, :])

# Show companies that did spacial missions
print(dataset[1:, 1])

# Show the different companies that did spacial missions
print(np.unique(dataset[1:, 1]))

# Show how many missions were done by each company
print(np.unique(dataset[1:, 1], return_counts=True))
