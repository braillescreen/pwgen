"""
Password generator
Made by Patrick Wilson.
"""

#We do our importing of everything we need here.
import pyperclip
import random
import string
import os
import sys

#I must thank the code example of a random string I found on the internet. I did not code this part.

def randomstring(stringLength=10):
	password_characters = string.ascii_letters + string.digits + string.punctuation
	return ''.join(random.choice(password_characters) for i in range(stringLength))

print("Welcome to the password generator!")
print("Written by Patrick Wilson <https://pwilson-web.com>")
min=input("Enter minimum value you want to generate from.")
max=input("Enter maximum value you would like to generate from.")
if min=="" or max=="":
	print("Error! Blank field detected.")
	sys.exit()
n=random.randint(int(min),int(max))
pw=randomstring(n)
print("Copied a "+str(n)+" character password to your clipboard.")
pyperclip.copy(pw)
fn=input("Enter file name not including extension you want to save to. Leave blank for none")
if fn!="":
	with open(fn+".txt","a") as f:
		f.write(pw)
