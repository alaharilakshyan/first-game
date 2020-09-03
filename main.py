import pygame
import sys
import random

BLUE = (0,0,255)
RED = (255,0,0)

pygame.init()

# set screen info
WIDTH = 900
HEIGHT = 700
size = (WIDTH, HEIGHT)
SCREEN = pygame.display.set_mode(size)
pygame.display.update()

game_over = False

score = 0

RAINSIZE = 50
rain_list = []

SPEED = 5
AMOUNT = 10