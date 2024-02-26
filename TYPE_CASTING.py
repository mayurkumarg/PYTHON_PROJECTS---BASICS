# TYPE CASTING OR TYPE CONVERSION.
a= "5"
b= "5"
c=2
print(a+b)
print("TYPE>> ",type(a),"\n")
# STRING TO INTEGER.
# this in "EXPLICITE" type casting. Here we type casting manually.
print(int(a)+int(b))
c=int(a)
print("TYPE>> ", type(c),"\n")

# this is "IMPLICIT" type casting. the python intepreter type cast's itself, in the time of execution.
a=5 #typecasting "int" - "float".
b=2.5
c=a+b
print(c)
print("TYPE>>>", type(c))