import pandas as pd

# Loading dataset
dataset = pd.read_csv('paises.csv', delimiter=';')

# Showing head
print(dataset.head())

literacyColumn = dataset['Literacy (%)']
print(f'Mean Literacy in the world is: {literacyColumn.mean()}')
