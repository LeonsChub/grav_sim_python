import pygame
import random
import math
from Planet import Planet, draw_planets

pygame.init()

width, height = 500,500

size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("2D Gravity Simulator")

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
CYAN = (0,255,255)
WHITE = (255,255,255)
BLACK = (0,0,0)

running = True

planets = []

planet_1 = Planet(100,(100,250),den=15)
planet_1.v = (0,0.25)
planet_2 = Planet(100,(400,250),den=15)
planet_2.v = (0,-0.25)


planets.append(planet_1)
planets.append(planet_2)

# earth = Planet(7,(100,300))
# earth.density = 2
# earth.v = (0,0.5)
# planets.append(earth)

# for i in range(2):
#     if i == 1:
#          p = Planet(15 , (750,750))
#          p.v = (0.5,-0.75)
#     elif i == 0:
#          p = Planet(30 , (1000,0))
#          p.v = (-0.25,1)
#     else:
#         p = Planet(random.randint(3,25) , (random.randint(500,1000),random.randint(500,1000)))
#     planets.append(p)


clock = pygame.time.Clock()

while running:

    m_pos = pygame.mouse.get_pos()
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
              running = False 
    
    screen.fill(BLACK)


    draw_planets(Planet,screen)

    for p in planets:
        #net_force_x , net_force_y = p.calc_net_force(screen)
        p.calc_next_pos(screen)
        p.trace(screen)
    

    pygame.display.flip() 
    clock.tick(60) # set n frames per second
    
    

pygame.quit()