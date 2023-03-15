# Working with lists in Python

names = ['Goku', 'Vegeta', 'Trunks', 'Gohan']

# CRUD in Lists

# Inserting an element
names.append('Pan')

# Updating an element
names[0] = 'Piccolo'

# Deleting an element

# Deleting by value
names.remove('Trunks')

# Deleting by index
names.pop(2)

print('New list: ', names)