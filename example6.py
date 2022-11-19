# Functions
# A function is a set of statement that takes input, do some specific computation and produces output.
# why functions: for code re-usability
# function syntax is:

# def function_name(function parameters):
#     function body  # a set of python statement
#     return   #optional return statement
def sum():
    c = 3 + 4
    print(c)

sum()     # calling a function

# function with parameters
def add(a,b):
    d = a + b
    print(d)

add(5,4)
add(17,31)
add(20,35)

# return statement : for re-using the output of a function
def AddingNumber(a,b):
    e = a + b
    return e
p1 = AddingNumber(2,3)
if p1 > 3:
    print("the sum value is greater than 3")