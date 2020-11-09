#Script: remove_vowels.py
#Author: Mahalakshmi Subramanian
#Anita Borg - Python Certification Course

#DESCRIPTION: A python program that takes a string as input and returns a string with vowels removed

user_text=input("Enter a string").strip()
try:
    if len(user_text)<1:
        raise ValueError
except:
    print("Please enter a valid text")
    exit()

vowel_list=['a','e','i','o','u']
text_consonants=[i for i in user_text if i not in vowel_list]
print("".join(text_consonants))