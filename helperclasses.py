import pygame



class Color:
    def __init__(self, rgb, h):
        self.rgb = rgb
        self.h = h


Tan = Color((237, 242, 235),"#edf2eb")
Red = Color((255, 0, 0), "#ff0000")
Black = Color((0, 0, 0), "#00000")
Sirocco = Color((123, 125, 125), "#7b7d7d")
White = Color((255, 255, 255), "#fffff")
Yellow = Color((201, 180, 88), "#c9b458")
Green = Color((106, 170, 100), "#6aaa64")

class LetterBox:
    def __init__(self, width, height, posx, posy):
        
        # Location and Size
        self.x = posx
        self.y = posy
        self.w = width
        self.h = height
        
        # Default letter value
        self.letter = "0"
        
        # Color state
        self.green = False
        self.yellow = False
        
        # Rectangles
        self.box = pygame.Rect((self.x, self.y), (self.w, self.h))
        self.innerbox = pygame.Rect((posx, posy), (width - 4, height - 4))
        self.innerbox.center = self.box.center 
        
        # Colors
        self.boxcol = Sirocco
        self.innerboxcol = Tan
        
        # Font
        self.font = pygame.font.Font("font.ttf", 80)
        self.text_surface = self.font.render(self.letter, False, White.rgb).convert_alpha()
        
        # Links
        self.next = None
        self.prev = None
        
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.boxcol.rgb, self.box)
        
        # Draws innerbox
        if (self.letter == "0"):
            pygame.draw.rect(screen, self.innerboxcol.rgb, self.innerbox)

        # Draws text
        else:
            self.text_surface = self.font.render(self.letter, False , White.rgb).convert_alpha()
            screen.blit(self.text_surface, (self.x + 18, self.y - 20))
            
        
        
    # Removing text
    def removeText(self, screen):
        self.letter = "0"
        
    # Placing text
    def placeText(self, event, screen):
        self.letter = event.unicode.upper()
        
    def changeToYellow(self):
        self.boxcol = Yellow
        self.yellow = True
    
    def changeToGreen(self):
        self.boxcol = Green
        self.green = True
        
    
    
        
        
        
class WordBox:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail
        
        self.next = None
        self.prev = None

        
    def draw(self, screen):
        x = self.head
        while (x != None):
            x.draw(screen)
            x = x.next

            
    def getWord(self):
        word = ""
        x = self.head
        while (x != None):
            word += x.letter
            x = x.next
            
        return word
            
    def checkFilled(self, screen):
        x = self.head 
        for i in range (0, 5):
            if (x.letter == "0"):
                return False
        
            x = x.next
            
        return True
            
            
    
    def checkGreens(self, wordAnswer):
        wordGuess = self.getWord()
        x = self.head
        i = 0
        while (x != None):
            
            # Checks if it is in the word AND same position
            if ((x.letter in wordAnswer) and (wordGuess[i] == wordAnswer[i])):
                x.changeToGreen()
                
                
            i += 1
            x = x.next
            
            
    def checkYellows(self, wordAnswer):
        x = self.head
        
        guessedLetters = []
        while (x != None):
            if (x.green == True):
                guessedLetters.append(x.letter)
                
            x = x.next
        
        neededLetters = list(wordAnswer)
        
        finList = []
        for i in range(0, len(neededLetters)):
            
            if (neededLetters[i] in guessedLetters):
                guessedLetters.remove(neededLetters[i])
                continue
            
            finList.append(neededLetters[i])
 
            
        
            
        x = self.head
        while (x != None):
            
            if (x.letter in wordAnswer) and (x.green == False) and (x.letter in finList):
                x.changeToYellow()
                finList.remove(x.letter)
                
                
            x = x.next
                
                
                
                
    def checkCorrect(self):
        x = self.head
        
        while (x != None):
            if (x.boxcol != Green):
                return False
            
            x = x.next
            
        return True
    
    def drawCorrect(self, wordAnswer):
        
        x = self.head
        i = 0
        while (x != None):
            x.letter = wordAnswer[i]
            x.changeToGreen()
            
            x = x.next
            i += 1
        

            
    
            
    # Typing a letter
    def removeInnerBox(self, event, screen):
        x = self.head
        while (x.letter != "0"):
            x = x.next
            if (x == None):
                return
            
        x.placeText(event, screen)
        
        
        
    # Backspacing letters
    def placeInnerBox(self, event, screen):
        x = self.tail
        while (x.letter == "0"):
            x = x.prev
            if (x == None):
                return
            
        x.removeText(screen)
        
        
        
            

class WordCollection:
    
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail
        
        self.currWord = None
        
    def setCurrentWord(self, word):
        self.currWord = word
        
    def setNextWord(self):
        self.currWord = self.currWord.next
        
            

    
            
            
            
            
            
            
            
            
            
            
            
            
