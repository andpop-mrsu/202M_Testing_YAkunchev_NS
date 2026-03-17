class IncorrectTriangleSides(Exception):
    pass

def get_triangle_type(a, b, c):
    """   
    >>> get_triangle_type(7, 7, 7)
    'equilateral'
    
    >>> get_triangle_type(5, 5, 3)
    'isosceles'
    
    >>> get_triangle_type(6, 8, 6)
    'isosceles'

    >>> get_triangle_type(3, 4, 5)
    'nonequilateral'

    >>> get_triangle_type(12, 12, 12)
    'equilateral'

    >>> get_triangle_type(7.5, 10.5, 15.5)
    'nonequilateral'
    
    >>> get_triangle_type(0, 7, 7)
    Traceback (most recent call last):
        ...
    IncorrectTriangleSides: Стороны должны быть больше нуля

    >>> get_triangle_type(-1, 5, 5)
    Traceback (most recent call last):
        ...
    IncorrectTriangleSides: Стороны должны быть больше нуля
    
    >>> get_triangle_type(1, 2, 3)
    Traceback (most recent call last):
        ...
    IncorrectTriangleSides: Недопустимые стороны треугольника: сумма двух сторон должна быть больше третьей
    
    >>> get_triangle_type(1.5, 2.5, 10.5)
    Traceback (most recent call last):
        ...
    IncorrectTriangleSides: Недопустимые стороны треугольника: сумма двух сторон должна быть больше третьей

    >>> get_triangle_type(0, 0, 0)
    Traceback (most recent call last):
        ...
    IncorrectTriangleSides: Стороны должны быть больше нуля

    >>> get_triangle_type(1, 1, 2)
    Traceback (most recent call last):
        ...
    IncorrectTriangleSides: Недопустимые стороны треугольника: сумма двух сторон должна быть больше третьей
    """
    if a <= 0 or b <= 0 or c <= 0:
        raise IncorrectTriangleSides("Стороны должны быть больше нуля")
    
    if a + b <= c or a + c <= b or b + c <= a:
        raise IncorrectTriangleSides("Недопустимые стороны треугольника: сумма двух сторон должна быть больше третьей")
    
    if a == b == c:
        return "equilateral"
    elif a == b or a == c or b == c:
        return "isosceles"
    else:
        return "nonequilateral"