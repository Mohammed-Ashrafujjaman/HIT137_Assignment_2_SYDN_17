'''
Create a program that reads the text file "raw_text.txt", encrypts its contents using a 
simple encryption method, and writes the encrypted text to a new file 
"encrypted_text.txt". Then create a function to decrypt the content and a function to 
verify the decryption was successful. 

Requirements:
 
    The encryption should take two user inputs (shift1, shift2), and follow these rules: 
    • For lowercase letters: 
        o If the letter is in the first half of the alphabet (a-m): shift forward by shift1 * 
        shift2 positions 
        o If the letter is in the second half (n-z): shift backward by shift1 + shift2 
        positions 
    • For uppercase letters: 
        o If the letter is in the first half (A-M): shift backward by shift1 positions 
        o If the letter is in the second half (N-Z): shift forward by shift2² positions 
        (shift2 squared) 
    • Other characters: 
        o Spaces, tabs, newlines, special characters, and numbers remain 
        unchanged 

Main Functions to Implement:
 
    Encryption function: Reads from "raw_text.txt" and writes encrypted content to 
    "encrypted_text.txt". 

    Decryption function: Reads from "encrypted_text.txt" and writes the decrypted 
    content to "decrypted_text.txt". 

    Verification function: Compares "raw_text.txt" with "decrypted_text.txt" and prints 
    whether the decryption was successful or not. 
    Program Behavior 

When run, your program should automatically:  
    1. Prompt the user for shift1 and shift2 values 
    2. Encrypt the contents of "raw_text.txt" 
    3. Decrypt the encrypted file 
    4. Verify the decryption matches the original 

'''

'''
Group Name: Sydney Group 17
Group Members: 4
Mohammed Ashrafujjaman Hera - 391197
Pujan Dey  - 395076
Shaown Imtiaz - 396121
Al-Amin Dhaly - 395230
'''

import os

#Alamin Dhly (Encryption)
def encryption(plain_data):
    #User input
    shift1 = int(input("Enter shift1: "))
    shift2 = int(input("Enter shift2: "))

    encrypted = ""
    for char in plain_data:
        if char.islower():
            if 'a' <= char <= 'm':
                # Shift forward by shift1 * shift2
                new_char = chr((ord(char) - ord('a') + shift1 * shift2) % 26 + ord('a'))
            else:  # n-z
                # Shift backward by shift1 + shift2
                new_char = chr((ord(char) - ord('a') - (shift1 + shift2)) % 26 + ord('a'))
        elif char.isupper():
            if 'A' <= char <= 'M':
                # Shift backward by shift1
                new_char = chr((ord(char) - ord('A') - shift1) % 26 + ord('A'))
            else:  # N-Z
                # Shift forward by shift2 squared
                new_char = chr((ord(char) - ord('A') + shift2**2) % 26 + ord('A'))
        else:
            # Leave spaces, numbers, special characters unchanged
            new_char = char
        encrypted += new_char

    # Write encrypted content to file AFTER loop (merge-safe)
    cwd = os.path.dirname(__file__)
    path = os.path.join(cwd, "encrypted_text.txt")
    with open(path, 'w') as f:
        f.write(encrypted)

    return encrypted


#Encryption Part Ends

# Imtiaz (Decryption)
def decryption(encrypted_data):
    # User must enter same shift1 and shift2 used during encryption
    shift1 = int(input("Enter shift1 (for decryption): "))
    shift2 = int(input("Enter shift2 (for decryption): "))

    decrypted = ""
    for char in encrypted_data:
        if char.islower():
            if 'a' <= char <= 'm':
                # Reverse of encryption: subtract shift1 * shift2
                new_char = chr((ord(char) - ord('a') - (shift1 * shift2)) % 26 + ord('a'))
            else:  # n-z
                # Reverse: add shift1 + shift2
                new_char = chr((ord(char) - ord('a') + (shift1 + shift2)) % 26 + ord('a'))
        elif char.isupper():
            if 'A' <= char <= 'M':
                # Reverse: add shift1
                new_char = chr((ord(char) - ord('A') + shift1) % 26 + ord('A'))
            else:  # N-Z
                # Reverse: subtract shift2 squared
                new_char = chr((ord(char) - ord('A') - (shift2**2)) % 26 + ord('A'))
        else:
            # Leave unchanged
            new_char = char
        decrypted += new_char

    # Write decrypted content to file
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
    # below code find the absolute directory/folder path of the current python execution file
    cwd = os.path.dirname(__file__)
    # manual debug
    # print(cwd)
    
    # This code below join the "raw_text.txt" file location with the current working directory
    # This is essential because vs-code sometimes execute code from the parents directory instead of local directory
    path = os.path.join(cwd,"raw_text.txt")
    try: 
        # Opening file in read mode
        with open(path,'r') as original_data:
            # this function below Encrypt the original data to produce encrypted text
            encrypted_data = encryption(original_data)
            
            # this function below Decrypt the encrypted data to plain text
            decrypted_data = decryption(encrypted_data)
            
            # this dunction below verify if the original data and decrypted(plain text) is the same or not
            verification(original_data, decrypted_data)
            
            # Manual debugging
            # print(raw_data.read())
    except Exception as e:
        print(f"\nFile Does not exist in this directory:\n{cwd}\n")

# this is to ensure that, this python file execute directly form here
if __name__ == "__main__":
    main()