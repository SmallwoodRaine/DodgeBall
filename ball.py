import pygame
import time
import sys
import random
import wall
import player
import projectile
from tkinter import *
from math import *
from pygame.locals import *

# intializes pygame
pygame.init()

# constants
DW = 1000
DH = 750
BALLRADIUS = 20
BALLVELOCITY = 2
INITIALPOSITION = (DW/2, DH/2)
COLLISIONRADIUS = 10
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SCOREFONT = pygame.font.SysFont("Times New Roman", 18)
GAMEDISPLAY = pygame.display.set_mode((DW, DH))
clock = pygame.time.Clock()

pygame.display.set_caption('Ball')
GAMEDISPLAY.fill(WHITE)


# allows easy way to dynamically create projectiles
def createRock(x, y, velocity):
    rock = projectile.Projectile(x, y, velocity)
    return rock


def gameLoop():
    # pygame.init()
    # # constants
    # DW = 1000
    # DH = 750
    # BALLRADIUS = 20
    # BALLVELOCITY = 2
    # INITIALPOSITION = (DW/2, DH/2)
    # COLLISIONRADIUS = 10
    # WHITE = (255, 255, 255)
    # BLACK = (0, 0, 0)

    # SCOREFONT = pygame.font.SysFont("Times New Roman", 18)
    # GAMEDISPLAY = pygame.display.set_mode((DW, DH))
    # clock = pygame.time.Clock()

    # pygame.display.set_caption('Ball')
    # GAMEDISPLAY.fill(WHITE)

    score = 0
    boundary = wall.Wall(DW, 0, DH, 0)
    rocks = []
    ball = player.Player(INITIALPOSITION[0], INITIALPOSITION[1])   
    xDiff = 0
    yDiff = 0
    while True:
        # Check for collision
        for i in rocks:
            if ((i.x <= ball.x + BALLRADIUS and
                 i.x >= ball.x - BALLRADIUS) and 
                (i.y <= ball.y + BALLRADIUS and 
                 i.y >= ball.y - BALLRADIUS)):
                pygame.quit()
                sys.exit()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # movement
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    xDiff = -ball.speed
                    yDiff = 0
                if event.key == K_RIGHT:
                    xDiff = ball.speed
                    yDiff = 0
                if event.key == K_DOWN:
                    yDiff = -ball.speed
                    xDiff = 0
                if event.key == K_UP:
                    yDiff = ball.speed
                    xDiff = 0
        # shooting projectiles
                if event.key == K_a:
                    rocks.append(createRock(ball.x-25, ball.y, [-3, 0]))
                    score += 1
                elif event.key == K_d:
                    rocks.append(createRock(ball.x+25, ball.y, [3, 0]))
                    score += 1
                elif event.key == K_s:
                    rocks.append(createRock(ball.x, ball.y+25, [0, 3]))
                    score += 1
                elif event.key == K_w:
                    rocks.append(createRock(ball.x, ball.y-25, [0, -3]))    
                    score += 1

        ball.x += xDiff
        ball.y -= yDiff
        GAMEDISPLAY.fill(WHITE)
        # check if ball hits boundaries
        ball.bounceBoundaries(boundary)

        # check for collisions between projectiles
        for i, rck in enumerate(rocks):
            for j, rck1 in enumerate(rocks):
                # cover the entire radius of projectiles
                if ((rck.x <= rck1.x + COLLISIONRADIUS and
                     rck.x >= rck1.x - COLLISIONRADIUS) and
                    (rck.y <= rck1.y + COLLISIONRADIUS and
                     rck.y >= rck1.y - COLLISIONRADIUS) and (i != j)):
                    rck.collision(rck1)
            rck.deflectBoundaries(boundary)
            rck.move()
            pygame.draw.circle(GAMEDISPLAY, 
                               BLACK, 
                               (int(rck.x), int(rck.y)), 5, 0)       
        pygame.draw.circle(
            GAMEDISPLAY, BLACK, (int(ball.x), int(ball.y)), 20, 0)       
        displayScore = SCOREFONT.render(str(score), 1, BLACK)
        GAMEDISPLAY.blit(displayScore, (520, 20))
        clock.tick(30)
        pygame.display.update()
    pygame.quit()    


# def mainMenu():
#     root = Tk()
#     button = Button(root, 
#                     text='Main Menu', 
#                     command=gameLoop)
#     label = Canvas(root,
#                    background='orange',
#                    height=100, 
#                    width=150)
#     text = Label(root, 
#                  font=('Helvetica', 16, 'bold'),
#                  foreground='yellow',
#                  # background='white',
#                  padx=25,
#                  pady=10,
#                  text='Welcome to Balls',
#                  width=70,
#                  height=35)
#     label.grid(row=0, column=0, columnspan=3, rowspan=3)
#     text.grid(row=0, column=0, columnspan=2, rowspan=2)
#     # label.pack(side=RIGHT, fill='both', expand=True)
#     button.grid(row=4, column=3)
#     root.mainloop()
def mainMenu():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())

mainMenu()
gameLoop()
# mainMenu()
