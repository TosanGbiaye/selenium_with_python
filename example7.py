# OOPS
# Python is an Object-Oriented Programming language. OOP is a methodolgy that simplifies software
# development and maintains it by providing some rules . OOP consist of object, class etc
# an Object is an entity that has attributes and behaviour example : Rajesh is an object that has
# attributes such as height, weight, color etc as well as behaviour such as walking,talking, eating.

class DemoClass:
    a = 10

    def sum(self):
        print("Hello sample program")
# This is an object creation and the syntax is object= classname()
object= DemoClass()
# we call the object plus the desired method
print(object.a)
object.sum()