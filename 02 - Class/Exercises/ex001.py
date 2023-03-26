# Ranking of FIFA Club World Cup
champions = ['Real Madrid', 'Liverpool', 'Chelsea', 'Bayern de Munique', 'Barcelona']

# Item A
print('Top three:',champions[:3])
# Item B
print('Fourth and Fifth places:',champions[-2:])
# Item D
print('The rank of Barcelona:',champions.index('Barcelona')+1) # Real rank of Barcelona: index + 1
# Item C
champions.sort()
print('Alphabetical ordered:',champions)