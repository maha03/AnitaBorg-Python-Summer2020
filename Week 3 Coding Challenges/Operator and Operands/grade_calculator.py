#Script: grade_calculator.py
#Author: Mahalakshmi Subramanian
#Anita Borg - Python Certification Course

#DESCRIPTION:A python program that calculates the grades of students.A final letter grade is returned based on average
#            of five subjects marks

#function to calculate percentage and compute grade
def computegrade(markslist):
    per=sum(markslist)/len(markslist)
    if per>=90:return "A"
    elif per>=80 and per<90:return "B"
    elif per>=70 and per<80:return "C"
    elif per>=60 and per<70:return "D"
    else:return "F"

#Receive inputs
try:
    marks1=float(input("Enter subject 1 marks"))
    marks2=float(input("Enter subject 2 marks"))
    marks3=float(input("Enter subject 3 marks"))
    marks4=float(input("Enter subject 4 marks"))
    marks5=float(input("Enter subject 5 marks"))
    if((marks1 or marks2 or marks3 or marks4 or marks5)<0 or (marks1 or marks2 or marks3 or marks4 or marks5) >100):
        raise ValueError
    else:
        marks_list=[marks1, marks2, marks3, marks4, marks5]
except:
    print("Please enter marks between 0 and 100")
    exit()

#call to function and printing return value
print("Grade is",computegrade(marks_list))