import random


text = list('가나다라마바사아자차카타파하')

with open('info.csv', 'w') as file:
    
    for i in range(1000):
        name = random.choice(text) + random.choice(text)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 180)
        
        file.write('{}, {}, {}\n'.format(name, weight, height))