
import pygame
from pygame import display, image

pygame.init()

test_font = pygame.font.Font('font\Pixeltype.ttf', 50)
clock = pygame.time.Clock()
screen = display.set_mode((800, 400))
display.set_caption('Runner')


sky_surface = image.load('graphics/Sky.png').convert()
ground_surface = image.load('graphics/ground.png').convert()
text_surface = test_font.render('My Game', False, 'Black')
snail_surface = image.load('graphics\snail\snail1.png').convert_alpha()
player_surface = image.load('graphics\Player\player_stand.png').convert_alpha()

player_rect = player_surface.get_rect(midbottom = (80, 300))
snail_rect = snail_surface.get_rect(midbottom = (600, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEMOTION:
            mouse_pos = event.pos
            if player_rect.collidepoint(mouse_pos):
                print('ouch!')   
    
    #Move snail right
    snail_rect.x -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800;
    
    #render surfaces
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface, (300,50))
    screen.blit(snail_surface, snail_rect)
    screen.blit(player_surface,player_rect)
    
    #player collision
    # if player_rect.colliderect(snail_rect):
    #     print('Ouch!')
    
    display.update()
    clock.tick(60)