import pytest
import math
from triangle_class import Triangle, IncorrectTriangleSides
 
def test_equilateral_triangle():
    """Тест создания равностороннего треугольника"""
    triangle1 = Triangle(7, 7, 7)
    assert triangle1.triangle_type() == "equilateral"
    assert triangle1.perimeter() == 21

    triangle2 = Triangle(12, 12, 12)
    assert triangle2.triangle_type() == "equilateral"
    assert triangle2.perimeter() == 36

def test_isosceles_triangle():
    """Тест создания равнобедренного треугольника"""
    triangle1 = Triangle(5, 5, 3)
    assert triangle1.triangle_type() == "isosceles"
    assert triangle1.perimeter() == 13
    
    triangle2 = Triangle(6, 8, 6)
    assert triangle2.triangle_type() == "isosceles"
    assert triangle2.perimeter() == 20

def test_nonequilateral_triangle():
    """Тест создания разностороннего треугольника"""
    triangle1 = Triangle(3, 4, 5)
    assert triangle1.triangle_type() == "nonequilateral"
    assert triangle1.perimeter() == 12
    
    triangle2 = Triangle(7.5, 10.5, 15.5)
    assert triangle2.triangle_type() == "nonequilateral"
    assert triangle2.perimeter() == 33.5

def test_negative_side():
    """Тест на отрицательные стороны"""
    with pytest.raises(IncorrectTriangleSides) as info:
        Triangle(-1, 5, 5)
    assert str(info.value) == "Стороны должны быть больше нуля"
    
    with pytest.raises(IncorrectTriangleSides) as info:
        Triangle(5, -2, 5)
    assert str(info.value) == "Стороны должны быть больше нуля"
    
    with pytest.raises(IncorrectTriangleSides) as info:
        Triangle(1, 2, -3)
    assert str(info.value) == "Стороны должны быть больше нуля"

def test_zero_side():
    """Тест на нулевые стороны"""
    with pytest.raises(IncorrectTriangleSides) as info:
        Triangle(0, 7, 7)
    assert str(info.value) == "Стороны должны быть больше нуля"
    
    with pytest.raises(IncorrectTriangleSides) as info:
        Triangle(5, 0, 5)
    assert str(info.value) == "Стороны должны быть больше нуля"
    
    with pytest.raises(IncorrectTriangleSides) as info:
        Triangle(0, 0, 0)
    assert str(info.value) == "Стороны должны быть больше нуля"

def test_triangle_inequality_violation():
    """Тест на нарушение неравенства треугольника"""
    with pytest.raises(IncorrectTriangleSides) as info:
        Triangle(1.5, 2.5, 10.5)
    assert str(info.value) == "Недопустимые стороны треугольника: сумма двух сторон должна быть больше третьей"
    
    with pytest.raises(IncorrectTriangleSides) as info:
        Triangle(1, 1, 2)
    assert str(info.value) == "Недопустимые стороны треугольника: сумма двух сторон должна быть больше третьей"
    
    with pytest.raises(IncorrectTriangleSides) as info:
        Triangle(1, 2, 3) 
    assert str(info.value) == "Недопустимые стороны треугольника: сумма двух сторон должна быть больше третьей"

def test_valid_triangle_creation():
    """Тест корректного создания треугольника"""
    triangle = Triangle(7, 8, 9)
    assert isinstance(triangle, Triangle)
    assert triangle.a == 7
    assert triangle.b == 8
    assert triangle.c == 9

if __name__ == "__main__":
    pytest.main([__file__, "-v"])