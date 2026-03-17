import unittest
from triangle_func import get_triangle_type, IncorrectTriangleSides

class TestTriangleType(unittest.TestCase):
    def test_equilateral(self):
        self.assertEqual(get_triangle_type(7, 7, 7), "equilateral")
        self.assertEqual(get_triangle_type(12, 12, 12), "equilateral")
        self.assertEqual(get_triangle_type(0.5, 0.5, 0.5), "equilateral")
    
    def test_isosceles(self):
        self.assertEqual(get_triangle_type(5, 5, 3), "isosceles")
        self.assertEqual(get_triangle_type(6, 8, 6), "isosceles")
        self.assertEqual(get_triangle_type(17.9, 30.1, 30.1), "isosceles")
    
    def test_nonequilateral(self):
        self.assertEqual(get_triangle_type(3, 4, 5), "nonequilateral")
        self.assertEqual(get_triangle_type(7.5, 10.5, 12.5), "nonequilateral")
        self.assertEqual(get_triangle_type(5, 6, 7), "nonequilateral")
    
    def test_zero_or_negative_sides(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(0, 7, 7)
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(-1, 5, 5)
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(0, 0, 0)
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(-6, 0.5, 0)
    
    def test_invalid_triangle_inequality(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1.5, 2.5, 10.5)
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 10, 2)
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 2, 3)
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 1, 2)

if __name__ == '__main__':
    import doctest
    print("Запуск doctest")
    doctest.testmod()
    print("\nЗапуск unittest")
    unittest.main()