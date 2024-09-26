#game usually run as a huge "while" loop. 
import pygame
import sys
from spaceShip import SpaceShip
from bullets import Bullet

class Game:
    def __init__(self):
        #creation of the main window
        pygame.init() # init is initialization method
        self._display = pygame.display.set_mode((800,800)) #screen size
        self._clock = pygame.time.Clock()# actively tracks FPS
        pygame.display.set_caption("Space Invaders") # allows changing of the test of the window
        
        #creation of a surface
        self._space_surface = pygame.Surface((900,800))
        #createSpaceShip
        self._space_ship = SpaceShip("SpaceInvaders/assets/SpaceShip.png", 400,800)
        self._all_bullet = pygame.sprite.Group()

    def run(self):
        while True:
            #checks for events
            for event in pygame.event.get(): # to see when an event is happening
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    current_ship_location = self._space_ship.get_position()
                    bullet_object = Bullet(current_ship_location[0] + 40, current_ship_location[1])
                    self._all_bullet.add(bullet_object)   

            #handling pressing keys
            keys = pygame.key.get_pressed()
            ship_x, ship_y = self._space_ship.get_position()

            #Movement Logic
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self._space_ship.move("d")
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self._space_ship.move("a")
            if keys[pygame.K_w] or keys[pygame.K_UP]:
                self._space_ship.move("w")
            if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                self._space_ship.move("s")


            self._display.blit(self._space_surface, (0,0)) # blit essentially " draws" on the display
            self._space_surface.blit(pygame.image.load("SpaceInvaders/assets/OuterSpace.png"),(0,0))# blit draws on the surface itself.
            self._space_surface.blit(self._space_ship.get_surface(), self._space_ship.get_position())
            self._all_bullet.draw(self._space_surface)
            self._all_bullet.update()
            #updates window
            pygame.display.update()
            self._clock.tick(60) # timer set to 60 fps


my_game=Game()
my_game.run()