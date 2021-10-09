def jadval (n , m):
    
    for j in range(m):
        if j%2==0:
            print('\n')
            for i in range(n):
                if i % 2 == 0:
                    print("*" , end="")
                else :
                    print("#" , end="")
        elif j%2!=0:
            print('\n')
            for i in range(n):
                if i % 2 == 0:
                    print("#" , end="")
                else :
                    print("*" , end="")

n = int(input("enter n:"))
m = int(input("enter m:"))
jadval(n , m)