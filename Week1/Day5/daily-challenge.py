# Challenge

from math import pi


class Circle:

    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def area(self):
        return pi * (self.radius**2)

    def __str__(self):
        return (
            f"Cercle(radius={self.radius}, "
            f"diameter={self.diameter}, "
            f"area={self.area:.2f})"
        )

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __gt__(self, other):
        return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius


# =========================
# TESTS
# =========================

# Création des cercles
c1 = Circle(5)
c2 = Circle.from_diameter(20)

# Affichage
print(c1)
print(c2)

# Aire
print(f"Aire du cercle 1 : {c1.area:.2f}")

# Addition
c3 = c1 + c2
print(f"Nouveau cercle après addition : {c3}")

# Comparaison
print(c1 > c2)  # False
print(c1 == c2)  # False

# Tri des cercles
circles = [c2, c1, c3]

sorted_circles = sorted(circles)

print("\nCercles triés :")

for circle in sorted_circles:
    print(circle)
