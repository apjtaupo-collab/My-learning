import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+',
           '=', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>',
           ',', '.', '?', '/']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

k_letter = int(input("How many letters do you want\n"))# int is needed to turn string into number for function to work

k_number = int(input("How many numbers do you want\n"))
k_symbol = int(input("How many symbols do you want\n"))

# The variable below "random_choices" selects the items from the list a the number of items required
# random.choices...in the brackets first variable is the list you want randomised, second variable "K
# is the number of items in that list use want extracted and randomised

random_choices = random.choices(letters, k =k_letter) + random.choices(numbers, k=k_number) + random.choices(symbols, k=k_symbol)  


randy = random_choices

random.shuffle(randy) #shuffle up the selected items so XHic801)" becomes  10H"8Xci for example

password = ''.join(randy)

print(password) #prints randonmised password

score = k_letter + k_number + k_symbol

if score <= 3:
    print("Password is Weak!")
elif score <= 6:
    print("Password is Medium")
else:
    print("Password is Strong!")







