alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

def decrypt(cipher, shift):
    cipher_map = []
    text_map = []
    decrypted_text_list = []
    for char in cipher:
        if char in alphabet:
            idx = alphabet.index(char)
            cipher_map.append(idx)
        else:
            cipher_map.append(char)
    for idx in cipher_map:
        if type(idx) == int:
            text_map.append(idx - shift)
        else:
            text_map.append(idx)
    for idx in text_map:
        if type(idx) == int:
            decrypted_text_list.append(alphabet[idx % 26])
        else:
            decrypted_text_list.append(idx)
    decrypted_text = "".join(decrypted_text_list)

    print("The encoded message text is,", decrypted_text)
