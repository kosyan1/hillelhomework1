class Fraction:
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b

    def __mul__(self, other: 'Fraction') -> 'Fraction':
        a = self.a * other.a
        b = self.b * other.b
        return Fraction(a, b)

    def __add__(self, other: 'Fraction') -> 'Fraction':
        a = self.a * other.b + self.b * other.a
        b = self.b * other.b
        return Fraction(a, b)

    def __sub__(self, other: 'Fraction') -> 'Fraction':
        a = self.a * other.b - self.b * other.a
        b = self.b * other.b
        return Fraction(a, b)

    def __eq__(self, other) -> bool:
        return self.a / self.b == other.a / other.b

    def __gt__(self, other) -> bool:
        return self.a / self.b > other.a / other.b

    def __lt__(self, other) -> bool:
        return self.a / self.b < other.a / other.b

    def __str__(self) -> str:
        return f"Fraction: {self.a}, {self.b}"


f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
print(f_c)
assert str(f_c) == 'Fraction: 21, 18'
f_d = f_b * f_a
print(f_d)
assert str(f_d) == 'Fraction: 6, 18'
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'
print(f_e)

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
