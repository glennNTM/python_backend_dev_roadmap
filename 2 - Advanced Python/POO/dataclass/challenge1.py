from dataclasses import dataclass

@dataclass
class Point():
    x : int
    y : int

point_1 = Point(x=3, y=5)
point_2 = Point(x=1, y=-7)
point_3 = Point(x=3, y=5)

print(point_1 == point_3)
