import pygame
from sys import exit
pygame.init()
screen=pygame.display.set_mode((800,400))
pygame.display.set_caption("runner")
clock=pygame.time.Clock()
test_surface=pygame.Surface((100,200))
sky_surface=pygame.image.load('sky.webp').convert_alpha()
ground_surface=pygame.image.load('ground.webp').convert_alpha()
test_font=pygame.font.Font(None,50)
text_surface=test_font.render('my game',False,'Green')

snail_surface=pygame.image.load('snail.jpg').convert_alpha()
snail_rect=snail_surface.get_rect(bottomright =(600,300))
player_surface=pygame.image.load('charecter.webp').convert_alpha()
player_rectangle=player_surface.get_rect(topleft=(80,300))
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type==pygame.MOUSEMOTION:
        #      if player_rectangle.collidepoint(event.pos):print('collesion')  
        if event.type==pygame.KEYDOWN:
             if event.key==pygame.K_SPACE:
                 print('jump')
             if event.type==pygame.KEYUP:
                print('keyup')
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,350))
    screen.blit(text_surface,(300,50))
    screen.blit(player_surface,(80,300))
    snail_rect.x-=4
    if snail_rect.right <=0: snail_rect.left=800
    screen.blit(snail_surface,snail_rect)
    
    
    # if player_rectangle.colliderect(snail_rect):
    #     print('collision')
    mouse_pos=pygame.mouse.get_pos()
    # if player_rectangle.collidepoint(mouse_pos):
    #     print(pygame.mouse.get_)
    #draw all
    #update everything
    pygame.display.update()
    clock.tick(60)