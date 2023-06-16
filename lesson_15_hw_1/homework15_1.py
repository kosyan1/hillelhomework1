class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def get_square(self) -> float:
        return self.width * self.height

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Rectangle):
            return self.get_square() == other.get_square()

        return NotImplemented

    def __add__(self, other: object) -> float:
        if isinstance(other, Rectangle):
            new_area = self.get_square() + other.get_square()
            return new_area

        return NotImplemented

    def __mul__(self, n: float) -> float:
        if isinstance(n, (int, float)):
            new_area = self.get_square() * n
            return new_area

        return NotImplemented

    def __str__(self) -> str:
        return f"This is rectangle"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8
assert r2.get_square() == 18

print(r1 == r2)

r3 = r1 + r2
print(r3)

r4 = r1 * 4
print(r4)
