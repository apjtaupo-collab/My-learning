weight = float(input("enter your weight "))
height = 1.85

bmi = weight / (height ** 2) #    ** to the power of


if bmi <  18.5:
    print(f" Your BMI is {bmi:.2f}.You  are under weight") # :.2F 2 decimal places
elif bmi<=24.90:
     print(f" Your BMI is {bmi:.2f}.Your weight is normal")
elif bmi <= 29.9:
      print(f" Your BMI is {bmi:.2f}.You are overweight")




