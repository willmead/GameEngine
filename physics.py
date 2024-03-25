from dataclasses import dataclass
from collections import namedtuple
import math


Vector = namedtuple('Vector', 'x y')


@dataclass
class PhysicsEntity:
    dimensions: Vector
    position: Vector


def direction(position1: Vector, position2: Vector) -> float:
    x = position2.x - position1.x
    y = position2.y - position1.y

    angle_in_radians = math.atan2(y, x)
    angle_in_degrees = math.degrees(angle_in_radians)

    return angle_in_degrees
    

def magnitude(position1: Vector, position2: Vector) -> float:
    x = position2.x - position1.x
    y = position2.y - position1.y
    return math.sqrt(x**2 + y**2)


def travel_vector(position1: Vector, position2: Vector):
    x = position2.x - position1.x
    y = position2.y - position1.y
    return Vector(x / 100, y / 100)


def collides(entity: PhysicsEntity, other: PhysicsEntity) -> bool:
    entity_left = entity.position.x - entity.dimensions.x / 2
    entity_right = entity.position.x + entity.dimensions.x / 2
    entity_top = entity.position.y + entity.dimensions.y / 2
    entity_bottom = entity.position.y - entity.dimensions.y / 2

    other_left = other.position.x - other.dimensions.x / 2
    other_right = other.position.x + other.dimensions.x / 2
    other_top = other.position.y + other.dimensions.y / 2
    other_bottom = other.position.y - other.dimensions.y / 2

    to_left = entity_right < other_left
    to_right = entity_left > other_right
    above = entity_bottom > other_top
    below = entity_top < other_bottom

    return not (to_left or to_right or above or below)


def move(entity: PhysicsEntity, destination: Vector, entities: list[PhysicsEntity]) -> dict[str, any]:

    # Get Direction Of Travel
    direction_of_travel = direction(entity.position, destination)
    print(f'Direction (Degrees): {direction_of_travel}')

    # Get Magnitude Of Travel  
    magnitude_of_travel = magnitude(entity.position, destination)
    print(f'Magnitude: {magnitude_of_travel}')

    # Get Travel Vector
    vector_of_travel = travel_vector(entity.position, destination)
    print(f'Unit Vector: {vector_of_travel}')

    moving = True
    while moving:
        next_position = Vector(entity.position.x + vector_of_travel.x, entity.position.y + vector_of_travel.y)
        collisions = [collides(entity, other) for other in entities]
        if any(collisions):
            print(f'Collision at: ({next_position.x}, {next_position.y})')
            return entity.position
        entity.position = next_position
        if next_position == destination:
            print(f'Reached Final Destination')
            return entity.position


if __name__ == '__main__':

    e1 = PhysicsEntity(dimensions=Vector(2, 2), position=Vector(0, 0))
    e2 = PhysicsEntity(dimensions=Vector(4, 4), position=Vector(5, 5))

    print('START OF PHYSICS TEST')
    result = move(e1, Vector(20, 20), [e2])
    print(f'Final Position: {result}')
    print('END OF PHYSICS TEST')