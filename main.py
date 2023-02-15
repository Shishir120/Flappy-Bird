import threading, time
import pygame, sys
pygame.init()

SCREENWIDTH = 350
SCREENHEIGHT = 450
PIPEHEIGHT = 500
offset = 80

size = SCREENWIDTH , SCREENHEIGHT
screen = pygame.display.set_mode(size) 
pygame.display.set_caption("Game")     

bg = pygame.image.load('Sprites/background.jpg').convert()
logo = pygame.image.load('Sprites/flappybirdlogo.png').convert_alpha()
name = pygame.image.load('Sprites/name.png').convert_alpha()
player = pygame.image.load('Sprites/flappybird.png').convert_alpha()
lowerpipe = pygame.image.load('Sprites/pipe.png').convert_alpha()
upperpipe = pygame.transform.rotate(lowerpipe, 180)


GAME_IMAGES = {}
GAME_SOUNDS = {}

def welcomesound():
    """Trial function to play the background sound using threads"""

    GAME_SOUNDS['background'] = pygame.mixer.music.load('Sounds/welcomesound.wav')
    pygame.mixer.music.play()


def welcomescreen():
    """Displays the image on the welcome screen"""

    screen.blit(GAME_IMAGES['bg'], (0, 0))
    screen.blit(GAME_IMAGES['logo'], (82, 50))
    screen.blit(GAME_IMAGES['player'], (150, 170))
    # screen.blit(GAME_IMAGES['upperpipe'], (0, 0))
    # screen.blit(GAME_IMAGES['lowerpipe'], (0, 450-200))
    screen.blit(GAME_IMAGES['name'], [-180, -50])
    pygame.display.flip()


# def getRandomPipes():


if __name__ == '__main__':

    #Images
    GAME_IMAGES['bg'] = pygame.transform.scale(bg, (SCREENWIDTH, SCREENHEIGHT)) 
    GAME_IMAGES['logo'] = pygame.transform.scale(logo, (200, 50)) 
    GAME_IMAGES['player'] = pygame.transform.scale(player, (50, 50)) 
    GAME_IMAGES['name'] = name
    # GAME_IMAGES['lowerpipe'] = pygame.transform.scale(lowerpipe, (50, 200)) 
    # GAME_IMAGES['upperpipe'] = pygame.transform.scale(upperpipe, (50, 200)) 

    

    #Sounds
    # bgsound = threading.Thread(target=welcomesound)
    # bgsound.start()
    welcomesound()

    while True:
        
        for event in pygame.event.get():

            # To quit the game
            if event.type == pygame.QUIT:
                print("User exited the game:") #Change it later
                pygame.quit()
                sys.exit()
                

        welcomescreen()
