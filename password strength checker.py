def password(a):
    l = list(a)
    num_l = []
    cha_l = []
    spch_l = []

    # Separating the num, char, special char.
    for i in range(len(l)):
        if l[i].isnumeric():
            num_l.append(l[i])
        elif l[i].isupper() or l[i].islower():
            cha_l.append(l[i])
        elif l[i] == " ":
            print("Do not give whitespace in the password")
        else:
            spch_l.append(l[i])

    # Calculating the strength
    strength = 0
    if len(num_l) >= 2:
        strength = strength + 1
        if len(num_l) >= 4:
            strength = strength + 1
    if len(cha_l) >= 5:
        strength = strength + 1
        if len(cha_l) >= 10:
            strength = strength + 1
    if len(spch_l) >= 2:
        strength = strength + 1
        if len(spch_l) >= 5:
            strength = strength + 1

    # match strength:
    #     case 1:
    #         print("your password is not eligible")
    #     case 2:
    #         print("ALERT !!! \n password is too weak ")
    #     case 3:
    #         print("Your password is weak !!!")
    #     case 4:
    #         print("your password is strong ")
    #     case 5:
    #         print(" your password is strong ")
    #     case 6:
    #         print("your password is too strong ")

    return strength


p = input("Enter the password>>> ")
pp = password(p)
if pp == 1:
    print("Your password is not eligible")
elif pp == 2:
    print("ALERT !!!\nPassword is too weak")
elif pp == 3:
    print("Your password is weak")
elif pp == 4:
    print("Your password is strong")
elif pp == 5 or pp == 6:
    print("Your password is too strong")