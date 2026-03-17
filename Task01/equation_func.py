import math

def solve_quadratic_equation(a, b, c):
    if a == 0:
        if b == 0:
            return None if c != 0 else "infinite"
        return -c / b
    
    discriminant = b**2 - 4*a*c
    
    if discriminant < 0:
        return None
    elif discriminant == 0:
        x = -b / (2*a)
        return x
    else:
        sqrt_discriminant = math.sqrt(discriminant)
        x1 = (-b - sqrt_discriminant) / (2*a)
        x2 = (-b + sqrt_discriminant) / (2*a)
        return (min(x1, x2), max(x1, x2))

if __name__ == "__main__":
    test = [
        (1, -3, 2), 
        (1, -4, 4),  
        (1, 2, 5),   
        (0, 2, -4),
        (4, -4, -3),
        (0, 0, 5),
        (0, 0, 0),
        (2, 0, -8),
        (-1, 3, -2),
        (0.5, -1, 0.5)
    ]

    for i, (a, b, c) in enumerate(test):
        print(f"{i+1}. Коэффициенты уравнения: a={a}, b={b}, c={c} | Корни: {solve_quadratic_equation(a, b, c)}\n")