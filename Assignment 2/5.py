import random
while True:
    dice= random.randint(1 , 6)
    print("your random number is:" , dice)

    if dice == 6 :
        bonus= random.randint(1 , 6)
        print("your bonus is:" , bonus)
        break
    else:
        break