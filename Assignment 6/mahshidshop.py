from enum import Flag
from pyfiglet import Figlet
import qrcode
Flag = 1
def ShowMenu():
    print('1-Add product')
    print('2-edit product')
    print('3-search by name')
    print('4-Qr code')
    print('5-remove product')
    print('6-buy product')
    print('7-exit store')


product_list =[]
cart = []

openfile=open('database.txt' , 'r')
data = openfile.read()
templist = data.split('\n')
for i in range(len(templist)):
    product_info=templist[i].split(',')
    product_dict={}
    product_dict['code']=product_info[0]
    product_dict['name']=product_info[1]
    product_dict['price']=product_info[2]
    product_dict['amount']=product_info[3]
    product_list.append(product_dict)    
 

def product_qrcode(qr_input):
    for i in range(len(product_list)):
        if product_qrcode==product_list[i]['products_code']:
            img = qrcode.make(product_list[i])
            img.save('qrcode.png')
            break
    

f = Figlet(font='standard')
print(f.renderText('MahshidStore'))

               

while True:

    ShowMenu() 
    options = int(input('choose one of the options above: '))

    if options == 1:
        product_dict['code']=input(('Enter products code: '))
        product_dict['name']=input(('Enter the name of product:'))
        product_dict['price']=input(('Enter the price of product:'))
        product_dict['amount']=int(input(('Enter the amount of the product: ')))
        product_list.append(product_dict)
        print(product_list)
        

    elif options == 2:
        edit_list = input('which product you want to edit?')
        edit_item = input('which item you want to edit?')
        replace_info = input("enter new info:")
        product_list[edit_list][edit_item].append(replace_info)
        print(product_list)
        
                
    elif options == 3 and Flag==1 :
        search_name = input(('Enter products name: '))
        for i in range(len(product_list)):
            if search_name == product_list[i]['name']:
                print(product_list[i]['name'])
                Flag == 0
            
            else:
                print('this list dosent contain the name')

    elif options == 4:
        qr_input = input(('Enter products code: '))
        product_qrcode(qr_input)


    elif options == 5 :
        remove_item = input(('Enter products name: '))
        for i in range(len(product_list)):
            if remove_item==product_list[i]['name']:
                del product_list[i]
        print(product_list)    
             
    

    elif options == 6:
        while True:
            buy_product_code = input(('Enter products code: '))
            for i in range(len(product_list)):
                if buy_product_code == product_dict[i]['code']:

                    buy_product_number= int(input('how many of this product you want to buy?'))

                    if product_list[i]['amount'] >= buy_product_number:
                        count = product_list[i]['amount']-buy_product_number    
                        final_price = (product_list[i]['price']) * buy_product_number
                        cart.append(product_list[i])
                        openfile=open('factor.txt' , 'a')
                        factor = openfile.write( cart , final_price)
                        print(factor)
                        
                    else:
                        print('sorry!this product is out of stock')

                elif buy_product_code not in product_list[i]['code']:
                    print('sorry!this product is out of stock')
    elif options == 7:
        exit