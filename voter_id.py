#CONDITIONAL STATEMENTS.( if, elif, else ):

# Conditional operators: > , < , >= , <= , == , != .
while True:
    a=int(input("enter the age"))
    if a>18 :
        print("you are eligible for voting")
    elif a==18:
        b=input("do you have voter id")
        if b=="yes":
            print("you are eligible for voting")
        elif b=="no":
            c=input("do you want to create voter id")
            if c=="yes":
                d=input("enter your name")
                e=input("enter your district")
                print("...............................\n"
                      "...............................\n"
                      ".......THE GOVT OF INDIA.......""\n\n"
                      "      NAME:",d,"\n"
                      "      DISTRICT:",e,"\n\n"
                      "...............................\n"
                      "..............................."
                      )
                print("your voter id created")
            else:
                print("then...you are not eligible")
    else:
        if a<=0:
            print("enter the valid age")
        else:
            print("you are not eligible")