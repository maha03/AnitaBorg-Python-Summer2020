#Coding Challenge:W6:More programs and flow control-Astha
#Mahalakshmi Subramanian
n=int(input("Enter a integer number between 1 and 10"))
space=" "
even="#"
for i in range(n):
    i+=1
    if i%2!=0:
        print(space*(n-i)+str(i)*i)
    else:
        print(space*(n-i)+even*i)
"""
#Using rjust():
n=int(input("Enter a integer number between 1 and 10"))
space=" "
even="#"
for i in range(n):
    i+=1
    if i%2!=0:
        print((str(i)*i).rjust(n))
    else:
        print((even*i).rjust(n))
#Using format():
"""
