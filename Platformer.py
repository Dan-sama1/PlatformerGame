import pygame
import sys
from scripts.entities import PhysicsEntity
from scripts.utils import load_image
class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("NINJA GAME")
        self.screen = pygame.display.set_mode((640, 480))

        #MAKE THE GAME RUN AT 60 FPS
        self.clock = pygame.time.Clock()
        
        '''self.img = pygame.image.load('data/images/clouds/cloud_1.png')
        #REMOVE A CERTAIN COLOR IN A YOUR PHOTO
        self.img.set_colorkey((0,0,0)) #0,0,0 IS BLACK WHICH IS THE BG OF OUR PHOTO
        self.img_pos = [160, 260]
        self.collision_area = pygame.Rect(50, 50, 300, 50) #CREATE RECTANGLE'''
        
        self.movement = [False, False]
        
        self.assets = {
            'player': load_image('entities./player.png')
        }
        
        self.player = PhysicsEntity(self, 'Player', (50, 50), (8, 15))
    
    def run(self):
        while True:
            
            self.screen.fill((14,219,248))
            
            '''#CREATE NEW RECTANGLE IMAGE
            img_r = pygame.Rect(self.img_pos[0], self.img_pos[1], self.img.get_width(), self.img.get_height())
            if img_r.colliderect(self.collision_area):
                #IF THE CLOUD IS TOUCHING THE WALL
                pygame.draw.rect(self.screen, (0, 100, 255), self.collision_area)
            else:
                #IF THE CLOUD IS NOT TOUCHING THE WALL
                pygame.draw.rect(self.screen, (0, 50, 255), self.collision_area)
                
            self.img_pos[1] += (self.movement[1] - self.movement[0]) * 5
            self.screen.blit(self.img, self.img_pos)'''
            
            self.player.update((self.movement[1] - self.movement[0], 0))
            self.player.render(self.screen)
            #GAME LOOP
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False
                    
            pygame.display.update()
            self.clock.tick(60)
            
Game().run()