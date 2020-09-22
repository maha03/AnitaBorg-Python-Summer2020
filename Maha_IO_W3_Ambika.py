#Coding Challenge:W3:Input & output functions-Ambika
#Mahalakshmi Subramanian
#Display marks with names
name=input("Enter your name:")
marks=input("Enter your marks:")
marks=[int(x) for x in marks.split(',')]
print(name,"your marks are {}".format(marks),sep=",")
