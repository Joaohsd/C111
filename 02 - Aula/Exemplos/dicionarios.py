# Dicionários no Python
pessoa = {
    'nome': 'Goku',
    'idade': 42
}

# Inserindo um elemento com chave 'sexo'
pessoa['sexo'] = 'M'
print(pessoa)

# Atualizando um elemento pela chave 'idade'
pessoa['idade'] = 40
print(pessoa)

# Deletando os elementos com as chaves 'nome' e 'sexo'
del pessoa['nome']
print(pessoa)
pessoa.pop('sexo')
print(pessoa)