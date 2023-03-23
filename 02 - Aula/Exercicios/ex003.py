nome = str(input('Qual é o seu nome: '))
media = float(input('Média obtida: '))

# Criando o dicionário
infoAluno = {}

# Inserindo os elementos no dicionário
infoAluno['nome'] = nome
infoAluno['media'] = media

if infoAluno['media'] >= 60:
    infoAluno['situacao'] = 'AP'
    print(infoAluno['situacao'])
else:
    infoAluno['situacao'] = 'RP'
    print(infoAluno['situacao'])

print(infoAluno)