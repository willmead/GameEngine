import arcade

from kobold.entities import Entity
from kobold.components import Collider, Position, ShapeSprite, Interactive


TILESIZE = 40


class FloorTile(Entity):

    def __init__(self, x: int, y: int):
        super().__init__()
        self.add_component(Position(x, y))
        shape = arcade.create_rectangle_filled(
            self.get_component('Position').x, 
            self.get_component('Position').y, 
            TILESIZE, 
            TILESIZE, 
            arcade.color.BLACK
        )
        self.add_component(ShapeSprite(shape))


class WallTile(Entity):

    def __init__(self, x: int, y: int):
        super().__init__()
        self.add_component(Position(x, y))
        self.add_component(Collider())
        shape = arcade.create_rectangle_filled(
            self.get_component('Position').x, 
            self.get_component('Position').y, 
            TILESIZE, 
            TILESIZE, 
            arcade.color.WHITE
        )
        self.add_component(ShapeSprite(shape))


class InteractiveTile(Entity):

    def interact(self, entity) -> None:
        print('Interacting!')

    def __init__(self, x: int, y: int):
        super().__init__()
        self.add_component(Position(x, y))
        self.add_component(Collider())
        shape = arcade.create_rectangle_filled(
            self.get_component('Position').x, 
            self.get_component('Position').y, 
            TILESIZE, 
            TILESIZE, 
            arcade.color.BLUE
        )
        self.add_component(ShapeSprite(shape))
        self.add_component(Interactive(self.interact))