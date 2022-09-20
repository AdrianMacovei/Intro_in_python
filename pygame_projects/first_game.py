import pygame
import random
import math
# initialize the pygame - always used
pygame.init()

# create a screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('space-galaxy-background.jpg')

# global score
score = 0

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("space-invaders.png")
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("alien.png"))
    enemyX.append(random.randint(0, 720))
    enemyY.append(random.randint(50, 100))
    enemyX_change.append(0.3)
    enemyY_change.append(40)

# Bullet
# Ready - You can't see the bullet on the screen
# Fire -The bullet is currently moving
bulletImg = pygame.image.load("bullet.png")
bulletX = 370
bulletY = 480
bulletX_change = 0
bulletY_change = 1
bullet_state = "ready"




def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    # matematic formula for distance 2 oject with 2 axes coord x and y
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

# Game loop
running = True

while running:
    # RGB - red, green, blue
    screen.fill((0, 150, 255))

    # background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressd ckeck whether its right or left
        if event.type == pygame.KEYDOWN:
            # this verify if a key is pressed
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    # Get the curent x coordinate of spaceship
                    bulletX = playerX
                    fire_bullet(playerX, bulletY)
        if event.type == pygame.KEYUP:
            # this verify if a key is released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    playerY += playerY_change
    playerX += playerX_change
    if playerX < 0:
        playerX = 0
    elif playerX >= 720:
        playerX = 720

    # Enemy Movement
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.1
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 720:
            enemyX_change[i] = - 0.1
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score += 1
            print(score)
            enemyX[i] = random.randint(0, 720)
            enemyY[i] = random.randint(50, 100)
        enemy(enemyX[i], enemyY[i], i)

    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    # this need to be here always
    pygame.display.update()
