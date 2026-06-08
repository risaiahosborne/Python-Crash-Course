import json

from pathlib import Path

class GameStats:
    """Track statistics for Alien Invasion."""
    
    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        
        self.high_score = self.saved_high_score()
    
    def saved_high_score(self):
        """Gets high score from file, if it exists."""
        path = Path("Part II\\alien_invasion\\alien_invasion_game\\high_score.json")
        
        try:
            contents = path.read_text()
            high_score = json.loads(contents)
            return high_score
        except FileNotFoundError:
            return 0
            
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
        

        
        