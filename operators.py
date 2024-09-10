"""
When editing your code, if you want to test a task simply put a print statement
at the bottom of the page, then inside type out its name, with the brackets, 
then run the file.

For example to run and check your solution to task 1 you would type

print(task_1())
"""

# 1.
def task_1():
    x = 10
    y = 10

    return x != y # Edit only this line

# 2.
def task_2():
    data = input("Enter something: ")
    return type(data) == str

#3.
def task_3(): # Store your completed string in a variable called message
    message = None

    name = input("what is your name: ")
    age = input("how old are you: ")
    message = "Hello, your name is", name, "and you are", age, "years old!"

    # -------------------#

    return message

print(task_1())
print(task_2())
print(task_3())