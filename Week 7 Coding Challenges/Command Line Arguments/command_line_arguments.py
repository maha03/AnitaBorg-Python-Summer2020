#Script: command_line_arguments.py
#Author: Mahalakshmi Subramanian
#Anita Borg - Python Certification Course

#DESCRIPTION: A Python program using sys. Argv to depict the name of the script,the number of the arguments and lastly
#             the list of the arguments used.

import sys
print("Name of the script",sys.argv[0])
print("Number of arguments",len(sys.argv))
print("List of arguments",str(sys.argv))