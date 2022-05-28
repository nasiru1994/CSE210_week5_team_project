"""The puzzle class is a list of words. The responsibility of the class is to choose a
random word
from the list."""
import random
class Puzzle:
    """Constructs a new Puzzle.

        Args:
            self (Puzzle): An instance of Puzzle.
        """
    def __init__(self):
        self._word = ["class", "mango"]
        self._choice = random.choice(self._word)
        

    def get_word(self):
        """Gets a word for the player.

        Args:
            self (Puzzle): An instance of Puzzle.
        
        Returns:
            string: A word for the player.
        """
        return self._word
        
    def get_choice(self):
        """Gets a choice word from list choose by the computer.

        Args:
            self (Puzzle): An instance of Puzzle.
        
        Returns:
            string: A choice from the computer.
        """
        return self._choice
        
#obj = Puzzle()
#print(obj._word)

 

 


