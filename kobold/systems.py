from enum import Enum, auto
import random
import arcade

from kobold import entities


class Key(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()
    

class InputSystem:

    instance = None

    def __init__(self) -> None:
        self.keyboard = {
            Key.UP: False,
            Key.DOWN: False,
            Key.LEFT: False,
            Key.RIGHT: False
        }


    @staticmethod
    def get_instance() -> 'InputSystem':
        if InputSystem.instance:
            return InputSystem.instance
        else:
            InputSystem.instance = InputSystem()
            return InputSystem.instance
    
    def handle_input(self, key: int, pressed: bool):
        if key == arcade.key.UP: 
            self.keyboard[Key.UP] = pressed
        elif key == arcade.key.DOWN:
            self.keyboard[Key.DOWN] = pressed
        elif key == arcade.key.LEFT:
            self.keyboard[Key.LEFT] = pressed
        elif key == arcade.key.RIGHT:
            self.keyboard[Key.RIGHT] = pressed


class CollisionSystem:

    @staticmethod
    def collides(entity: entities.Entity, other: entities.Entity) -> bool:
        to_left = entity.get_component('Position').x + 20 < other.get_component('Position').x - 20
        to_right = entity.get_component('Position').x - 20 > other.get_component('Position').x + 20
        above = entity.get_component('Position').y - 20 > other.get_component('Position').y + 20
        below = entity.get_component('Position').y + 20 < other.get_component('Position').y - 20
        return not (to_left or to_right or above or below)

    @staticmethod
    def update(entity: entities.Entity, entities: list[entities.Entity]) -> None:
        if not (entity.has_component('Collider') and entity.has_component('Position') and entity.has_component('Velocity')):
            return
        for other in entities:
            if other == entity:
                continue
            if not other.has_component('Collider'):
                continue
            if not CollisionSystem.collides(entity, other) and other in entity.get_component('Collider').current_collisions:
                entity.get_component('Collider').current_collisions.remove(other)
            if CollisionSystem.collides(entity, other) and other in entity.get_component('Collider').current_collisions:
                continue
            if CollisionSystem.collides(entity, other) and not other in entity.get_component('Collider').current_collisions:
                entity.get_component('Collider').current_collisions.append(other)
            

class MovementSystem:
    
    @staticmethod
    def update(entity: entities.Entity) -> None:
        if not (entity.has_component('Velocity') and entity.has_component('Position')):
            return
        
        if entity.has_component('Collider'):
            current_collisions = entity.get_component('Collider').current_collisions
            if current_collisions:
                entity.get_component('Position').x = entity.get_component('Position').last_valid_x
                entity.get_component('Position').y = entity.get_component('Position').last_valid_y
                
        entity.get_component('Position').last_valid_x = entity.get_component('Position').x
        entity.get_component('Position').last_valid_y = entity.get_component('Position').y
        entity.get_component('Position').x += entity.get_component('Velocity').x
        entity.get_component('Position').y += entity.get_component('Velocity').y
        entity.get_component('Velocity').x = 0
        entity.get_component('Velocity').y = 0
                
            
class TextureRendererSystem:

    @staticmethod
    def update(entity: entities.Entity) -> None:
        if entity.has_component('TextureSprite') and entity.has_component('Position'):
            entity.get_component('TextureSprite').texture.draw_scaled(entity.get_component('Position').x, entity.get_component('Position').y)


class ShapeRendererSystem:

    @staticmethod
    def update(entity: entities.Entity) -> None:
        if entity.has_component('ShapeSprite') and entity.has_component('Position'):
            entity.get_component('ShapeSprite').shape.draw()


class RandomAIMovementSystem:

    @staticmethod
    def update(entity: entities.Entity) -> None:
        if entity.has_component('RandomMovementAI') and entity.has_component('Velocity'):
            if entity.get_component('RandomMovementAI').counter > 0:
                entity.get_component('RandomMovementAI').counter -= 1
            else:
                entity.get_component('Velocity').x = random.randint(-2, 2)
                entity.get_component('Velocity').y = random.randint(-2, 2)
                entity.get_component('RandomMovementAI').counter = 50


class ControllerSystem:

    @staticmethod
    def update(entity: entities.Entity) -> None:
        if not (entity.has_component('Velocity') and entity.has_component('KeyboardController')):
            return
        
        keyboard = InputSystem.get_instance().keyboard
        if keyboard[Key.UP] and not keyboard[Key.DOWN]:
            entity.get_component('Velocity').y = 5
        if keyboard[Key.DOWN] and not keyboard[Key.UP]:
            entity.get_component('Velocity').y = -5
        if keyboard[Key.LEFT] and not keyboard[Key.RIGHT]:
            entity.get_component('Velocity').x = -5
        if keyboard[Key.RIGHT] and not keyboard[Key.LEFT]:
            entity.get_component('Velocity').x = 5


class InteractionSystem:

    @staticmethod
    def update(entity: entities.Entity, entities: list[entities.Entity]) -> None:
        for other in entities:
            if not other:
                continue
            if entity.has_component('Collider') and other.has_component('Collider') and other.has_component('Interactive'):
                current_interactions = other.get_component('Interactive').current_interactions
                current_collisions = entity.get_component('Collider').current_collisions

                if entity in current_interactions and other in current_collisions:
                    continue
                if entity in current_interactions and not other in current_collisions:
                    other.get_component('Interactive').current_interactions.remove(entity)
                if not entity in current_interactions and other in current_collisions:
                    other.get_component('Interactive').interact(other)
                    other.get_component('Interactive').current_interactions.append(entity)