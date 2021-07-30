import collections

from app.schemas.schemas import Score

class DequeDB(collections.deque):
    def __init__(self):
        self = collections.deque['Score']()
    
    def update_score(self, score: Score):
        """
        Update score and return it.
        Args:
            score (Score): Current score.
        Returns:
            Score: Updated score.
        """
        self.appendleft(score)
        return self[0]
    
    def get_current_score(self):
        """
        Get current score.
        Returns:
            Score: Current score.
        """
        return self[0]
    
    def clear_db(self):
        """
        Clear the deque database.
        """
        self.clear()