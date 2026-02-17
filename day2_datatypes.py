#subscripting
print("hello"[0])# this will print the letter "h".
print("hello"[-1])# this will print the letter "o".the last letter. use can also use 4.

print("123" + "345")# will print 123345 as it is concatinating the string(combining)

#intergers are whole numbers (int)
number = 123345
numbers = int("123_345") # converts string to whole numbers

print(f"{number}\n{numbers}") # will print 123345

# float is a floating point number Ie. has a movable decimal point
numbers1 = float("123_345") # converts string to whole numbers
print(numbers1)

#Boolean is True or False

print(type(1234)) # prints what type the "number is"  in terminal, prints <class 'int'>
print(type("hello"))
print(type(12.00))
print(type(True))

#changing class type
print("123" + "345") #  will print 123345
print(int("123") + int("345")) # will now do math and result will be 468 as int()converted string to whole numbers


# fix this code
# print("number of letters in your name")
# len(input"enter your here)
name_length = len(input("enter your here\n"))
print(f"Number of letters in name\n{name_length}" )
print(type(name_length ))

#or

print("number of letters in your name\n" + str(name_length))# "str converts the int to a string"





