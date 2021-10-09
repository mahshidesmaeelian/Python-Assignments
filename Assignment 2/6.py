fibonachi = []
n = int(input("enter fibonachi number:"))

for i in range(n):
    if i>1 and i != 0:
        fibonachi.append(fibonachi[i-1]+fibonachi[i-2])
    elif i==0 or i ==1 :
        print("error")
    
print(fibonachi)