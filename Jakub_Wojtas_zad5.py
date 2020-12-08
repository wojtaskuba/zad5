names = ['Damian', 'Ola', 'Barbara', 'Robert']
names = [name[0] for name in names]
print(names)



print('\ndruga część\n')



import random

i = random.randrange(1, 10)

list = [[random.randrange(1, 10) for element in range(4)] for y in range(5)]
print(list)

