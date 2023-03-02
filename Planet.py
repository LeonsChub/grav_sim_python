import math
import pygame
import random

class Planet:

        
        planets = []
        GRAV_CONSTANT = 30
        d_t = 1/60
        
        def __init__(self,mass,pos,no_draw = False, den = 3):
            
            self.prev_positions = []
            self.dont_draw = no_draw

            self.mass = mass 
            self.position = pos 
            self.color = color = ((random.randint(0,200)),(random.randint(0,200)),(random.randint(0,200)))

            self.density = den # higher the value smaller the planet

            self.a = (0,0) #acceleration (x axis,y axis)
            self.v = (0,0) #velocity            ||

            self.planets.append(self)
            
        def to_draw(self):
            return self.dont_draw
            
        def get_pos(self):
            return self.position

        def set_pos(self,new_pos):
            i = self.planets.index(self)
            self.position = new_pos
            self.planets[i].position = new_pos

        def calc_next_pos(self,screen):
           # curr_a = self.a
            curr_v = self.v
            ax, ay = self.calc_net_force(screen)
            ax = ax/self.mass
            ay = ay/self.mass
            
            curr_v = self.v
            curr_v = (curr_v[0] + ax * self.d_t ,curr_v[1] + ay * self.d_t)

            self.v = curr_v

            if screen != None:
                pos = self.get_pos()
                pygame.draw.line(screen,(255,255,255),pos,(pos[0]+self.v[0],pos[1]+self.v[1]))

            self.position = (self.position[0] + self.v[0] , self.position[1] + self.v[1])

            if len(self.prev_positions) <= 100:
                self.prev_positions.append(self.position)
            else:
                self.prev_positions.pop(0)
                self.prev_positions.append(self.position)

        def get_mass(self):
            return self.mass
        
        def calc_dist_vector(self, pos):
            my_pos,p_pos = (self.get_pos(),pos)
            #my_pos,p_pos = (self.pos,planet.get_pos())

            dx = p_pos[0] - my_pos[0] 
            dy = p_pos[1] - my_pos[1] 

            dist_vector = (dx,dy)

            return  dist_vector
        
        def calc_force(self,planet):
            a,b = self.calc_dist_vector(planet.get_pos())
            r = a**2 + b**2
            r = math.sqrt(r)
            m1 =   self.get_mass()
            m2 = planet.get_mass()

            if r == 0:
                r = 0.1
            
            f = (self.GRAV_CONSTANT * m1 * m2)/(r**2)
                
            
            return f

        def calc_net_force(self,screen = None):
            net_f_x = 0
            net_f_y = 0
            for p in self.planets:
                if p != self:
                    f = self.calc_force(p)
                    v = self.calc_dist_vector(p.get_pos())

                    theta = math.atan2(v[1],v[0])

                    fx ,fy = (math.cos(theta) * f ,math.sin(theta) * f)

                    net_f_x += fx
                    net_f_y += fy
            
            if screen != None:
                pos = self.get_pos()
                pygame.draw.line(screen,(255,255,255),pos,(pos[0]+net_f_x,pos[1]+net_f_y))

            return((net_f_x,net_f_y))

        def trace(self,screen):
            for pos in self.prev_positions:
                pygame.draw.circle(screen, (0,255,255),pos, 1)
    





def draw_planets(self,screen):
    for p in self.planets:
        i = self.planets.index(p)
        if not p.to_draw():
            pygame.draw.circle(screen, self.planets[i].color,self.planets[i].position, self.planets[i].mass/self.planets[i].density)
