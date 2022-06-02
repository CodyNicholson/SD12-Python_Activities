#name_args
#  Accepts any number of named arguments and prints 
#  them in the pattern key : value one at a time.

def name_args(**kwargs):
    for k in kwargs.keys():
        print(f"{k}:{kwargs[k]}")
name_args(thing="one",stuff="this",color="orange",asdf="x")

#all_true
#  Returns True if all the elements in an iterable are true. 
#  Hint: there is an existing built-in function that could be very helpful here.

def all_true(myList):
    return all(myList)
print(all_true([True,True,True]))
print(all_true([True,True,True,False]))

#one_true
#  Returns True if one of the elements in an iterable is true.
#  Hint: there is an existing built-in function that could be very helpful here.

def one_true(myList):
    return any(myList)
print(all_true([True,True,True]))
print(all_true([True,True,True,False]))
print(all_true([False,False,False]))

#recursive_factorial
#  Uses recursion to find the factorial of an integer.


#recursive_deduplicate
#  Recursively removes all adjacent duplicate letters from a string.
#   Input: AABBCCDD
#   Output: ABCD

#recursive_reverse
#  Uses recursion to reverse a string.

def reverseRecurse(s, i=0):
    if len(s) == 0:
        return ""
    elif i == len(s)-1:
        return s[0]
    else:
        return s[-1-i] + reverseRecurse(s, i+1)
print(reverseRecurse("abc"))
print(reverseRecurse("aba"))
print(reverseRecurse("orange"))
print(reverseRecurse(""))