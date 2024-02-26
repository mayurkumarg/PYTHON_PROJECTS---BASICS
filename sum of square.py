#SUM OF THE SQUARE FOR THE 'N' NUMBERS
def a(num):
    sum_sqr=0
    for i in range(0,num+1):
        sum_sqr=sum_sqr+(i*i)
    print(sum_sqr)
aa=int(input("enter the limit>>"))
a(aa)