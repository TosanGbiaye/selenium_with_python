# Loop Statements : for loop
# a loop is used for iterating over a set of statements repeatedly.
# in python we have 3 types of loops: for loop, while loop , do-while loop
a = [1,2,3,4,5,6,7,7,8,9,10]
# a is a list which have 10 diff values
# I want to print all the values in a one after the other
# for loop is used to print all values in a list
# the for loop syntax for this is:
# for variable in a:
for num in a:
    print(num)
# another for loop syntax for this is:
for num in range(5):
    print(num)
# I want to start printing from 2 not from 0, so the syntax for this is:
for num in range(2, 10):
    print(num)
# 2 is the start index while 10 is the stop index