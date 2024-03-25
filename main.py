from kobold.game import Game, Scene, load_map_from_arrays

from entities import Enemy, Player
from tiles import FloorTile, WallTile, InteractiveTile


class MyScene(Scene):

    def setup(self) -> None:
        tilemap = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 2, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]
        tile_types = {
            0: FloorTile,
            1: WallTile,
            2: InteractiveTile
        }
        tiles = load_map_from_arrays(tilemap, tile_types, tilesize=40)
        
        for tile in tiles:
            self.add_entity(tile)
            
        player = Player()
        self.add_entity(player)
        self.camera.follow(player)

        enemy = Enemy()
        self.add_entity(enemy)


game = Game('Demo Game', 1280, 720)
game.add_scene('MyScene', MyScene())
game.set_current_scene('MyScene')
game.run()
