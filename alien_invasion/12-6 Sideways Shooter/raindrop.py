import pygame
from pygame.sprite import Sprite


class Raindrop(Sprite):
    """A class to represent a grid of stars on the screen."""
    def __init__(self, bs_game):
        """Alien, and starting position."""
        super().__init__()
        self.screen = bs_game.screen
        self.shooter_settings = bs_game.shooter_settings
        #Load the star and its rect attribute
        self.image = pygame.image.load(
            'Part II\\alien_invasion\\12-6 Sideways Shooter\\images\\Elegantthemes-Beautiful-Flat-Water.48.png'
                                        )
        self.rect = self.image.get_rect()
        
        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y =  self.rect.height
        
        # Store horizontal position
        self.y = float(self.rect.y)
 
    def check_disappeared(self):
        if self.rect.top > self.screen.get_rect().bottom:
            return True
        else:
            return False
           
    def update(self):
        """Move the alien to the right."""
        self.y += self.shooter_settings.rain_drop_speed
        self.rect.y = self.y