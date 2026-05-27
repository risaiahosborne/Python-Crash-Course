import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """A class to represent a grid of stars on the screen."""
    def __init__(self, bs_game):
        """Alien, and starting position."""
        super().__init__()
        self.screen = bs_game.screen
        self.settings = bs_game.shooter_settings
        
        #Load the star and its rect attribute
        self.image = pygame.image.load('Part II\\alien_invasion\\12-6 Sideways Shooter\\images\\Oxygen-Icons.org-Oxygen-Actions-rating.48.png')
        self.rect = self.image.get_rect()
        
        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y =  self.rect.height
        
        # Store horizontal position
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
    
    def check_disappeared(self):
        """Check if drop has disappeared off bottom of screen."""
        if self.rect.top > self.screen.get_rect().bottom:
            return True
        else:
            return False
                    
    def update(self):
        """Move the alien to the right."""
        self.x += self.settings.star_drop_speed * self.settings.star_drop_direction
        self.rect.x = self.x