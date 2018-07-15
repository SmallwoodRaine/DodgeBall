import pygame
import time 
from pygame.locals import *

pygame.init()

class Player:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		shoot = False

class Projectile:
	def __init__(self, x, y):
		self.x = x
		self.y = y

rocks = [Projectile(0,0) for i in range(100)]
DW = 800 
DH = 600
INTIALPOSITION = (DW/2,DH/2 )
WHITE = (255, 255, 255)
BLACK = (0, 0 ,0)
GAMEDISPLAY = pygame.display.set_mode((DW, DH))

pygame.display.set_caption('Ball')

clock = pygame.time.Clock()

GAMEDISPLAY.fill(WHITE)


#start player at middle of screen
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
			if event.key == K_SPACE:
				if event.key == K_LEFT:
					pass
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
	ball.x += xDiff
	ball.y -= yDiff
	GAMEDISPLAY.fill(WHITE)					
	pygame.draw.circle(GAMEDISPLAY, BLACK, (int(ball.x), int(ball.y)), 20, 0)
	clock.tick(30)
	pygame.display.update()

pygame.quit()