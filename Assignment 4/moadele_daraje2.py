a = float(input("enter a:"))
b = float(input("enter b:"))
c = float(input("enter c:"))

#def moadele(a , b , x):
delta = b**2-4*a*c
if delta >= 0:
    x1 = (-1 * b + delta **(0.5)/(2*a))
    x2 = (-1 * b - delta **(0.5)/(2*a))
    print('x1=' , x1)
    print('x2=' , x2)

else:
    print("error!")
    exit()