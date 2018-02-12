"""
Very modest attempt at making a library on Matrix operations in Python
This probably isn't the fastest thing I could've came up with, i just 
tried to make it relatively easy to debug.
I'll probably have a version, without any debugging elements, which i'll
use whenever their use in the general algorithm is safe and sound.
"""

__version__ = "1.1"
__all__     = ['Matrix']

def   inputTypeAssert(inputs):
    """
    Asserting Input Type
    """
    for el in inputs:
        if not isinstance(el[0], el[1]):
            types = [el[1][i].__name__ for i, x in enumerate(el[1])]
            if len(el[1]) > 1:
                types = " or ".join([', '.join(types[:-1]),types[-1]])
            raise TypeError("Parameter |" + str(el[0]) + 
            "| is of type %s but should be of type %s"
            % (el[0].__class__.__name__, types))

def   arrayShapeAssert(array):
    try:
        rows = len(array)
    except TypeError:
        raise TypeError("Object of type " + array.__class__.__name__ +
        " should a two-dimension array")
    try:
        columns = len(array[0])
    except TypeError:
        raise TypeError("Object should be a two-dimensionnal array")
    for i, row in enumerate(array):
        if len(row) != columns:
            raise IndexError("Dimensions are not consistent: row [%d] is of "
            "size %d and row [%d] is of size %d"
            % (i-1, columns, i, len(row)))
        inputTypeAssert([[el, (int, float)] for el in row])
    return [rows, columns]

class Matrix(object):

    def __init__(self, fill, rows = None, columns = None):
        """
        Give an integer to fill a matrix of x rows by y columns
        or give a rectangular array (consistent number of columns)
        """
        self.newMatrix(fill, rows, columns)

    def newMatrix(self, fill, rows=None, columns=None):
        self.nrows = rows
        self.ncolumns = columns
        if type(fill) is list:
            [self.nrows, self.ncolumns] = arrayShapeAssert(fill)
            self.__grid__ = fill
        elif isinstance(fill, (float, int)):
            inputTypeAssert([[rows, int], [columns, int]])
            self.__grid__  = [[float(fill) for point in range(self.ncolumns)] for row in range(self.nrows)]
        else:
            raise TypeError("Bad Value type for the first parameter")

    def __add__(self, other):
        if isinstance(other, (float, int)):
            for n, el in enumerate(self.__grid__):
                for m, point in enumerate(el):
                    self.__grid__[i][j] += other
        elif isinstance(other, list):
            [rows, cols] = arrayShapeAssert(other)
            if [rows, cols] == [self.nrows, self.ncolumns]:
                return [[self.__grid__[n][m] + other[n][m] for m in range(cols)] for n in range(rows)]
            else:
                raise IndexError("Dimensions do not match")
        else:
            raise TypeError("Add either a scalar or a matrix of same dimensions")
                        

                    
