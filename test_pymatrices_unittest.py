import unittest
import pymatrices as pm

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
            pm.arrayShapeAssert(
                [ [1]
                , [2]
                , [3]
                , [4] ])
                , [4,1])

    def test_arrayShapeAssert_correctReturn_2(self):
        self.assertEqual(
            pm.arrayShapeAssert(
                [ [1, 2, 3, 4, 5] ])
                , [1,5])

    def test_arrayShapeAssert_correctReturn_3(self):
        self.assertEqual(
            pm.arrayShapeAssert(
                [ [1 , 2]
                , [3 , 4] ])
                , [2,2])

    def test_arrayShapeAssert_correctReturn_4(self):
        self.assertEqual(
            pm.arrayShapeAssert(
                [ [1 , 2]
                , [3 , 4]
                , [5 , 6] ])
                , [3, 2])
    
    def test_arrayShapeAssert_correctReturn_5(self):
        self.assertEqual(
            pm.arrayShapeAssert(
                [ [1 , 2 , 3 , 0]
                , [4 , 5 , 6 , 0]
                , [7 , 8 , 9 , 0] ])
                , [3,4])

if __name__ == "__main__":
    unittest.main()