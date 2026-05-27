import Caesar_Cipher_Encrypt as cipher_enc
import Caesar_Cipher_Decrypt as cipher_dec
import Caesar_Cipher_ASCII_Art as logo

print("Welcome to the \'Caesar Cipher Encryptor!\'")
print(logo.logo)
loop_status= "yes"

while loop_status == "yes":

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    in_text = input("Type your message:\n").lower()
    in_shift = int(input("Type the shift number:\n"))
    if direction == "encode":
        cipher_enc.encrypt(in_text, in_shift)
    else:
        cipher_dec.decrypt(in_text, in_shift)
    loop_status=input("Would you like to try encoding or decoding again? (type 'yes' or 'no'):\n")

print("Thanks for working with Caesar Cipher Encryptor!, Goodbye! Have a great day!")
