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

'''import string
try:
     with open("files challenge.txt", 'r+') as f:
         lines = f.readlines() #readlines() adds \n for each line until EOF is encountered; output is a list
         l1 = str(lines[0].translate(lines[0].maketrans(' ', ' ', string.punctuation))).split(" ")
         l2 = str(lines[1].translate(lines[1].maketrans(' ', ' ', string.punctuation))).split(" ")
         for i in l1:
             if i == '' or i == ' ':
                 l1.remove(i)
         print(l1 + l2)
         f.write("\nEditing the file through python scripting, wohoooo!")
except:
    print("File not found")
    exit()
'''