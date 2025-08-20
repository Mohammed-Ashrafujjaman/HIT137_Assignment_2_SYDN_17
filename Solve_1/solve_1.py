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