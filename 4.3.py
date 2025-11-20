class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width


    def __lt__(self, other):
        return self.area() < other.area()



l1 = float(input("Enter length of Rectangle 1: "))
w1 = float(input("Enter width of Rectangle 1: "))
r1 = Rectangle(l1, w1)

l2 = float(input("Enter length of Rectangle 2: "))
w2 = float(input("Enter width of Rectangle 2: "))
r2 = Rectangle(l2, w2)


if r1 < r2:
    print("Rectangle 1 is smaller than Rectangle 2")
else:
    print("Rectangle 1 is larger or equal to Rectangle 2")
