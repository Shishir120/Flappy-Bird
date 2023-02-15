"""Learning about get_rect() function"""

import pygame, sys
pygame.init()

PIPEHEIGHT = 250

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Shishir को गेम")

#Player
player = pygame.image.load("Sprites/flappybird.png").convert_alpha()
player = pygame.transform.scale(player, (50, 50))

#Pipes
pipe = pygame.image.load('Sprites/pipe.png').convert_alpha()
image_lowerpipe = pygame.transform.scale(pipe, (50, PIPEHEIGHT))
image_upperpipe = pygame.transform.rotate(image_lowerpipe, 180)



while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Blitting Sprites
    screen.blit(player, (250, 250))

    screen.blit(image_upperpipe, (250, -100))
    pygame.display.flip()

    # Rectangular position of player and pipe
    rectPlayer = player.get_rect()
    rectUpperPipe = image_upperpipe.get_rect()
    