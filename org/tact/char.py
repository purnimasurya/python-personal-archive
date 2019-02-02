import os

f=open("guru99.txt", "r")
if f.mode == 'r':
    contents =f.read()
    print(contents)
    count = 0
    for c in contents :
        if c.isspace() != True:
            count = count + 1
    print(count)
             
                
                            