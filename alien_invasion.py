import sys #functions to interact with the operating system
import pygame # video game library that makes it easier to create games
import json

from pathlib import Path
from time import sleep
from random import randint

from settings import Settings 
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button
from scoreboard import Scoreboard
#from game_character import GameCharacter as GC

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
        
        #Create an instance to store game statistics.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
        #self.game_character = GC(self)
        
        self._create_fleet()
        
        #True = on/ False = off
        self.game_active = False
        
        #Make the Play button.
        self.play_button = Button(self, "Press 'p' or Spacebar to Play.")
        self._difficulty_buttons()
    
    def _difficulty_buttons(self):
        """Make buttons to select the difficulty."""
        self.easy_button = Button(self, "Easy")
        self.medium_button = Button(self, "Medium")
        self.hard_button = Button(self, "Hard")
        
        self.easy_button.rect.top = (
            self.play_button.rect.top + 1.5*self.play_button.rect.height)
        self.easy_button._update_msg_position()
        
        self.medium_button.rect.top = (
            self.easy_button.rect.top + 1.5*self.easy_button.rect.height)
        self.medium_button._update_msg_position()
        
        self.hard_button.rect.top = (
            self.medium_button.rect.top + 1.5*self.medium_button.rect.height)
        self.hard_button._update_msg_position()
                    
    def run_game(self):
        """Start the main game loop."""
        while True:
            self._check_events()
            
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()
            self.clock.tick(60) #60 fps limit
            
            #Get rid of bullets that have disappeared.
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            
    def _check_events(self): # Refactored _check_events to keydown and keyup
        """Respond to mouse and keyboard."""
        for event in pygame.event.get():  #get the list of events since last call and loops through them.
            if event.type == pygame.QUIT: 
                sys._close_game()
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
                self._check_difficulty_button(mouse_pos)
                
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
            sys._close_game()
        
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
    
    def _check_difficulty_button(self, mouse_pos):
        """ Start a new game by clicking play."""
        easy_button_clicked = self.easy_button.rect.collidepoint(mouse_pos)
        medium_button_clicked = self.medium_button.rect.collidepoint(mouse_pos)
        hard_button_clicked = self.hard_button.rect.collidepoint(mouse_pos)
        if easy_button_clicked and not self.game_active:
            self.settings.difficulty_level = 'easy'
        elif medium_button_clicked and not self.game_active:
            self.settings.difficulty_level = 'medium'
        elif hard_button_clicked and not self.game_active:
            self.settings.difficulty_level = 'hard'       
                
    def _start_game(self):
        """Starts the game."""
        self.settings.initialize_dynamic_settings()
        self.stats.reset_stats() # Reset the stats to play another game. 
        self.game_active = True
        self.sb.prep_images()
        
        self.bullets.empty()
        self.aliens.empty()
            
        self._create_fleet()
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
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        self._check_bullet_alien_collision()
            
    def _check_bullet_alien_collision(self):
        """Respond to bullet-alien collisions."""
        #Remove any bullets that have hit aliens.         
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
            
        if not self.aliens:
        #Destroy existing bullets and create new fleet.
            self.start_new_level()
    
    def start_new_level(self):
        """Starts a new level."""
        self.bullets.empty()
        self._create_fleet()
        self.settings.increase_speed()
        self.stats.level += 1
        self.sb.prep_level()
        
    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            #Decrement ships left, and update scoreboard.
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            #Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()
            
            #Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()
            
            #Pause.
            sleep(0.5)      
        else:
            self.game_active = False 
            print("Game Over.")
            pygame.mouse.set_visible(True)
               
    def _update_aliens(self):
        """Check if the fleet is at an edge, then update positions."""
        self._check_fleet_edges()
        self.aliens.update()
        
        #Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
            
        #Look for aliens hitting the bottom. 
        self._check_aliens_bottom()
        
        make_new_aliens = False
        for alien in self.aliens.copy():
            if alien.check_disappeared():
                #Remove this drop, and we'll need to make new ones. 
                self.aliens.remove(alien)
                make_new_aliens = True
        
    def _create_fleet(self):
        """Create the fleet of aliens."""
        #Create an alien and keep adding aliens until there's no room left. 
        #Spacing between aliens is one alien width and one alien height.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        
        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            #Finished a row; reset x value, and increment y value.
            current_x = alien_width
            current_y += 2 * alien_height
            
    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the row."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = randint(0, 1) * x_position
        new_alien.rect.y = randint(0 , 1) * y_position
        self.aliens.add(new_alien)

    def _create_new_alien_row(self):
        """Create a new row of raindrops after a row disappears."""
        # Note: There are a number of ways to do this. This approach just
        #   copies the code from _create_drops() that's used for a single
        #   row of raindrops. This is simpler than trying to make 
        #   _create_drops() handle the full screen of raindrops, or a single
        #   new row of raindrops.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x = alien_width
        current_y = -1 * alien_height
        while current_x < (self.settings.screen_width - 2 * alien_width):
            self._create_drop(current_x, current_y)
            current_x += 2 * alien_width
            
    def _check_fleet_edges(self):
        """Respond if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
        
    def _check_aliens_bottom(self):
        """Check if any aliens reached the bottom."""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                #Treat this the same as if the ship got hit. 
                self._ship_hit()
                break
            
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        #Redaw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color) #fill() method is applied to the screen object and adds the color. 
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()        
        self.ship.blitme()
        self.aliens.draw(self.screen)
        #self.game_character.blitme_1()
        self.sb.show_score()
        
        if not self.game_active:
            self.play_button.draw_button()
            self.easy_button.draw_button()
            self.medium_button.draw_button()
            self.hard_button.draw_button()
            
        pygame.display.flip()
                    
    def _close_game(self):
        """Saves the highscore and exits"""
        if self.stats.high_score > self.stats.saved_high_score():
            path = Path("Part II\\alien_invasion\\alien_invasion_game\\high_score.json")
            contents = json.dumps(self.stats.high_score)
            path.write_text(contents)
        
        sys.exit()
        
if __name__ == '__main__': 
    #Make a game instance, and run. 
    ai = AlienInvasion()
    ai.run_game()