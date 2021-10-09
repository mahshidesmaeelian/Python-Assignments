for i in range(10): 
    name = (input("enter your name:"))
    last_name = (input("enter your last name:"))
    math_grade = int(input("enter your math grade:"))
    sience_grade = int(input("enter your sience grade:"))
    english_grade = int(input("enter your english grade:"))
    average = (math_grade+sience_grade+english_grade)/3
    if average >= 17 :
        print("Great")
    if average < 17 and average >=  12 :
        print("Normal")
    if average < 12 :
        print("fail")
