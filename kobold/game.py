import arcade

from kobold.systems import CollisionSystem, InteractionSystem, MovementSystem, InputSystem, ControllerSystem, RandomAIMovementSystem, ShapeRendererSystem, TextureRendererSystem
import kobold.entities


def load_map_from_arrays(arrays: list[list[int]], tile_types: dict[str, callable], tilesize: int) -> list[kobold.entities.Entity]:
    tiles = []
    number_of_rows = len(arrays)
    number_of_columns = len(arrays[0])
    for y in range(number_of_rows):
        for x in range(number_of_columns):
            tiles.append(tile_types[arrays[y][x]](x * tilesize + tilesize // 2, y * tilesize + tilesize // 2))
    return tiles


class Camera:

    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.following = False
        self.entity_to_follow = None

    def goto(self, x, y) -> None:
        self.x = x
        self.y = y

    def follow(self, entity: kobold.entities.Entity) -> None:
        self.following = True
        self.entity_to_follow = entity

    def update(self) -> None:
        if not self.following:
            return
        self.x = self.entity_to_follow.get_component('Position').x
        self.y = self.entity_to_follow.get_component('Position').y


class Scene:

    def __init__(self) -> None:
        super().__init__()
        self.entities = []
        self.camera = Camera()

    def add_entity(self, entity: kobold.entities.Entity) -> None:
        self.entities.append(entity)

    def handle_input(self, key: int, pressed: bool) -> None:
        InputSystem.get_instance().handle_input(key, pressed)
    
    def update(self) -> None:
        self.camera.update()
        for entity in self.entities:
            MovementSystem.update(entity)
            ControllerSystem.update(entity)
            RandomAIMovementSystem.update(entity)
            # CollisionSystem.update(entity, self.entities)
            # InteractionSystem.update(entity, self.entities)

    def draw(self) -> None:
        arcade.set_viewport(self.camera.x - 640, self.camera.x + 640, self.camera.y - 360, self.camera.y + 360)
        for entity in self.entities:
            TextureRendererSystem.update(entity)
            ShapeRendererSystem.update(entity)


class Game(arcade.Window):

    def __init__(self, title: str, width: int, height: int) -> None:
        super().__init__(width, height, title)
        self.scenes = {}
    
    def on_update(self, delta_time: float) -> None:
        self.current_scene.update()

    def on_draw(self) -> None:
        self.clear()
        self.current_scene.draw()

    def add_scene(self, scene_name: str, scene: Scene) -> None:
        self.scenes[scene_name] = scene

    def set_current_scene(self, scene_name: str) -> None:
        scene = self.scenes[scene_name]
        scene.setup()
        self.current_scene = scene

    def on_key_press(self, key: int, modifiers: int):
        self.current_scene.handle_input(key=key, pressed=True)
    
    def on_key_release(self, key: int, modifiers: int):
        self.current_scene.handle_input(key=key, pressed=False)
