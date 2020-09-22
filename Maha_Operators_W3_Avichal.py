#Coding Challenge:W3-Operators,operands & input output function:Chanchal
#Mahalakshmi Subramanian
#using bitwise Operator
user_input=input("Enter a list of numbers")
num_list=[int(x) for x in user_input.split(',')]
a=0
for i in range(len(num_list)):
    #print(a,i)
    a=num_list[i]^a
    #print(a,i)
print(a)

#implement the solution w/o minding about complexity
"""
user_input=input("Enter a list of numbers")
num_list=user_input.split()
num_unique=set(num_list)
j=[]
for ele in num_unique:
    if (num_list.count(ele)%2!=0): #since count iterates through all elements in list,time cpxity becomes n^2
        j+=ele
print(j)
"""
