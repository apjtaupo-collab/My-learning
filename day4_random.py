import random

#random_integer = random.randint( 1, 10)
#print(random_integer)

#random_integer_0_to_1 = random.random() # oreturns a random float number between 0 and 1
#print(random_integer_0_to_1)

#random_number_0_to_1 = random.random()*10 # oreturns a random float number between 0 and 10
#print(random_number_0_to_1)

#random_float_0_to_1 = random.uniform(1, 10)
#print(random_float_0_to_1 )

head_tails = random.randint(0,10)

if head_tails >=0 and  head_tails <=5:
    print(head_tails )
    print("Tails!")
else:
    print(head_tails )
    print("Heads!")