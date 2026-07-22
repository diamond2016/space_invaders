from turtle import Turtle
from app.core.config import BULLET_BOTTOM_LIMIT, BULLET_COLLISION_DISTANCE, BULLET_MOVE_DISTANCE, BULLET_TOP_LIMIT
from app.assets import ASSET_PATH


class Bullet(Turtle):

    def __init__(self, bullet_position, bullet_type):
        super().__init__()
        match bullet_type:
            case "missile":
                self.bullet_type = bullet_type
                self.screen.register_shape(f"{ASSET_PATH}/missile.png")
                self.shape(f"{ASSET_PATH}/missile.png")
            case "grenade":
                self.bullet_type = bullet_type
                self.screen.register_shape(f"{ASSET_PATH}/grenade.png")
                self.shape(f"{ASSET_PATH}/grenade.png")
            case _: return
        
        self.penup()
        self.goto(bullet_position)

    def go_down(self): # only for missiles, from aliens
        if (self.ycor() > BULLET_BOTTOM_LIMIT):
            new_y = self.ycor() - BULLET_MOVE_DISTANCE
            self.goto(self.xcor(), new_y)
        else:
            self.delete()

    def go_up(self):  # only for grenades, from gun
        if (self.ycor() < BULLET_TOP_LIMIT):
            new_y = self.ycor() + BULLET_MOVE_DISTANCE
            self.goto(self.xcor(), new_y)
        else:
            self.delete()

    def fire(self, bullets):
        match self.bullet_type:
            case "missile":
                self.go_down()
                bullets.append(self)
            case "grenade":
                self.go_up()
                bullets.append(self)
            case _: return
    
    def delete(self):
        self.hideturtle()
        self.clear()

    @staticmethod
    def collide_gun(gun, bullets):
        for bullet in bullets:
            if bullet.distance(gun) < BULLET_COLLISION_DISTANCE and bullet.bullet_type == "missile":
                bullet.delete()
                bullets.remove(bullet)
                gun.delete()
                return True 
        return False

