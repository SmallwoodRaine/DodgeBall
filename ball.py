import pygame
import time 
import sys
from pygame.locals import *
# The point of the game is to survive 
# with as many balls as you can spawn
# on the screen.
# The score will be based on amount of balls and time spent.
# I will be making functions for all the if statements.


# Todo List
	#Add rectangles that randomly appear upon map start that are boundaries
	#Add random score bonus drops after score is so high
pygame.init()

class Player:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		#shoot = False

class Projectile:
	def __init__(self, x, y, intialDirection):
		self.x = x
		self.y = y
		self.direction = intialDirection

LEFT = 0b01
RIGHT = 0b010
UP = 0b0100
DOWN = 0b01000

DW = 800 
DH = 600
INTIALPOSITION = (DW/2,DH/2 )
WHITE = (255, 255, 255)
BLACK = (0, 0 ,0)
myFont = pygame.font.SysFont("Times New Roman", 18)


GAMEDISPLAY = pygame.display.set_mode((DW, DH))
BALLVELOCITY = 2
pygame.display.set_caption('Ball')

clock = pygame.time.Clock()

GAMEDISPLAY.fill(WHITE)

def createRock(x, y, direction):
	rock = Projectile(x, y, direction)
	return rock

#start player at middle of screen
def gameLoop():
	score = 0
	rocks = []
	ball = Player(INTIALPOSITION[0], INTIALPOSITION[1])	
	xDiff = 0
	yDiff = 0
	while True:
		# Check if 
		for i in rocks:
			if (i.x <= ball.x + 12 and i.x >= ball.x - 12) and (i.y <= ball.y + 12 and i.y >= ball.y - 12):
				pygame.quit()

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			# movement 
			if event.type == KEYDOWN:
				if event.key == K_LEFT:
					xDiff = -5
					yDiff = 0
				if event.key == K_RIGHT:
					xDiff = 5
					yDiff = 0
				if event.key == K_DOWN:
					yDiff = -5
					xDiff = 0
				if event.key == K_UP:	
					yDiff = 5
					xDiff = 0
				
		#shooting projectiles		
				if event.key == K_a:
					rocks.append(createRock(ball.x-25, ball.y, LEFT))
					score += 1
				elif event.key == K_d:
					rocks.append(createRock(ball.x+25, ball.y, RIGHT))
					score += 1
				elif event.key == K_s:
					rocks.append(createRock(ball.x, ball.y+25, DOWN))
					score += 1
				elif event.key == K_w:	
					rocks.append(createRock(ball.x, ball.y-25, UP)) 		
					score += 1
		ball.x += xDiff
		ball.y -= yDiff
		GAMEDISPLAY.fill(WHITE)
		if ball.x < 0:
			ball.x = 0
		if ball.x > DW:
			ball.x = DW
		if ball.y < 0:
			ball.y = 0
		if ball.y > DH:
			ball.y = DH

		# make all if statements a function to clean up
		for i in rocks:	
			if i.x < 0:
				i.direction = RIGHT
			if i.x > DW:
				i.direction = LEFT
			if i.y < 0:
				i.direction = DOWN
			if i.y > DH:
				i.direction = UP

			if i.direction == LEFT:
				i.x -= BALLVELOCITY
			if i.direction == RIGHT:
				i.x += BALLVELOCITY
			if i.direction == UP:
				i.y -= BALLVELOCITY
			if i.direction == DOWN:
				i.y += BALLVELOCITY	
			 #and int(i.y) == int(ball.y):
			pygame.draw.circle(GAMEDISPLAY, BLACK, (int(i.x), int(i.y)), 5, 0)
		pygame.draw.circle(GAMEDISPLAY, BLACK, (int(ball.x), int(ball.y)), 20, 0)
		displayScore = myFont.render(str(score),1,BLACK)
		GAMEDISPLAY.blit(displayScore, (520, 20))
		clock.tick(30)
		pygame.display.update()
gameLoop()
pygame.quit()