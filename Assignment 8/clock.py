def show_menu():
    print('1-time operation' , '\n' ,'2-time convertion')

def show_operation_options():
    print('1-times addition' , '\n' ,'2-times subtraction' )

def show_convert_options():
    print('3-convert time to seconds' , '\n' , '4-convert seconds to time')

def times_addition(t1,t2):
    result = {}
    result['h']= t1['h'] + t2['h']
    result['m']= t1['m'] + t2['m']
    result['s']= t1['s'] + t2['s']

    if result['s'] >= 60:
        result['s'] -= 60
        result['m'] += 1

    if result['m'] >= 60:
        result['m'] -= 60
        result['h'] += 1

    return result

def times_subtraction(t1,t2):
    result = {}
    result['h']= t1['h'] - t2['h']
    result['m']= t1['m'] - t2['m']
    result['s']= t1['s'] - t2['s']

    if result['m'] >= 0 :
        result['h'] -= 1
        result['m'] += 60

    if result['s'] >= 0:
        result['m'] -= 1
        result['s'] += 60

    return result
def convert_seconds_to_hours(a):
    result = {'h': 0, 'm': 0, 's': 0}
    while True:
        if a >= 3600:
            a -= 3600
            result['h'] = result['h']+1
        elif a >= 60:
            a -= 60
            result['m'] = result['m']+1
        else:
            result['s'] = a
            break
    print(result)
    

def convert_hours_to_seconds():
    hour = int(input("enter the hour: "))
    minute = int(input("enter minutes: "))
    second = int(input("enter seconds: "))
    temp = 0
    for i in range(hour):
        temp = temp+3600
    for j in range(minute):
        temp= temp+60
    print(temp+second)
    
   
        
def show_time(x):
    print(x['h'] , ':' , x['m'] , ':' , x['s'])



while True:
    show_menu()
    answer1 = int(input('choose one of the options:'))
    if answer1 == 1:
        print('time 1' , ' \n' , ('-')*10)
        h1 = int(input('enter hour:'))
        m1 = int(input('enter minute:'))
        s1 = int(input('enter second:'))

        print()

        print('time 2' , ' \n' , ('-')*10)
        h2 = int(input('enter hour:'))
        m2 = int(input('enter minute:'))
        s2 = int(input('enter second:'))

        time1 = {'h': h1 , 'm': m1 , 's':s1}
        time2 = {'h': h2 , 'm': m2 , 's':s2}

        show_operation_options()
        answer2 = int(input('choose one of the options:'))
        if answer2 == 1:
            time3 =times_addition(time1,time2)
            show_time(time3)

        if answer2 == 2:
            time4 =times_subtraction(time1,time2)
            show_time(time4)


    if answer1 == 2:
        show_convert_options()

        answer3 = int(input('choose one of the options:'))

        if answer3 == 3:
            s1 = int(input('enter second:'))
            convert_seconds_to_hours(s1)  

        if answer3 == 4:
            convert_hours_to_seconds()
            
    

    

    

    
