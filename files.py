a=input("Enter The High Score :")

# Create 
f=open('new.txt','w')
# Write
f.write(a)

f.close()

# Read
p=open("new.txt",'r')
# Print File Content
print(p.read())
p.close()


p=open("new.txt","a")
p.write("102")
p.close()

import os

os.remove('new.txt')