import random
import pygame
import sys

print("Hello")

pygame.init()

game_font = pygame.font.Font(None, 22)

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Shooter")

STEP = 0.3
BALL_STEP = 0.3
background_color = (32, 52, 71)

game = True
restart = False

class Player():
    figther_image = pygame.image.load("images/fighter.png")
    width,height = figther_image.get_size()
    x, y = screen_width / 2 - width / 2, screen_height - height
    fighter_left, fighter_right = False, False

class Ball:
    ball_image = pygame.image.load("images/ball.png")
    width, height = ball_image.get_size()
    x, y = Player.x + Player.width / 2 - width / 2, Player.y - height
    start = False

class Enemy:
    enemy_image = pygame.image.load("images/alien.png")
    width, height = enemy_image.get_size()
    cicle = 1
    enemy_speed = 0.1
    x, y = random.randint(0, screen_width - width), 0
    spawner = False

class Score_board:
    with open("score.txt", "r") as file:
        previous_score = file.read()
    score = 0

def restart_game():
    global restart
    restart = False
    Score_board.score = 0
    Ball.start = False
    Player.x, Player.y = screen_width / 2 - Player.width / 2, screen_height - Player.height
    Enemy.cicle = 1
    Enemy.x, Enemy.y = random.randint(0, 500), 0
    Player.fighter_left = False
    Player.fighter_right = False
    with open("score.txt", "r") as file:
        Score_board.previous_score = file.read()

def remember_score():
    with open("score.txt", "r") as file:
        now = Score_board.score
        in_file = file.read()
        if int(in_file) < now:
            with open("score.txt", "w") as file2:
                file2.write(str(now))

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_LEFT:
                Player.fighter_left = True
            if event.key == pygame.K_RIGHT:
                Player.fighter_right = True
            if event.key == pygame.K_SPACE:
                Ball.x, Ball.y = Player.x + Player.width / 2 - Ball.width / 2, Player.y - Ball.height
                Ball.start = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                Player.fighter_left = False
            if event.key == pygame.K_RIGHT:
                Player.fighter_right = False

    if Player.fighter_left and Player.x >= STEP:
        Player.x -= STEP

    if Player.fighter_right and Player.x <= screen_width - Player.width - STEP:
        Player.x += STEP

    if Ball.start and Ball.y + Ball.height < 0:
        Ball.start = False

    if Ball.start:
        Ball.y -= BALL_STEP

    if Enemy.spawner:
        Enemy.y += (Enemy.enemy_speed * Enemy.cicle)

    if not Enemy.spawner:
        Enemy.spawner = True
        Enemy.cicle += 0.1

    screen.fill(background_color)

    screen.blit(Player.figther_image, (Player.x, Player.y))

    if Enemy.spawner:
        screen.blit(Enemy.enemy_image, (Enemy.x, Enemy.y))

    if Ball.start:
        screen.blit(Ball.ball_image, (Ball.x, Ball.y))

    score_text = game_font.render(f"Score: {Score_board.score}", True, "white")
    screen.blit(score_text, (20, 20))

    score_previous_text = game_font.render(f"Best Score: {Score_board.previous_score}", True, "white")
    screen.blit(score_previous_text, (20, 45))

    pygame.display.update()

    if Enemy.y + Enemy.height > Player.y:
        restart = True

    if Ball.start and Enemy.x < Ball.x < Enemy.x + Enemy.width - Ball.width + 15 and Enemy.y < Ball.y < Enemy.y + Enemy.height - Ball.height  + 15:
        Score_board.score += 1
        Enemy.x, Enemy.y = random.randint(0, 500), 0
        Enemy.spawner = False
        Ball.start = False

    while restart:
        game_over = game_font.render("Game Over", True, "white")
        game_over_rect = game_over.get_rect()
        game_over_rect.center  = (screen_width / 2, screen_height / 2)
        screen.blit(game_over, game_over_rect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                remember_score()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    remember_score()
                    restart_game()