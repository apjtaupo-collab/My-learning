print("welcome to Pete's Carwash")

wash_type = input("What Type of Wash would you like:\nType S for Standard, D for Delux and P for Premium\n").lower()

if wash_type in ["s", "d,","p"]: 
 
    
 if wash_type == "s":
    bill = 10            # sets value for standard wash
 elif wash_type =="d":
    bill = 15            # sets value for delux wash
 elif wash_type =="p":
    bill = 25            # set value for premium wash
 else:
      print("not a valid input")

 wax_coating = input( "Would you like a wax coating?: Y or N\n").lower()
 interior_clean = input("Would you like an interor clean?: Y or N\n").lower()
 air_freshener = input("Would you like an Air freshener? Y or N\n").lower()

     # nested if statement. " if waxcoating is a yes it asks is your wash standard? if so, your wax coating is $5.00. any other wash is $7.00"
 if wax_coating == "y":
     if wash_type == "s":
            bill += 5
     else:
            bill += 7   
 if interior_clean == "y":
        bill += 8
    
       
 if  air_freshener == "y":
        bill += 2
    
      
 print(f" your final bill is {bill}") 
else:

 print("invalid choice Type s, d or p")




