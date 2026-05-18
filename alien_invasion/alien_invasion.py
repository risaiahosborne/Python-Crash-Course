import sys #functions to interact with the operating system

import pygame # video game library that makes it easier to create games

from settings import Settings 
from ship import Ship
from bullet import Bullet
from game_character import GameCharacter as GC

class AlienInvasion:
    """Overall class to manage game assets and behavior."""
    
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init() #Always call this before any other pygame functions
        
        self.clock = pygame.time.Clock() #Tracks the time to set the frameramte.
        self.settings = Settings() #Create an instance to use the settings class.
        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) #This creates a display window of the specified width and height.
        #FUll Screen Code COMMENTED OUT
        #self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height
        
        pygame.display.set_caption("Alien Invasion") #Title
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        
        #self.game_character = GC(self)

    def run_game(self):
        """Start the main game loop."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60) #60 fps limit
            
            #Get rid of bullets that have disappeared.
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            
            
            #Make the most recent display visible
            pygame.display.flip()

            
    def _check_events(self): # Refactored _check_events to keydown and keyup
        """Respond to mouse and keyboard."""
        for event in pygame.event.get():  #get the list of events since last call and loops through them.
            if event.type == pygame.QUIT: 
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event) 
            elif event.type == pygame.K_LEFT:
                self._check_keydown_events(event)
            elif event.type == pygame.K_RIGHT:
                self._check_keyup_events(event)   
                #Move the skip to the right.
   
    def _check_keydown_events(self, event):
        """Respond to key presses."""                
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True

        elif event.key == pygame.K_q: #Close on 'q' 
            sys.exit()
        
        while event.key == pygame.K_SPACE: 
            self._fire_bullet()      
              
    def _check_keyup_events(self, event):
        """Respond to key releases."""      
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False 
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False 
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
    
                                    
    def _fire_bullet(self):
        """
        Create a new bullet and add it to the bullets group
        Making an automatic
        """
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)                              
    
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        self.bullets.update()

        #Get rid of bullets 
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
    
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        #Redaw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color) #fill() method is applied to the screen object and adds the color. 
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()        
        self.ship.blitme()
        #self.game_character.blitme_1()
                    
if __name__ == '__main__': 
    #Make a game instance, and run. 
    ai = AlienInvasion()
    ai.run_game()