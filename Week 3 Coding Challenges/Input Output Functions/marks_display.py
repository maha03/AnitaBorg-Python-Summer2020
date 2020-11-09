#Script: marks_display.py
#Author: Mahalakshmi Subramanian
#Anita Borg - Python Certification Course

#DESCRIPTION: A program to input your name, and your marks in 3 subjects; Display the marks with your name,
#             as shown in the sample output. Do not use more than 2 input statements in the program.

'''Sample Input:
Enter your name: Anita
Enter your marks: 80,70,60
Sample Output: Anita, your marks are [80,70,60]
'''

#Display marks with names
name=input("Enter your name:")
marks=input("Enter your marks:")
marks=[int(x) for x in marks.split(',')]
print(name,"your marks are {}".format(marks),sep=",")