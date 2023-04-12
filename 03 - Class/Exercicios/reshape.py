'''
    Nome: João Henrique Silva Delfino
    Curso: Engenharia de Computação
'''

import numpy as np

print('Exercise 1')
print('21 values linearly spaced between 0 and 1:')
arr = np.linspace(start=0, stop=1, num=21)
print(arr)

print('\nExercise 2')
even_1 = np.arange(start=0, stop=51, step=2)
print('Even values between 0 and 50:')
print(even_1)
even_2 = np.arange(start=100, stop=49, step=-2)
print('Even values between 100 and 50:')
print(even_2)

print('\nExercise 3')
print('Sorting even values between 0 and 50 in descending order:')
print(np.flip(np.sort(even_1)))
print('Sorting even values between 100 and 50 in descending order:')
print(np.flip(np.sort(even_2)))

print('\nExercise 4')
print('Reshaping an array with 3x4 to 1-D:')
arr_ones = np.ones((3,4)).reshape((12,))
print(arr_ones)

print('\nExercise 5')
arr_zeros = np.zeros((10,11))
print('Verifying 1-D shape of an 2-D array:')
result = 'even' if (arr_zeros.shape[0] * arr_zeros.shape[1]) % 2 == 0 else 'odd'
print('Number of elements of the 1-D array will be', result)