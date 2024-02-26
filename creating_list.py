in1=int(input("enter the number of elements>>>"))
no1=0
el=[]
while no1<in1:
	in2=input("enter first element>>")
	el.append(in2)
	no1+=1
a=el
b=0
aa=len(a)
c=[]
bb=0
while aa>bb:
	c.append(a[b])
	b=b+2
	bb=len(c+c)
print(("your list created succesfully\n"),a)
print("even form skip\n",c)