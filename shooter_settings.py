class Settings:
    """A class to manage game assets and behavior."""
    
    def __init__(self):
        """Initialize game settings."""
        #Screen settings
        self.screen_width = 1600
        self.screen_height = 1200
        
        #Set background color with a tuple for RBG values. 
        self.bg_color = (75, 225, 50) #Light gray background color.
        
        #ship settings
        self.ship_speed = 2.0
        
        #Bullet strings
        self.bullet_speed = 4.0
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (125, 125, 125)
        self.bullets_allowed = 9
        
        #Drop settings
        #self.rain_drop_speed = 1.0
        self.rain_drop_speed = 10
        #fleet_direction of 1 represents right; -1 represent left.
        self.rain_drop_direction = 1        
     
        #star settings
        #self.star_drop_speed = 1.0
        self.star_drop_speed = 10
        #fleet_direction of 1 represents right; -1 represent left.
        self.star_drop_direction = 1           