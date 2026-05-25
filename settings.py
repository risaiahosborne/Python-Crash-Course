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
        self.bullets_allowed = 3
        
        #Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #fleet_direction of 1 represents right; -1 represent left.
        self.fleet_direction = 1
        
        