import pygame 

pygame.init()
screen = pygame.display.set_mode((800,600), pygame.FULLSCREEN)
# screen size
pygame.display.set_caption("Valorant")
# title of the window
clock = pygame.time.Clock()
# game loop
FPS = 1000
# fps rate
game = True
# runs the game 
while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game = False
                # sets the 'game' variable to False
            elif event.key == pygame.K_SPACE:
                game = True
                # sets the 'game' variable to True
            elif event.key == pygame.K_UP:
                # handle up arrow key event
                pass
            elif event.key == pygame.K_DOWN:
                # handle down arrow key event
                pass
            elif event.key == pygame.K_LEFT:
                # handle left arrow key event
                pass
            elif event.key == pygame.K_RIGHT:
                # handle right arrow key event
                pass
    
    # update game state and render graphics
    # ...
    pygame.display.update()
    clock.tick(FPS)
    
pygame.quit()
# Made by your friendly neighborhood KlyntarX :)
# lol Idc if it uses ram I will fix it sooner or later
# try changing the fps rate variable to something smaller :)
# thanks