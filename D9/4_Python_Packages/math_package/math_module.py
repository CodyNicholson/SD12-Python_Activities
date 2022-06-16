def add(*args):
    sum = 0
    for int in args:
        sum += int
    return sum

def multiply(*args):
    product = 1
    for int in args:
        product = product * int
    return product

def subtract(*args):
    print(args)
    result = 0
    for int in args:
        result = int - result
    return result