# Implement a function that will flatten and sort an array of integers 
# in ascending order, and which adheres to a functional programming paradigm.

def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)

# print(flatten_and_sort([[12,55,1],[2,33,4],[88,44,3]]))
# print(flatten_and_sort([[12,55,1],[2,33,4],[88,44,3]]))
# print(flatten_and_sort([[12,55,1],[2,33,4],[88,44,3]]))

'''
Make sure to answer the following questions about your coding process:

How does this solution ensure data immutability?

Is this solution a pure function? Why or why not?

Is this solution a higher order function? Why or why not?

Would it have been easier to solve this problem using a different programming style?

Why in particular is functional programming a helpful paradigm when solving this problem?
'''

class TestArray:
    def __init__(self):
        self.arr = []

    def flatten_and_sort(self, newArray):
        for item in newArray:
            for i in item:
                self.arr.append(i)
        return sorted(self.arr)

testOOP = TestArray()
testResult1 = testOOP.flatten_and_sort([[12,55,1],[2,33,4],[88,44,3]])
testResult2 = testOOP.flatten_and_sort([[12,55,1],[2,33,4],[88,44,3]])
testResult3 = testOOP.flatten_and_sort([[12,55,1],[2,33,4],[88,44,3]])
print(testResult1)
print(testResult2)
print(testResult3)
