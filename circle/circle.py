import math

class Circle():

    def __init__(self, radius):
        if radius <= 0:
            raise ValueError('El radio debe ser mayor a cero.')
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        if radius <= 0:
            raise ValueError('El radio debe ser mayor a cero.')
        else:
            self.radius = radius
    
    def get_area(self):
        return math.pi * self.radius ** 2
    
    def get_perimeter(self):
        return 2 * math.pi * self.radius