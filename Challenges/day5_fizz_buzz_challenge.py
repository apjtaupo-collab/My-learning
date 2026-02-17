

for number in range(1, 101): # loops through numbers 1 to 100
    # % is modulo - it gives the remainder after division. If remainder is 0, the number is divisible
    # "not" flips True to False - so "not number % 3 == 0" means "number is NOT divisible by 3"
    # number % 1 == 0 is always True for any number, so it doesn't do anything here
    if number % 1 == 0 and not number % 3 == 0 and not number % 5 == 0:
        print( number) # prints numbers that arent divisible by 3 or 5

    # each if is checked separately (not elif), so we need "not" checks to avoid double printing
    if number % 3 == 0 and not number % 5 == 0: # divisible by 3 but NOT by 5
           result ="fizz"
           print(result)

    if number % 5 == 0 and not number % 3 == 0: # divisible by 5 but NOT by 3
        buzz ="Buzz"
        print(buzz)
    if number % 5 == 0 and number % 3 == 0: # divisible by BOTH 5 and 3 (e.g. 15, 30, 45)
             buzzfizz = "FizzBuzz"
             print(buzzfizz)

  # A better way below but both work           

for number in range(1, 101): # loop through numbers 1 to 100
    if number % 3 == 0 and number % 5 == 0: # check FizzBuzz first - divisible by both 3 and 5 (e.g. 15, 30)
        print("FizzBuzz")
    elif number % 3 == 0: # only divisible by 3 (e.g. 3, 6, 9) - no need to check "not 5" because elif skips if the above matched
        print("Fizz")
    elif number % 5 == 0: # only divisible by 5 (e.g. 5, 10, 20) - same idea, elif means it's not divisible by 3
        print("Buzz")
    else: # not divisible by 3 or 5, just print the number
        print(number)



       

