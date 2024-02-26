def std_1():
	detels=[f"name:{name}","reg_no:105me21045",'year:2nd year','sem:3rd sem']
	for x in detels:
		print(x)
def std_2():
	detels=[f"name:{name}","reg_no:105me210",'year:3nd year','sem:5th sem']
	for x in detels:
		print(x)
name=input('enter student name>>')
if name=='sharath':
	print(std_1())
elif name=='xyz':
	print(std_2())
else:
	print(f'no student regesterd with this name>>{name}')