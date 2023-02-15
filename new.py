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


leftover_upper_list  = []

def getRandomPipes():
    """Generates random pipes"""
    global x1, x2, leftover_upper, leftover_upper_list

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
def crash(upperpipe, lowerpipe, PLAYERY):
    """Determines whether the bird crashed with the pipes or not"""
    global upperpipes
    # Error here 
    # Error Assumption: It may be because we are running a for loop and everytime
    # the bird passes through the pipe sometimes it shows game over sometimes not.
    # Maybe because the value of next pipe which may not be similar to the previous
    # pipe is used and the condition holds incorrect. Also value of PLAYERY and 
    # leftover_upper is not as expected.


    # Error here.............................Main Problem
    
    # Find the algorithm for player touching the upperpipes and then for
    # lowerpipes

    if PLAYERY <= leftover_upper_list[0] and abs(PLAYERX - upperpipes[0]['x']) < image_upperpipe.get_width():
        print(leftover_upper_list[0], PLAYERY, image_upperpipe.get_height())
        return True


    if PLAYERY <= 0 or PLAYERY >= SCREENHEIGHT - player.get_height():
        return True
    pass



def mainGame():
    """The main game begins"""

    global PLAYERY, x1, x2, upperpipes


    x1 = 280    #Initial position of first upperpipe
    x2 = 280    #Initial position of first lowerpipe

    PLAYERX = 130
    PLAYERY = 170    #It is the player's initial position
    velPipe = -1
    velPlayerY = -18
    velPlayerYDown = 1
    playerFlapped = True
    
    newpipe1 = getRandomPipes()

    #Working with leftoverUpper List
    leftover_upper_list.append(leftover_upper)

    newpipe2 = getRandomPipes()

    leftover_upper_list.append(leftover_upper)
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

    # Trial copy of pipes 
    upperpipes_copy = upperpipes.copy()
    lowerpipes_copy = lowerpipes.copy()

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

        if upperpipes[0]['x'] + image_upperpipe.get_width() < PLAYERX:
            upperpipes_copy.pop(0)
            lowerpipes_copy.pop(0)

            #Working with the list of leftover_upper
            leftover_upper_list.pop(0)

            leftover_upper_list.append(leftover_upper)

            """To do work"""
            # Check whether the data in the leftover_upper_list repeats or not by 
            # checking the code line 160-164 and code line 174- 177. If new pipe 
            # is not generated then leftover_upper will be reapeated in the
            # leftover_upper_list[0]


        # Generating new pipes
        # Add new pipes to the list to blit
        if upperpipes[0]['x'] <= 300 and lowerpipes[0]['x'] <= 300:
            newPipeGeneration = getRandomPipes()

            upperpipes.append({'x' : newPipeGeneration[0]['x'], 'y' : newPipeGeneration[0]['y']})

            lowerpipes.append({'x' : newPipeGeneration[1]['x'], 'y' : newPipeGeneration[1]['y']})

            # Working in the copy of the pipes
            upperpipes_copy.append({'x' : newPipeGeneration[0]['x'], 'y' : newPipeGeneration[0]['y']})

            lowerpipes_copy.append({'x' : newPipeGeneration[1]['x'], 'y' : newPipeGeneration[1]['y']})



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
                    



        #Error
        if crash(upperpipes_copy[0]['x'], lowerpipes_copy[0]['x'], PLAYERY) == True:
            print("Game Over")
            # break

        screen.blit(player, (PLAYERX, PLAYERY))  #Player blit
        pygame.display.update()

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