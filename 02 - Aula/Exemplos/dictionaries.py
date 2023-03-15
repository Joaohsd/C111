# Working with Dictionaries in Python
person = {
    'name': 'Goku',
    'age': 42
}

# Inserting an element with key 'sex'
person['sex'] = 'M'
print(person)

# Updating an element by key 'age'
person['age'] = 40
print(person)

# Deleting an element by key 'nome' e 'sex'
del person['name']
print(person)
person.pop('sex')
print(person)