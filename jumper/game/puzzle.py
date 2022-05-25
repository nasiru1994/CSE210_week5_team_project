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
        self._chosen_letters = []
        self._blank_spaces = ""

    def _get_word(self):
        """Gets a word for the player.

        Args:
            self (Puzzle): An instance of Puzzle.
        
        Returns:
            string: A word for the player.
        """
        return self._word
        
    def _get_choice(self):
        """Gets a choice from the player.

        Args:
            self (Puzzle): An instance of Puzzle.
        
        Returns:
            string: A choice from the player.
        """
        return self._choice
    
    def _split_chosen_word(self, chosen_word):
        """Splits chosen word into letters.

        Args:
            self (Puzzle): An instance of Puzzle.
        """
        self._chosen_letters = []

        for letter in chosen_word:
            self._chosen_letters.append(letter)
    
    def solve_puzzle(self, letter):
        """Decides if letter matches chosen letters.

        Args:
            self (Puzzle): An instance of Puzzle.
        """
        if letter in self._chosen_letters:
            print("\nCorrect Letter!")
        else:
            print("\nWrong letter!")