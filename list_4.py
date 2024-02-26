list=[]
for x in range(1,int(input("enter no.of element to add in your list>>"))+1):
    inp=input("enter the values for u r list>>")
    list.append(inp)
print("your list\n",list)
inp2=input("do u want access this element>>yes/no:")
if inp2.lower()=="yes":
    try:
        print("your accesed value is>>",list[int(input("enter the index value"))])
    except Exception as e:
        print(e)

list2=[]
count=0
for x in list:
    if x.isnumeric():
        x=int(x)
        count+=1
        list2.append(x)
    else:
        list2.append(x)

if count>0:
    print("u r list contains number in string format")
    inp3=input('do want to convert it to int()>>yes/on')
    if inp3.lower()=="yes":
        print("your list>>",list2)
print("!this progarm ends here!")