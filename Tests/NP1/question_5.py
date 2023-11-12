import numpy as np

dataset = np.loadtxt('paises.csv', delimiter=';', encoding='utf-8', dtype=str)

print(f'First row: \n {dataset[0,:]}\n\n')

# Question 5
print('------ Question 5 ------')
regionColumn = dataset[1:, 1]
regionLAandCaribeFiltering = np.char.find(regionColumn,'LATIN AMER. & CARIB') >= 0

gdpColumn = dataset[1:,8].astype(np.float64)
gdpCountriesLAandCaribe = gdpColumn[regionLAandCaribeFiltering]
maxGdpLAandCaribe = np.max(gdpCountriesLAandCaribe)
posMaxGdpLAandCaribe = gdpCountriesLAandCaribe == maxGdpLAandCaribe

countriesColumn = dataset[1:,0]
countriesLAandCaribe = countriesColumn[regionLAandCaribeFiltering]

print(f'The biggest GDP in LA and Caribe is from {countriesLAandCaribe[posMaxGdpLAandCaribe]}')