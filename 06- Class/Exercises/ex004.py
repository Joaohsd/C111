import pandas as pd

# Loading dataset
dataset = pd.read_csv('paises.csv', delimiter=';')

# Showing head
print(dataset.head())

coastLineColumn = dataset['Coastline (coast/area ratio)']
countryColumn = dataset['Country']

coastLineFiltering = coastLineColumn == 0

countryColumn[coastLineFiltering].to_csv('noCoast.csv', sep=';', header=False)