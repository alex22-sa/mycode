#!/usr/bin/python3
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

choice = input("Pick a farm:")
for farm in farms:
    if farm["name"] == choice:
        print(f"Here is the {choice} we have: ")
        for animals in farm["agriculture"]:
            print(animals)



