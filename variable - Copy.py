name = input("what is your name ") # name is now the variable for any name entered
print(name.title()) ## title( capitalises the name)
print(len(name)) # len() counts the number of charators in a string, (in this case)

names = "Tanya"
print(len(name)) # Will return a value of 5 as "Tanya" has 5 letters

print(len("Graham"))# uses 1 lime but name is locked

print(len(input("What is your name "))) # Wraps everything up in one line

username = input("Name ")
length = len(username)
print(length)