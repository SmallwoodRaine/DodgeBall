import mainMenu

# constants
DW = 1000
DH = 750
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

if __name__ == "__main__":
    gameInitialize = mainMenu.MainMenu(DW, DH)
    gameInitialize.mainMenuLoop()