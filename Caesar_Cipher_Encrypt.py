alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
    text_map = []
    cipher_map = []
    cipher_text_list = []
    for char in text:
        if char in alphabet:
            idx = alphabet.index(char)
            text_map.append(idx)
        else:
            text_map.append(char)
    for idx in text_map:
        if type(idx) == int:
            cipher_map.append(idx + shift)
        else:
            cipher_map.append(idx)
    for idx in cipher_map:
        if type(idx) == int:
            cipher_text_list.append(alphabet[idx % 26])
        else:
            cipher_text_list.append(idx)
    cipher_text = "".join(cipher_text_list)

    print("The encoded cipher text is,", cipher_text)
