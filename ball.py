import pygame
import time 
import sys
import random
from math import *
from pygame.locals import *

# The point of the game is to survive 
# with as many balls as you can spawn
# on the screen.
# The score will be based on amount of balls and time spent.
# I will be making functions for all the if statements.


# Todo List
	#Add rectangles that randomly appear upon map start that are boundaries
	#Add random score bonus drops after score is so high
class Wall:
	def __init__(self, maxX, minX, maxY, minY):
		self.maxX = maxX
		self.minX = minX
		self.maxY = maxY
		self.minY = minY

class Player:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.speed = 5

	def bounceBoundaries(self, wall):
		if self.x <= wall.minX:
			self.x += self.speed * 5
		if self.x >= wall.maxX:
			self.x -= self.speed * 5 
		if self.y <= wall.minY:
			self.y += self.speed * 5
		if self.y >= wall.maxY: 
			self.y -= self.speed * 5
		return self
	
	def move(self, key):
		if key == K_LEFT:
			xDiff = -self.speed
			yDiff = 0
		if key == K_RIGHT:
			xDiff = self.speed
			yDiff = 0
		if key == K_DOWN:
			yDiff = -self.speed
			xDiff = 0
		if key == K_UP:	
			yDiff = self.speed
			xDiff = 0
		return (xDiff, yDiff)

class Projectile:
	def __init__(self, x, y, initialVelocity):
		self.x = x
		self.y = y
		self.speed = 2
		self.velocity = initialVelocity 
			
	def deflectBoundaries(self, wall):
		if self.x < wall.minX:
			self.velocity[0] *= -1 
		if self.x > wall.maxX:
			self.velocity[0] *= -1
		if self.y < wall.minY:
			self.velocity[1] *= -1
		if self.y > wall.maxY:
			self.velocity[1] *= -1
		return self 			
	
	def move(self):
		self.x += self.velocity[0]
		self.y += self.velocity[1]
		return self

	def setAngle(self, angle):
		self.velocity[0] = 3 * cos(angle)
		self.velocity[1] = 3 * sin(angle)		

	def getAngle(self):
		return atan2(self.velocity[1], self.velocity[0])	

	def collision(self, rock):
		xDiff = self.x - rock.x
		yDiff = self.y - rock.y
		theta = atan2(yDiff, xDiff)
		self.setAngle(2 * theta - self.getAngle())
		rock.setAngle(2 * theta - rock.getAngle())
		(self.velocity[0], rock.velocity[0]) = (rock.velocity[0], self.velocity[0])
		(self.velocity[1], rock.velocity[1]) = (rock.velocity[1], self.velocity[1])
		
		# projectiles sticking together fix
		angle = 0.5 * pi + theta
		self.x += sin(angle)
		self.y -= cos(angle)
		rock.x -= sin(angle)
		rock.y += cos(angle)
		return(self, rock)

# intializes pygame
pygame.init()

# constants
DW = 1000 
DH = 750
BALLRADIUS = 20
BALLVELOCITY = 2
INITIALPOSITION = (DW/2,DH/2 )
COLLISIONRADIUS = 10
WHITE = (255, 255, 255)
BLACK = (0, 0 ,0)

SCOREFONT = pygame.font.SysFont("Times New Roman", 18)
GAMEDISPLAY = pygame.display.set_mode((DW, DH))
clock = pygame.time.Clock()

pygame.display.set_caption('Ball')
GAMEDISPLAY.fill(WHITE)

# allows easy way to dynamically create projectiles
def createRock(x, y, velocity):
	rock = Projectile(x, y, velocity)
	return rock
