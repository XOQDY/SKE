    class Point2D:
    """Point class represents and operate on x, y coordinates
    """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return (self.x*self.x + self.y*self.y)**0.5

    def halfway(self, other):
        halfway_x = (other.x + self.x) / 2
        halfway_y = (other.y + self.y) / 2
        return Point2D(halfway_x, halfway_y)

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

class Rectangle:
    """Reactangle class represents a rectangle object wiht its size and location
    """
    def __init__(self, point, width, height):
        self.corner = point
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

    def grow(self, delta_width, delta_height):
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        self.corner.x += dx
        self.corner.y += dy

    def __str__(self):
        return "[{0}, {1}, {2}]".format(self.corner, self.width, self.height)

    def __eq__(self, other):
        return (self.corner == other.corner) and (self.width == other.width) and (self.height == other.height)
