numbers =[]
verified_numbers=0
n = int(input("enter numbers list length:"))
for j in range(n):
    input_num=int(input("enter a number: "))
    numbers.append(input_num)
    
for i in range (len(numbers)-1): 
    if (input_num[i] < input_num[i+1]):
        verified_numbers=verified_numbers+1
    else :
        verified_numbers=verified_numbers-1

if verified_numbers == len(numbers):
    print("they're sorted")
else :
    print("the numbers are not sorted!") 