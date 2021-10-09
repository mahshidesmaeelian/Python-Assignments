w = int(input("enter your current weight:"))
h = int(input("enter your current height:"))
h = h/100
BMI = w/(h**2)
if BMI <= 18.5 :
    print("underweight")
if BMI > 18.5 and BMI <= 24.9 :
    print("healthy/average")
if BMI > 25 and BMI <= 29.9  :
    print("overweight")
if BMI > 30 :
    print("fat")