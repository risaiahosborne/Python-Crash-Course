import pygame

from pygame.sprite import Sprite

class SideBullet(Sprite):
    """A class to manage bullets fired from the ship."""
    
    def __init__(self, bs_game):
        """Create a bullet object at the ship's current position."""
        
        super().__init__()
        
        self.screen = bs_game.screen
        self.shooter_settings = bs_game.shooter_settings
        self.color = self.shooter_settings.bullet_color
        
        #Create a bullet rect at (0,0) and then set correct position.
        self.rect = pygame.Rect(0,0, self.shooter_settings.bullet_width, 
                            self.shooter_settings.bullet_height)
        self.rect.midtop = bs_game.battleship.rect.midtop
    
        #Store the bullet's position as a float.
        self.x = float(self.rect.x)
        
    def update(self):
        """Move the bullet up the screen. """
        
        #Update the exact position of the bullet.
        self.x -= self.shooter_settings.bullet_speed
        
        #Update the rect position. 
        self.rect.x = self.x
        
    def draw_bullet(self):
        """Draw teh bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)