campeoes = ['Real Madrid', 'Liverpool', 'Chelsea', 'Bayern de Munique', 'Barcelona']

# Item A
print(campeoes[:3])
# Item B
print(campeoes[-2:])
# Item D
print(campeoes.index('Barcelona')+1) # Posição real, por isso o +1
# Item C
campeoes.sort()
print(campeoes)