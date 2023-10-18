import numpy as np

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# function for caesar cipher encryption
def caesar_encrypt(message, shift):
        encrypted = ""
        for character in message:
            if character in alphabet:
                number = alphabet.find(character)
                number = (number+shift)%len(alphabet)
                encrypted = encrypted + alphabet[number]
            else:
                encrypted = encrypted + character
        return encrypted


# function for caesar cipher decrpytion
def caesar_decrypt(message, shift):
    for shift in range(len(alphabet)):
        decrypted= ""
        for character in message:
            if character in alphabet:
                number = alphabet.find(character)
                number = (number - shift) % (len(alphabet))
                decrypted = decrypted + alphabet[number]
            else:
                decrypted = decrypted + character
        print('\nShift value: %s \n\nMessage: %s' % (shift, decrypted)) 



# Vigenere encryption function
def vigenere_encrypt(message, keyword):
    encrypted = ""
    # Ensure the keyword is in uppercase
    keyword = keyword.upper()  
    keyword_length = len(keyword)
    
    for i, character in enumerate(message):
        if character in alphabet:
            number = alphabet.find(character)
            
            # Repeating the keyword if the message is longer
            keyword_char = keyword[i % keyword_length]  
            keyword_shift = alphabet.find(keyword_char)
            number = (number + keyword_shift) % len(alphabet)
            encrypted = encrypted + alphabet[number]
        else:
            encrypted = encrypted + character
    return encrypted

#Vigenere decryption function
def vigenere_decrypt(message, keyword):
    # Empty string to store decrypted message
    decrypted = ""
    keyword = keyword.upper()
    keyword_length = len(keyword)
    x=0
    
    # Iterates through each character in encrypted message
    for i, character in enumerate(message):
        if character in alphabet:

            # Finds position of character
            number = alphabet.find(character)
            keyword_char = keyword[x % keyword_length]
            keyword_shift = alphabet.find(keyword_char)

            # Decrypts the character by shifting in reverse
            number = (number - keyword_shift) % len(alphabet)
            decrypted = decrypted + alphabet[number]
            x+=1
        else:
            decrypted = decrypted + character
    return decrypted   


# function for hill cipher 2*2 matrix encryption
def hill_encrypt(message, key_matrix):

    #Ensure the message is in uppercase and has an even length
    message = message.upper()
    if len(message) % 2 != 0:
        message += 'X'

    # convert the key matrix to a matrix
    key_matrix = np.array(key_matrix)

    # Convert the message into matrices
    plaintext_blocks  = [message[i:i+2] for i in range(0, len(message), 2)]
    ciphertext = ''

    for block in plaintext_blocks:
        input1, input2 = [ord(char) - ord('A') for char in block]
        result = np.dot(key_matrix, np.array([input1, input2])) % 26
        ciphertext += ''.join([chr(int(val) + ord('A')) for val in result]) 
    
    return ciphertext
# function for main for menu 
def main():

    print("Welcome! \n 1.Encrypt (Caesar Cipher) \n 2.Decrypt (Caesar Cipher) \n 3. Encrypt (Vinegere Cipher) \n 4. Decrypt (Vinegere Cipher) \n 5. Encrypt (Hill Cipher)")
    menu = int((input("Please choose from the options below: ")))
    
    if menu == 1:
        message = str(input("Enter the text to encrypt a message :")).upper()
        shift = int(input("Input your shift to use for encryption:"))
        encrypted = caesar_encrypt(message, shift)
        print("Encrypted Message: " , encrypted)

    elif menu == 2:
        message = input("Enter the text to decrypt: ").upper()
        shift = int(input("Enter the shift used for decryption: "))
        decrypted = caesar_decrypt(message, shift)
        print("\nDecrypted message: ", decrypted)

    elif menu == 3:
        message = input("Enter the text to encrypt: ").upper()
        keyword = input("Enter the keyword for encryption: ").upper()
        encrypted = vigenere_encrypt(message, keyword)
        print("\nEncrypted message: ", encrypted)

    elif menu == 4:
        message = input("Enter the text to decrypt: ").upper()
        keyword = input("Enter the keyword used for decryption: ").upper()
        decrypted = vigenere_decrypt(message, keyword)
        print("\nDecrypted message: ", decrypted)

    elif menu == 5:

        # Gets the key matrix from the user
        key_matrix = []
        message = input("Enter the 2x2 key matrix (4 values seperated by spaces): ")
        for i in range(2):
            row = input().split()
            # Error checking for misinput 
            if len(row) != 2:
                print("Enter 2 values per row: ")
                exit(1)
            key_matrix.append([int(val) for val in row])
        # User enters message
        message = (input("Enter the nessage you want to encrypt: "))

        # Encrypts the message using key
        ciphertext = hill_encrypt(message, key_matrix)
        print("Encrypted text: ", ciphertext)

if __name__ == "__main__":
    main()

    
            