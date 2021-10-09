def kmm_function(num1, num2):

    if num1 > num2:
        greater = num1
    else:
        greater = num2
    while True:
        if((greater % num1 == 0) and (greater % num2== 0)):
           kmm = greater
           break
        greater = greater + 1
    print(kmm)

n1 = int(input("enter the first number :"))
n2 = int(input("enter the second number :"))
kmm_function(n1,n2)

    