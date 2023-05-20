# file=open("my_dir/my_file.txt",'r')
# a = file.read()
# print(a)

with open("my_dir/my_file.txt",'r')as a:
    
    contents=a.read()
    print(contents)


import os
#####os=chmod("my_dir/my_file.txt")



with open("my_dir/my_file.txt",'r')as a:
    
    contents=a.read()
    print(contents)


file=open("my_dir/my_file.txt",'a')
file.write("I'm adding a new line to the file!")

with open("my_dir/my_file.txt",'r')as file:
    
    app=file.read()
    print(app)
