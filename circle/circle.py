import math

class Circle():

    def __init__(self, radius):
        if radius <= 0:
            raise ValueError('El radio debe ser mayor a cero.')
        self.radius = radius

    def get_radius(self):
        return self.radius

    