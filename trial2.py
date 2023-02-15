"""Event Handling in Python"""

import pygame

size = width, height = 600, 400 
new_window = pygame.display.set_mode(size)
pygame.display.set_caption("Event Handling")
running = True

while running:

    for event in pygame.event.get():

        #For exiting the new window
        if event.type == pygame.QUIT:
            print("User exit the new window")
            running = False
        

        #When Pressing Keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print('Player moves forward')
            
            elif event.key == pygame.K_s:
                print("Player moves backward")

            elif event.key == pygame.K_a:
                print("Player moves left")
            
            elif event.key == pygame.K_d:
                print("Player moves right")
            
            elif event.key == pygame.K_UP:
                print('Player moves forward')

        # When releases the Keys
        if event.type == pygame.KEYUP:
            
            if event.key == pygame.K_w:
                print("Player released 'w' key")
                                
            if event.key == pygame.K_s:
                print("Player released 's' key")


        #Mouse Events

        #On clicking mouse buttons
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("User pressed left mouse button")    

            if event.button == 4:
                print("User scrolled up")    

        #On releasing mouse buttons
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                print("User released 'left' mouse button")    

            if event.button == 4:
                print("User is now not going up") 
            

        #Mouse motion events
        if event.type == pygame.MOUSEMOTION:

            # For x-coordinate  rel = (x, y)
            if event.rel[0] > 0:
                print("User going towards right")
                
            elif event.rel[0] < width:
                print("user going left")       

            # For y-coordinate  rel = (x, y)
            elif event.rel[1] > 0:
                print("User going down")

            elif event.rel[1] < height:
                print("User going up")