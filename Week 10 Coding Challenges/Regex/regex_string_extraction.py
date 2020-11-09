#Script: regex_string_extraction.py
#Author: Mahalakshmi Subramanian
#Anita Borg - Python Certification Course

#DESCRIPTION: A python program to solve a series of regex questions

import re

#Question 1: Extract email extension
input_string_1 = "From john.doe@ab.etc Thu Jun 15 02:04:09 2010"
output=re.findall(r'\@(\w+\S\w+)', input_string_1)
print(output)

#Question 2: Extract email from a given string using re.findall
output=re.findall(r'[^"From"]\w+\.?\w+\@\w+\.\w+', input_string_1)
print(output)

#Question 3: Extract 'From: Using the :' from a given string using re.findall
input_string_2 = 'From: Using the : character'
output=re.findall(r'^F.+:', input_string_2)
print(output)