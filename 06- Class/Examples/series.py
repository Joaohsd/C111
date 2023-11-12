import pandas as pd

# Creating a dictionary
dic = {'a':10, 'b':20, 'c':30}

# Creating a series using the dictionary above
s1 = pd.Series(dic)

# Series and type
print(s1)
print(type(s1))

# Getting an element from Series at position index
print(s1['b'])

# Creating second series 
s2 = pd.Series({'a':10, 'c':50, 'd':80})

# Summing series element by element
print(s1 + s2)

# Summing series element by element filling values
# with 0
print(s1.add(s2, fill_value=0))

# Slicing series
print(s1[['b', 'c']])

# Conditional in Series
print(s1[s1 >= 20])
