#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""


message = 'You are in front of your house , but forgot the code. You have three tries to get in or you sleep on the back yard cauch '
truecode = "357"
print(truecode)
print("You walk to the door. The rotary padlock contains three digits. You enter a code")

while True:
    try:
       option1 = int(input("Digit one: "))
       break
    except:
       print("Digit one must be a whole number between 0-9:")

while True:
    try:
       option2 = int(input("Digit two: "))
       break
    except:
       print("Digit two must be a whole number between 0-9:")

while True:
    try:
       option3 = int(input("Digit three: "))
       break
    except:
       print("Digit three must be a whole number between 0-9:")
       
chosenCode = int(str(option1) + str(option2) + str(option3))
print(chosenCode)
        
if chosenCode == truecode:
    print("You hear a click, and the padlock shifts. As you press open the door a rush of fresh, warm air caresses your face. At last, you are free."
print(truecode)
else:
    print(" The code is incorrect!!! Do to your backyard.")
		
           
