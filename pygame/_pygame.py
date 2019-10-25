import pygame
from pygame.locals import *
import sys
import os
import math
pygame.init()
screen = pygame.display.set_mode((800,600))
p_img = pygame.image.load("planet_1.png")
p_rect = p_img.get_rect().move(400,300)
screen.blit(p_img, p_rect)
pygame.display.update()

 
img = pygame.image.load("planet_1.png")
rect = img.get_rect().move(100,300)
screen.blit(img, rect)
pygame.display.update()
os.system("pause")
