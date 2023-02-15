"""Trial"""


import pygame, sys, random, threading

pygame.init()

SIZE =  SCREENWIDTH, SCREENHEIGHT = 350, 450
PIPEHEIGHT = 500
PLAYERX = 130
PLAYERY = 170
FPS = 30
offset = 120    #Gap between two pipes

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Trying Something")

clock = pygame.time.Clock()

def welcomeScreen():
    """ Welcome screen to display"""

    PLAYERY = 170
    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) :
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_UP):
                return  #Left to complete the main game.

            else:
                screen.blit(background, (0, 0))
                screen.blit(logo, (82, 50))
                screen.blit(name, (-180, -50))
                screen.blit(player, (PLAYERX, PLAYERY))
            
                pygame.display.update()
                clock.tick(FPS)


#Arranging upper and lower pipes
pipe = pygame.image.load('Sprites/pipe.png').convert_alpha()
image_lowerpipe = pygame.transform.scale(pipe, (50, PIPEHEIGHT))
image_upperpipe = pygame.transform.rotate(image_lowerpipe, 180)
 

x1 = 280    #Initial position of first upperpipe
x2 = 280    #Initial position of first lowerpipe


def getRandomPipes():
    """Generates random pipes"""

    global x1, x2, leftover_upper

    start_of_y1 = -(PIPEHEIGHT - 50)   
    end_of_y1 = -(PIPEHEIGHT - 300)     
    y1 = random.randrange(start_of_y1, end_of_y1)     #To randomly generate the position of upper pipe

    leftover_upper = PIPEHEIGHT - (abs(y1))    #Position of upperpipe left after y = 0 or (top)

    y2 = leftover_upper + offset               #For position of lowerpipe

    pipes = [{'x' : x1, 'y' : y1},      #Upper Pipes
    {'x' : x2, 'y' : y2}]               #Lower Pipes

    x1 = x1 + 210       #Updating position of upperpipe
    x2 = x2 + 210       #Updating position of lowerpipe

    return pipes


# .................... Work in progress ......................
# Error crash() function
def crash(upperpipes, lowerpipes):
    """Determines whether the bird crashed with the pipes or not"""

    #Error here
    for upperpipe in upperpipes:
        if PLAYERY + 10 <= leftover_upper and abs(PLAYERX - upperpipe['x']) < image_upperpipe.get_width():
            print(leftover_upper, PLAYERY)
            return True
    

    if PLAYERY <= 0 or PLAYERY >= SCREENHEIGHT - player.get_height():
        return True
    pass



def mainGame():
    """The main game begins"""

    global PLAYERY, x1, x2

    x1 = 280    #Initial position of first upperpipe
    x2 = 280    #Initial position of first lowerpipe

    PLAYERX = 130
    PLAYERY = 170    #It is the player's initial position
    velPipe = -1
    velPlayerY = -18
    velPlayerYDown = 1
    playerFlapped = True
    
    newpipe1 = getRandomPipes()
    newpipe2 = getRandomPipes()
    print(newpipe1)
    print(newpipe2)

    upperpipes = [
        {'x' : newpipe1[0]['x'], 'y' : newpipe1[0]['y']},
        {'x' : newpipe2[0]['x'], 'y' : newpipe2[0]['y']}   
        ]

    lowerpipes = [
        {'x' : newpipe1[1]['x'], 'y' : newpipe1[1]['y']},
        {'x' : newpipe2[1]['x'], 'y' : newpipe2[1]['y']}
        ]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and (event.key == pygame.K_UP or event.key == pygame.K_SPACE):

                playerFlapped = True

        if upperpipes[0]['x'] <= -image_upperpipe.get_width():
                upperpipes.pop(0)
                lowerpipes.pop(0)


        # Generating new pipes
        # Add new pipes to the list to blit
        if upperpipes[0]['x'] <= 300 and lowerpipes[0]['x'] <= 300:
            newPipeGeneration = getRandomPipes()

            upperpipes.append({'x' : newPipeGeneration[0]['x'], 'y' : newPipeGeneration[0]['y']})

            lowerpipes.append({'x' : newPipeGeneration[1]['x'], 'y' : newPipeGeneration[1]['y']})


        # Reversing the position of upperpipes and lowerpies
        for upperpipe, lowerpipe in zip(upperpipes, lowerpipes):
            upperpipe['x'] = upperpipe['x'] + velPipe
            lowerpipe['x'] = lowerpipe['x'] + velPipe
        
        
        # Blitting the sprites
        screen.blit(background, (0, 0))

        # Not complete correctly blited

        # Error
        if playerFlapped == True:
            PLAYERY = PLAYERY + velPlayerY
            playerFlapped = False

        # Error
        if playerFlapped == False:
            PLAYERY = PLAYERY + velPlayerYDown                          

        for upperpipe, lowerpipe in zip(upperpipes, lowerpipes):
            screen.blit(image_upperpipe, (upperpipe['x'], upperpipe['y']))
            screen.blit(image_lowerpipe, (lowerpipe['x'], lowerpipe['y']))
                    
        screen.blit(player, (PLAYERX, PLAYERY))  #Player blit

        pygame.display.flip()


        #Error
        if crash(upperpipes, lowerpipes) == True:
            print("Game Over")
            break

        #Error. Take a closer look into the FPS and manage the velocity
        # FPS may be okay but change the velocity.
        clock.tick(FPS)



if __name__ == '__main__':

    background = pygame.image.load('Sprites/background.jpg')
    background = pygame.transform.scale(background, (SCREENWIDTH, SCREENHEIGHT))
    player = pygame.image.load('Sprites/flappybird.png').convert_alpha()
    player = pygame.transform.scale(player, (50, 50))
    logo = pygame.image.load('Sprites/flappybirdlogo.png').convert_alpha()
    logo = pygame.transform.scale(logo, (200, 50)) 
    name = pygame.image.load('Sprites/name.png').convert_alpha()


    while True:

        welcomeScreen()
        mainGame()


    # PIPEHEIGHT - upperpipe.get_height() - abs(y1)