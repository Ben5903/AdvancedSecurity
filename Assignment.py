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
        print('Shift value %s \n Message: %s' % (shift, decrypted))


# Vigenere encryption function
def vigenere_encrypt(message, keyword):
    encrypted = ""
    keyword = keyword.upper()  # Ensure the keyword is in uppercase
    keyword_length = len(keyword)
    
    for i, character in enumerate(message):
        if character in alphabet:
            number = alphabet.find(character)
            keyword_char = keyword[i % keyword_length]  # Repeating the keyword if the message is longer
            keyword_shift = alphabet.find(keyword_char)
            number = (number + keyword_shift) % len(alphabet)
            encrypted = encrypted + alphabet[number]
        else:
            encrypted = encrypted + character
    return encrypted

#Vigenere decryption function
def vigenere_decrypt(message, keyword):
    decrypted = ""
    keyword = keyword.upper()
    keyword_length = len(keyword)

    for i, character in enumerate(message):
        if character in alphabet:
            number = alphabet.find(character)
            keyword_char = keyword[i % keyword_length]
            keyword_shift = alphabet.find(keyword_char)
            number = (number - keyword_shift) % len(alphabet)
            decrypted = decrypted + alphabet[number]
        else:
            decrypted = decrypted + character
    return decrypted   
          
                
# function for main for menu 
def main():

    print("Welcome! \n 1.Encrypt (Caesar Cipher) \n 2.Decrypt (Caesar Cipher) \n 3. Encrypted (Vinegere Cipher) \n 4. Decrypt (Vinegere Cipher)")
    menu = int((input("Please choose from the options below: ")))
    
    if menu == 1:
        message = str(input("Enter the text to encrypt a message :")).upper()
        shift = int(input("Input your shift to use for encryption:"))
        encrypted = caesar_encrypt(message, shift)
        print("Encrypted Message: " , encrypted)

    elif menu == 2:
        message = input("Enter the text to decrypt: ").upper()
        shift = int(input("Enter the shift used for encryption: "))
        decrypted = caesar_decrypt(message, shift)
        print("Decrypted message:", decrypted)

    elif menu == 3:
        message = input("Enter the text to encrypt: ").upper()
        keyword = input("Enter the keyword for encryption: ").upper()
        encrypted = vigenere_encrypt(message, keyword)
        print("Encrypted message:", encrypted)

    elif menu == 4:
        message = input("Enter the text to decrypt: ").upper()
        keyword = input("Enter the keyword used for encryption: ").upper()
        decrypted = vigenere_decrypt(message, keyword)
        print("Decrypted message:", decrypted)



if __name__ == "__main__":
    main()


    
            