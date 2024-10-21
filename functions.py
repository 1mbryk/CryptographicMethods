import numpy as np

ALPHABET = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


def get_modular_invers(a, m):
    x = 1
    a = int(a)
    while True:
        if (a * x) % m == 1:
            return x
        x += 1


def get_minor(matrix, i, j):
    minor = []
    for ii in range(len(matrix)):
        vec = []
        if ii != i:
            for jj in range(len(matrix)):
                if jj != j:
                    vec.append(matrix[ii][jj])
            minor.append(vec)
    return minor


def get_adj_matrix(matrix):
    adj_matrix = []
    for i in range(len(matrix)):
        vec = []
        for j in range(len(matrix)):
            minor = get_minor(matrix, i, j)
            det = (np.linalg.det(minor))
            if det - int(det) > 0.5:
                det = det // 1 + 1
            else:
                det = det // 1
            adj = int((-1) ** (i + j) * det)
            vec.append(adj % len(ALPHABET))
        adj_matrix.append(vec)
    return np.linalg.matrix_transpose(adj_matrix)


def get_inverse_matrix(matrix):
    det = np.linalg.det(matrix)
    inv_det = get_modular_invers(det, len(ALPHABET))
    adj_matrix = get_adj_matrix(matrix)
    inv_matrix = [
        [int(x * inv_det) % len(ALPHABET) for x in vec]
        for vec in adj_matrix
    ]
    return inv_matrix


def multiplication(vec, matrix):
    res = list()
    for i in range(2):
        mul = 0
        for ii in range(2):
            mul += vec[ii] * matrix[ii][i]
        res.append(int(mul))
    return res
