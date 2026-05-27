import sys
import pygame
from random import randint

from shooter_settings import Settings
from battleship import BattleShip as BS
from side_bullet import SideBullet as SB
from star import Star
from raindrop import Raindrop

class SideShooter:
    """Manage the game assests and behaviors"""
    
    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        pygame.display.set_caption("New Shooter")
                
        #Attributes
        self.clock = pygame.time.Clock()
        self.shooter_settings = Settings()
        self.screen = pygame.display.set_mode(( self.shooter_settings.screen_width, self.shooter_settings.screen_height))
        self.battleship = BS(self)
        self.bullets = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()
        self.raindrops = pygame.sprite.Group()
        
        self._create_stars()        
        self._create_rain_drops()

    def run_game(self):
        """Start the main game loop."""
        while True:
            self._check_events()
            self.battleship.update()
            self._update_bullets()
            self._update_stars()
            self._update_rain_drops()            
            self._update_screen()
            self._create_new_drops()
            self.clock.tick(60) #60 fps limit
            
            #Get rid of bullets that have disappeared.
            for bullet in self.bullets.copy():
                if bullet.rect.left <= 0:
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
            self.battleship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.battleship.moving_left = True
        elif event.key == pygame.K_UP:
            self.battleship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.battleship.moving_down = True
        elif event.key == pygame.K_SPACE: 
            self._fire_bullet()
        elif event.key == pygame.K_q: #Close on 'q' 
            sys.exit()
              
    def _check_keyup_events(self, event):
        """Respond to key releases."""      
        if event.key == pygame.K_RIGHT:
            self.battleship.moving_right = False 
        elif event.key == pygame.K_LEFT:
            self.battleship.moving_left = False 
        elif event.key == pygame.K_UP:
            self.battleship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.battleship.moving_down = False
                                
    def _fire_bullet(self):
        """
        Create a new bullet and add it to the bullets group
        Making an automatic
        """
        if len(self.bullets) < self.shooter_settings.bullets_allowed:
            new_bullet = SB(self)
            self.bullets.add(new_bullet)                              
    
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        self.bullets.update()

        #Get rid of bullets 
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
    
    def _update_rain_drops(self):
        """Check if the fleet is at an edge, then update positions."""
        self._check_star_edges()
        self.raindrops.update()
    
    def _create_rain_drops(self):
        """Create the fleet of aliens."""
        #Create an alien and keep adding aliens until there's no room left. 
        #Spacing between aliens is one alien width and one alien height.
        raindrop = Raindrop(self)
        raindrops_width, raindrops_height = raindrop.rect.size
        
        current_x, current_y = raindrops_width, raindrops_height
        while current_y < (self.shooter_settings.screen_height - 3 * raindrops_height):
            while current_x < (self.shooter_settings.screen_width - 2 * raindrops_width):
                self._create_rain_drop(current_x, current_y)
                current_x += 2 * raindrops_width
            #Finished a row; reset x value, and increment y value.
            current_x = raindrops_width
            current_y += 2 * raindrops_height
            
    def _create_rain_drop(self, x_position, y_position):
        """Create an alien and place it in the row."""
        new_drop = Raindrop(self)
        new_drop.x = x_position
        new_drop.rect.x = x_position
        new_drop.rect.y = y_position
        self.raindrops.add(new_drop)
        
    def _create_new_drops(self):
        drop = Raindrop(self)
        drop_width, drop_height = drop.rect.size

    def _check_drop_edges(self):
        """Respond if any aliens have reached an edge."""
        for raindrop in self.raindrops.sprites():
            if raindrop.check_edges():
                self._change_drop_direction()
                break
    
    def _change_drop_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for raindrop in self.raindrops.sprites():
            raindrop.rect.y += self.shooter_settings.rain_drop_speed
        self.shooter_settings.rain_drop_direction *= -1    
    
    def _update_stars(self):
        """Check if the fleet is at an edge, then update positions."""
        self.stars.update()
        
        make_new_stars = False
        for star in self.stars.copy():
            if star.check_disappeared():
                #Remove this drop, and we'll need to make new ones. 
                self.stars.remove(star)
                make_new_stars = True
                    
    def _create_stars(self):
        """Create the fleet of aliens."""
        #Create an alien and keep adding aliens until there's no room left. 
        #Spacing between aliens is one alien width and one alien height.
        star = Star(self)
        star_width, star_height = star.rect.size
        
        current_x, current_y = star_width, star_height
        while current_y < (self.shooter_settings.screen_height - 3 * star_height):
            while current_x < (self.shooter_settings.screen_width - 2 * star_width):
                self._create_star(current_x, current_y)
                current_x += 2 * star_width

            #Finished a row; reset x value, and increment y value.
            current_x = star_width
            current_y += 2 * star_height        
    
    def _create_star(self, x_position, y_position):
        """Create a star and place it in the row."""
        new_star = Star(self)
        new_star.y = y_position
        new_star.rect.x = randint(0, 1) * x_position
        new_star.rect.y = randint(0 , 1) * y_position
        self.stars.add(new_star) 
           
    def _create_new_star_row(self):
        """Create a new row of raindrops after a row disappears."""
        # Note: There are a number of ways to do this. This approach just
        #   copies the code from _create_drops() that's used for a single
        #   row of raindrops. This is simpler than trying to make 
        #   _create_drops() handle the full screen of raindrops, or a single
        #   new row of raindrops.
        star = Star(self)
        star_width, star_height = star.rect.size

        current_x = star_width
        current_y = -1 * star_height
        while current_x < (self.settings.screen_width - 2 * star_width):
            self._create_drop(current_x, current_y)
            current_x += 2 * star_width
                    
    def _change_star_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for star in self.stars.sprites():
            star.rect.y += self.shooter_settings.star_drop_speed
        self.shooter_settings.star_drop_direction *= -1   
        
    def _check_star_edges(self):
        """Respond if any aliens have reached an edge."""
        for star in self.stars.sprites():
            if star.check_edges():
                self._change_star_direction()
                break
    
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        #Redaw the screen during each pass through the loop.
        self.screen.fill(self.shooter_settings.bg_color) #fill() method is applied to the screen object and adds the color. 
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()        
        self.battleship.blitme()
        self.stars.draw(self.screen)
        #self.game_character.blitme_1()
                    
if __name__ == '__main__': 
    #Make a game instance, and run. 
    ss = SideShooter()
    ss.run_game()