loja1 = {'Galaxy S20', 'Moto G7', 'Iphone 11', 'Iphone 12', 'Iphone 13'}
loja2 = {'Galaxy S20', 'Moto G8', 'Iphone 12', 'Iphone 13', 'Iphone 14'}

# Primeiro item
print('Modelos possíveis:',loja1.union(loja2))
# Segundo item
print('Modelos em ambas:',loja1.intersection(loja2))