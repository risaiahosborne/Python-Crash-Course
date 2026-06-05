import pygame.font

class Button:
    """A class to build buttons for the game."""
    
    def __init__(self, ai_game, msg):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        
        #Set dimension and properties
        self.width, self.height = 500, 50
        self.button_color = (0,135,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None, 48)
        
        #Build the button's rect obj and center.
        self.rect = pygame.Rect(0,0,self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        #The button msg need to be prepped ony once. 
        self._prep_msg(msg)
        
    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the bottom."""
        self.msg_image = self.font.render(msg, True, self.text_color,
                        self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def _update_msg_position(self):
        """If the button is moved, the text needs to be moved as well."""
        self.msg_image_rect.center = self.rect.center
        
    def draw_button(self):
        """Draw blank button and then draw message."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
    
        
        