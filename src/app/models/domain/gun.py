from turtle import Turtle
from app.models.domain.bullet import Bullet
from app.core.config import (
    GUN_INITIAL_POSITION,
    GUN_LEFT_LIMIT,
    GUN_MOVE_DISTANCE,
    GUN_RIGHT_LIMIT,
)
from app.assets import ASSET_PATH


class Gun(Turtle):

    def __init__(self, position):
        super().__init__()
        self.screen.register_shape(f"{ASSET_PATH}/gun.png")
        self.shape(f"{ASSET_PATH}/gun.png")
        self.penup()
        self.hideturtle()
        self.goto(position)

    def go_left(self):
        if self.xcor() > GUN_LEFT_LIMIT:
            new_x = self.xcor() - GUN_MOVE_DISTANCE
            self.goto(new_x, self.ycor())

    def go_right(self):
        if self.xcor() < GUN_RIGHT_LIMIT:
            new_x = self.xcor() + GUN_MOVE_DISTANCE
            self.goto(new_x, self.ycor())

    def fire_gun(self):
        new_bullet = Bullet((self.xcor(), self.ycor() + 10), "grenade")
        new_bullet.go_up()
        return new_bullet

    def reset_position_gun(self):
        self.goto(GUN_INITIAL_POSITION)

    def delete(self):
        self.hideturtle()
        self.clear()
