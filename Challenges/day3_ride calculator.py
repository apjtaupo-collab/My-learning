print("Welcome to the ride Calculator")
min_height = 120


height =float(input("What is your height in cm\n"))

print(f" Your height is {height}cm")
                
if height >= min_height:
 print(" you can go on ride")
 age =  int(input("How old are you\n"))
 if age <= 12:
  print( "your admission is $5.00")
 elif age <= 18:
  print( "your admission is $7.00")
 elif age > 18:
  print( "your admission is $12.00")

else:
 print("Sorry, you cant go on the ride")


  





