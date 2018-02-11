import unittest
import pymatrices as pm

class   testArray(object):

    def __init__(self, value, result):
        self.value = value
        self.result  = result


verticalVector = testArray([[1]
                        ,[2]
                        ,[3]
                        ,[4]], [4, 1])

horizontalVector = testArray([[1, 2, 3, 4, 5]], [1, 5])

squareMatrix = testArray([[1 , 2]
                        , [3 , 4]], [2,2])

rectangularMatrix_1 = testArray([[1 , 2]
                              , [ 3 , 4]
                              , [ 5 , 6]], [3, 2])

rectangularMatrix_2 = testArray([ [1 , 2 , 3 , 0]
                                , [4 , 5 , 6 , 0]
                                , [7 , 8 , 9 , 0]], [3, 4])

matrix_1 = [[ 0, 0, 0],
            [ 0, 0, 0]]

matrix_2 = [[ 1, 1],
            [ 1, 1],
            [ 1, 1]]

matrix_3 = [[ 3, 3, 3],
            [ 3, 3, 3],
            [ 3, 3, 3]]

variable = pm.Matrix(0, 2, 3)

class TestPM(unittest.TestCase):
    
    def test_inputTypeAssert_CorrectInput(self):
        self.assertEqual(
            pm.inputTypeAssert(
                [ [1234    , int]
                , ["string", str]
                , [0.2     , (int, float)]
                , [ []     , list]
                , [ [[]]   , list]])
                , None)

    def test_inputTypeAssert_incorrectInput(self):
        self.assertRaises(TypeError,
            pm.inputTypeAssert,
            [ [1234    , str]
            , ["string", int]
            , [None    , str]
            , [0.2     , float] ])

    def test_arrayShapeAssert_notAList(self):
        self.assertRaises(TypeError,
            pm.arrayShapeAssert,
            123)

    def test_arrayShapeAssert_singleDimensionList(self):
        self.assertRaises(TypeError,
            pm.arrayShapeAssert,
            [1,2])

    def test_arrayShapeAssert_wrongList(self):
        self.assertRaises(TypeError,
            pm.arrayShapeAssert,
            list("this is a string"))

    def test_arrayShapeAssert_badElementType(self):
        self.assertRaises(TypeError,
            pm.arrayShapeAssert,
            [ [1 ,  2  , 1.2]
            , [1 , "a" ,  3 ] ])
    
    def test_arrayShapeAssert_notConsistentDimensions(self):
        self.assertRaises(IndexError,
            pm.arrayShapeAssert,
            [ [1 , 2 , 3]
            , [2 , 3 , 4]
            , [2 , 3 , 4, 5] ])

    def test_arrayShapeAssert_correctReturn_1(self):
        self.assertEqual(
            pm.arrayShapeAssert(verticalVector.value)
            , verticalVector.result)

    def test_arrayShapeAssert_correctReturn_2(self):
        self.assertEqual(
            pm.arrayShapeAssert(horizontalVector.value)
            , horizontalVector.result)

    def test_arrayShapeAssert_correctReturn_3(self):
        self.assertEqual(
            pm.arrayShapeAssert(squareMatrix.value)
            , squareMatrix.result)

    def test_arrayShapeAssert_correctReturn_4(self):
        self.assertEqual(
            pm.arrayShapeAssert(rectangularMatrix_1.value)
            , rectangularMatrix_1.result)
    
    def test_arrayShapeAssert_correctReturn_5(self):
        self.assertEqual(
            pm.arrayShapeAssert(rectangularMatrix_2.value)
            , rectangularMatrix_2.result)

    def test_newMatrix_wrongFillerType(self):
        self.assertRaises(TypeError,
        pm.Matrix, 'a', 2, 3)

    def test_newMatrix_Return_1(self):
        variable.newMatrix(0, 2, 3)
        self.assertEqual(variable.grid
        , matrix_1)

    def test_newMatrix_Return_2(self):
        variable.newMatrix(1, 3, 2)
        self.assertEqual(variable.grid
        , matrix_2)

    def test_newMatrix_Return_3(self):
        variable.newMatrix(3, 3, 3)
        self.assertEqual(variable.grid
        , matrix_3)

if __name__ == "__main__":
    unittest.main()