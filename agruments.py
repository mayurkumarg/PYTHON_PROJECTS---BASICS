def lis(*argu):
	lis1=list(argu)
	len1=(len(lis1))
	lis2=[]
	len2=len(lis2)
	while len1>len2:
		lis2.append(lis1[len2])
		len2+=2
	print(lis2)
lis(1,2,3,4,5,6,7,8,9)