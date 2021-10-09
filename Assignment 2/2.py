hour = int(input("enter the hour: "))
minute = int(input("enter minutes: "))
second = int(input("enter seconds: "))
temp = 0
for i in range(hour):
    temp = temp+3600
for j in range(minute):
    temp= temp+60
print(temp+second)



