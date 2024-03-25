class Component:
    pass


class Position(Component):

    def __init__(self, x: int, y: int) -> None:
        self.name = 'Position'
        self.x = x
        self.y = y
        self.last_valid_x = x
        self.last_valid_y = y


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


class Velocity(Component):

    def __init__(self, x: int, y: int) -> None:
        self.name = 'Velocity'
        self.x = x
        self.y = y


class Acceleration(Component):

    def __init__(self, x: int, y: int) -> None:
        self.name = 'Acceleration'
        self.x = x
        self.y = y


class TextureSprite(Component):

    def __init__(self, texture: any) -> None:
        self.name = 'TextureSprite'
        self.texture = texture
    

class ShapeSprite(Component):

    def __init__(self, shape: any) -> None:
        self.name = 'ShapeSprite'
        self.shape = shape


class Collider(Component):

    def __init__(self) -> None:
        self.name = 'Collider'
        self.current_collisions = []


class Interactive(Component):

    def __init__(self, interact: callable) -> None:
        self.name = 'Interactive'
        self.interact = interact
        self.current_interactions = []