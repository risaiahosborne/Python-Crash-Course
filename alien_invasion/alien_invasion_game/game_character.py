import pygame

class GameCharacter:
    """A class to manage the ship."""
    
    def __init__(self, bs_game):
        """Initialize the ship and set its starting position."""
        
        self.screen = bs_game.screen #
        self.screen_rect = bs_game.screen.get_rect()
        
        #Load the ship image and get its rect. 
        self.image = pygame.image.load("Part II\\alien_invasion\\images\\OIP-3763699465.jpg")
        self.rect = self.image.get_rect()
        
        #Start each character at bottom center of the screen. 
        self.rect.midtop = self.screen_rect.midtop
        
    def blitme_1(self):
        """Draw the character at its current location."""
        
        self.screen.blit(self.image, self.rect)