#!/usr/bin/env python3

from matplotlib.pylab import shape


if __name__ == "__main__":
    def matrix_shape(matrix):
        shape = []
        while isinstance(matrix, list):
            shape.append(len(matrix))
            if len(matrix) == 0:
                break
            matrix = matrix[0]
        return shape
