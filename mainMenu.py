import game
import pygame
from pygame.locals import *
from button import *
# constants
DW = 1000
DH = 750
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class MainMenu:

    def __init__(self, displayWidth, displayHeight):
        pygame.init()
        self.displayWidth = displayWidth
        self.displayHeight = displayHeight
        self.menuDisplay = pygame.display.set_mode((
                                               self.displayWidth,
                                               self.displayHeight))
    
    def mainMenuLoop(self):
        playGameBttn = Button(
                              self.displayWidth/4,
                              self.displayWidth/2,
                              self.displayHeight/1.5,
                              self.displayHeight/5,
                              self.menuDisplay)
        menuFont = pygame.font.SysFont("Times New Roman", 18)
        clock = pygame.time.Clock()
        pygame.display.set_caption('Main Menu')
        self.menuDisplay.fill(WHITE)
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                if event.type == MOUSEBUTTONDOWN:
                    print(pygame.mouse.get_pos()[0])
                    print(pygame.mouse.get_pos()[1])
            # pygame.draw.rect(self.menuDisplay, BLACK, [250, 500, 500, 150])
            playGameBttn.draw(BLACK)
            pygame.display.update()
        pygame.quit()            


main = MainMenu(DW, DH)
main.mainMenuLoop()