#!/usr/bin/env python3
"""_summary_
"""
def matrix_shape(matrix):
    """_summary_
    Args:
        matrix (_type_): _description_
    Returns:
        _type_: _description_
    """
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        if len(matrix) == 0:
            break
        matrix = matrix[0]
    return shape
