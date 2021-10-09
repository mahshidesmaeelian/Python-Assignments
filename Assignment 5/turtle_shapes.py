import turtle
t = turtle.Pen()

side_number = 3
t.penup()
#turtle.goto(0 , 50)
for i in range(10):
    for j in range(side_number):
        t.pendown()
        t.forward(100)
        t.right(360/side_number)
    side_number = side_number+1
    t.penup()
    
        
        

t.done()