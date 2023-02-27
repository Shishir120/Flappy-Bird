"""Trial"""

# To Do: Declare the score of the user after the game is over

# After major game completes make "press space or up key to continue" sign and blit and unblit it 
# simultaneously to make it look good 

import pygame, sys, random, time, threading

pygame.init()

SIZE =  SCREENWIDTH, SCREENHEIGHT = 350, 450
PIPEHEIGHT = 500
PLAYERX = 100
PLAYERY = 170
FPS = 60
offset = 120    #Gap between two pipes

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Trying Something")

clock = pygame.time.Clock()


def welcomeScreen():
    """ Welcome screen to display"""

    pygame.mixer.music.load('Sounds/welcomesound.wav')
    pygame.mixer.music.set_volume(0.8)
    pygame.mixer.music.play()   

    PLAYERY = 170
    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) :
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE):
                pygame.mixer.music.stop()
                return

            else:
                screen.blit(background, (0, 0))
                screen.blit(logo, (82, 50))
                screen.blit(name, (50, -45))
                screen.blit(player, (PLAYERX, PLAYERY))
            
                screen.blit(spaceToContinue, (50, 210))
                pygame.display.update()
                clock.tick(FPS)


#Arranging upper and lower pipes
pipe = pygame.image.load('Sprites/pipe.png').convert_alpha()
image_lowerpipe = pygame.transform.scale(pipe, (50, PIPEHEIGHT))
image_upperpipe = pygame.transform.rotate(image_lowerpipe, 180)


# x1 = 280    #Initial position of first upperpipe
# x2 = 280    #Initial position of first lowerpipe


leftover_upper_list  = []

def getRandomPipes(latestUpperpipe):
    """Generates random pipes"""
    # latestUpperpipe argument is passed into the function to maintain the x-coordinate
    # distance of the pipes. So that they don't exceed certain value i.e 520

    global x1, x2, leftover_upper, leftover_upper_list

    start_of_y1 = -(PIPEHEIGHT - 50)   
    end_of_y1 = -(PIPEHEIGHT - 220)     
    y1 = random.randrange(start_of_y1, end_of_y1)     #To randomly generate the position of upper pipe

    leftover_upper = PIPEHEIGHT - (abs(y1))    #Position of upperpipe left after y = 0 or (top)

    y2 = leftover_upper + offset               #For position of lowerpipe

    x1 = latestUpperpipe + 210       #Updating position of upperpipe
    x2 = latestUpperpipe + 210       #Updating position of lowerpipe

    pipes = [{'x' : x1, 'y' : y1},      #Upper Pipes
    {'x' : x2, 'y' : y2}]               #Lower Pipes


    # print(x1)
    return pipes


playCrashSound = False
def crash(PLAYERY):
    """Determines whether the bird crashed with the pipes or not"""
    global upperpipes, lowerpipes, leftover_upper_list, playCrashSound

    # For crash test of upperpipes
    if len(leftover_upper_list) > 0 and PLAYERY <= leftover_upper_list[0] and abs(PLAYERX - upperpipes[0]['x']) <= image_upperpipe.get_width():
        playCrashSound = True

    # For crash test of lowerpipe
    if PLAYERY + player.get_height() >= lowerpipes[0]['y']  and abs(PLAYERX - lowerpipes[0]['x']) <= image_lowerpipe.get_width():
        playCrashSound = True

    if PLAYERY <= 0 or PLAYERY >= SCREENHEIGHT - player.get_height():
        playCrashSound = True
    
    if playCrashSound == True:
        pygame.mixer.music.load('Sounds/game over.wav')
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play()
        playCrashSound = False
        for upperpipe, lowerpipe in zip(upperpipes, lowerpipes):
            screen.blit(image_upperpipe, (upperpipe['x'], upperpipe['y']))
            screen.blit(image_lowerpipe, (lowerpipe['x'], lowerpipe['y']))

        screen.blit(player, (PLAYERX, PLAYERY))
        pygame.display.update()
        time.sleep(0.7)               # Gives time to the program so that music can be played

        # screen.blit(gameover, (50, 50))

        screen.blit(background, (0, 0))
        screen.blit(gameover, (50, 50))
        pygame.display.update()
        return True


playScoreSound = False           # Condition need to be satisfied to play point scoring sound
def score():
    """Counts the score upto 99"""

    global i, doubleDigit, numberBlit, number_X, j, playScoreSound

    if PLAYERX + 25 == upperpipes[0]['x'] + image_upperpipe.get_width()/2:  # image width is 50
        numberBlit = True
        i += 1
        playScoreSound = True

    if i == 9:
        doubleDigit = True
        i = -1
        j += 1

    if doubleDigit == True:
        screen.blit(numberss[j], (SCREENWIDTH / 2.3, 0))
        number_X = SCREENWIDTH / 2.05

    if numberBlit == True:
        screen.blit(numberss[i], (number_X, 0))

    if playScoreSound == True:
            pygame.mixer.music.load('Sounds/score.wav')
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.play()
            playScoreSound = False
        


