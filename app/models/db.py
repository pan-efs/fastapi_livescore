import collections

from app.schemas.schemas import Score

class DequeDB(collections.deque):
    def __init__(self):
        self = collections.deque['Score']()
    
    def get_current_score(self):
        """
        Get current score.
        Returns:
            Score: Current score.
        """
        return self[0]
    
    def reset_score(self):
        """
        Clear the deque data structure.
        """
        self.clear()
        self.appendleft(Score())
        return self[0]
    
    def update_home_score(self):
        """
        Update the score for home team.
        Returns:
            Score: The updated score.
        """
        new_score = Score()
        
        new_score.home = self[0].home + 1
        new_score.away = self[0].away
        
        self.appendleft(new_score)
        
        return self[0]
    
    def update_away_score(self):
        """
        Update the score for away team.
        Returns:
            Score: The updated score.
        """
        new_score = Score()
        
        new_score.away = self[0].away + 1
        new_score.home = self[0].home
        
        self.appendleft(new_score)
        
        return self[0]