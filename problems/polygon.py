previos_x=0
previous_y=0
perimeter=0
while True: 
    x=(input("enter the value of x coordinate: "))

    if x=="":
        break
    x=int(x)
    y=int(input("enter the value of y coordinate: "))
    if previos_x==0 and previous_y==0:
        perimeter+=0
    else:
        perimeter+= pow(((previos_x-x)**2)+(previous_y-y)**2,1/2)
    previos_x=x
    previous_y=y
print(perimeter)
    
    
 