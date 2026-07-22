from turtle import Turtle
from app.core.config import BUTTON_FONT, BUTTON_START_POS

button_start = Turtle()
button_start.hideturtle()
button_start.shape("square")
button_start.shapesize(stretch_wid=1, stretch_len=2)
button_start.fillcolor("cyan")
button_start.penup()
button_start.goto(BUTTON_START_POS)
button_start.write("start", align="center", font=BUTTON_FONT)
button_start.pendown()
button_start.showturtle()
