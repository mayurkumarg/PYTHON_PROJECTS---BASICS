Range=10
for i in range(Range):
    for j in range(i):
        # print(""*(Range-j), i, end="")
        print(i,end=" ")
    print("")

for i in range(Range+1):
    print(" "*(Range-i),"* "*i)