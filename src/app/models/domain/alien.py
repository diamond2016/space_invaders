from turtle import Turtle
from unittest import case
from app.core.config import ALIEN_FIRE_TICK, ALIEN_MOVE_DISTANCE
from app.assets import ASSET_PATH

class Alien(Turtle):
    
    def __init__(self, alien_type, position):
        super().__init__()
        self.alien_type = alien_type
        self.screen = self.getscreen()
        self.initial_tick = 0
        match alien_type:
            case "alien1":
                self.screen.register_shape(f"{ASSET_PATH}/alien1.png")
                self.shape(f"{ASSET_PATH}/alien1.png")
            case "alien2":
                self.screen.register_shape(f"{ASSET_PATH}/alien2.png")
                self.shape(f"{ASSET_PATH}/alien2.png")
            case "saucer1":
                self.screen.register_shape(f"{ASSET_PATH}/saucer1.png")
                self.shape(f"{ASSET_PATH}/saucer1.png")
            case _: return
        
        self.penup()
        self.goto(position)
        self.initial_position = position

    def go_left(self):
        if (self.xcor() > self.initial_position[0] - ALIEN_MOVE_DISTANCE):
            new_x = self.xcor() - ALIEN_MOVE_DISTANCE
            self.goto(new_x, self.ycor())

    def go_right(self):
        if (self.xcor() < self.initial_position[0] + ALIEN_MOVE_DISTANCE):
            new_x = self.xcor() + ALIEN_MOVE_DISTANCE
            self.goto(new_x, self.ycor())

    def move(self):
        if self.heading() == 0:
            self.go_right()
            if self.xcor() >= self.initial_position[0] + ALIEN_MOVE_DISTANCE:
                self.setheading(180)
        else:
            self.go_left()
            if self.xcor() <= self.initial_position[0] - ALIEN_MOVE_DISTANCE:
                self.setheading(0)

    def delete(self):
        self.hideturtle()
        self.clear()

