import pygame
import sys
import random

def text_objects(text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()

def message_display(text, text_x, text_y, text_size, color):
        largeText = pygame.font.Font('freesansbold.ttf',text_size)
        TextSurf, TextRect = text_objects(text, largeText, color)
        TextRect.center = (text_x, text_y)
        gameDisplay.blit(TextSurf, TextRect)

pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Dino Game')

player_x = 100
player_y = 460
width = 40
height = 40
blue = (0,0,255)
green = (0,255,0)
black = (0,0,0)
red = (255,0,0)
white = (255,255,255)
crashed = False
x_change = 0
y_change = 0
clock = pygame.time.Clock()
gravity = True
timer = 0
frame_num = 0
key_up_has_been_pressed = False
you_lose = False
score = 0
obs1 = [1, 760, 460, "Cactus", False, 40, 40, 0]
obs2 = [2, 760, 460, "Cactus", False, 40, 40, 0]
obs3 = [3, 760, 460, "Cactus", False, 40, 40, 0]
obs4 = [4, 760, 455, "Pterodactyl", True, 40, 20, 0]
obs5 = [5, 760, 455, "Pterodactyl", False, 40, 20, 0]
obs6 = [6, 760, 455, "Pterodactyl", False, 40, 20, 0]
chooseObstacle = [obs1, obs2, obs3, obs4, obs5, obs6]
j = 1

# One iter of this while loop = basically 1 frame
while not crashed:

    # On a single frame, this for goes through each event made because multiple events could have been made
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_UP and player_y == 460:
                key_up_has_been_pressed = True
            elif event.key == pygame.K_DOWN and player_y == 460:
                height = 20
                player_y += 20
            elif event.key == pygame.K_r and you_lose == True:
                you_lose = False
                chooseObstacle[1] [4] = True
                score = 0
                j = 1

        if event.type == pygame.KEYUP:
                height = 40

    # If it should run every frame it should be under this

    for elem in chooseObstacle:
        if elem[4] == True and elem[7] <= 0:
            elem[1] += -3
        if elem[4] == True and elem[1] <= 500 and elem[1] >= 498:
            notExit = True
            while notExit:
                i = random.randint(1,6)
                if elem[0] != i and chooseObstacle[i - 1] [4] != True:
                    chooseObstacle[i - 1] [4] = True
                    chooseObstacle[i - 1] [1] = 760
                    chooseObstacle[i - 1] [7] = random.randint(0, 50)
                    notExit = False

    # Check if you hit a obstacle
    for elem in chooseObstacle:
        if player_y <= 420 or (player_y == 480 and elem[3] == "Pterodactyl"):
            continue
        elif player_x >= (elem[1] - width) and player_x <= (elem[1] + width):
            you_lose = True
            for elem in chooseObstacle:
                elem[4] = False
                elem[1] = 760
                elem[7] = 0

    # Scoring
    if you_lose == True and j == 1:
        current_Score = score
        j = 2

    # Jump
    if key_up_has_been_pressed and frame_num < 30:
        gravity = False
        y_change = -4
        frame_num += 1
    else:
        gravity = True
        key_up_has_been_pressed = False
        y_change = 0
        frame_num = 0

    # Gravity
    if gravity == True:
        if player_y < (500 - height):
            y_change = 3
        else:
            y_change = 0
            player_y = (500 - height)

    # All drawing should be under this
    gameDisplay.fill(blue)

    player_y += y_change
    score += 1
    timer += 1

    for elem in chooseObstacle:
        if elem[1] <= 2:
            elem[4] = False
            elem[7] = 0
            elem[1] = 760
        if elem[4] == True:
            if elem[7] <= 0:
                pygame.draw.rect(gameDisplay, green, [elem[1], elem[2], elem[5], elem[6]])
            else:
                elem[7] += -1

    pygame.draw.rect(gameDisplay, black, [0, 500, 800, 100])
    pygame.draw.rect(gameDisplay, red, [player_x, player_y, width, height])
    message_display(f"Current Score: {score}", 700, 10, 20, white)
    
    # Draw you lose
    if you_lose == True:
        gameDisplay.fill(black)
        message_display('Game Over', 400, 200, 115, red)
        message_display(f"Your score is {current_Score}" , 400, 450, 40, blue) 
        message_display('To restart press R', 400, 500, 20, red)

    pygame.display.update()
    clock.tick(60)