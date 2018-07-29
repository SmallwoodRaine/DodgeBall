import pygame
from math import *
from pygame.locals import *
import time
import sys
import wall
import player
import projectile


# constants
DW = 1000
DH = 750

BALLRADIUS = 20
BALLVELOCITY = 2
INITIALPOSITION = (DW/2, DH/2)
COLLISIONRADIUS = 10
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# extra functions 
def createRock(x, y, velocity):
    rock = projectile.Projectile(x, y, velocity)
    return rock


class Game:

    def __init__(self, displayWidth, displayHeight): 
        
        pygame.init()
        self.displayWidth = displayWidth
        self.displayHeight = displayHeight
        self.gameDisplay = pygame.display.set_mode((
                                                    self.displayWidth,
                                                    self.displayHeight))
        self.score = 0
    
    def gameLoop(self):
        
        scoreFont = pygame.font.SysFont("Times New Roman", 18)
        clock = pygame.time.Clock()
        pygame.display.set_caption('Ball')
        self.gameDisplay.fill(WHITE)
        # creates game boudary
        boundary = wall.Wall(self.displayWidth, 0, self.displayHeight, 0)
        rocks = []
        # creates player (main ball)
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
                    self.gameDisplay.fill(WHITE)
                    return
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
                        self.score += 1
                    elif event.key == K_d:
                        rocks.append(createRock(ball.x+25, ball.y, [3, 0]))
                        self.score += 1
                    elif event.key == K_s:
                        rocks.append(createRock(ball.x, ball.y+25, [0, 3]))
                        self.score += 1
                    elif event.key == K_w:
                        rocks.append(createRock(ball.x, ball.y-25, [0, -3]))    
                        self.score += 1

            ball.x += xDiff
            ball.y -= yDiff
            self.gameDisplay.fill(WHITE)
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
                pygame.draw.circle(self.gameDisplay, 
                                   BLACK, 
                                   (int(rck.x), int(rck.y)), 5, 0)       
            pygame.draw.circle(
                self.gameDisplay, BLACK, (int(ball.x), int(ball.y)), 20, 0)    
            displayScore = scoreFont.render(str(self.score), 1, BLACK)
            self.gameDisplay.blit(displayScore, (520, 20))
            clock.tick(30)
            pygame.display.update()

