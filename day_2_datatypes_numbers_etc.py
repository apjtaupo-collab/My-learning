print("Welcome to the tip calculator")
prelimanary_bill = float(input("What was to total bill\n"))# float converts string to a number
tip_amount = float(input("How much would you like to Tip\n10% ,12$ 0r 15%\n"))
number_people = int(input("How many guests\n"))
tip_percent = tip_amount / 100 # convert tip_amount to a decimal
tip_total = tip_percent * prelimanary_bill # give actual value of tip
total_bill = (prelimanary_bill + tip_total ) # calculates total bill including tip
total_bill_portion = (prelimanary_bill + tip_total ) / number_people # devides total bill by the number of people paying

print(f"The tip is caculated as:\n${tip_total:.2f}" )
print(f" The Total Bill, Including tip is:\n${total_bill:.2f}\n Each person pays:\n${total_bill_portion:.2f}")








    

