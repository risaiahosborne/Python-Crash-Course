import pygame

class BattleShip:
    """A class to manage the ship."""
    
    def __init__(self, bs_game):
        """Initialize the ship and set its starting position."""
        self.screen = bs_game.screen #
        self.settings = bs_game.shooter_settings
        self.screen_rect = bs_game.screen.get_rect()
        
        #Load the ship image and get its rect. 
        self.image = pygame.image.load("Part II\\alien_invasion\\12-6 Sideways Shooter\\images\\ship (2).bmp")
        self.rect = self.image.get_rect()
        
        #Start each chip at bottom center of the screen. 
        self.rect.center = self.screen_rect.center
        
        #Store a float for the ship's exact  position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        #Movement flags: start with a ship that's not moving. 
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
    def update(self):
        """Update the ship's position based on the movement flags."""
        
        # First update the ship's float x and y values based on movement flags.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:  
            self.x -= self.settings.ship_speed
        # y values
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:  
            self.y += self.settings.ship_speed  
        
        #Update rect object from self.x.
        self.rect.x = int(self.x)
        self.rect.y = int(self.y) 
        
    def blitme(self):
        """Draw the ship at its current location."""
        
        self.screen.blit(self.image, self.rect)
        