import numpy as np

dataset = np.loadtxt('paises.csv', delimiter=';', encoding='utf-8', dtype=str)

print(f'First row: \n {dataset[0,:]}\n\n')

# Question 4
print('------ Question 4 ------')
regionColumn = dataset[1:, 1]
regionNAFiltering = np.char.find(regionColumn,'NORTHERN AMERICA') >= 0

countriesColumn = dataset[1:,0]
numCountriesNA = len(countriesColumn[regionNAFiltering])

print(f'Number of countries from NORTHERN AMERICA: {numCountriesNA}')