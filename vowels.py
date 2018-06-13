""" Short, one line description of the module ending with a period.
A longer description of the module with details that may help the user or anybody
reviewing the code later. make sure you outline in detail what the module does and how it can be used.
"""

__author__ = "Your Name"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "your.address@education.nsw.com.au"
__status__ = "Prototype, Development or Production"

#dependencies
import pygame as P # accesses pygame files
import sys  # to communicate with windows


# pygame setup - only runs once
P.init()  # starts the game engine
clock = P.time.Clock()  # creates clock to limit frames per second
loopRate = 60  # sets max speed of main loop
SCREENSIZE = SCREENWIDTH, SCREENHEIGHT = 1024, 768  # sets size of screen/window
DEFAULT_TEXT_SIZE = 48
screen = P.display.set_mode(SCREENSIZE)  # creates window and game screen
P.display.set_caption('Know your vowels!')
defaultFont = P.font.Font(None,80) #create a font for the letters, default font
selectedFont = P.font.Font(None,40) #a smaller font for after the letters have been selected

# set variables for some colours RGB (0-255)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (128, 0, 128)
lightBlue = (125, 125, 255)

#clear and fill the screen
screen.fill(purple)

#define necessary classes
class renderedLetter(object):
    """letters rendered for display on screen
    
    to be displayer in pygame text has to be 'rendered'
    to be selectable with a mouse also need to define a rectangle
    for each letter
    """
    def __init__(self, letter):
        """ inits the letter"""
        self.text = letter
        self.size = DEFAULT_TEXT_SIZE
        self.color = blue
        self.backColor = black
        self.x = 10
        self.y = 100
        #self.font = P.font.Font(None,self.size)
        self.font = P.font.SysFont("Lucida Console", self.size) #rendered best with monospace font
        self.renderedText = self.font.render(self.text,1,self.color,self.backColor)
        self.rectangle = self.renderedText.get_rect().move(self.x,self.y)
        
    def update(self):
        #self.font = P.font.Font(None,self.size)
        self.font = P.font.SysFont("Lucida Console", self.size) #rendered best with monospace font
        self.renderedText = self.font.render(self.text,1,self.color,self.backColor)
        self.rectangle = self.renderedText.get_rect().move(self.x,self.y)
        
#define other setup variables
alphabet = "abcdefghijklmnopqrstuvwxyz"
vowels = "aeiou"

#create arrays to display the rendered letters
alphabetArray = [] #an initially empty array
for letter in alphabet:
    rLetter = renderedLetter(letter)
    alphabetArray.append(rLetter)
    
vowelArray = [] #an initially empty array
for letter in vowels:
    rLetter = renderedLetter(letter)
    vowelArray.append(rLetter)

xPosition = 10
yPosition = 400
for l in alphabetArray:
    l.x = xPosition
    l.y = yPosition
    l.color = blue
    l.backColor = purple
    l.update()
    screen.blit(l.renderedText,l.rectangle)
    xPosition += (l.rectangle.width + 10)

xPosition = 320
yPosition = 200
for l in vowelArray:
    l.x = xPosition
    l.y = yPosition
    l.color = lightBlue
    l.backColor = lightBlue
    l.size = 2 * DEFAULT_TEXT_SIZE
    l.update()
    screen.blit(l.renderedText,l.rectangle)
    xPosition += (l.rectangle.width + 20)


play = True  # controls whether to keep playing

# game loop - runs 'loopRate' times a second!
while play:  # game loop - note:  everything in this loop is indented one tab

    for event in P.event.get():  # get user interaction events
        if event.type == P.QUIT:  # tests if window's X (close) has been clicked
            play = False  # causes exit of game loop
    # your code starts here ##############################
        if event.type == P.MOUSEBUTTONDOWN:
            mousePosition = P.mouse.get_pos()
            for a in alphabetArray:
                if a.rectangle.collidepoint(mousePosition):
                    a.color = red
                    #a.update()
                    for v in vowelArray:
                        if a.text == v.text:
                            a.color = green
                            v.backColor = purple
                            v.update()
                            screen.blit(v.renderedText, v.rectangle)
                    a.update()
                    screen.blit(a.renderedText, a.rectangle)
                



    # your code ends here ###############################
    P.display.flip()  # makes any changes visible on the screen
    clock.tick(loopRate)  # limits game to frame per second, FPS value

# out of game loop ###############
P.quit()   # stops the game engine
sys.exit()  # close operating system window
