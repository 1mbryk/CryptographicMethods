from pprint import pprint
from functions import *


class FeistelCipher:

    def __init__(self, key: str):
        if (len(key) != 12):
            raise Exception("The length of key must be 12!")

        self.plaintext = ""
        self.ciphertext = ""
        self.encoded_text = []
        self.decoded_text = ""
        self.encrypted_text = []
        self.key = key
        self.decrypted_text = []

        k = [[1, 4, 7, 10, 2, 5, 8, 11],
             [2, 5, 8, 11, 3, 6, 9, 12],
             [3, 6, 9, 12, 10, 4, 7, 1]]
        self.round_keys = [int(''.join(key[x-1] for x in y), 2) for y in k]
        self.AMOUNT_ROUND_KEYS = len(self.round_keys)

        self.S = [
            [10, 9, 13, 6, 14, 11, 4, 5, 15, 1, 3, 12, 7, 0, 8, 2],
            [8, 0, 12, 4, 9, 6, 7, 11, 2, 3, 1, 15, 5, 14, 10, 13],
            [15, 6, 5, 8, 14, 11, 10, 4, 12, 0, 3, 7, 2, 9, 1, 13],
            [3, 8, 13, 9, 6, 11, 15, 0, 2, 5, 12, 10, 4, 14, 1, 7],
            [15, 8, 14, 9, 7, 2, 0, 13, 12, 6, 1, 5, 11, 4, 3, 10],
            [2, 8, 9, 7, 5, 15, 0, 11, 12, 1, 13, 14, 10, 3, 6, 4],
            [3, 8, 11, 5, 6, 4, 14, 10, 2, 12, 1, 7, 9, 15, 14, 0],
            [1, 2, 3, 14, 6, 13, 11, 8, 15, 10, 12, 5, 7, 9, 0, 4]]

    def read(self, filepath: str, type="plaintext"):
        f = open(filepath)
        text = f.read()
        f.close()
        if len(text) % 2 != 0:
            raise Exception("The length of the text must be an even!")
        if type == 'plaintext':
            self.plaintext = text
            self.__encode(True)
        elif type == 'ciphertext':
            self.ciphertext = text
            self.__encode(False)

    def write(self, filepath: str, type='ciphertext'):
        if type == 'ciphertext':
            text = self.ciphertext
        elif type == 'plaintext':
            text = self.plaintext
        f = open(filepath, 'w')
        f.write(text)
        f.close()

    def __encode(self, mode: bool):  # mode True – encrypt, False – decrypt
        if mode:
            self.encoded_text = [ord(x) for x in self.plaintext]
        else:
            self.encoded_text = [ord(x) for x in self.ciphertext]

        self.encoded_text = [self.encoded_text[i * 2:(i + 1)*2]
                             for i in range(len(self.encoded_text)//2)]

    def __decode(self, mode: bool):  # mode True – encrypt, False – decrypt
        if mode:
            self.decoded_text = ''.join(chr(x) for x in self.encrypted_text)
        else:
            self.decoded_text = ''.join(chr(x) for x in self.decrypted_text)

    def __subtitution(self, round: int, t: int):
        return self.S[round % len(self.S)][t]

    def __inner_loop(self, left: int, right: int, i: int):
        t = to_bin(right ^ self.round_keys[i % self.AMOUNT_ROUND_KEYS], 8)
        t1 = int(t[:4], 2)
        t2 = int(t[4:], 2)
        n1 = self.__subtitution(i, t1)
        n2 = self.__subtitution(i, t2)
        tmp = cycle_shift(int(to_bin(n1, 4) + to_bin(n2, 4), 2), 4)

        left ^= tmp
        left, right = right, left
        return (left, right)

    def encrypt(self, round_amount: int):
        for left, right in self.encoded_text:
            for i in range(round_amount):
                left, right = self.__inner_loop(left, right, i)
            self.encrypted_text.append(left)
            self.encrypted_text.append(right)
        self.__decode(True)
        self.ciphertext = self.decoded_text

    def decrypt(self, round_amount: int):
        self.__encode(False)
        for right, left in self.encoded_text:
            for i in range(round_amount-1, -1, -1):
                left, right = self.__inner_loop(left, right, i)
            self.decrypted_text.append(right)
            self.decrypted_text.append(left)
        self.__decode(False)

    def get_encrypted(self):
        return self.ciphertext

    def get_decrypted(self):
        return self.plaintext
