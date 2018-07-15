import pygame
import time 
from pygame.locals import *
# The point of the game is to survive 
# with as many balls as you can spawn
# on the screen.
# The score will be based on amount of balls and time spent.
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
GAMEDISPLAY = pygame.display.set_mode((DW, DH))
BALLVELOCITYx = 1
BALLVELOCITYy = 1
pygame.display.set_caption('Ball')

clock = pygame.time.Clock()

GAMEDISPLAY.fill(WHITE)

def createRock(x, y, direction):
	rock = Projectile(x, y, direction)
	return rock

#start player at middle of screen
rocks = []
ball = Player(INTIALPOSITION[0], INTIALPOSITION[1])	
xDiff = 0
yDiff = 0
while True:
	for event in pygame.event.get():
		
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		
		# movement 
		if event.type == KEYDOWN:
			if event.key == K_LEFT:
				xDiff = -5
			if event.key == K_RIGHT:
				xDiff = 5
			if event.key == K_DOWN:
				yDiff = -5
			if event.key == K_UP:	
				yDiff = 5
			
	#shooting projectiles		
			if event.key == K_a:
				rocks.append(createRock(ball.x, ball.y, LEFT))
			if event.key == K_RIGHT:
				xDiff = 5
			if event.key == K_DOWN:
				yDiff = -5
			if event.key == K_UP:	
				yDiff = 5

		if event.type ==KEYUP:
		  	if event.key == K_DOWN or event.key == K_UP: 
		  		yDiff = 0
		  	if event.key == K_RIGHT or event.key == K_LEFT:
		  		xDiff = 0
		  	if event.key == K_SPACE:
		  		xDiff = 0
		  		yDiff = 0
	ball.x += xDiff
	ball.y -= yDiff
	GAMEDISPLAY.fill(WHITE)
	for i in rocks:
		if i.direction == LEFT:
			i.x -= BALLVELOCITYx
		pygame.draw.circle(GAMEDISPLAY, BLACK, (int(i.x), int(i.y)), 5, 0)					
	pygame.draw.circle(GAMEDISPLAY, BLACK, (int(ball.x), int(ball.y)), 20, 0)
	clock.tick(30)
	pygame.display.update()

pygame.quit()