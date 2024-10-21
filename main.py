from functions import *

original_text = 'ПАЖИТНЫХ'
encode = dict()
decode = dict()
for i, letter in enumerate(ALPHABET):
    encode[letter] = i
    decode[i] = letter


def encrypt(text: str, key):
    is_odd = False
    if len(text) & 1 != 0:
        text += 'А'
        is_odd = True

    encoded_text = [encode[x] for x in text]
    encrypted = []

    for i in range(0, len(encoded_text), 2):
        encrypted += multiplication(encoded_text[i: i+2], key)

    encrypted_text = ""
    for letter in encrypted:
        encrypted_text += decode[letter % len(ALPHABET)]

    if is_odd:
        encrypted_text = encrypted_text[:-1]
    return encrypted_text


def decrypt(text: str, key):
    is_odd = False
    if len(text) & 1 != 0:
        text += 'А'
        is_odd = True

    encoded_text = [encode[x] for x in text]
    decrypted = []

    for i in range(0, len(encoded_text), 2):
        decrypted += multiplication(encoded_text[i:i+2], key)
    decrypted_text = ""
    for letter in decrypted:
        decrypted_text += decode[letter % len(ALPHABET)]

    if is_odd:
        decrypted_text = decrypted_text[:-1]
    return decrypted_text


# text = encrypt(original_text, matrix)
# print(text)
# text = decrypt(text, [[13, 25], [10, 12]])
# print(text)

def main():
    matrix = [
        [9, 28],
        [31, 29]]

    text = 'ПАЖИТНЫХ'
    encrypted = encrypt(text, matrix)
    print(f'Encrypted text: {encrypted}')
    decrypted = decrypt(encrypted, get_inverse_matrix(matrix))
    print(f'Decrupted text: {decrypted}')

    print('-'*25)

    encrypted = 'ЁЦФЮЗЮ'
    print(f'Encrypted text: {encrypted}')
    matrix = [
        [21, 20],
        [11, 30]
    ]
    decrypted = decrypt(encrypted, get_inverse_matrix(matrix))
    print(f'Decrypted text: {decrypted}')


if __name__ == '__main__':
    main()
