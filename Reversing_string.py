# REVESRSING THE STRING

#1st method:
a=input("enter the string >>>")
length=len(a)
reverse=""
end=len(a)
while 0<end:
    reverse=reverse+a[end-1]
    end-=1
print("Reversed string: ",reverse)
#palindrom:
if reverse==a:
    print("it's palindrom")

#2nd method:
def reverse_string(s):
    # Convert string to a list of characters
    s_list = list(s)
    # Initialize pointers
    start = 0
    end = len(s_list) - 1
    # Swap characters until start pointer crosses end pointer
    while start < end:
        # Swap characters at start and end positions
        s_list[start], s_list[end] = s_list[end], s_list[start]
        # Move start pointer one step forward
        start += 1
        # Move end pointer one step backward
        end -= 1
    # Convert the list of characters back to a string
    reversed_string = ''.join(s_list)
    return reversed_string
# Test the function
input_string = input("Enter the string >>> ")
reversed_string = reverse_string(input_string)
print("Reversed string:", reversed_string)
