#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   CHALLENGE 01 - Solution"""    

def main():
    name= input("Waht is your name?")
    data = input("What is the date today?")
    # print objects
    print("Hello, ", name,"! Happy ",day,"!", sep="")
    # concatenation
    print("Hello, " + name + "! Happy " + day + "!")
    # format method
    print("Hello, {}! Happy {}!".format(name, day))
    # f string
    print(f"Hello, {name}! Happy {day}!")
main()


