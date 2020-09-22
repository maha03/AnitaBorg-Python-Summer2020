#Coding Challenge:W3-Operators,operands & input output function:Chanchal
#Mahalakshmi Subramanian
#obtain five marks as input
marks1=float(input("Enter subject 1 marks"))
marks2=float(input("Enter subject 2 marks"))
marks3=float(input("Enter subject 3 marks"))
marks4=float(input("Enter subject 4 marks"))
marks5=float(input("Enter subject 5 marks"))
markslist=[marks1,marks2,marks3,marks4,marks5]
#function to calaculate percentage and compute grade
def computegrade(markslist):
    per=sum(markslist)/len(markslist)
    if per>=90:return "A"
    elif per>=80 and per<90:return "B"
    elif per>=70 and per<80:return "C"
    elif per>=60 and per<70:return "D"
    else:return "F"
#call to function and printing return value
print(computegrade(markslist))
