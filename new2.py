"""Trial"""     """No Use now Adios"""


import pygame, sys, random, time

pygame.init()

size =  SCREENWIDTH, SCREENHEIGHT = 350, 450
PIPEHEIGHT = 500
offset = 80

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Trying Something")


background = pygame.image.load('Sprites/background.jpg')
pipe = pygame.image.load('Sprites/pipe.png')
background = pygame.transform.scale(background, (SCREENWIDTH, SCREENHEIGHT))


lowerpipe = pygame.transform.scale(pipe, (50, PIPEHEIGHT))
upperpipe = pygame.transform.rotate(lowerpipe, 180)




start_of_y1 = -(PIPEHEIGHT-50)
end_of_y1 = -(PIPEHEIGHT-300)

x1, x2 = 0, 0
i = 0

print(upperpipe.get_width())
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#     screen.blit(background, (0, 0))

#     while i < 2:

#         y1 = random.randrange(start_of_y1, end_of_y1)     #To randomly generate the position of upper pipe

#         leftover_upper = PIPEHEIGHT - (abs(y1))    #Position of upperpipe left after y = 0 or (top)

#         y2 = leftover_upper + offset                    #For position of lowerpipe
    
#         screen.blit(upperpipe, (x1, y1))
#         screen.blit(lowerpipe, (x2, y2))
#         pygame.display.flip()
#         x1, x2 = x1 + 150, x2 + 150

#         i += 1