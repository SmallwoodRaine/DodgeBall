import pygame
from pygame.locals import *


class Button:

    # x and y intial give top left coordinates of button and the Span's give the 
    def __init__(self, xInitial, yInitial, xSpan, ySpan, display):
        self.xInitial = xInitial
        self.yInitial = yInitial
        self.xSpan = xSpan
        self.ySpan = ySpan
        self.display = display
        self.isPressed = False

    # check if coordinates(tuple) are within button 
    def isButtonPressed(self, coordinates):
        if (coordinates[0] > self.xInitial and
            coordinates[0] < (self.xInitial + self.xSpan) and
            coordinates[1] > self.yInitial and
                coordinates[1] < (self.yInitial + self.ySpan)):
            self.isPressed = True
        else:        
            self.isPressed = False
        return self

    # draw button to screen 
    def draw(self, color, label, labelColor, fontSize):
        labelFont = pygame.font.SysFont("Times New Roman", fontSize)
        displayLabel = labelFont.render(label, 1, labelColor)
        if not self.isPressed:
            pygame.draw.rect(
                             self.display, 
                             color, 
                             [self.xInitial, 
                              self.yInitial, 
                              self.xSpan, 
                              self.ySpan])
            self.display.blit(displayLabel, (self.xInitial, self.yInitial))       
        # when pressed creates second rectangle that appears as a border
        else:
            pygame.draw.rect(
                             self.display, 
                             (30, 30, 30), 
                             [self.xInitial - 20, 
                              self.yInitial - 20, 
                              self.xSpan + 40, 
                              self.ySpan + 40])
            pygame.draw.rect(
                             self.display, 
                             color, 
                             [self.xInitial, 
                              self.yInitial, 
                              self.xSpan, 
                              self.ySpan])
            
            self.display.blit(displayLabel, (self.xInitial, self.yInitial))
