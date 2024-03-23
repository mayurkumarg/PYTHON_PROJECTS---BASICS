def shuffle(a,b):
    w1=a.replace(" ","")
    w2=b.replace(" ","")
    sh=""
    wl1=len(w1)
    wl2=len(w2)
    min_val=min(wl1,wl2) #finding min value
    for k in range(min_val):
        sh=sh+w1[k]+w2[k]
    #adding remaining value for bigger string
    sh=sh+w1[min_val::]
    return sh

a=input("Enter the 1st string>>> ")
b=input("Enter the 2nd string>>> ")
s=shuffle(a,b)
print(s)