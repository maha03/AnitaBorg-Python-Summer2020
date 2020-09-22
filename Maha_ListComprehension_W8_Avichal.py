#Coding Challenge:W8:List COmprehension -Avichal
#Mahalakshmi Subramanian
#square negative numbers from input and leave positive numbers as it is
user_list=[int(i) for i in input("Enter a list of numbers seperated by space").split()]
print(user_list)
result=[i**2 if i<0 else i for i in user_list]
print(result)
