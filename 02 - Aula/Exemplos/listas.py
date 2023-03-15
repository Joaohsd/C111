# Listas no Python

nomes = ['Goku', 'Vegeta', 'Trunks', 'Gohan']

# CRUD em Listas

# nserindo um elemento
nomes.append('Pan')

# Atualizando um elemento
nomes[0] = 'Piccolo'

# Deletando um elemento

# Deletando pelo valor
nomes.remove('Trunks')

# Deletando pelo índice
nomes.pop(2)

print('New list: ', nomes)