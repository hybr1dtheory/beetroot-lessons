from functools import total_ordering


def gcd(a: int, b: int):
    """Find the greatest common divisor to reduce fractions"""
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b


@total_ordering  # decorator to simplify the implementation of comparison operations
class MyFraction:
    """Represents simple fractions type with / as separator. Fractions are always reduced"""
    def __init__(self, nom: int, denom=1):
        if not (isinstance(nom, int) and isinstance(denom, int)):
            raise ValueError("MyFraction attributes must be integer")
        elif denom == 0:
            raise ZeroDivisionError
        gd = gcd(abs(nom), abs(denom))
        self.sign = -1 if (nom < 0 < denom) or (nom > 0 > denom) else 1
        self.nom = abs(nom) // gd
        self.denom = abs(denom) // gd

    def __str__(self):
        if self.denom == 1:
            return str(self.nom * self.sign)
        elif self.nom == 0:
            return '0'
        else:
            return f"{self.nom * self.sign}/{self.denom}"

    def __eq__(self, other):
        return self.nom == other.nom and self.denom == other.denom and self.sign == other.sign

    def __gt__(self, other):
        return (self.nom * self.sign / self.denom) > (other.nom * other.sign / other.denom)

    def __mul__(self, other):
        if not isinstance(other, MyFraction):
            raise TypeError("Class MyFraction do not support operations with other types")
        return MyFraction(self.nom * other.nom * self.sign * other.sign, self.denom * other.denom)

    def __truediv__(self, other):
        if not isinstance(other, MyFraction):
            raise TypeError("Class MyFraction do not support operations with other types")
        return MyFraction(self.nom * other.denom * self.sign * other.sign, self.denom * other.nom)

    def __add__(self, other):
        if not isinstance(other, MyFraction):
            raise TypeError("Class MyFraction do not support operations with other types")
        d = self.denom * other.denom
        n1 = self.nom * self.sign * other.denom
        n2 = other.nom * other.sign * self.denom
        return MyFraction(n1 + n2, d)

    def __sub__(self, other):
        if not isinstance(other, MyFraction):
            raise TypeError("Class MyFraction do not support operations with other types")
        d = self.denom * other.denom
        n1 = self.nom * self.sign * other.denom
        n2 = other.nom * other.sign * self.denom
        return MyFraction(n1 - n2, d)


if __name__ == "__main__":
    x = MyFraction(1, 2)
    y = MyFraction(1, 4)
    print(x + y == MyFraction(3, 4))
    print(x - y)
    a = MyFraction(1, -3)
    b = MyFraction(-1, 3)
    print(a == b)
    print(a * b)
    print(x / y)

