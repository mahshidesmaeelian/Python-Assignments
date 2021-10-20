import random

boys = ['ali', 'reza', 'yasin', 'benyamin', 'mehrdad', 'sajjad', 'aidin', 'shahin']
girls = ['sara', 'zari', 'neda', 'homa', 'eli', 'goli', 'mary', 'mina']

marriage = boys[random.randint(0,(len(boys)-1))] + ' has been married to '+ girls[random.randint(0,(len(girls)-1))]

print(marriage)
