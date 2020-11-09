#Script: regex_dictionary_formation.py
#Author: Mahalakshmi Subramanian
#Anita Borg - Python Certification Course

#DESCRIPTION: A python program to print the dictionary of name and scores from the given string "MathScores"

'''Sample input:
MathScores = """
Ann got 99 and Maria got 95,
David got 84 and Jose got 21
"""
Sample output:{'Ann': '99', 'Maria': '95', 'David': '84', 'Jose': '21'}
'''

import re

MathScores = """
Ann got 99 and Maria got 95,
David got 84 and Jose got 21
"""

MathScores_List=MathScores.split(',')
line1=MathScores_List[0].split()
line2=MathScores_List[1].split()
Mathscores_Dict={}
i=0
j=0
count=0
while count<4:
    if count<2:
        search_string=' '.join(line1[i:i+3])
        Mathscores_Dict[(re.search(r'.\w+',search_string)).group()]=re.search(r'.\d+',search_string).group()
        count+=1
        i += 4
    else:
        search_string = ' '.join(line2[j:j + 3])
        Mathscores_Dict[(re.search(r'.\w+', search_string)).group()] = re.search(r'.\d+', search_string).group()
        j += 4
        count += 1
print(Mathscores_Dict)