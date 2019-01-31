import os
f=open("guru99.txt", "r")
if f.mode == 'r':
    contents =f.read()
    print(contents)