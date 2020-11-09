#Script: CeasarCipherFunction.py
#Author: Mahalakshmi Subramanian
#Anita Borg - Python Certification Course

#DESCRIPTION: A python function to perform decryption of Caesar Ciphers with a right shift of 3

def my_ceasar_decryption(encrypted_text):
    decrypted_text = ""
    for i in range(len(encrypted_text)):
        character = encrypted_text[i]
		# my output is going to be uppercase always; subracting 32 after circular shift for lower case acheives that
        if (character.isupper()):
            decrypted_text +=(chr((ord(character) + 3 - 65) % 26 + 65))
        elif character.islower():
            decrypted_text +=chr(((ord(character) + 3 - 97) % 26 + 97)-32)
        else:
            decrypted_text += ' '
    return decrypted_text

#Code to test the working of Ceasar decryption function
'''text = input("Enter an encrytped text")
output = my_ceasar_decryption(text)
print(output)
'''