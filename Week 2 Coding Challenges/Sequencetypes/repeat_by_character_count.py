#Script: repeat_by_character_count.py
#Author: Mahalakshmi Subramanian
#Anita Borg - Python Certification Course

#DESCRIPTION: Input a list of strings “str_list” separated by spaces and input a character “ch”.
#             For each string in str_list, count the number of occurrences of the character “ch” in that string
#             and store in a new answer list and print the answer list.
#             Note: The order of the occurrence of the words and the corresponding answer list matters.

'''Sample Input:
List: python sword happy code star good wow
Character: o
Sample Output:
[‘python’, ’sword’, ’code’, ’good’, ’good’, ’wow’]
'''

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