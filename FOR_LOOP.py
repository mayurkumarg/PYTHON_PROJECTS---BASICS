# FOR LOOPS:

#EXAMPLE:1
name="mayur kumar"
for i in name:
    print(i)
    if (i==" "):
        print("this is surname")

#EXAMPLE:2
list=["RED","BLUE","YELLOW","GREEN"]
for color in list:
    print(color)
    for i in color:
        print(i)

#EXAMPLE:3
for i in range(5,20,2):#range(start,stop,step)
    print(i)