def mainGame():
    """The main game begins"""

    global PLAYERY, x1, x2, upperpipes, lowerpipes, leftover_upper_list, i, j, doubleDigit, numberBlit, number_X


    # x1 = 280    #Initial position of first upperpipe
    # x2 = 280    #Initial position of first lowerpipe

    PLAYERX = 100
    PLAYERY = 170    #It is the player's initial position
    velPipe = -2
    velPlayerY = -40
    velPlayerYDown = 1.5
    playerFlapped = True
    
    newpipe1 = getRandomPipes(70)      # First set of pipes, arg = 70 to make x1 as 280

    #Working with leftoverUpper List
    leftover_upper_list.append(leftover_upper)

    newpipe2 = getRandomPipes(280)      #Second set of pipes

    leftover_upper_list.append(leftover_upper)

    upperpipes = [
        {'x' : newpipe1[0]['x'], 'y' : newpipe1[0]['y']},
        {'x' : newpipe2[1]['x'], 'y' : newpipe2[0]['y']}   
        ]

    lowerpipes = [
        {'x' : newpipe1[1]['x'], 'y' : newpipe1[1]['y']},
        {'x' : newpipe2[1]['x'], 'y' : newpipe2[1]['y']}
        ]

    i, j = -1, -1                            # This is for blitting scores
    number_X = SCREENWIDTH / 2.3             # This is for blitting score
    numberBlit, doubleDigit = False, False   # This is for blitting score

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and (event.key == pygame.K_UP or event.key == pygame.K_SPACE):

                playerFlapped = True

        if upperpipes[0]['x'] <= -10:  # previous: -image_upperpipe.get_width()
                upperpipes.pop(0)
                lowerpipes.pop(0)


        if upperpipes[0]['x'] + image_upperpipe.get_width() == PLAYERX:

            leftover_upper_list.pop(0)

        if upperpipes[0]['x'] == 150 and lowerpipes[0]['x'] == 150 :

            newPipeGeneration = getRandomPipes(upperpipes[1]['x'])

            leftover_upper_list.append(leftover_upper)

            # print(leftover_upper_list[0])

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
                    
        score()         # Counting score
    
        #Error
        if crash(PLAYERY) == True:
            print("Game Over")
            pygame.mixer.music.load('Sounds/game over.wav')
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.play()
            leftover_upper_list = []
            upperpipes = []
            lowerpipes = []
            break


        # print(upperpipes_copy[0]['x'])
        # print(upperpipes[0]['x'])

        screen.blit(player, (PLAYERX, PLAYERY))  #Player blit
        pygame.display.update()

        # Error. Take a closer look into the FPS and manage the velocity
        # FPS may be okay but change the velocity.
        clock.tick(FPS)



if __name__ == '__main__':

    background = pygame.image.load('Sprites/background.jpg')
    background = pygame.transform.scale(background, (SCREENWIDTH, SCREENHEIGHT))
    player = pygame.image.load('Sprites/flappybird.png').convert_alpha()
    player = pygame.transform.scale(player, (50, 40))
    logo = pygame.image.load('Sprites/flappybirdlogo.png').convert_alpha()
    logo = pygame.transform.scale(logo, (200, 50)) 
    name = pygame.image.load('Sprites/name.png').convert_alpha()
    name = pygame.transform.scale(name, (270, 350))
    gameover = pygame.image.load('Sprites/game over.png').convert_alpha()
    gameover = pygame.transform.scale(gameover, (270, 350))

    spaceToContinue = pygame.image.load('Sprites/space to continue.png').convert_alpha()
    spaceToContinue = pygame.transform.scale(spaceToContinue, (270, 250))

    numbers = [
    pygame.image.load('Sprites/numbers/1 number.png').convert_alpha(),
    pygame.image.load('Sprites/numbers/2 number.png').convert_alpha(),
    pygame.image.load('Sprites/numbers/3 number.png').convert_alpha(),
    pygame.image.load('Sprites/numbers/4 number.png').convert_alpha(),
    pygame.image.load('Sprites/numbers/5 number.png').convert_alpha(),
    pygame.image.load('Sprites/numbers/6 number.png').convert_alpha(),
    pygame.image.load('Sprites/numbers/7 number.png').convert_alpha(),
    pygame.image.load('Sprites/numbers/8 number.png').convert_alpha(),
    pygame.image.load('Sprites/numbers/9 number.png').convert_alpha(),
    pygame.image.load('Sprites/numbers/0 number.png').convert_alpha(),
    ]

    numberss = [
    pygame.transform.scale(numbers[0], (40, 40)),
    pygame.transform.scale(numbers[1], (40, 40)),
    pygame.transform.scale(numbers[2], (40, 40)),
    pygame.transform.scale(numbers[3], (40, 40)),
    pygame.transform.scale(numbers[4], (40, 40)),
    pygame.transform.scale(numbers[5], (40, 40)),
    pygame.transform.scale(numbers[6], (40, 40)),
    pygame.transform.scale(numbers[7], (40, 40)),
    pygame.transform.scale(numbers[8], (40, 40)),
    pygame.transform.scale(numbers[9], (40, 40))
    ]


    # Sounds
    pygame.mixer.init()

    while True:

        welcomeScreen()
        mainGame()


    # PIPEHEIGHT - upperpipe.get_height() - abs(y1)