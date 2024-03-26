
import arcade

from kobold.components import Acceleration, Collider, CollisionType, Position, Velocity, TextureSprite, RandomMovementAI, KeyboardController
from kobold.entities import Entity
from kobold.geometry import Rectangle, Vector


class Enemy(Entity):

    def __init__(self):
        super().__init__()
        self.add_component(Position(Vector(100, 200)))
        self.add_component(Velocity(Vector(0, 0)))
        self.add_component(TextureSprite(arcade.make_circle_texture(40, arcade.color.RED)))
        # self.add_component(RandomMovementAI())
        self.add_component(Collider(Rectangle(Vector(100, 100), Vector(40, 40)), CollisionType.BLOCKING))
        self.add_component(Acceleration(Vector(0, -1)))
        

class Player(Entity):

    def __init__(self) -> None:
        super().__init__()
        self.add_component(Position(Vector(150, 150)))
        self.add_component(Velocity(Vector(0, 0)))
        self.add_component(TextureSprite(arcade.make_circle_texture(40, arcade.color.GREEN)))
        self.add_component(KeyboardController())
        self.add_component(Collider(Rectangle(Vector(150, 150), Vector(40, 40)), CollisionType.BLOCKING))
