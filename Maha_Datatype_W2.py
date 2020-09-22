#Coding Challenge: Datatypes
#Mahalakshmi Subramanian
#A.Compute Area of circle
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

#B.Comma seperated inputs into list and tuple
user_input=input("Enter comma seperated values")
if len(user_input)>0:
    lst=user_input.split(',')
    tpl=tuple(lst)
    print("List is",lst)
    print("Tuple is",tpl)
else:
    print("Input a sequence of numbers")

#C. Check whether a number is within 1100 and 2100
user_input=input("Enter a number")
try:
    check_num=float(user_input)
except:
    print("Input a number")
    exit()
if check_num>=1000:
    if((abs(1000-check_num)>0.0) and (abs(1000-check_num)<100.0)):
        print("The number is within 100 of 1000")
    elif((abs(2000-check_num)>0.0) and (abs(2000-check_num)<100.0)):
        print("The number is within 100 of 2000")
    else:
        print("The number is neither within 100 of 1000 or 2000")
else:
    print("The number is neither within 100 of 1000 or 2000")

#D.Check whether input number is in a list
user_input=input("Enter a number")
user_list=input("Enter a sequence of numbers seperated by comma")
try:
    defined_list=user_list.split(',')
    check_num=float(user_input)
    if len(defined_list)>0:
        print("continue")
except:
    print("Input a number and sequence of numbers")
    exit()
for i in range(len(defined_list)):
    if check_num==float(defined_list[i]):
        a=True
        break
    else:
        a=False
        continue
print(a)
