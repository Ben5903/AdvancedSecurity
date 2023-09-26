alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def caesar_encrypt(message, shift):
        encrypt = ""
        for character in message:
            if character in alphabet:
                number = alphabet.find(character)
                number = (number+shift)%len(alphabet)
                encrypt = encrypt + alphabet[number]
            else:
                encrypt = encrypt + character
        print(encrypt)

def caesar_decrypt(message):
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
          
                

def main():

    print("Welcome! \n 1.Encrypt (Caesar Cipher) \n 2.Decrypt (Caesar Cipher)")
    menu = int((input("Please choose from the options below: ")))
    
    if menu == 1:
        message = str(input("Enter the text to encrypt a message :"))
        message = message.upper()
        shift = int(input("Input your shift to use for encryption:"))
        caesar_encrypt(message, shift)

    elif menu == 2: 
        message = str(input("Insert message to be decrypted"))
        caesar_decrypt(message)



if __name__ == "__main__":
    main()


    
            