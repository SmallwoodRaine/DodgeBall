import sys
import mainMenu
sys.path.append('Resources')

# Welcome to Dodgeball.
# The point of the game it to shoot as many balls
# as you can without dying.
# Enjoy!!!
# will need to install pygame to play

# constants
DW = 1000
DH = 750
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

if __name__ == "__main__":
    gameInitialize = mainMenu.MainMenu(DW, DH)
    gameInitialize.mainMenuLoop()