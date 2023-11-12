'''
    João Henrique Silva Delfino
    GEC
    1662
'''

import numpy as np

dataset = np.loadtxt('paises.csv', delimiter=';', encoding='utf-8', dtype=str)

print(f'First row: \n {dataset[0,:]}\n\n\n')

# Question 1 
print('------ Question 1 ------')
print(dataset[1:,:4])

# Question 2
print('------ Question 2 ------')
regionColumn = dataset[1:, 1]
regions = np.unique(regionColumn)
print(regions)
print(f'Number of different regions: {len(regions)}')

# Question 3
print('------ Question 3 ------')
literacyColumn = dataset[1:,9].astype(np.float64)
print(f'Mean literacy in the world is {np.mean(literacyColumn)}%')

# Question 4
print('------ Question 4 ------')
regionNAFiltering = np.char.find(regionColumn,'NORTHERN AMERICA') >= 0
countriesColumn = dataset[1:,0]
numCountriesNA = len(countriesColumn[regionNAFiltering])
print(f'Number of countries from NORTHERN AMERICA: {numCountriesNA}')

# Question 5
print('------ Question 5 ------')
regionLAandCaribeFiltering = np.char.find(regionColumn,'LATIN AMER. & CARIB') >= 0

gdpColumn = dataset[1:,8].astype(np.float64)
gdpCountriesLAandCaribe = gdpColumn[regionLAandCaribeFiltering]

maxGdpLAandCaribe = np.max(gdpCountriesLAandCaribe)
posMaxGdpLAandCaribe = gdpCountriesLAandCaribe == maxGdpLAandCaribe
print(posMaxGdpLAandCaribe)

countriesLAandCaribe = countriesColumn[regionLAandCaribeFiltering]

print(f'The biggest GDP in LA and Caribe is from {countriesLAandCaribe[posMaxGdpLAandCaribe][0]}')