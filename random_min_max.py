import random as r
min=int(input("enter min>>"))
max=int(input("enter max>>"))
if min<max:
		list=[x for x in range(min,max+1)]
		print(r.choice(list))
else:
		a=min
		min=max
		max=a
		list2=[x for x in range(min,max+1)]
		print(r.choice(list2))