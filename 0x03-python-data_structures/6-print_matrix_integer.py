#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        mat_len = len(matrix[i])
        for j in range(mat_len):
            if j != mat_len -1:
                endN = ' '
            else:
                endN = ''
            print("{:d}".format(matrix[i][j]), end=endN)
        print("")
