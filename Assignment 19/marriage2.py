import random

boys = ['ali', 'reza', 'yasin', 'benyamin', 'mehrdad', 'sajjad', 'aidin', 'shahin']
girls = ['sara', 'zari', 'neda', 'homa', 'eli', 'goli', 'mary', 'mina']
marriage = []

random.shuffle(boys)
random.shuffle(girls)

for i in range(len(boys)):
    marriage.append(boys[i] + ' has been married to ' + girls[i])

print(marriage)
