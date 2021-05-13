from turtle import *
from player import Player
from bullet import Bullet
from enemy import Enemy
import math
from scoreboard import Scoreboard, Lives, Lose

screen = Screen()
screen.bgcolor('black')
screen.setup(800, 600)
screen.tracer(0)

gameover = False
run = True
bullets = []
player = Player()
enemies = []
score = 0
lives = 3
scoreboard = Scoreboard()
live = Lives()
scoreboard.create_scoreboard(score)
live.create_scoreboard(lives)
lose = Lose()


def bullet_handler():
    global bullets
    if len(bullets) <= 0:
        bullet = Bullet(player)
        bullets.append(bullet)


def spawn_enemy():
    global enemies
    enemy = Enemy()
    enemies.append(enemy)


screen.listen()
screen.onkey(player.move_left, 'Left')
screen.onkey(player.move_right, 'Right')
screen.onkey(bullet_handler, 'space')


def isCollision(t1,t2):
    """
    Checks for collision between two Turtle Objects. Taken from 'https://ygok17.medium.com/space-invaders-game-using-python-e9d878dd227f'.
    """
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False


while run:
    if not gameover:
        for bullet in bullets:
            bullet.move()

            if bullet.ycor() > 300:
                bullet.hideturtle()
                bullets.remove(bullet)

        for i in range(3):
            if len(enemies) < 3:
                spawn_enemy()

        for enemy in enemies:
            enemy.move_down()

        for enemy in enemies:
            for bullet in bullets:
                if isCollision(enemy, bullet):
                    enemy.hideturtle()
                    bullet.hideturtle()
                    try:
                        enemies.remove(enemy)
                        bullets.remove(bullet)
                    except:
                        pass
                    score += 20
                    scoreboard.create_scoreboard(score)

        for enemy in enemies:
            if enemy.ycor() < -280:
                enemy.hideturtle()
                enemies.remove(enemy)
                lives -= 1
                live.create_scoreboard(lives)

        if lives < 1:
            gameover = True
            lose.create_scoreboard()

    screen.update()

screen.exitonclick()
