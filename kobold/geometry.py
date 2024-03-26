from dataclasses import dataclass
import math


@dataclass
class Vector:
    x: float
    y: float

    def __add__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scale: float) -> 'Vector':
        '''Returns a scaled version of self.'''
        return Vector(self.x * scale, self.y * scale)
    
    def __truediv__(self, scale: float) -> 'Vector':
        '''Returns a scaled version of self.'''
        return Vector(self.x / scale, self.y / scale)
    
    @property
    def unit_vector(self) -> 'Vector':
        return self / self.magnitude

    @property
    def rounded(self) -> 'Vector':
        return Vector(round(self.x), round(self.y))
    
    @property
    def magnitude(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)
    
    @property
    def direction(self) -> float:
        angle_in_radians = math.atan2(self.y, self.x)
        return math.degrees(angle_in_radians)
    
    def direction_to(self, other: 'Vector') -> float:
        vector = other - self
        return vector.direction
    

@dataclass
class Rectangle:
    center: Vector
    dimensions: Vector

    @property
    def top(self) -> float:
        return self.center.y + self.dimensions.y / 2
    
    @property
    def bottom(self) -> float:
        return self.center.y - self.dimensions.y / 2
    
    @property
    def left(self) -> float:
        return self.center.x - self.dimensions.x / 2
    
    @property
    def right(self) -> float:
        return self.center.x + self.dimensions.x / 2
    
    def intersects(self, other: 'Rectangle') -> bool:
        to_left = self.right < other.left
        to_right = self.left > other.right
        above = self.bottom > other.top
        below = self.top < other.bottom

        return not (to_left or to_right or above or below)