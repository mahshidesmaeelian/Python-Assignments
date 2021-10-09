class Clock:
    def __init__(self,h1,m1,s1,h2,m2,s2):
        self.hour1 = h1
        self.min1 = m1
        self.sec1 = s1

        self.hour2 = h2
        self.min2 = m2
        self.sec2 = s2

    def times_addition(self):
        self.result_h= self.hour1 + self.hour2
        self.result_m= self.min1 + self.min2
        self.result_s= self.sec1 + self.sec2

        if self.result_s >= 60:
            self.result_s -= 60
            self.result_m += 1

        if self.result_m >= 60:
            self.result_m -= 60
            self.result_h += 1
        
        print(self.result_h , ':' , self.result_m , ':' , self.result_s)


    def times_subtraction(self):
        self.result_h= self.hour1 - self.hour2
        self.result_m= self.min1 - self.min2
        self.result_s= self.sec1 - self.sec2

        if self.result_m >= 60:
            self.result_h -= 1
            self.result_m += 60

        if self.result_s >= 0:
            self.result_m -= 1
            self.result_s += 60
        
        print(self.result_h , ':' , self.result_m , ':' , self.result_s) 


    def convert_seconds_to_hours(self,a):
        while True:
            if a >= 3600:
                a -= 3600
                self.result_h = self.result_h+1
            elif a >= 60:
                a -= 60
                self.result_m = self.result_m+1
            else:
                self.result_s = a
                break
        print(self.result_h , ':' , self.result_m , ':' , self.result_s)   


    def convert_hours_to_seconds(self , hour , minute ,second): 
        temp = 0
        for i in range(hour):
            temp = temp+3600
        for j in range(minute):
            temp= temp+60
        print(temp+second) 


    def show_menu():
        print('1-times addition' , '\n' ,'2-times subtraction' , '\n ', '3-convert time to seconds' , '\n' , '4-convert seconds to time' , '\n' , '5-break' )

while True:
    print('time 1' , ' \n' , ('-')*10)
    h1 = int(input('enter hour:'))
    m1 = int(input('enter minutes:'))
    s1 = int(input('enter seconds:'))

    print()

    print('time 2' , ' \n' , ('-')*10)
    h2 = int(input('enter hour:'))
    m2 = int(input('enter minutes:'))
    s2 = int(input('enter seconds:'))



    time1 = Clock(h1,m1,s1,h2,m2,s2)

    Clock.show_menu()
    option = int(input('choose one of the options above:'))
    if option == 1: 
        time1.times_addition()
        
    elif option == 2: 
        time1.times_subtraction()

    elif option == 3: 
        seconds = int(input('seconds:'))
        time1.convert_seconds_to_hours(seconds)

    elif option == 4: 
        hour = int(input("enter the hour: "))   
        minute = int(input("enter minutes: "))
        second = int(input("enter seconds: "))
        time1.convert_hours_to_seconds(hour,minute,second)

    elif option == 5:
        exit()