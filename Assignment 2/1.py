total = 0
while True :
    num = input("enter a number: ")
    if num == "exit" :
        break
    total = (int(num) + total)

print (total)