print( 'Hello welcome to Pete\'s Cinama')
age = {"child":7, "adult":12, "senior":8}

how_old = input("What is your current age?\nType Child, Adult or Senior ").lower()

if how_old == "child":
    print(f"The admission is ${age['child']}.00")
elif how_old == "adult" or how_old == "senior": # checks if adult or senior
    loyalty = input('Do you have a loyalty card? Type "y" for Yes and "n" for No\n').lower()

    if loyalty == "y":
        price = age[how_old] - 2 # will automatically apply discount to right age group
        print(f"Loyalty discount applied! Your admission is ${price}.00")
    else:
        print(f"Your admission is ${age[how_old]}.00") # prints normal admission price to age range

else:
    print("no admission")