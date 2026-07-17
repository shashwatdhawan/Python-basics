# day 15 of python learning from basics 
# topic functions arrangements
# def average(a, b, c=1):
#     print("The average is ", (a + b + c) / 3)
def average(*numbers):
    print(type(numbers))
    sum = 0 
    for i in numbers:
        sum = sum + i
    print("The average is ", sum / len(numbers))
    return sum / len(numbers)


c = average(5, 6, 7, 8, 9, 10)
print(c)

# and return should be used in functions when we have to call the function and store the value in a variable for later use.
# today i learned about return statement and variable length arguments in functions and required arguments and keyword arguments in functions and default arguments in functions and how to use them in python programming language.

def end():
    print("This is the end of day 15 of python learning from basics")

end()
# or 
def end():
    return "This is the end of day 15 of python learning from basics"

a = end()
print(a)

    