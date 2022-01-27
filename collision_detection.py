# Pygame COllision Detection Practice, Julian Cunningham, January 27, 2022, 2:14pm, v0.2

import pygame, sys, random
from pygame.locals import *

# Setup PyGame
pygame.init()
mainClock = pygame.time.Clock() 

# Setup the PyGame Window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)   
pygame.display.set_caption('Collision Detection 2022')