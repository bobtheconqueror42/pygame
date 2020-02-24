import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 60

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


pygame.INIT()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("game")
clock = pygame.time.Clock()

running = True
while running:
    # keep loop running at right speed
    clock.tick(FPS)
    #procss input (events)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False


    #update

    #draw / render
    screen.fill(green)
    #after drawing everything
    pygame.display.flip()




pygame.quit()
