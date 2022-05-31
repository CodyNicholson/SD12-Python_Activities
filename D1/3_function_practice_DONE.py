# Function Definition Practice:
# Define functions according to the following prompts. Run the Replit to verify correct output.


# 1. Function that accepts no arguments. It's called say_hello and returns nothing, just prints 'hello'.
print("Hi class!!")

def say_hello():
    print("HELLO")
say_hello()

# 2. a 'sum' function that accepts two integers and returns the sum.
def sum(a,b):
    return a + b
print(sum(2,3))

# 3. an 'average' function that accepts two numbers and returns the average.
def avg(a,b):
    return (a+b)/2
print(avg(10,30))

# 4. A function that accepts a first name and a last name and formats it to "{last_name}, {first_name}" (returns a string).
def fullName(fname, lname):
    return f"{lname}, {fname}"
print(fullName("Cody", "Nicholson"))

# 5. A function that accepts a first name, last name, graduation year, and student number and returns those four items together in a list.
def getUserData(fName, lName, gradYear, studentNum):
    return [fName, lName, gradYear, studentNum]
print(getUserData("Cody","Nicholson", 2014, 138599))

# 6. A function that accepts an integer and returns whether it is above 18 or not (Boolean).
def are18(age):
    if age > 18:
        print("Age is greater than 18")
    else:
        print("nah")
    #return age > 18
print(are18(6))
print(are18(60))

#7. A function that accepts a string and prints the string in reverse (no return value).
def reverseStr(s):
    #print(s[::-1])
    for i in range(len(s)-1, -1, -1):
        print(s[i])
reverseStr("abc")