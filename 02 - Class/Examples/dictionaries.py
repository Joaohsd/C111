# Dictionaries in Python
person = {
    'name': 'Goku',
    'age': 42
}

# Inserting an element with key 'sex'
person['sex'] = 'M'
print(person)

# Inserting an element with key 'sex'
person['age'] = 40
print(person)

# Deleting elements with key 'name' and 'sex'
del person['name']
print(person)

person.pop('sex')
print(person)