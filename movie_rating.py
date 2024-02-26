print("THE MOVIE RATINGS FOR KGF")
a=int(input("enter the number of people are rating this movie"))
b=0
c=[]
while b<a:
    d=int(input("RATE THE MOVIE'1-10'"))
    c.append(d)
    b=b+1
    if d>10 or d<0:
        print("'RATE'1 to 10 only")
        break
    # elif d<0:
    #     print("'RATE'1 to 10 only")
    #     break
rate=sum(c)
if d>0 and d<10:
        print(f"IMDB>>>>>{rate/a}/10")