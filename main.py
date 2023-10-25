class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calc_area(self):
        return self.height * self.width


class Parallelepiped(Rectangle):
    def __init__(self, height, width, length):
        super().__init__(height, width)
        self.length = length

    def calc_volume(self):
        return self.height * self.width * self.length


rectangle = Rectangle(3, 3)
print(rectangle.calc_area())

parallelepiped = Parallelepiped(3, 3, 3)
print(parallelepiped.calc_volume())
