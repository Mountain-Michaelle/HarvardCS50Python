import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """
    Overall class to manage all the game assets and behavior
    """
    
    def __init__(self):
        # This initialize pygame and creates its resource
        pygame.init()

        pygame.display.set_caption("De Bees Alien Invasion")
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.ship = Ship(self)
        
        
    def run_game(self):
        """ starting main loop for the game """
        while True:
            # Watch for keyboard and mouse input
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _update_screen(self):
        #Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()
        self.clock.tick(60)

    def _check_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        #Move the ship to the right
                        self.ship.moving_right = True
                    
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = True
                        
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False
                        
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = False
            
if __name__ == '__main__':
    # Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()