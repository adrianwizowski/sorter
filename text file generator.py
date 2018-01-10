import random
position = ['A', 'B', 'C', 'D', 'E', 'F']
hangers = ['ADULT', 'KNIT', 'CLIP', 'JACKET', 'KIDS', 'SCRAP']


for i in range(0, 500):
    with open('hangers.txt', 'a') as the_file:
        the_file.write(random.choice(position)+str(random.randint(1,2))+random.choice(hangers)+'\n')
        i += 1

