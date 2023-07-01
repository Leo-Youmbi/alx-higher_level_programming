#!/usr/bin/python3

def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a number

    Args:
        matrix (list): The matrix to be divided
        div (int or float): The quotient of the matrix
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix[1:]):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    newMatrix = []
    for i in range(len(matrix)):
        newMatrix.append([])
        for col in matrix[i]:
            newMatrix[i].append(round(col / div, 2))
    return newMatrix
