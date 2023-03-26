# Input of data
name = str(input('Qual é o seu name: '))
mean = float(input('Média obtida: '))

# Creating a dictionary
studentInfo = {}

# Inserting elements in dictionary
studentInfo['name'] = name
studentInfo['mean'] = mean

# Verifying condition of the student
if studentInfo['mean'] >= 60:
    studentInfo['condition'] = 'AP'
else:
    studentInfo['condition'] = 'RP'

print(studentInfo)