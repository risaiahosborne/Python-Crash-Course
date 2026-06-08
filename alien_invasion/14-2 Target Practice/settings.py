class Settings:
    """A class to manage game assets and behavior."""
    
    def __init__(self):
        """Initialize game static settings."""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        
        #Set background color with a tuple for RBG values. 
        self.bg_color = (235, 180, 235) #Light gray background color.
        
        #ship settings
        self.ship_speed = 3
        self.ship_limit = 3
        
        #Bullet strings
        self.bullet_speed = 15
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        
        #target settings
        self.target_speed = 1.0
        self.target_height = 100
        self.target_width = 100
        self.target_color = (180, 60,10)
        self.miss_limit = 3
        
        #Speeds up the game
        self.speedup_scale = 1.1
        
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """Initialize settings that change"""
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0
        
        #fleet direction 1 = right -1 = left
        self.fleet_direction = 1
        
    def increase_speed(self):
        """Controls speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale 