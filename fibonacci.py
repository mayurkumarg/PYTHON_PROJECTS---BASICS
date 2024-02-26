a=int(input("enter the fibonacci no"))
n1=0
n2=1
b=0
print(f"your fibonacci no of {a} is >>>>",)
if a<=0:
    print("enter positive no")
while b<a:
    c=n2+n1
    n1=n2
    n2=c
    b=b+1
    print(n1)