#Coding Challenge: Sequence types-Avichal
#Mahalakshmi Subramanian
#Solution5:Using set and list append using operator w/o using .extend()
user_list=input("Enter a list of strings separated by spaces")
user_char=input("Enter a test character")
user_list=user_list.split()
unique_string=set(user_list)
unique_list=list(unique_string)
solution_list=[]
#if the input string not in solution list, count the user char and add it in solution list based on count_char
for i in range(len(unique_list)):
    char_count=unique_list[i].count(user_char)
    solution_list+=[unique_list[i]]*char_count
print(solution_list)
"""
#Solution4:Using only lists-2
user_list=input("Enter a list of strings separated by spaces")
user_char=input("Enter a test character")
user_list=user_list.split()
solution_list=[]
#if the input string not in solution list, count the user char and add it in solution list based on count_char
for i in range(len(user_list)):
    if user_list[i] not in solution_list:
        char_count=user_list[i].count(user_char)
        solution_list.extend([user_list[i] for j in range(char_count)])
print("Output",solution_list)


#Solution3: Using only lists
user_list=input("Enter a list of strings separated by spaces")
user_char=input("Enter a test character")
user_list=user_list.split()
solution_list=[]
#if the input string not in solution list, count the user char and add it in solution list based on count_char
for i in range(len(user_list)):
    if user_list[i] not in solution_list:
        char_count=user_list[i].count(user_char)
        if char_count>0:
            solution_list.extend([user_list[i] for j in range(char_count)])
if len(solution_list)>0:print(solution_list)
else:
    print("Character not found in list elements")

#Solution2: Using dictionary
user_list=input("Enter a list of strings separated by spaces")
user_char=input("Enter a test character")
try:
    #print("Inside try")
    if len(user_list)!=0 and len(user_char)!=0:
        user_list=user_list.split()
except:
    print("Input list of integers and a character")
    exit()
#create list removing spaces from input list
dict={}
solution_list=[]
#create dictionary that has keys as unique string and values as frequency of user_char
for i in range(len(user_list)):
    dict.update({user_list[i]:user_list[i].count(user_char)})
#getting keys and values as list
k=list(dict.keys())
v=list(dict.values())
#appending keys as string based on frequency of user_char
for i in range(len(k)):
    if int(v[i])>0:
        solution_list.extend([k[i] for j in range(v[i])])
#print solution list if there's an element;else display message
if len(solution_list)>0:print(solution_list)
else:
    print("Character not found in list elements")


#Solution1: old,lengthy
user_list=input("Enter a list of strings separated by spaces")
user_char=input("Enter a test character")
try:
    if len(user_list)>0 & len(user_char)>0:
        print("continue")
except:
    print("Input list of integers and a character")
#create list removing spaces from input list
user_list=user_list.split(' ')
#define empty lists for storing unique list, repetition times and solution
unique_list=list()
repeat_times=list()
solution_list=list()
#Creating a unique list
for i in range(len(user_list)):
    if user_list[i] in unique_list:
        continue
    else:
        unique_list.append(user_list[i])
#Checking how many time the char appears in each list element(repeat_times)
for i in range(len(unique_list)):
    repeat_times.append(unique_list[i].count(user_char))
    if repeat_times[i]==1:
        solution_list.append(unique_list[i]*int(repeat_times[i]))
        solution_list.insert()
    elif repeat_times[i]>1:
        n=repeat_times[i]
        while n>0:
            solution_list.append(unique_list[i])
            n=n-1
    else:
        continue
if len(solution_list)>1:print(solution_list)
else:
    print("Character not found in list elements")
"""
