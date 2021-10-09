def multiplication_table(n,m):
    for i in range (1 , 11):
        print('\n')
        print(i , end=' ')
        for j in range(1 , m):
            print(i*j , end=' ')

n = int(input("enter n:"))
m = int(input("enter m:"))
multiplication_table(n,m)