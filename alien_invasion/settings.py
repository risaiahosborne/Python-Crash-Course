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
        
        #Bullet strings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        