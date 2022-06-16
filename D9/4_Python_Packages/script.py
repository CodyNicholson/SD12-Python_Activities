from math_package.math_module import add
from math_package.sub_package.math_helper import list_to

if __name__ == '__main__':
    print(list_to(5))
    print(add(*list_to(5)))