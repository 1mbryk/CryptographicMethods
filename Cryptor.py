from functions import *


class Cryptor:
    def __init__(self, key: str):
        self.S1 = [15, 6, 5, 8, 14, 11, 10, 4, 12, 0, 3, 7, 2, 9, 1, 13]
        self.S2 = [1, 2, 3, 14, 6, 13, 11, 8, 15, 10, 12, 5, 7, 9, 0, 4]
        self.P = [1, 3, 5, 7, 2, 4, 6, 8]
        self.K = key
        k = [[1, 4, 7, 10, 2, 5, 8, 11],
             [2, 5, 8, 11, 3, 6, 9, 12],
             [3, 6, 9, 12, 10, 4, 7, 1]]
        self.round_keys = [int(''.join(key[x-1] for x in y), 2) for y in k]
        self.AMOUNT_ROUND_KEYS = len(self.round_keys)

    def __subtitution(self, s, t):
        return to_bin(s[t], 4)

    def __permutation(self, p: list, t: str):
        return ''.join(t[x-1] for x in p)

    def encrypt(self, msg):
        for i in range(self.AMOUNT_ROUND_KEYS):
            t = to_bin(int(msg, 2) ^ self.round_keys[i], 8)
            t1, t2 = t[:4], t[4:]
            n = self.__subtitution(self.S1, int(t1, 2)) + \
                self.__subtitution(self.S2, int(t2, 2))
            encrypted = self.__permutation(self.P, n)
            print(f"Y on round {i}: {encrypted}")
        return encrypted
