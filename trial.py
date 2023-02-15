import sys, pygame  #Importing sys and pygame module
pygame.init()       #Initializing pygame module

size = width, height = 640, 480 #Setting up the size of the new display window
speed = [1, 1]                  #Setting up the speed at which the image will move.
black = 0, 0, 0                 #Setting up 'black' variable as black color.

screen = pygame.display.set_mode(size)      #Displaying a new window
pygame.display.set_caption("Ball Bounce")

ball = pygame.image.load("intro_ball.gif")  #loading image into the new window
ballrect = ball.get_rect()       #Getting the rectangle which is large enough to
                                 # cover the image.

while True:

    # Iterating over pygame.event.get() allows us to close the
    # program if cross button was clicked. If this two line
    # is not written then the program will run indefinitely 
    # and the script will not detect it even if the cross was
    # pressed and will have to forcibly end the process.
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed) #Moving the image

    # Take reference position as left and top of the window.
    # The first if statement says:
    # if ballrect.left < 0 means that the left position of the rectangle created
    # is 0 or ballrect.right > width means that the right position of the 
    # rectangle created is greater than the width of the window. 

    """Actual Explanation:"""
    """
    -> Take left position of the new window as reference point(x-coordinate = 0) 
    and top position of the new window as reference point(y-coordinate = 0).
    -> Maximum width of the new window is rightmost position of the new window 
    and bottommost position of the new window.

    -> At first our image is at position (0, 0).
    -> When our image moves, it moves towads right and bottom.
    -> If our image reaches maximum width at right (ballrect.right > width)
    then the x-coordinate speed becomes negative as per the condtion given below
    which means out image starts going reverse. 
    -> It is same for (ballrect.bottom > width) 
    -> If our image reaches at x-coordinate 0 (ballrect.left < 0)i.e. 
    it touches the leftmost part of the window then, again the speed becomes 
    negative which means the image goes in the reverse order.
    -> It is same for (ballrect.top < 0)
    """
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    # It  fills the screen with black colour in every iteration.
    # What if we don't write this, see for yourself. (The image will leave its 
    # mark in each iteration and we cannot exactly see ball bouncing) 
    screen.fill(black)

    # blit() syntax:
    # blit(source, destination) or blit(image, position)
    # It is used to draw the image 'ball' at the position defined by 'ballrect'
    # at the screen(new window)
    screen.blit(ball, ballrect)

    # flip() flips the screen
    # The image of the ball we draw on the screen using the blit() function is
    # actually drawn on another screen(Let us assume). Or we can say it is drawn
    # at backend  :)  (Trying to sound cool using word 'backend')
    # Then the flip() funtion flips (swaps) the screen so that the position
    # of new image is displayed.

    # Think of it like a flipbook where you draw drawing and after fliping your
    # book the image your have drawn appers to move during the time you flip.

    # It is the same case here too. When you are drawing or (positioning) the
    # image at a new position using blit, you are drawing it in next page of 
    # your flipbook. So, you need to consecutively flip your book so that your
    # eyes are fooled and think it as animation.
    pygame.display.flip()