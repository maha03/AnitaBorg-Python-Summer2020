#Script: right_triangle.py
#Author: Mahalakshmi Subramanian
#Anita Borg - Python Certification Course

#DESCRIPTION: A python program which takes an input number n from the user and prints a right angled triangle of height
#             n. Also,the triangle should display the respective line numbers if the line number is odd
#             and censor out the even numbered lines using the hash (‘#’) symbol. Also, 1 ≤ n ≤ 10

'''Sample input:
5
Sample output:
    1
   ##
  333
 ####
55555
'''

n=input("Enter a integer number between 1 and 10")
try:
    height=int(n)
    if height<1 or height>10:
        raise ValueError
except:
    print("Enter valid integer as height")
    exit()
space=" "
even_line="#"
for i in range(height):
    i+=1
    if i%2!=0:
        print(space*(height-i)+str(i)*i)
    else:
        print(space*(height-i)+even_line*i)