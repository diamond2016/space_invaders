from app.core.config import BULLET_COLLISION_DISTANCE, TILE_COLUMNS, TILE_ROWS, TILE_LEFT_LIMIT, TILE_SEP_X, TILE_SEP_Y, TILE_TOP_LIMIT

from .alien import Alien
from .bullet import Bullet


class Alien_Tile():
    
    @staticmethod
    def create_alien_tiles():
        tiles = []
        for row in range(TILE_ROWS):
            for col in range(TILE_COLUMNS):
                x = TILE_LEFT_LIMIT + col * TILE_SEP_X
                y = TILE_TOP_LIMIT - row * TILE_SEP_Y
                t = (col + row) % 3
                match t:
                    case 0:
                        alien_type = "alien1"
                    case 1:
                        alien_type = "alien2"
                    case 2:
                        alien_type = "saucer1"
                tile = Alien(alien_type, (x, y))
                tile.showturtle()
                tiles.append(tile)
        return tiles
    

    @staticmethod
    def collide_alien_tiles(bullet, bullets, tiles, screen):
        for tile in tiles:
        #Detect collision with bullet
            if bullet.distance(tile) < BULLET_COLLISION_DISTANCE:
                print("Tile hit!")
                bullet.delete()
                bullets.remove(bullet)
                tile.delete()
                tiles.remove(tile)
                break  # Exit after first collision to prevent multiple bounces


    def fire_alien_tiles(self, tiles, bullets):
        for tile in tiles:
            if tile.isvisible():
                new_missile = Bullet("misssile", tile.position())
                bullets.append(new_missile)
                