def multiplication(x,y):
    result = {}
    result['s']= x['s'] * y['s']
    result['m']= x['m'] * y['m']
    return result 
def addition(x,y):
    result = {}
    result['s']=x['s']* y['m'] + y['s'] * x['m']
    result['m']= x['m'] * y['m']
    return result

def division(x,y):
    result = {}
    result['s']= x['s'] * y['m']
    result['m']= x['m'] * y['s']
    return result

def subtraction(x,y):
    result = {}
    result['s']=x['s']* y['m'] - y['s'] * x['m']
    result['m']=x['m'] * y['m']
    return result

def show(x):
    print(x['s'])
    print('--')
    print(x['m'])
    print()

def show_menu():
    print('1-multiplication' , '\n' ,'2-addition' , '\n' , '3-division' , '\n' , '4-subtraction')

while True:
    s1 = int(input('soorate kasre aval ra vared konid:'))
    m1 = int(input('makhraje kasre aval ra vared konid:'))
    s2 = int(input('soorate kasre dovom ra vared konid:'))
    m2 = int(input('makhraje kasre dovom ra vared konid:'))
    a = {'s':s1 , 'm':m1}
    b = {'s':s2 , 'm':m2}
    show_menu()
    answer = int(input('choose one of the options:'))
    if answer==1:
        c = multiplication(a,b)
        show(c)
    if answer==2:
        d=addition(a,b)
        show(d)
    if answer==3:
        e=division(a,b)
        show(e)
    if answer==4:
        f=subtraction(a,b)
        show(f)