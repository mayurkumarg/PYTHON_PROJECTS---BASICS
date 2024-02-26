list=[x for x in range(1,21)]
list2=list[::-1]
list3=[]
a=0
len=len(list)
while len>a:
	aa,bb=list[a] ,list2[a]
	list3.append(aa)
	list3.append(bb)
	a+=2
print(list3)