#paskal = [1]

n = int(input("enter the column number:"))
paskal = [[1 for i in range (n)] for j in range(n) ] 

for i in range(n):
    for j in range(1, i):
        paskal[i][j] = paskal[i-1][j] + paskal[i-1][j-1]

for i in range(n):
    for j in range(i+1):
        print(paskal[i][j] , end= '')
    print()

        
        
#print(paskal)