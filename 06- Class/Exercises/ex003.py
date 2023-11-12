import pandas as pd

# Loading dataset
dataset = pd.read_csv('paises.csv', delimiter=';')

# Showing head
print(dataset.head())

populationColumn = dataset['Population']
countryColumn = dataset['Country']
regionColumn = dataset['Region']

countryRegion = dataset[['Country', 'Region']]

populationFiltering = populationColumn == populationColumn.max()

print(f'Country: {countryColumn[populationFiltering].iloc[0]}')
print(f'Region: {regionColumn[populationFiltering].iloc[0]}')
