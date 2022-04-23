import unittest

from White import Triangle


class MyTest(unittest.TestCase):
    # 编写测试用例，记得要以t开头，例：test
    def testTriangle(self):
        # 调用内部的测试方法，如：assertEqual,assertNotEqual 等
        self.assertEqual(Triangle.triangle("3", 4, 5), "not a triangle!")
        self.assertEqual(Triangle.triangle(3.1, 4, 5), "not a triangle!")
        self.assertEqual(Triangle.triangle(0, 4, 5), "not a triangle!")
        self.assertEqual(Triangle.triangle(10001, 4, 5), "not a triangle!")
        self.assertEqual(Triangle.triangle(3, 3, 9), "not a triangle!")
        self.assertEqual(Triangle.triangle(3, 3, 3), "equilateral triangle!")
        self.assertEqual(Triangle.triangle(3, 3, 4), "isosceles triangle!")
        self.assertEqual(Triangle.triangle(3, 4, 4), "isosceles triangle!")
        self.assertEqual(Triangle.triangle(3, 4, 3), "isosceles triangle!")
        self.assertEqual(Triangle.triangle(3, 4, 5), "regular triangle!")

    pass


# 运行测试
if __name__ == '__main__':
    unittest.main()