def mainMenu():
	GAMEDISPLAY.fill(WHITE)
	welcomeFont = pygame.font.SysFont("Times New Roman", 50)
	# GAMEDISPLAY.blit()
	while True:
		welcome = welcomeFont.render("Hello, welcome to DodgeBall!", 1, BLACK)
		pressToEnter = welcomeFont.render("PRESS SPACE TO START", 1, BLACK)
		GAMEDISPLAY.blit(pressToEnter, (DW/2 - 300, DH/2 - 60))
		GAMEDISPLAY.blit(welcome, (DW/2 - 315, DH/2 - 160))
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_SPACE:
					return
				if event.key == K_h:
					highScores()
					GAMEDISPLAY.fill(WHITE)
		clock.tick(30)
		pygame.display.update()

def getHighScores():
	scores = []
	fromFile = open('highScoreList.txt', 'r')
	for line in fromFile:
		scores.append(line)
	scores.sort(reverse = True)
	return scores

#drop newline and formate into numbered list 
def formatScores(scores):
	for i in range(len(scores)):
		scores[i] = scores[i].strip('\n')
		scores[i] = "{0}. {1}".format(i+1, scores[i])
	return scores

# display scores to screen
def highScores():
	# intialize with black white screen
	GAMEDISPLAY.fill(WHITE)
	
	#intialize font
	highScoreFont = pygame.font.SysFont("Times New Roman", 20)
	scores = formatScores(getHighScores())
	
	#use counter to put scores in list layout
	newLine = 0

	for i in scores:
		score = highScoreFont.render(i, 1, BLACK) 
		GAMEDISPLAY.blit(score, (DW/2 - 200, 50 + newLine))
		newLine += 20
	
	while True:		
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				return
		pygame.display.update()

def toHighScores(score):
	scores = getHighScores()
	for i in range(scores):
		scores[i] = int(scores[i][:2])
	print(scores)
	return


def gameLoop():
	# pygame.init()
	score = 0
	boundary = Wall(DW, 0, DH, 0)
	rocks = []
	ball = Player(INITIALPOSITION[0], INITIALPOSITION[1])	
	xDiff = 0
	yDiff = 0
	while True:
		# Check if 
		for i in rocks:
			if ((i.x <= ball.x + BALLRADIUS 
					and i.x >= ball.x - BALLRADIUS) 
					and (i.y <= ball.y + BALLRADIUS 
					and i.y >= ball.y - BALLRADIUS)):
				pygame.quit()
				toHighScores(score)
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
				
		#shooting projectiles		
				if event.key == K_a:
					rocks.append(createRock(ball.x-25, ball.y, [-3, 0] ))
					score += 1
				elif event.key == K_d:
					rocks.append(createRock(ball.x+25, ball.y, [3, 0]))
					score += 1
				elif event.key == K_s:
					rocks.append(createRock(ball.x, ball.y+25, [0, 3]))
					score += 1
				elif event.key == K_w:	
					rocks.append(createRock(ball.x, ball.y-25, [0,-3]))		
					score += 1

		ball.x += xDiff
		ball.y -= yDiff
		GAMEDISPLAY.fill(WHITE)
		
		# check if ball hits boundaries  
		ball.bounceBoundaries(boundary)

		#check for collisions between projectiles 
		for i, rck in enumerate(rocks):	
			for j, rck1 in enumerate(rocks):
				# cover the entire radius of projectiles
				if ((rck.x <= rck1.x + COLLISIONRADIUS 
						and rck.x >= rck1.x - COLLISIONRADIUS) 
						and (rck.y <= rck1.y + COLLISIONRADIUS 
						and rck.y >= rck1.y - COLLISIONRADIUS) 
						and (i != j)):
					rck.collision(rck1)
			rck.deflectBoundaries(boundary)
			rck.move()
			pygame.draw.circle(GAMEDISPLAY, BLACK, (int(rck.x), int(rck.y)), 5, 0)
		
		pygame.draw.circle(GAMEDISPLAY, BLACK, (int(ball.x), int(ball.y)), 20, 0)
		displayScore = SCOREFONT.render(str(score),1,BLACK)
		GAMEDISPLAY.blit(displayScore, (520, 20))
		clock.tick(30)
		pygame.display.update()

mainMenu()
gameLoop()
pygame.quit()