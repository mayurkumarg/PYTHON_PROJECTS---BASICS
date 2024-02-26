print("•"*18,"IMDB","•"*18)
inp1=int(input("enter no.of people rating this series:>>"))
if inp1<0:
	print(f"{inp1} negitive number")
print("How would you rate STRANGER THINGS out of 10")
list=[]
for x in range(1,inp1+1):
	rate=float(input(f"{x} person rating ⭐>>"))
	list.append(rate)
	if rate>10:
		print(f"{rate} this no.is out of range")
		break
	elif rate<0:
		print(f"this {rate} is negetive number ")
		break
a=0
for x in list:
	a=a+x
if rate<=10 and rate>=0:
	print("\nIMDB RATING>>",a/inp1)