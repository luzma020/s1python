class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)



r1 = Rectangle(18, 8)
r2 = Rectangle(10, 10)


if r1.area() > r2.area():
    print("Rectangle 1 has a larger area")
elif r1.area() < r2.area():
    print("Rectangle 2 has a larger area")
else:
    print("Both rectangles have the same area")


print("Area of Rectangle 1:", r1.area())
print("Perimeter of Rectangle 1:", r1.perimeter())

print("Area of Rectangle 2:", r2.area())
print("Perimeter of Rectangle 2:", r2.perimeter())
