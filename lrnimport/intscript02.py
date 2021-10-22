#!/usr/bin/env python3
import subprocess  ## <-------- changed
print(type(subprocess))
print(dir(subprocess))
print(dir(subprocess.call)) 

subprocess.call(["ip", "link", "show", "up"])
print("This program will check your interfaces.")
interface = input("Enter an interface, like, ens3: ")
subprocess.call(["ip", "addr", "show", "dev", interface])  ## <--- changed
subprocess.call(["ip", "route", "show", "dev", interface]) ## <--- changed

