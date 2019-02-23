# Test project

# import the pygame module, so you can use it
import pygame

xpos = 0
ypos = 0
step_x = 1
step_y = 1

pygame.init()

screen = pygame.display.set_mode((1000,750))
image = pygame.image.load("alex.jpg")  
screen.fill((100,8,60)) 
pygame.display.flip()

logo = pygame.image.load("ham.jpg")
pygame.display.set_icon(logo)
pygame.display.set_caption("This is a screen")
    
for i in range(400):
    xpos += step_x # move it to the right
    ypos += step_y # move it down    
    screen.fill((100,8,60))
    screen.blit(image, (xpos, ypos))
    pygame.display.flip()
while True:
    pygame.display.flip()