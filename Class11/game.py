
import pygame
import random
import time

background_color = (255, 255, 255)
score_color = (0, 0, 0)
gameover_color = (255, 0, 0)

pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('My first game')
clock = pygame.time.Clock()

pygame.mixer.music.load('8-bitmusic.wav')
pygame.mixer.music.play(-1)

space_ship_image = pygame.image.load('spaceshipthumbnail.png')
enemy_image = pygame.image.load('ISISflagthumbnail.png')
explosion_image = pygame.image.load('Explosionthumbnail.png')

explosion_sound = pygame.mixer.Sound('Explosionsound.wav')

def show_space_ship(x, y):
    gameDisplay.blit(space_ship_image, (x,y))

def show_enemy(x, y):
    gameDisplay.blit(enemy_image, (x, y))

def crash(x,y):
    pygame.mixer.Sound.play(explosion_sound)
    pygame.mixer.music.stop()
    gameDisplay.blit(explosion_image, (x, y))
    font = pygame.font.SysFont(None, 100)
    text = font.render('Game Over', True, gameover_color)
    gameDisplay.blit(text, (200, 250))
    pygame.display.update()
    time.sleep(4)

def show_score(score):
    font = pygame.font.SysFont(None, 25)
    text = font.render(f'Score {score}', True, score_color)
    gameDisplay.blit(text, (0,0))

gameover = False

x = 400
y = 300
speed_x = 0
speed_y = 0
score = 0

enemy_x = random.randint(0, 800)
enemy_y = 0
enemy_speed = 7

while not gameover:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame. K_LEFT:
                speed_x = -5
            elif event.key == pygame.K_RIGHT:
                speed_x = 5

        if event.type == pygame.KEYDOWN:
            if event.key == pygame. K_DOWN:
                y += 5
            elif event.key == pygame. K_UP:
                y -= 5
    
    gameDisplay.fill(background_color)

    enemy_y += enemy_speed
    if enemy_y > 600:
        enemy_x = random.randint(0, 600)
        enemy_y = 0
        score += 10
    x += speed_x
    y += speed_y
    show_space_ship(x, y)
    show_enemy(enemy_x, enemy_y)
    show_score(score)
    if enemy_x > x - 64 and enemy_x < x + 64 and enemy_y > y - 64 and enemy_y < y + 64:
        crash(x, y)
        gameover = True
    pygame.display.update()
    clock.tick(60)

pygame.quit()