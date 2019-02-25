##basics
import pygame
pygame.init()

def screen_on():
    screen=pygame.display.set_mode((1200,500))
    return screen

white=(255,255,255)
black=(0,0,0)
blue=(0,0,255)

clock=pygame.time.Clock()
