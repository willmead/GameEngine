from enum import Enum
from kobold.geometry import Rectangle, Vector


class Component:
    pass


##########
# MOVEMENT
##########

class Position(Component):

    def __init__(self, position: Vector) -> None:
        self.name = 'Position'
        self.position = position
        

class Velocity(Component):

    def __init__(self, velocity: Vector) -> None:
        self.name = 'Velocity'
        self.velocity = velocity


class Acceleration(Component):

    def __init__(self, acceleration: Vector) -> None:
        self.name = 'Acceleration'
        self.acceleration = acceleration


##########
# CONTROLS
##########

class RandomMovementAI(Component):

    def __init__(self) -> None:
        self.name = 'RandomMovementAI'
        self.counter = 0


class KeyboardController(Component):

    def __init__(self) -> None:
        self.name = 'KeyboardController'
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

    @property
    def up(self) -> bool:
        return self.up_pressed and not self.down_pressed

    @property
    def down(self) -> bool:
        return self.down_pressed and not self.up_pressed
    
    @property
    def left(self) -> bool:
        return self.left_pressed and not self.right_pressed
    
    @property
    def right(self) -> bool:
        return self.right_pressed and not self.left_pressed


##########
# GRAPHICS
##########

class TextureSprite(Component):

    def __init__(self, texture: any) -> None:
        self.name = 'TextureSprite'
        self.texture = texture
    

class ShapeSprite(Component):

    def __init__(self, shape: any) -> None:
        self.name = 'ShapeSprite'
        self.shape = shape


############
# COLLISIONS
############
        
class CollisionType(Enum):
    BLOCKING = 0
    PASSING = 1
    BOUNCING = 2

        
class Collider(Component):

    def __init__(self, bounding_box: Rectangle, collision_type: CollisionType) -> None:
        self.name = 'Collider'
        self.current_collisions = []
        self.bounding_box = bounding_box
        self.collision_type = collision_type


class Interactive(Component):

    def __init__(self, interact: callable) -> None:
        self.name = 'Interactive'
        self.interact = interact
        self.current_interactions = []