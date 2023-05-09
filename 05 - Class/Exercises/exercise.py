import numpy as np

# Loading dataset
dataset = np.loadtxt('space.csv', delimiter=';', encoding='utf-8', dtype=str)

# Show header
print(f'Name of columns: {dataset[0,:]}')

# Question 1
statusColumn = dataset[1:,7]
missionSuccess = dataset[1:,7]=='Success'
filteredStatusColumn = statusColumn[missionSuccess]
print(f'Number of successed missions was {len(filteredStatusColumn)}')

# Question 2
costColumn = dataset[1:, 6].astype(np.float64)
costAvailable = costColumn > 0
filteredCostColumn = costColumn[costAvailable]
print(f'Mean cost was {np.mean(filteredCostColumn)}')

# Question 3
locationColumn = dataset[1:, 2]
USAPositionsInStrings = np.char.find(locationColumn, 'USA')
USAMissions = locationColumn[USAPositionsInStrings >= 0]
print(f'Number of missions done by USA: {len(USAMissions)}')

# Question 4
companyColumn = dataset[1:, 1]
spaceXLines = np.char.find(companyColumn, 'SpaceX') >= 0
spaceXCosts = costColumn[spaceXLines]
maxCostSpaceX = max(spaceXCosts)
print(f'Maximum cost of mission done by SpaceX: {maxCostSpaceX}')

# Question 5
companiesName, numberMissions = np.unique(companyColumn, return_counts=True)
print('Companies and number of missions done:')
for name, numMissions in zip(companiesName, numberMissions):
    print(f'\tThe company {name} did {numMissions} spacial missions')