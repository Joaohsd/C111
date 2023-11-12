import numpy as np

dataset = np.loadtxt('paises.csv', delimiter=';', encoding='utf-8', dtype=str)

print(f'First row: \n {dataset[0,:]}\n\n')

# Question 2
print('------ Question 2 ------')
regionColumn = dataset[1:, 1]
regions = np.unique(regionColumn)
print(regions)
print(f'Number of different regions: {len(regions)}')