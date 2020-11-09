#Script: circle_area.py
#Author: Mahalakshmi Subramanian
#Anita Borg - Python Certification Course

#DESCRIPTION: A Python program which accepts the radius of a circle from the user and computes the area of the circle

user_input=input("Enter the radius of circle")
try:
    radius=float(user_input)
except:
    print("Enter a number")
    exit()
if radius>0.0:
    area=3.14*(radius**2)
    print("Area of the circle is", area)
else:
    print("Invalid radius")