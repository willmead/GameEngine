
import arcade

from kobold.components import Acceleration, Collider, Position, Velocity, TextureSprite, RandomMovementAI, KeyboardController
from kobold.entities import Entity


class Enemy(Entity):

    def __init__(self):
        super().__init__()
        self.add_component(Position(100, 300))
        self.add_component(Velocity(0, 0))
        self.add_component(TextureSprite(arcade.make_circle_texture(40, arcade.color.RED)))
        # self.add_component(RandomMovementAI())
        self.add_component(Collider())
        self.add_component(Acceleration(0, -1))
        

class Player(Entity):

    def __init__(self) -> None:
        super().__init__()
        self.add_component(Position(150, 100))
        self.add_component(Velocity(0, 0))
        self.add_component(TextureSprite(arcade.make_circle_texture(40, arcade.color.GREEN)))
        self.add_component(KeyboardController())
        self.add_component(Collider())
