second = int(input("enter seconds: "))
minute=0
hour = 0

while True:
    
    if second>=3600:
        second=second-3600
        hour=hour+1

    elif second>=60:
        second=second-60   
        minute=minute+1 
        
    else:
        break
       
print(hour,":",minute,":",second)     