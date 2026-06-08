class Settings:
    """A class to manage game assets and behavior."""
    
    def __init__(self):
        """Initialize game settings."""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        
        #Set background color with a tuple for RBG values. 
        self.bg_color = (135, 206, 235) #Light gray background color.
        
        #ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3
        
        #Bullet strings
        self.bullet_speed = 2.5
        self.bullet_width = 3000
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 30
        
        #Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #fleet_direction of 1 represents right; -1 represent left.
        self.fleet_direction = 1
        self.difficulty_level = 'medium'
        
        self.speedup_scale = 2.1
        #How quickly point values increase
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """Initialize settings that change"""
        if self.difficulty_level == 'easy':
            self.ship_speed = 1.5
            self.bullet_speed = 2.5
            self.alien_speed = 1.0
            self.fleet_direction = 1 #fleet direction 1 = right -1 = left
        elif self.difficulty_level == 'medium':
            self.ship_speed = 1.8
            self.bullet_speed = 2.8
            self.alien_speed = 1.3
            self.fleet_direction = 1
        elif self.difficulty_level == 'hard':
            self.ship_speed = 2.0
            self.bullet_speed = 3.0
            self.alien_speed = 1.5
            self.fleet_direction = 1.5
        
        self.alien_points = 50
        
    def increase_speed(self):
        """Controls speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale  
        #Increase points with speed
        self.alien_points = int(self.alien_points * self.score_scale)
    
    def set_difficulty(self, diff_setting):
        if diff_setting == 'easy':
            print('Easy')
        elif diff_setting == 'medium':
            pass
        elif diff_setting == 'hard':
            pass  