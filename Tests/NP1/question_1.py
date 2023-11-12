import numpy as np

dataset = np.loadtxt('paises.csv', delimiter=';', encoding='utf-8', dtype=str)

print(f'First row: \n {dataset[0,:]}\n\n')

# Question 1 
print('------ Question 1 ------')
print(dataset[1:,:4])