first_side=(input("enter the first side :"))
second_side=(input("enter the second side :"))
third_side=(input("enter the third side :"))
if first_side < (second_side+third_side) or second_side < (first_side+third_side)  or third_side < (first_side+second_side) :
    print("you can draw a triangle :)")
else : 
    print("there's no way to draw a triangle with these dimentions!")