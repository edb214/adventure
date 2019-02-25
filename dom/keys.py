##using keys

import pygame
pygame.init()
from basics import *
import time
import random

x=600
y=250
xsp=0
ysp=0
done = False
dom=pygame.image.load("dom.png")
screen=screen_on()
screen.blit(dom,(x,y))
pygame.display.flip()
while done!=True:
    key=pygame.key.get_pressed()
    screen.fill(white)
    screen.blit(dom,(x,y))
    pygame.display.flip()
    clock.tick(60)
    xsp=0
    ysp=0
    for event in pygame.event.get():
        if event.type==pygame.K_ESCAPE:
            done=True
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                xsp=-5
            elif event.key==pygame.K_RIGHT:
                xsp=5
            elif event.key==pygame.K_UP:
                ysp=-5
            elif event.key==pygame.K_DOWN:
                ysp=5
    if x>1180 or x<0:
        xsp*=-1
    if y>480 or y<0:
        ysp*=-1
    x+=xsp
    y+=ysp
pygame.quit()
