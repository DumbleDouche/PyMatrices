"""
Very modest try at making a library on Matrix operations in Python

"""

__version__ = "1.0"
__all__     = ['Matrix']

class Matrix:

    def __init__(self, x, y, default=0):
        self.nrows = x
        self.ncols  = y
        self.array = [[default for point in range(self.ncols)] for row in range(self.nrows)]
