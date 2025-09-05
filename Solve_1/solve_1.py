
'''
Group Name: Sydney Group 17
Group Members: 4
Mohammed Ashrafujjaman Hera - 391197
Pujan Dey  - 395076
Shaown Imtiaz - 396121
Al-Amin Dhaly - 395230
'''

import os
from termcolor import colored # this is for colored output in terminal

# Input validation and filtering
def input_validation(users_input,shift_num):
    try:
        # integer number
        # Trying to convert string input from user into a Interger number
        temp_x = int(users_input)
        users_input = temp_x
        print(f"\nFor {shift_num}: ")
        # Green Colored text for better user experience.
        print(colored("User provided an Integer number.","green"))
    except ValueError:
        try:
            # float number
            # Trying to convert string input from user into a float number then an interger number
            float_x = float(users_input)
            round_x = round(float_x)
            users_input = int(round_x)
            print(f"\nFor {shift_num}: ")
            print(colored(f"User provided a float value for the {shift_num}.\nConverting it to integer.\n","blue"))           
        except ValueError:
            # In case of no value input by the user it will assign the default values accordingly
            if users_input == "" or users_input.isalpha(): # placing a default values
                if shift_num == "shift_1":
                    users_input = 5
                else:
                    users_input = 7
                
                print(f"\nFor {shift_num}")
                print(colored(f"user did not provide any value or input 'characters/strings' for {shift_num}.\nDefault value={users_input}, Assigned.\n","cyan"))       
    return users_input

#Alamin Dhly (Encryption)
def encryption(plain_data, shift1, shift2):
    encrypted = ""
    markers = []
    for char in plain_data:
        if char.islower():
            if 'a' <= char <= 'm':
                # lowercase a-m → forward shift (shift1 * shift2)
                shift = shift1 * shift2
                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
                # marker is to save the shift direction and shift rules to reverse later
                # marker 0 means 'a-m → forward shift (shift1 * shift2)'
                marker = 0
            else:
                # lowercase n-z → backward shift(shift 1 + shift 2)
                shift = -(shift1 + shift2)
                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
                # marker is to save the shift direction and shift rules to reverse later
                # marker 1 means 'backward shift (shift 1 + shift 2)'
                marker = 1
        elif char.isupper():
            if 'A' <= char <= 'M':
                # uppercase A-M → backward shift
                shift = -shift1
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                # marker 2 means 'backward shift'
                marker = 2
            else:
                # uppercase N-Z → forward shift
                shift = shift2 ** 2
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                # market 3 means 'uppercase N-Z → forward shift(shift**2)"
                marker = 3
        else:
            new_char = char
            # marker 'x' means all other characters
            marker = 'x' 
            
        encrypted += new_char
        # preserving markers according to index value of the original text.
        markers.append(marker)

    # Write encrypted content to file
    cwd = os.path.dirname(__file__)
    path = os.path.join(cwd, "encrypted_text.txt")
    with open(path, 'w') as f:
        f.write(encrypted)
        print(colored("New file created for encrypted data!", "green"))

    return encrypted,markers

#Encryption Part Ends

# Imtiaz (Decryption)
def decryption(encrypted_data, markers, shift1, shift2):
    # print("\nDecryption started!!\n")
    decrypted = ""
    for char, marker in zip(encrypted_data, markers):
        # Based on marker we are applying the reverse shifting calculation to retrieve the original text
        # without the markers all the characters does not return to its original form
        # while encrypting some letters inter-change from upper to lower and vise versa. 
        # by implenting markers we are preserving the original shifting rules to reverse accordingly
        if marker == 0:
            # for 'a' - 'm' backward shift "-(shift1 * shift2)" opposite of encryption method
            shift = -(shift1 * shift2)
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        elif marker == 1:
            # for 'n' - 'z' forward shift "+(shift1 + shift2)" opposite of encryption method
            shift = (shift1 + shift2)
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        elif marker == 2:
            # for 'A' - 'Z' forward shift "+shift1"
            shift = shift1
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif marker == 3:
            # for 'N' - 'Z' backward shift '-shift2 ** 2'
            shift = -(shift2 ** 2)
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            # all other character remains unchange
            new_char = char  
            
        decrypted += new_char

    
    cwd = os.path.dirname(__file__)
    path = os.path.join(cwd, "decrypted_text.txt")
    with open(path, 'w') as f:
        f.write(decrypted)
        print(colored("New file created for decryption data!", "green"))

    return decrypted

#Decryption Part Ends

# Pujan → Verification

def verification(original_data, decrypted_data):
    if original_data == decrypted_data:
        print(colored("Verification: Decrypted text matches the original.\n","green"))
    else:
        print(colored("Verification: Decrypted text does not match the original.\n","red"))

def main():   
    #User input
    shift1 = input("Enter shift_1 for both encryptions and decryptions(default 5): ")
    shift2 = input("Enter shift_2 for both encryptions and decryptions(default 7): ")
    
    #Input validation
    shift1 = input_validation(shift1,"shift_1")
    shift2 = input_validation(shift2,"shift_2")
    # print("\ninput validation complete!!\n")
   
    # below code find the absolute directory/folder path of the current python execution file
    # This is essential because vs-code sometimes execute code from the parents directory instead of local directory
    cwd = os.path.dirname(__file__)
    # manual debug
    # print(cwd)
    
    # This code below join the "raw_text.txt" file location with the current working directory
    path = os.path.join(cwd,"raw_text.txt")
    original_data =""
    try: 
        # Opening file in read mode
        with open(path,'r') as file:
            original_data = file.read()
    except Exception as e:
        print(colored(f"\nFile Does not exist in this directory:\n{path}\n{e}\n","red"))
        
    # this function below Encrypt the original data to produce encrypted text
    encrypted_data,markers = encryption(original_data,shift1,shift2)
    # print("\nencryption complete!!\n")
    # this function below Decrypt the encrypted data to plain text
    decrypted_data = decryption(encrypted_data,markers,shift1,shift2)
    

    # this dunction below verify if the original data and decrypted(plain text) is the same or not
    verification(original_data, decrypted_data)
    
    # Manual debugging
    # print(raw_data.read())

# this is to ensure that, this python file execute directly form here
if __name__ == "__main__":
    main()
    
'''
References:
https://thepythoncode.com/article/implement-caesar-cipher-in-python

https://dev.to/immah/implementing-a-caesar-cipher-program-in-python-1gf3

https://chat.openai.com (OpenAI GPT-4o, Sept 2025)

'''