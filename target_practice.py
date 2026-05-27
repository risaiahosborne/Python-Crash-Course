import sys
from random import randint

import pygame

from bullet import Bullet
from button import Button
from game_stats import GameStats
from settings import Settings
from ship import Ship
from target import Target

class TargetPractice:
    """Overall class to manage game."""
    
    def __init__(self):
        """Initialize the game assests."""
        pygame.init()
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Target Practice")
        
        self.settings = Settings()     
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)) 

        self.game_active = False
        self.play_button = Button(self, "Play")           
        self.bullets = pygame.sprite.Group()
        self.target = Target(self)      
        self.stats = GameStats(self)
        self.ship = Ship(self)
        
    def run_game(self):
        """Start the loop."""
        while True:
            self._check_events()
                
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self.target.update()
                
            self._update_screen()
            self.clock.tick(60) #60 fps limit
                
            #Get rid of bullets that have disappeared.
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
                     
            #Make the most recent display visible
            pygame.display.flip()
    
    def _check_events(self):
        """Respond to mouse and keyboard."""
        for event in pygame.event.get():
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                
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
        elif event.key == pygame.K_SPACE: 
            self._fire_bullet()
        elif (event.key == pygame.K_p) and (not self.game_active):
            self._start_game()   
        elif event.key == pygame.K_q: #Close on 'q' 
            sys.exit()
                
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
        
    def _check_play_button(self, mouse_pos):
        """ Start a new game by clicking play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self._start_game()    
            
    def _start_game(self):
        """Starts the game."""
        self.stats.reset_stats() # Reset the stats to play another game. 
        self.game_active = True
            
        self.bullets.empty()
        self.target.center_target()
        self.ship.center_ship()

        pygame.mouse.set_visible(False)   
        
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
            if bullet.rect.left >= self.screen.get_rect().right:
                self.bullets.remove(bullet)
                self._increment_misses()        

        self._check_bullet_target_collision()
     
    def _increment_misses(self):
        self.stats.num_misses += 1
        if self.stats.num_misses >= self.settings.miss_limit:
            self.game_active = False
            pygame.mouse.set_visible(True)    
        
    def _check_bullet_target_collision(self):
        """Respond to bullet-target collisions."""
        #Remove any bullets that have hit target.         
        collisions = pygame.sprite.spritecollide(
            self.target, self.bullets, True)  

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        #Redaw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color) #fill() method is applied to the screen object and adds the color. 
        self.ship.blitme()
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()        
        
        self.target.draw_target()
        #self.game_character.blitme_1()
        
        if not self.game_active:
            self.play_button.draw_button()
            
        pygame.display.flip()
                    
if __name__ == '__main__': 
    #Make a game instance, and run. 
    tp = TargetPractice()
    tp.run_game()