a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
b=a[::-1]
c=[]
aa=len(a)
bb=len(b)
cc=len(c)
while cc<aa:
    c.append(a[cc])
    c.append(b[cc])
    cc+=2
print(c)