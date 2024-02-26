# WHILE LOOP:

#EXAMPLE:1 (countdown and blasting)
i=10
while i>0:
    print(i)
    i-=1
else:
    print("blast")

#EXAMPLE:2 (sum of even numbers from 1 to 20)
sum_of_even_number=0
a=0
while a<20:
    a+=2
    sum_of_even_number=sum_of_even_number+a
print("THE SUM OF EVEN NUMBERS FROM 1 to 20: ", sum_of_even_number)

#EXAMPLE:3 (calculating the result of raising a number to an exponent without using the "**"<exponential operator> )
num=int(input("enter the number>>"))
exp=int(input("enter the exponential value>>"))
a=0
v=1
while a<exp:
    v=v*num
    a+=1
print(v)