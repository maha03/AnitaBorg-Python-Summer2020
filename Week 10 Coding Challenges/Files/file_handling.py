# Script: file_handling.py
# Author: Mahalakshmi Subramanian
# Anita Borg - Python Certification Course

# DESCRIPTION: A python program to read a file and print strings in the file as a list
#              Constraints: Do not count the special characters  ! @ # $ % ^ & * ” + - ~

'''Sample Input:Use file in the folder
Sample Output: ['Believe', 'you', 'can', 'and', 'you', 'are', 'already', 'half', 'way', 'there', 'roosevelt\n',
               'Document', 'number', 'one']
'''

import re
try:
     with open("files challenge.txt", 'r+') as f:
         lines = f.readlines()
         output=[]
         length=len(lines)
         for i,line in enumerate(lines):
             if i!=length-1:
                 output+=re.findall(r'\w+\s',line)
             else:
                 output += re.findall(r'\w+', line)
         print(output)
         f.write("\nEditing the file through python scripting, wohoooo!")
except:
    print("File not found")
    exit()