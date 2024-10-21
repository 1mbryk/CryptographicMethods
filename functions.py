def to_bin(num: int, length: int):
    binary = bin(num).removeprefix('0b')
    diff = length - len(binary)
    return '0' * diff + binary


def cycle_shift(n, d):
    return ((n << d) % (1 << 8)) | (n >> (8 - d))
