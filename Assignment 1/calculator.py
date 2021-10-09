import math
num1= int(input("enter the first num :"))
q = input("do u want to use any advanced operators? type y for yes and n for no :")
if q == 'y' :
    advanced_operator = input("enter advanced operator: ")
if advanced_operator == 'radical' :
    resault = print(math.sqrt(math.radians(num1)))
if advanced_operator == 'tan' :
    resault = print(math.tan(math.radians(num1)))
if advanced_operator == 'sin' :
    resault = print(math.sin(math.radians(num1)))
if advanced_operator == 'cos' :
    resault = print(math.cos(math.radians(num1)))
if advanced_operator == 'factorial' :
    resault = print(math.factorial(math.radians(num1)))

elif q == 'n' :
    num2= int(input("enter the second num :"))
    operator = input("enter an operator :")
if num2 == 0 :
    print("ERROR!")
elif operator == '+' :
    resault=print(num1+num2)
elif operator == '-' :
    resault=print(num1-num2)
elif operator == '/' :
    resault=print(num1/num2)
elif operator == '*' :
    resault=print(num1*num2)

