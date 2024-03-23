def word_count(a):
    list=a.split(" ")
    if list[-1]=="":
        list.pop(-1)
    l=len(list)
    return l

a=input("Type any sentence>>> ")
word=word_count(a)
print("The number of word in sentence>>> ",word)

# import re
#
# def word_count(a):
#     # Split the input string using a regular expression to match whitespace characters
#     words = re.split(r'\s+', a)
#
#     # Remove empty strings from the list
#     words = [word for word in words if word]
#
#     return len(words)
#
#
# a = input("Type any sentence>>> ")
# word = word_count(a)
# print("The number of words in the sentence:", word)


