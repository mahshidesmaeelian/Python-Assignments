class Fraction: 
   
    def __init__(self,s1,m1,s2,m2):
        self.kasr1_soorat= s1
        self.kasr1_makhraj= m1

        self.kasr2_soorat= s2
        self.kasr2_makhraj= m2

    def multiplication(self):
        result_s= self.kasr1_soorat * self.kasr2_soorat
        result_m= self.kasr1_makhraj * self.kasr2_makhraj
        print(result_s)
        print('--') 
        print(result_m)
        print()
        return result_s , result_m 
        
        

    def addition(self):
        result_s=self.kasr1_soorat* self.kasr2_makhraj + self.kasr2_soorat * self.kasr1_makhraj
        result_m= self.kasr1_makhraj * self.kasr2_makhraj
        print(result_s)
        print('--') 
        print(result_m)
        print()
        return result_s , result_m

    def division(self):
        result_s= self.kasr1_soorat * self.kasr2_makhraj
        result_m= self.kasr1_makhraj * self.kasr2_soorat
        print(result_s)
        print('--') 
        print(result_m)
        print()
        return result_s , result_m

    def subtraction(self):
        result_s=self.kasr1_soorat* self.kasr2_makhraj - self.kasr2_soorat * self.kasr1_makhraj
        result_m=self.kasr1_makhraj * self.kasr2_makhraj
        print(result_s)
        print('--') 
        print(result_m)
        print()
        return result_s , result_m

    def show_menu():
        print('1-multiplication' , '\n' ,'2-addition' , '\n' , '3-division' , '\n' , '4-subtraction', '\n' , '5-exit')


while True:
    s1 = int(input('soorate kasre aval ra vared konid:'))
    m1 = int(input('makhraje kasre aval ra vared konid:'))
    s2 = int(input('soorate kasre dovom ra vared konid:'))
    m2 = int(input('makhraje kasre dovom ra vared konid:'))

    kasr1= Fraction(s1,m1,s2,m2)

    Fraction.show_menu()
    option = int(input('choose one of the options above:'))
    if option == 1: 
        (kasr1.multiplication())
        
    elif option == 2: 
        (kasr1.addition())

    elif option == 3: 
        (kasr1.subtraction())

    elif option == 4: 
        (kasr1.division())

    elif option == 5:
        exit()


