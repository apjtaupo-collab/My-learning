print(5 + 5)
print(5 - 5)
print(5 * 5)
print(5 / 5) # will always default as a float not an interger
print(5 // 5) # // forces it to become a integer only use is you need an integer
print(2 ** 3) # "##"to the power of. so 2 ** 3 = 8 . 2 x 2 x 2 =8

# PEMDASLR =Parentheses, Exponants, Multiplication/Division, Addition,Subtraction, Left to Right
# this is the order of doing equation lines. (), **, *, /, +, -

print(3 * 3 + 3 / 3 - 3) # results in a 7
print(3 * (3 + 3)/ 3 - 3) # results in a 3 by putting brackets around the 3+3, it forced that to be calculated first
                          # giving the baracketed number top priority, then it calculated from left to right


height = 1.65 
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
bmi = (weight)/(height**2) # remenber to put the power value after the **

print(bmi)
print(int(bmi))
print(round(bmi)) # rounds up or down depending on first decimal point
print(round(bmi, 2)) # rounds to 2 decimal places in this instance


   
print(6 + 4 / 2 - (1 * 2))

