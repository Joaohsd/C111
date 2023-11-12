import numpy as np

dataset = np.loadtxt('paises.csv', delimiter=';', encoding='utf-8', dtype=str)

print(f'First row: \n {dataset[0,:]}\n\n')

# Question 3
print('------ Question 3 ------')
literacyColumn = dataset[1:,9].astype(np.float64)
print(f'Mean literacy in the world is {np.mean(literacyColumn)}%')