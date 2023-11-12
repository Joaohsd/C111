import pandas as pd
import numpy as np

np.random.seed(10)

df = pd.DataFrame(data=np.random.randint(1, 50, [5, 4]), 
                  index=['A', 'B', 'C', 'D', 'E'], 
                  columns= ['X', 'Y', 'Z', 'W'])
# DataFrame
print(df)

# Slicing DataFrame for getting two columns
print(df[['X','W']])

# Slicing with loc (categorical indexes)
print(df.loc[['A', 'B'], ['X', 'Y', 'Z']]) # First list of rows, then list of columns

# Slicing with iloc (numerical indexes)
print(df.iloc[:2, :3])

# Loading dataset
dataset = pd.read_csv('paises.csv', delimiter=';')

# HEAD
print(dataset.head(10))

# TAIL
print(dataset.tail(10))

# Columns
print(dataset.columns)