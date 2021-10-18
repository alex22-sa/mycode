#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   List - making selections from complex lists"""

def main():

    # create a list called list1
    icecream= ["flavors", "salty"]
    
    northerntrust= ["Alex","Andrew","Dave","Julia","Kurt","Marlon","Roger","Seth","Tim","Viq"]
    print(icecream)
    int2append = 99

    icecream.append(int2append)
    print(icecream)

    member= int(input("Please choose the number between 0 and 9\ n>"))
    print(f"{northerntrust[member]}")







main()

