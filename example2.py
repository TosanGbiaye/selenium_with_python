# strings
a = 'This is'
b = "Tosan"
c = """welcome to class , Tosan """
print(a)
print(b)
print(c)
# + operator is used to concatenate strings
print(a+b+c)
# * operator is used to repeat a string for n number of times
print(a + b * 4)
print(b * 3)
# in operator is used to compare a string in another string, it returns false if the content in both string is not equal
print(a in b)
# not in returns true if the content in both strings is not equal
print(a not in b)

# list is a string having different data types
value = ['gender', 3 , True, 'sandra']
print(value)

# len() gives the total number of value in a list
print(len(value))

...
"To get value in a list" \
"Every value starts from index 0" \
"0: first value in the list " \
"1: second value in the list " \
"2: third value in the list" \
"3: fourth value in the list" \
"n-1: gives the last value in a list"

...
print(value[0])
print(value[1])
print(value[3])

# append is used to add value to a list
value.append("lucky student")
print(value)