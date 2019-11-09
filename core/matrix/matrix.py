from typing import List

class Matrix(object):
    def __init__(self, matrix_string: str) -> 'Matrix':
        """Create a matrix from the given string"""
        self.matrix = [[int(c) for c in row.split()] for row in matrix_string.splitlines()]

    def row(self, index: int) -> List[int]:
        """Return the given row as a list"""

        if index <= 0 or index > len(self.matrix):
            raise IndexError("Index out of range")
        return self.matrix[index-1]


    def column(self, index: int) -> List[int]:
        """Return the given column as a list"""

        if index <= 0 or index > len(self.matrix[0]):
            raise IndexError("Index out of range")

        return [self.matrix[r][index-1] for r in range(len(self.matrix))]

