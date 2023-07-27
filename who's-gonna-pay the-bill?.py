import random
last = int(input('how many people are there? '))
pp = input('insert the names of the people: (separated with a space)')
p = pp.split(' ')
n = int(random.randint(0,last))
o = (p [n])
print(f'{o} has to pay the bill, sorry friend')
