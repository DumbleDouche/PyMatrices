"""
Very modest attempt at making a library on Matrix operations in Python

"""

__version__ = "1.0"
__all__     = ['Matrix']

def   matrix(array):
    try:
        nrows = len(array)
    except TypeError:
        raise TypeError("Object of type", type(array), "should a two-dimension array")
    try:
        ncolumns = len(array[0])
    except IndexError:
        raise IndexError("Object should be a two-dimensionnal array")
    for i, row in enumerate(array):
        if len(row) != ncolumns:
            raise ValueError("Dimensions are not consistent: [%d] is of size %d and [%d] is of size %d" % (i-1, ncolumns, i, len(row)))
    ret = Matrix(len(array), len(array[0]))
    ret.array = array
    return ret


class Matrix:

    def __init__(self, x, y, default=0):
        self.nrows = x
        self.ncols  = y
        self.array = [[default for point in range(self.ncols)] for row in range(self.nrows)]

    