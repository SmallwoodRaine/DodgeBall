import pygame


class Button:

    def __init__(self, xMin, xMax, yMin, yMax, gameDisplay):
        self.xMin = xMin
        self.xMax = xMax
        self.yMin = yMin
        self.yMax = yMax
        self.gameDisplay = gameDisplay
        self.isPressed = False

    # check if coordinates(tuple) are within button 
    def isPressed(self, coordinates):
        if (coordinates[0] > self.xMin and
            coordinates[0] < self.xMax and
            coordinates[1] > self.yMin and 
                coordinates[1] < self.yMax):
           
            self.isPressed = True
        else:
           
            self.isPressed = False
        return self.isPressed

    def draw(self, color):
        if not self.isPressed:
            pygame.draw.rect(
                             self.gameDisplay, 
                             color, 
                             [self.xMin, 
                              self.yMax, 
                              self.xMax, 
                              self.yMin])