"""
Very modest attempt at making a library on Matrix operations in Python
This isn't probably the fastest thing I could come up with, i just 
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
            raise ValueError("Parameter |" + str(el[0]) + 
            "| is of type %s but should be of type %s"
            % (el[0].__class__.__name__, el[1].__name__))

def   arrayShapeAssert(array):
    try:
        rows = len(array)
    except TypeError:
        raise TypeError("Object of", type(array), "should a two-dimension array")
    try:
        columns = len(array[0])
    except IndexError:
        raise IndexError("Object should be a two-dimensionnal array")
    for i, row in enumerate(array):
        if len(row) != columns:
            raise ValueError("Dimensions are not consistent: row [%d] is of "
            "size %d and row [%d] is of size %d"
            % (i-1, columns, i, len(row)))
            inputTypeAssert([[el, (int, float)] for el in row])
    return [row, columns]

class Matrix(object):

    def __init__(self, fill, rows = None, columns = None):
        """
        Give an integer to fill a matrix of x rows by y columns
        or give a rectangular array (consistent number of columns)
        """
        self.nrows = rows
        self.ncolumns = columns
        if type(fill) is list:
            [self.nrows, self.ncolumns] = arrayShapeAssert(fill)
            self.grid = fill
        elif isinstance(fill, (float, int)):
            if self.nrows == None or self.ncolumns == None or self.nrows <= 0 \
                or self.ncolumns <= 0:
                raise ValueError("If value provided is not an array"
                " the matrix's size must be specified by `rows` and `columns` "
                "greater than 0")
            self.newMatrix(fill, self.nrows, self.ncolumns)
        else:
            raise ValueError("Bad Value type for the first parameter")

    def newMatrix(self, value, rows, columns):
        inputTypeAssert([[rows, int], [columns, int], [value, (float, int)]])
        self.nrows = rows
        self.ncols = columns
        self.grid  = [[value for point in range(self.ncols)] for row in range(self.nrows)]