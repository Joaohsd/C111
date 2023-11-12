import pandas as pd

# Loading dataset
dataset = pd.read_csv('paises.csv', delimiter=';')

# Showing head
print(dataset.head())

regionNames = dataset.iloc[:, 1]
regionFiltering = regionNames.str.contains("OCEANIA")
countryNames = dataset.iloc[:, 0]
oceaniaCountries = countryNames[regionFiltering]

# Show countries from OCEANIA
print(oceaniaCountries)
print(oceaniaCountries.size)
