import random

friends = ['Tanya', 'Pete', 'Nancy', 'Nicci', 'Graham']

who_pays = random.randint(0,4)

print(f"Who pays the lunch bill???\n{friends[who_pays]}")

# uses a random module and list to determin who pays the bill

#
print(random.choice(friends))# .choice( is a fuction in the module random.)

print(friends[4]) # will print an IndexError as it is out of range lists start from zero so index will be 0 to 4, not 5.


fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
fruits[-1] = "Melons"
fruits.append("Lemons")
print(fruits)

ruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables] # create one lists with 2 lists inside it.
 
print(dirty_dozen[0][1]) # first square is the list within the list dirty_dozen. the second is the index( inthis case nectarines)