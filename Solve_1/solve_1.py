
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
    for char in plain_data:
        if char.islower():
            if 'a' <= char <= 'm':
                new_char = chr((ord(char) - ord('a') + shift1 * shift2) % 26 + ord('a'))
            else:  # n-z
                new_char = chr((ord(char) - ord('a') - (shift1 + shift2)) % 26 + ord('a'))
        elif char.isupper():
            if 'A' <= char <= 'M':
                new_char = chr((ord(char) - ord('A') - shift1) % 26 + ord('A'))
            else:  # N-Z
                new_char = chr((ord(char) - ord('A') + shift2**2) % 26 + ord('A'))
        else:
            new_char = char
        encrypted += new_char

    # Write encrypted content to file
    cwd = os.path.dirname(__file__)
    path = os.path.join(cwd, "encrypted_text.txt")
    with open(path, 'w') as f:
        f.write(encrypted)

    return encrypted

#Encryption Part Ends

# Imtiaz (Decryption)
def decryption(encrypted_data, shift1, shift2):
    print("\nDecryption started!!\n")
    decrypted = ""
    for char in encrypted_data:
        if char.islower():
            if 'a' <= char <= 'm':
                new_char = chr((ord(char) - ord('a') - (shift1 * shift2)) % 26 + ord('a'))
            else:  # n-z
                new_char = chr((ord(char) - ord('a') + (shift1 + shift2)) % 26 + ord('a'))
        elif char.isupper():
            if 'A' <= char <= 'M':
                new_char = chr((ord(char) - ord('A') + shift1) % 26 + ord('A'))
            else:  # N-Z
                new_char = chr((ord(char) - ord('A') - (shift2**2)) % 26 + ord('A'))
        else:
            new_char = char
        decrypted += new_char

    print("New file creation for decryption data!!")
    cwd = os.path.dirname(__file__)
    path = os.path.join(cwd, "decrypted_text.txt")
    with open(path, 'w') as f:
        f.write(decrypted)

    return decrypted

# Pujan → Verification
# -------------------------------
def verification(original_data, decrypted_data):
    if original_data == decrypted_data:
        print("✅ Verification successful: Decrypted text matches the original.")
    else:
        print("❌ Verification failed: Decrypted text does not match the original.")

def main():   
    #User input
    shift1 = input("Enter shift_1 for both encryptions and decryptions(default 5): ")
    shift2 = input("Enter shift_2 for both encryptions and decryptions(default 7): ")
    
    #Input validation
    shift1 = input_validation(shift1,"shift_1")
    shift2 = input_validation(shift2,"shift_2")
    # print("\ninput validation complete!!\n")
   
    # below code find the absolute directory/folder path of the current python execution file
    cwd = os.path.dirname(__file__)
    # manual debug
    # print(cwd)
    
    # This code below join the "raw_text.txt" file location with the current working directory
    # This is essential because vs-code sometimes execute code from the parents directory instead of local directory
    path = os.path.join(cwd,"raw_text.txt")
    original_data =""
    try: 
        # Opening file in read mode
        with open(path,'r') as file:
            original_data = file.read()
    except Exception as e:
        print(colored(f"\nFile Does not exist in this directory:\n{path}\n{e}\n","red"))
        
    # this function below Encrypt the original data to produce encrypted text
    encrypted_data = encryption(original_data,shift1,shift2)
    # print("\nencryption complete!!\n")
    # this function below Decrypt the encrypted data to plain text
    decrypted_data = decryption(encrypted_data,shift1,shift2)
    

    # this dunction below verify if the original data and decrypted(plain text) is the same or not
    # verification(original_data, decrypted_data)
    
    # Manual debugging
    # print(raw_data.read())

# this is to ensure that, this python file execute directly form here
if __name__ == "__main__":
    main()