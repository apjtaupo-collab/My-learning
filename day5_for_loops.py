fruits = ["Apple", "Peach", "Pear"]
item_wanted = input("tell me what fruit you want\n").lower()#input selection


for item in fruits: # loops through each item in the list
    #print(item)
   
    if item_wanted == item.lower():# sees if the item you inputed is in the list
      print(item)       # prints item if it is there
      break   # stops loop if item found
else:
       print("item not on list") # tell you item not in list


   
