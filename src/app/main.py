from turtle import Screen
from app.models.domain.alien_tile import Alien_Tile
from app.models.domain.bullet import Bullet
import time
from app.core.config import ALIEN_FIRE_TICK, BULLET_MOVE_SPEED, GUN_INITIAL_POSITION, SCREEN_WIDTH, SCREEN_HEIGHT, print_config
from app.models.domain.gun import Gun
import random

screen = Screen()
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Space Invaders")
screen.tracer(0)

gun = Gun(GUN_INITIAL_POSITION)
bullets = []  # contain bullets active fired from the gun, and on the screen
alien_fire_counter = 0
alien_tiles = []


screen.listen()
screen.onkey(gun.go_left, "Left")
screen.onkey(gun.go_right, "Right")

print("Starting the game...")
print_config()

def start_game():
    global game_is_on, alien_tiles, alien_fire_counter
    alien_fire_counter = 0
    alien_tiles = Alien_Tile.create_alien_tiles()
    game_is_on = True
    gun.showturtle()
    game_loop()

def end_game():
    global game_is_on, alien_tiles, alien_fire_counter, bullets
    game_is_on = False
    gun.hideturtle()
    for alien in alien_tiles:
        alien.hideturtle()
    for bullet in bullets:
        bullet.hideturtle()
    alien_tiles = []
    alien_fire_counter = 0
    bullets = []

def fire_grenade():
    new_bullet = Bullet(gun.position(), "grenade")
    new_bullet.fire(bullets)

def fire_missile(alien):
    new_bullet = Bullet(alien.position(), "missile")
    new_bullet.fire(bullets)

def update_bullets():
    global bullets, tiles, screen
    for bullet in bullets:
        if bullet.isvisible() and bullet.bullet_type == "grenade":
            bullet.go_up()
            # Detect collision with alien tiles
            Alien_Tile.collide_alien_tiles(bullet, bullets, alien_tiles, screen)

        elif bullet.isvisible() and bullet.bullet_type == "missile":
            bullet.go_down()
        
        else:
            bullet.delete()
            bullets.remove(bullet)


def update_alien_positions():
    global alien_fire_counter
    # move all aliens
    for alien in alien_tiles:
        alien.move()

    # increment counter and fire a missile from a random visible alien
    alien_fire_counter += 1
    if alien_fire_counter >= ALIEN_FIRE_TICK:
        # choose only visible (alive) aliens
        visible_aliens = [a for a in alien_tiles if a.isvisible()]
        if visible_aliens:
            alien_choice = random.choice(visible_aliens)
            fire_missile(alien_choice)
        alien_fire_counter = 0

screen.onkey(start_game, "s") 
screen.onkey(end_game, "q")
screen.onkey(fire_grenade, "space")


game_is_on = True
screen.update()
print("Game started. Press 's' to start/restart the game, 'q' to quit, <space> to fire.")

def game_loop():
    global game_is_on, screen, ball, paddle, gun
    while game_is_on:
        screen.update()

        update_bullets()
        update_alien_positions()
        screen.update()

    #detect collision of a missile with gun
        if Bullet.collide_gun(gun, bullets):
            print("Gun hit by missile! Game Over.")
            end_game()

        time.sleep(BULLET_MOVE_SPEED/1000)

screen.exitonclick()