from exercicio03 import computed_property


class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    @computed_property('radius', 'area')
    def diameter(self):
        """Circle diameter from radius"""
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

    @diameter.deleter
    def diameter(self):
        self.radius = 0


if __name__ == '__main__':
    circle = Circle()
    # help(circle.diameter)
    print(circle.diameter)
    circle.diameter = 3
    print(circle.radius)
    del circle.diameter
    print(circle.radius)
    # print(help(Circle))

