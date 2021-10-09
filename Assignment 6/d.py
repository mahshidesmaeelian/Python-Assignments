product_list =[]
cart = []

openfile=open('database.txt' , 'r')
data = openfile.read()
templist = data.split('\n')
print(templist)
for i in range(len(templist)):
    product_info=templist[i].split(',')  
    product_dict={}
    product_dict['code']=product_info[0]
    product_dict['name']=product_info[1]
    product_dict['price']=product_info[2]
    product_dict['amount']=product_info[3]
    product_list.append(product_dict) 
print(product_list)

