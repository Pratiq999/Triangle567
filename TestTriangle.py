

"""
The primary goal of this file is to demonstrate a simple unittest implementation

@author: "Pratik Kadam"
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality

class TestTriangles(unittest.TestCase):
    #Testing equilateral triangles
    def testEquilateralTriangle1(self):
        self.assertEqual(classifyTriangle(3,3,3),'Equilateral')

    def testEquilateralTriangle2(self):
        self.assertEqual(classifyTriangle(11,11,11),'Equilateral')

    def testEquilateralTriangle3(self):
        self.assertEqual(classifyTriangle(9,1,9),'Equilateral')

    #Testing Isosceles Triangles
    def testIsoscelesTriangle1(self):
        self.assertEqual(classifyTriangle(4,4,2),'Isosceles')

    def testIsoscelesTriangle2(self):
        self.assertEqual(classifyTriangle(3,5,5),'Isosceles')

    def testIsoscelesTriangle3(self):
        self.assertEqual(classifyTriangle(6,4,6),'Isosceles')

    def testIsoscelesTriangle4(self):
        self.assertEqual(classifyTriangle(7,7,3),'Isosceles')

    #Testing Scalene Triangles
    def testScaleneTriangle1(self):
        self.assertEqual(classifyTriangle(10,11,12),'Scalene')

    def testScaleneTriangle2(self):
        self.assertEqual(classifyTriangle(3,2,4),'Scalene')

    def testScaleneTriangle3(self):
        self.assertEqual(classifyTriangle(90,95,101),'Scalene')

    def testScaleneTriangle4(self):
        self.assertNotEqual(classifyTriangle(6,6,4),'Scalene')

    #Testing invalid inputs
    def testInvalidInput1(self):
        self.assertEqual(classifyTriangle(-2,-2,-2),'Invalid Input')

    def testInvalidInput2(self):
        self.assertEqual(classifyTriangle("1","2","0"),'Invalid Input')

    #Testing not a triangle
    def testNotATriangle1(self):
        self.assertEqual(classifyTriangle(4,2,2),'Not A Triangle')

    def testNotATriangle2(self):
        self.assertEqual(classifyTriangle(2,4,2),'Not A Triangle')

    def testNotATriangle3(self):
        self.assertEqual(classifyTriangle(2,2,4),'Not A Triangle')

    #Testing right angle triangle
    def testRightTriangle1(self):
        self.assertEqual(classifyTriangle(3,4,5),'Right Angled Triangle')

    def testRightTriangle2(self):
        self.assertEqual(classifyTriangle(5,3,4),'Right Angled Triangle')

    def testRightTriangle3(self):
        self.assertEqual(classifyTriangle(13,12,5),'Right Angled Triangle')

    def testRightTriangle4(self):
        self.assertEqual(classifyTriangle(8,6,10),'Right Angled Triangle')

    def testRightTriangle5(self):
        self.assertNotEqual(classifyTriangle(19,5,11),'Right Angled Triangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

