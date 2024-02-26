class student:

    def __init__(self):
        self.dict={}


    def update(self,name,marks):
        self.dict[name]=[marks]
        print(self.dict)

    def percentage(self,ann,li):
        per=sum(li)
        print("the percentage is>>",per/ann)




a=student()
ac=input("enter the name>>")
an=int(input("enter the number of subject>>>"))
aa=0
list=[]
while aa<an:
    aa+=1
    ab=int(input(f"enter the sub {aa} >"))
    list.append(ab)
    if ab>100:
        print("enter the marks below 100 ")
        break
a.update(ac,list)
a.percentage(an,list)