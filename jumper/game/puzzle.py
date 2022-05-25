import random

class Puzzle:
    """The puzzle class is a list of words. The responsibility of the class is to choose a
        random word from the list.
    """

    def __init__(self):
        """Constructs a new Puzzle.

        Args:
            self (Puzzle): An instance of Puzzle.
        """
        self._word = ["joel", "samoa", "limhi"]
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
        """Gets a choice from the player.

        Args:
            self (Puzzle): An instance of Puzzle.
        
        Returns:
            string: A choice from the player.
        """
        return self._choice
        
#obj = Puzzle()
#print(obj._word)
