from enum import Enum, auto
import random
import arcade

from kobold import entities
from kobold.components import CollisionType
from kobold.geometry import Vector


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


class PhysicsSystem:

    @staticmethod
    def update(entity: entities.Entity, entities: list[entities.Entity]) -> None:
        if not (entity.has_component('Position') and entity.has_component('Velocity')):
            return
        
        if entity.has_component('Acceleration'):
            entity.get_component('Velocity').velocity += entity.get_component('Acceleration').acceleration
        
        if entity.get_component('Velocity').velocity == Vector(0, 0):
            return
        
        starting_position = entity.get_component('Position').position
        incremental_distance = entity.get_component('Velocity').velocity.unit_vector
        total_distance = entity.get_component('Velocity').velocity.magnitude
        moving = True

        while moving:
            entity.get_component('Position').position += incremental_distance
            
            # Arrived At Intended Destination
            if (entity.get_component('Position').position - starting_position).magnitude >= total_distance:
                moving = False

            if not (entity.has_component('Collider') and entity.has_component('Velocity')):
                continue

            # Update Collider's Position
            entity.get_component('Collider').bounding_box.center = entity.get_component('Position').position

            other_collidables = [e for e in entities if e.has_component('Collider') and e != entity]
            
            # Check For Collisions
            for other in other_collidables:

                # If there's no collision then check if other needs to be removed from current collsions list
                if not entity.get_component('Collider').bounding_box.intersects(other.get_component('Collider').bounding_box):
                    if other in entity.get_component('Collider').current_collisions:
                        entity.get_component('Collider').current_collisions.remove(other)
                    continue

                # If entity is already colliding with other then nothing needs to happen
                if other in entity.get_component('Collider').current_collisions:
                    continue
                
                # Add other to current collisions list
                entity.get_component('Collider').current_collisions.append(other)

                # Handle Different Collision Types
                if other.get_component('Collider').collision_type is CollisionType.BLOCKING:
                    print("BANG")
                    entity.get_component('Position').position -= incremental_distance
                    entity.get_component('Velocity').velocity.y = 0  # This only works for vertical collisions, need to use something more complex for all angles
                    moving = False

                if other.get_component('Collider').collision_type is CollisionType.PASSING:
                    pass

                if other.get_component('Collider').collision_type is CollisionType.BOUNCING:
                    entity.get_component('Position').position -= incremental_distance
                    entity.get_component('Velocity').velocity.y *= -1  # This only works for vertical collisions, need to use something more complex for all angles
                    moving = False
                
            
class TextureRendererSystem:

    @staticmethod
    def update(entity: entities.Entity) -> None:
        if entity.has_component('TextureSprite') and entity.has_component('Position'):
            entity.get_component('TextureSprite').texture.draw_scaled(entity.get_component('Position').position.x, entity.get_component('Position').position.y)


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
                entity.get_component('Velocity').velocity = Vector(random.randint(-2, 2), random.randint(-2, 2))
                entity.get_component('RandomMovementAI').counter = 50


class ControllerSystem:

    @staticmethod
    def update(entity: entities.Entity) -> None:
        if not (entity.has_component('Velocity') and entity.has_component('KeyboardController')):
            return
        
        keyboard = InputSystem.get_instance().keyboard

        if keyboard[Key.UP] and not keyboard[Key.DOWN]:
            entity.get_component('Velocity').velocity.y = 5
        if keyboard[Key.DOWN] and not keyboard[Key.UP]:
            entity.get_component('Velocity').velocity.y = -5
        if keyboard[Key.LEFT] and not keyboard[Key.RIGHT]:
            entity.get_component('Velocity').velocity.x = -5
        if keyboard[Key.RIGHT] and not keyboard[Key.LEFT]:
            entity.get_component('Velocity').velocity.x = 5

        if not keyboard[Key.UP] and not keyboard[Key.DOWN]:
            entity.get_component('Velocity').velocity.y = 0
        if not keyboard[Key.LEFT] and not keyboard[Key.RIGHT]:
            entity.get_component('Velocity').velocity.x = 0


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