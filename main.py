"""
# variant 15

summary type: "круглый плюс"

round keys:
1 – (1, 4, 7, 10, 2, 5, 8, 11)
2 – (2, 5, 8, 11, 3, 6, 9, 12)
3 – (3, 6, 9, 12, 10, 4, 7, 1)

s1 block: 3 // [F, 6, 5, 8, E, B, A, 4, C, 0, 3, 7, 2, 9, 1, D]
s2 block: 8 // [1, 2, 3, E, 6, D, B, 8, F, A, C, 5, 7, 9, 0, 4]

p block: (1, 3, 5, 7, 2, 4, 6, 8)
"""

from FeistelCipher import FeistelCipher
from Cryptor import Cryptor
from functions import *


X = to_bin(9 * 15, 8)
K = to_bin(abs(4096 - 13 * len('macviej')*len('pazhytnykh')), 12)


def main():
    print('\nPART ONE:\n')
    print(f"key: {K}")
    cryptor = Cryptor(K)
    print(f"msg: {X}")
    cryptor.encrypt(X)
    print('')

    msg = to_bin(int(X, 2) ^ 16, 8)
    print(f"msg: {msg}")
    cryptor.encrypt(msg)
    print()

    msg = to_bin(int(X, 2) ^ 128, 8)
    print(f"msg: {msg}")
    cryptor.encrypt(msg)

    print('\nPART TWO')
    ROUNDS = 6
    cryptor = FeistelCipher(K)
    cryptor.read('./texts/text.txt', 'plaintext')
    print(f'plaintext: {cryptor.get_decrypted()}')
    cryptor.encrypt(ROUNDS)
    print(f'ciphertext: {cryptor.get_encrypted()}')
    cryptor.write('./texts/encrypted.txt', 'ciphertext')
    cryptor.read('./texts/encrypted.txt', 'ciphertext')
    cryptor.decrypt(ROUNDS)
    cryptor.write('./texts/decrypted.txt', 'plaintext')
    print(f'decrypted: {cryptor.get_decrypted()}')


if __name__ == '__main__':
    main()
