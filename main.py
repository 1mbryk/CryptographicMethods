"""
* Variant: 15
- p: 722227767914309
- q: 645306156219341
- e: 188343213856435087990117867713
- X1: 340693830559923670446313718411
- Y2: 401641252598150824512742688568
"""
from RSA import RSA


def main():
    cryptor = RSA('lab3/data-1.json')
    while True:
        option = input()
        cryptor(option)


if __name__ == '__main__':
    main()
