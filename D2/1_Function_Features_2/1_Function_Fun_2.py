'''
arb_args - Takes in any number of arguments and prints them one at a time.
inner_func - Takes in two integers. Two nested functions should perform separate, distinct math operations using the integers. The result of both nested functions should then be added together and printed.
lunch_lady - Takes in two strings: a student's name and their lunch preference. The function should print both strings. If a lunch preference is not given, "Mystery Meat" should be printed instead.
sum_n_product - Accepts two integers and returns both the sum and the product.
alias_arb_args - Should be arb_args but assigned an alias. Remember, variables can hold functions in Python just like they can in JS. Alternatively, you can call a function from inside another function.
arb_mean - Accepts any number of integers and prints their average.
arb_longest_string - Accepts any number of strings and returns the longest one.
'''

def arb_args(*args):
    for i in range(0, len(args)):
        print(args[i])

arb_args(1,2,3,4,"asdf")



def innerFunc(x,y):
    def sum1():
        return x+y
    def multi1():
        return x*y
    print(sum1() + multi1())
innerFunc(5,6)



def lunch_lady(name, lunch="Mystery Meat"):
    print(name, lunch)
lunch_lady("Andy", "Sandwich")
lunch_lady("Steve")


def sum_n_product(x,y):
    return x+y,x*y
print(sum_n_product(10,9))


alias_arb_args = arb_args
alias_arb_args(1,"2",True)
arb_args(3,"2",True)


def alias_arb_args(*args):
    arb_args(args)


def arb_mean(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum/len(args))
arb_mean(1,2,3,4,5,6)


def arb_longest_string(*args):
    longestStrCt = len(args[0])
    longestStr = args[0]
    for s in range(1, len(args)):
        if len(args[s]) > longestStrCt:
            longestStrCt = len(args[s])
            longestStr = args[s]
    print(longestStr)
    print(longestStrCt)
    return longestStr
arb_longest_string("a", "magic", "classroom", "python")
arb_longest_string("a")

for i in "abc123":
    print(i)

for i in range(0, len("abc123")):
    print(i)
