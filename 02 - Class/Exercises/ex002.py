# Sets of models for both stores 1 and 2
store1 = {'Galaxy S20', 'Moto G7', 'Iphone 11', 'Iphone 12', 'Iphone 13'}
store2 = {'Galaxy S20', 'Moto G8', 'Iphone 12', 'Iphone 13', 'Iphone 14'}

# First item
print('All possible models:',store1.union(store2))
# Second item
print('Models in both:',store1.intersection(store2))