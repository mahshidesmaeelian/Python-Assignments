import random
numbers_list=[]
n= int(input("tedad adad ra vared konid:"))

for i in range(n):
    random_number = random.randint(1,20)
    if random_number not in numbers_list :
        numbers_list.append(random_number)

    elif random_number in numbers_list:
        break


print(numbers_list)