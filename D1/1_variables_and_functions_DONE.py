## Section 1 - variables and functions: 

# Question 1: Create two variables. One should be a string data type, and the other should be of type int.
s = "My String"
i = 99
# Use a single print statement to print both variables:

print(s, i)

# Question 2: Create a Python function that prints a greeting with a name as the parameter.

# Invoke the function with a name argument of your choosing:

def greet(name):
  print("Hello " + name)

greet("class")
## Section 2 - lists:

# Question 3: Create a list of your favorite movies with  at least 4 elements:

movies = ["Forest Gump", "Titanic", "I am Legend", "Coco"]

# Question 4: Use a print statement to print the list item at the index of 1:

print(movies[0])

# Question 5: Append a movie to the end of your list:

movies.append("Grown Ups")

# Use a print statement to print this ammended list:

print(movies)

## Section 3 - dictionaries:

# Question 6: Create a dictionary named 'cellphone' with 2 key:value pairs that are the properties of your cellphone.
#The keys should be: "color" and "number".
#Fill out the values on your own:

myPhone = {
  "color":"black",
  "number": 1
}

# Question 7: Access a value from inside the dictionary (Try to print the value of the 'color' property).

print(myPhone['color'])


## Section 4 - strings:

# Question 8: Create a variable and store a string with multiple words in it:

myVar = "multiple words"

# Question 9: Utilize the method that capitalizes the first letter of each word in your string - store this new string in a new variable:
myVar = myVar.title()
# Use a print statement to print the new string:
print(myVar)

for i in range(10,0,-1):
  print(i)

#Bonus:

# Question 10: Uncomment and look into this nested dictionary - try to relate your knowledge of objects and arrays in JavaScript.

# students_in_order = {
#   1: {'name': 'Esteban', 'age': '27', 'eye color': 'blue'},
#   2: {'name': 'Jackson', 'age': '22', 'eye color': 'brown'},
#   3: {'name': 'Zayn', 'age': '26', 'eye color': 'green'}
# }

# Question 10 A: Write a print function that outputs the second student in the dictionary

# Question 10 B: Write a print statement that outputs the name "Zayn" using the dictionary

# Question 10 C: Write a print statment that outputs the age of Esteban from the dictionary