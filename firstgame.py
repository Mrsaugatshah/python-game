import pygame
from sys import exit
pygame.init()
screen=pygame.display.set_mode((800,400))
pygame.display.set_caption("runner")
clock=pygame.time.Clock()
test_surface=pygame.Surface((100,200))
sky_surface=pygame.image.load('sky.webp')
ground_surface=pygame.image.load('ground.webp')
test_font=pygame.font.Font(None,50)
text_surface=test_font.render('my game',False,'Green')
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,350))
    screen.blit(text_surface,(300,50))
    
    #draw all
    #update everything
    pygame.display.update()
    clock.tick(60)