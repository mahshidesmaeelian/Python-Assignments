def BMM(num1,num2):
    if num1==num2:
        print('BMM=',num1)
    elif num1<num2:
        print(num1 ,'<' ,num2)
    else:
        r=num1/num2
        t=num2*r
        if num1==t:
            print('BMM=',num2)
        else:
            b2=num1-t
            num1=num2
            BMM(num1,num2*2)
num1=input('num1=')
num2=input('num2=')
BMM(int(num1),int(num2))