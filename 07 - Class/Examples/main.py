import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

x = np.array([1,2,3,4])

y_1 = 2*x
y_2 = x*x

'''
#plt.plot(x, y_1, 's--r', x, y_2, 'o-.b', linewidth=3, markersize=10)
# Subplot (Numero de linhas, Numero de colunas, Índice do Grid)
plt.subplot(1,2,1)
plt.plot(x, y_1, 'r--')
plt.subplot(1,2,2)
plt.plot(x, y_2, 'b.-')
#plt.xlabel('X values')
#plt.ylabel('Y values')
plt.show()
'''

# Countries dataset Example

# Loading dataset
dataset = pd.read_csv('paises.csv', delimiter=';')

largestCountries = dataset.nlargest(n=6, columns='Area (sq. mi.)')

plt.scatter(largestCountries['Country'], largestCountries['GDP ($ per capita)'], s=largestCountries['Area (sq. mi.)']/5000)
plt.show()


