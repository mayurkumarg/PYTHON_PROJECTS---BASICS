def count(a):
    counts = {}
    for elem in a:
        if elem in counts:
            counts[elem] += 1
        else:
            counts[elem] = 1
    return [elem for elem in counts if counts[elem] > 1]
print(count([1,23,5,23,7,6,7]))

# This implementation initializes an empty dictionary called counts.
# Then, for each element elem in the input list a, we check if elem is
# already a key in the counts dictionary.If it is, we increment the corresponding
# value by 1. If it isn't, we add it to the dictionary with a value of 1.
# Finally, we create a new list by iterating over the keys of the counts
# dictionary and selecting only those keys whose corresponding values are greater than 1.
# This new list contains all the elements that appeared more than once in the input list.
# For example, calling count([1,2,3,3,3]) would return [3], since the only element that
# appears more than once in the input list is 3.