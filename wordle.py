import pygame
from sys import exit
import os

from helperclasses import Color
from helperclasses import LetterBox
from helperclasses import WordBox
from helperclasses import WordCollection

from helperfunctions import linkLetters
from helperfunctions import linkWords
from helperfunctions import getWord
from helperfunctions import ifValidWord


def main():
    
    Tan = Color((237, 242, 235),"#edf2eb")
    
    pygame.init()
    pygame.font.init()

    pygame.key.set_repeat(250,25)
    Clock = pygame.time.Clock()
    Width = 1370
    Height = 850
    Flags = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE
    Screen = pygame.display.set_mode((Width,Height), Flags)
    Screen.set_alpha(None)
    
    wordAnswer = getWord()

    
    ######################################################################################################
    
    letterboxDim = 80
    
    letterbox_xpos_1 = ((Width - letterboxDim) / 2)  - 180
    letterbox_xpos_2 = ((Width - letterboxDim) / 2) - 90
    letterbox_xpos_3 = ((Width - letterboxDim) / 2) 
    letterbox_xpos_4 = ((Width - letterboxDim) / 2) + 90
    letterbox_xpos_5 = ((Width - letterboxDim) / 2) + 180
    
    ######################################################################################################
    
    LetterOne1 = LetterBox(letterboxDim, letterboxDim, letterbox_xpos_1, 10)
    LetterTwo1 = LetterBox(letterboxDim, letterboxDim, letterbox_xpos_2, 10)
    LetterThree1 = LetterBox(letterboxDim, letterboxDim, letterbox_xpos_3, 10)
    LetterFour1 = LetterBox(letterboxDim, letterboxDim, letterbox_xpos_4, 10)
    LetterFive1 = LetterBox(letterboxDim, letterboxDim, letterbox_xpos_5, 10)
    
    # Links letters together
    linkLetters(LetterOne1, LetterTwo1, LetterThree1, LetterFour1, LetterFive1)
    WordBoxOne = WordBox(LetterOne1, LetterFive1)
    
    ######################################################################################################
    
    LetterOne2 = LetterBox(letterboxDim, letterboxDim, letterbox_xpos_1, 100)
    LetterTwo2 = LetterBox(letterboxDim, letterboxDim, letterbox_xpos_2, 100)
    LetterThree2 = LetterBox(letterboxDim, letterboxDim, letterbox_xpos_3, 100)
    LetterFour2 = LetterBox(letterboxDim, letterboxDim, letterbox_xpos_4, 100)
    LetterFive2 = LetterBox(letterboxDim, letterboxDim, letterbox_xpos_5, 100)
    
    # Links letters together
    linkLetters(LetterOne2, LetterTwo2, LetterThree2, LetterFour2, LetterFive2)
    WordBoxTwo = WordBox(LetterOne2, LetterFive2)

    ######################################################################################################
    
    LetterOne3 = LetterBox(letterboxDim, letterboxDim, letterbox_xpos_1, 190)
    LetterTwo3 = LetterBox(letterboxDim, letterboxDim, letterbox_xpos_2, 190)
    LetterThree3 = LetterBox(letterboxDim, letterboxDim, letterbox_xpos_3, 190)
    LetterFour3 = LetterBox(letterboxDim, letterboxDim, letterbox_xpos_4, 190)
    LetterFive3 = LetterBox(letterboxDim, letterboxDim, letterbox_xpos_5, 190)
    
    # Links letters together
    linkLetters(LetterOne3, LetterTwo3, LetterThree3, LetterFour3, LetterFive3)
    WordBoxThree = WordBox(LetterOne3, LetterFive3)
    
    ###########################################################################################ad###########
    
    LetterOne4 = LetterBox(letterboxDim, letterboxDim, letterbox_xpos_1, 280)
    LetterTwo4 = LetterBox(letterboxDim, letterboxDim, letterbox_xpos_2, 280)
    LetterThree4 = LetterBox(letterboxDim, letterboxDim, letterbox_xpos_3, 280)
    LetterFour4 = LetterBox(letterboxDim, letterboxDim, letterbox_xpos_4, 280)
    LetterFive4 = LetterBox(letterboxDim, letterboxDim, letterbox_xpos_5, 280)
    
    # Links letters together
    linkLetters(LetterOne4, LetterTwo4, LetterThree4, LetterFour4, LetterFive4)
    WordBoxFour = WordBox(LetterOne4, LetterFive4)
    
    ######################################################################################################

    LetterOne5 = LetterBox(letterboxDim, letterboxDim, letterbox_xpos_1, 370)
    LetterTwo5 = LetterBox(letterboxDim, letterboxDim, letterbox_xpos_2, 370)
    LetterThree5 = LetterBox(letterboxDim, letterboxDim, letterbox_xpos_3, 370)
    LetterFour5 = LetterBox(letterboxDim, letterboxDim, letterbox_xpos_4, 370)
    LetterFive5 = LetterBox(letterboxDim, letterboxDim, letterbox_xpos_5, 370)
    
    # Links letters together
    linkLetters(LetterOne5, LetterTwo5, LetterThree5, LetterFour5, LetterFive5)
    WordBoxFive = WordBox(LetterOne5, LetterFive5)
    
    ######################################################################################################
    
    LetterOne6 = LetterBox(letterboxDim, letterboxDim, letterbox_xpos_1, 460)
    LetterTwo6 = LetterBox(letterboxDim, letterboxDim, letterbox_xpos_2, 460)
    LetterThree6 = LetterBox(letterboxDim, letterboxDim, letterbox_xpos_3, 460)
    LetterFour6 = LetterBox(letterboxDim, letterboxDim, letterbox_xpos_4, 460)
    LetterFive6 = LetterBox(letterboxDim, letterboxDim, letterbox_xpos_5, 460)
    
    # Links letters together
    linkLetters(LetterOne6, LetterTwo6, LetterThree6, LetterFour6, LetterFive6)
    WordBoxSix = WordBox(LetterOne6, LetterFive6)
    
    ###################################################################################################### 
    
    LetterOne7 = LetterBox(letterboxDim, letterboxDim, letterbox_xpos_1, 550)
    LetterTwo7 = LetterBox(letterboxDim, letterboxDim, letterbox_xpos_2, 550)
    LetterThree7 = LetterBox(letterboxDim, letterboxDim, letterbox_xpos_3, 550)
    LetterFour7 = LetterBox(letterboxDim, letterboxDim, letterbox_xpos_4, 550)
    LetterFive7 = LetterBox(letterboxDim, letterboxDim, letterbox_xpos_5, 550)
    
    # Links letters together
    linkLetters(LetterOne7, LetterTwo7, LetterThree7, LetterFour7, LetterFive7)
    WordBoxSeven = WordBox(LetterOne7, LetterFive7)
    
    ###################################################################################################### 
    
    # Links words together
    linkWords(WordBoxOne, WordBoxTwo, WordBoxThree, WordBoxFour, WordBoxFive, WordBoxSix)
    collection = WordCollection(WordBoxOne, WordBoxSix)
    collection.setCurrentWord(WordBoxOne)
    
    currWordBox = collection.currWord
    restart = False
    lost = False

    # Creates list of valid guesses
    file = open("validlist.txt", "r")
    validList = []

    for row in file:
        validList.append(row.strip().upper())

    file.close()

    notShow = False

    while 1:
        
        # For each event
        for event in pygame.event.get():
            
            if restart == True:
                # pygame.time.delay(3000)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        main()
                continue

            # If event is quit
            if event.type == pygame.QUIT:
                pygame.quit()
                os._exit(00)
                exit()

            # Typing
            if event.type == pygame.KEYDOWN:
                
                # Checks backspace
                if event.key == pygame.K_BACKSPACE:
                    currWordBox.placeInnerBox(event, Screen)

                # Checks for characters typed
                if (len(event.unicode) != 0):
                    
                    # Lowercase check
                    if (ord(event.unicode) >= 97 and ord(event.unicode) <= 122):
                        currWordBox.removeInnerBox(event, Screen)
                        
                    # Uppercase check
                    if (ord(event.unicode) >= 65 and ord(event.unicode) <= 90):
                        currWordBox.removeInnerBox(event, Screen)

                        
                # Checks for return 
                if event.key == pygame.K_RETURN:
                    
                    # Checks if word is filled
                    valid = ifValidWord(currWordBox.getWord(), validList, 0, len(validList) - 1)
                    if currWordBox.checkFilled(Screen) and valid:
                        
                        # Changes the box colors to Green
                        currWordBox.checkGreens(wordAnswer)
                        
                        if (currWordBox.checkCorrect()):
                            notShow = True
                            restart = True

                        # Changes the box colors to Yellow
                        currWordBox.checkYellows(wordAnswer)

                        # Moves on to next word
                        collection.setNextWord()
                        
                        # Sets the currentword
                        currWordBox = collection.currWord

                        # Checks if all tries are exhausted
                        if (currWordBox == None):
                            restart = True


                            if (not notShow):
                                lost = True
                                WordBoxSeven.drawCorrect(wordAnswer)
                                WordBoxSeven.draw(Screen)
                        

                
            # Turns background tan
            Screen.fill(Tan.h)
            WordBoxOne.draw(Screen)
            WordBoxTwo.draw(Screen)
            WordBoxThree.draw(Screen)
            WordBoxFour.draw(Screen)
            WordBoxFive.draw(Screen)
            WordBoxSix.draw(Screen)
            
            if lost:
                WordBoxSeven.draw(Screen)
            


        # Updates the screen
        pygame.display.flip()
        Clock.tick(30)
                
if __name__ == "__main__":
    main()
              