import pygame
import numpy as np
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0,255,0)

from env import Environment
 
class Wall(pygame.sprite.Sprite):
 
    def __init__(self, x, y, width, height, color):
 
        super().__init__()
 
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
 
 
class Room(object):
 
    wall_list = None
    enemy_sprites = None
 
    def __init__(self):
        self.wall_list = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
 
 
class Room1(Room):
    def __init__(self,gelecekMatris,kısaYol):
        super().__init__()
        x = 15 
        walls = []
        x,y = (20,20)
        for i in range(x):
            for j in range(y):
                if gelecekMatris[i,j] == -100:
                    eklenecek = [j*x,i*x,x,x,BLUE]
                    walls.append(eklenecek)
                elif gelecekMatris[i,j] == 100 or gelecekMatris[i][j] == -1:
                    eklenecek = [j*x,i*x,x,x,GREEN]
                    walls.append(eklenecek)
                

        for i,j in kısaYol:
            eklenecek = [j*x,i*x,x,x,WHITE]
            walls.append(eklenecek)
 
        
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
        
 
 
 
def drw(gönderilicekMatris,kısaYol):

    pygame.init()
 
    
    screen = pygame.display.set_mode([500, 500])
 
    room = Room1(gönderilicekMatris,kısaYol)
 
    done = False
 
    while not done:
      
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
 
 
       
 
        # --- Drawing ---
        screen.fill(BLACK)
 
        room.wall_list.draw(screen)
 
        pygame.display.flip()
 
    pygame.quit()

