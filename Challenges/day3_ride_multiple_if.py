print("Welcome to the ride Calculator")
min_height = 120


height =float(input("What is your height in cm\n"))

print(f" Your height is {height}cm")

if height >= min_height:
 print(" you can go on ride")

 age =  int(input("How old are you\n"))
 if age <= 12:              # if your age is 12 or less.....
  bill = 5                  # variable which set the price for this ride

 elif age <= 18:           # if your age is from 13 to 18...if "if" statement == false, then you are older then 12 but less or = to 18

  bill = 7

 elif age >= 45 and age <= 55: # if your ages are  between and including the ages 45 to 55. 
      bill =0
      print("Congratulations! you ride for free!")
 
 
 else:
  bill = 12
  

 wants_photo = input("do you want a photo. Type y for y and n for no ")
 if wants_photo == "y":
  bill += 3 # adds $3.00 to bill

 print(f"your final bill is ${bill} ")

else:
 print("Sorry, you cant go on the ride")

# indentation is important. because it controls which "if" block code belongs to
