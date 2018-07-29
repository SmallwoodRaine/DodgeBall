import pygame
from pygame.locals import *
import game
from button import *

#constants
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
                              self.displayWidth / 4,
                              self.displayWidth / 2,
                              self.displayHeight / 1.5,
                              self.displayHeight / 5 - 60,
                              self.menuDisplay)
        highScoreBttn = Button(
                              self.displayWidth / 4,
                              self.displayWidth / 2 + 100,
                              self.displayHeight / 1.5,
                              self.displayHeight / 5 - 60,
                              self.menuDisplay)

        titleFont = pygame.font.SysFont("Times New Roman", 70)
        subTitleFont = pygame.font.SysFont("Times New Roman", 30)
        title = titleFont.render("WELCOME TO DODGEBALLS!!", 1, BLACK)
        subTitle = subTitleFont.render("I know, very creative...", 1, BLACK)

        clock = pygame.time.Clock()
        pygame.display.set_caption('Main Menu')
        highScoreList = HighScoresList(
                               "highScoreList.txt",
                               self.displayWidth,
                               self.displayHeight) 
        self.menuDisplay.fill(WHITE)
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    # check if buttons are pressed
                    playGameBttn.isButtonPressed(pygame.mouse.get_pos()) 
                    highScoreBttn.isButtonPressed(pygame.mouse.get_pos())                
                    
                    if playGameBttn.isPressed:
                        ballGame = game.Game(
                                             self.displayWidth, 
                                             self.displayHeight)
                        
                        ballGame.gameLoop()
                        highScoreList.adjustHighScoreList(ballGame.score)
                        playGameBttn.isPressed = False

                    if highScoreBttn.isPressed:
                        highScoreList.highScoreLoop()
                        highScoreBttn.isPressed = False
                        self.menuDisplay.fill(WHITE)         
                self.menuDisplay.blit(title, (5, 100))
                self.menuDisplay.blit(
                                      subTitle,
                                      (self.displayWidth / 2 - 120, 250))       
                
                playGameBttn.draw(BLACK, "PLAY GAME!!!!", WHITE, 75)
                highScoreBttn.draw(BLACK, "    High Scores", WHITE, 75)
            pygame.display.update()
        pygame.quit()            


class HighScoresList:
    def __init__(self, file, displayWidth, displayHeight):
        self.file = file
        self.displayWidth = displayWidth
        self.displayHeight = displayHeight
        self.highScoreDisplay = pygame.display.set_mode((
                                               self.displayWidth,
                                               self.displayHeight))
        self.newHighScore = False

    # check if new score is in high scores then copy to file
    def adjustHighScoreList(self, score):
        scoreList = self.fromHighScoreFile()
        for i, prevScores in enumerate(scoreList):
            if score > int(prevScores):
                self.newHighScore = True
                scoreList.insert(i, str(score))
                scoreList = scoreList[:5]
                break
        self.toHighScoreFile(scoreList)
    
    # open and write scores to file 
    def toHighScoreFile(self, scores):
        toFile = open(self.file, 'w')
        for i in scores:
            toFile.write(i + '\n')
        toFile.close()

    # open file and retrieve scores
    def fromHighScoreFile(self):
        fromFile = open(self.file, 'r')
        scoreList = [i.rstrip('\r\n') for i in fromFile.readlines()]
        fromFile.close()
        return scoreList

    # display scores by incrementing y coordinate by index number
    def displayScores(self):
        scores = self.fromHighScoreFile()
        scoreFont = pygame.font.SysFont("Times New Roman", 40)
        for i, score in enumerate(scores):
            scoreLabel = scoreFont.render(
                                          "{}. {}".format(i + 1, score),
                                          1, BLACK)
            self.highScoreDisplay.blit(
                                       scoreLabel,
                                       (self.displayWidth / 2 - 40,
                                        200 + i*40))

    def highScoreLoop(self):
        backBttn = Button(15, 40, 100, 40, self.highScoreDisplay)
        self.highScoreDisplay.fill(WHITE)
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                if event.type == MOUSEBUTTONDOWN:
                    backBttn.isButtonPressed(pygame.mouse.get_pos())
                    if backBttn.isPressed:
                        return
                backBttn.draw(BLACK, 'BACK', WHITE, 37)
                self.displayScores()
            pygame.display.update()

