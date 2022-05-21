from game.parachute import Parachute
from game.puzzle import Puzzle

class TerminalService:
    """A service that handles terminal operations.
    
    The responsibility of a TerminalService is to provide input and output operations for the 
    terminal.
    """

    def __init__(self):
        """Constructs a new TerminalService.

        Args:
            self (TerminalService): An instance of TerminalService.
        """
        self._input = ""
        self._win = "you win"
        self._loss = "you loss"
        self._message = ""
        self._parachute = Parachute()
        self._puzzle = Puzzle()
        self._random_word_chose = self._puzzle.get_choice()
     
    def _read_text(self):
        """Gets text input from the terminal. Directs the user with the given prompt.

        Args: 
            self (TerminalService): An instance of TerminalService.
        """
        self.input = input("please enter a lettter of the words [a-z]: ")

        return self.input
    
    def _game_win(self):
        """Displays the given text on the terminal. 

        Args: 
            self (TerminalService): An instance of TerminalService.
        """
        print(self._win)
        print("the word is " + self._random_word_chose)
        return self._win

    def _game_loss(self):
        """Displays the given text on the terminal. 

        Args: 
            self (TerminalService): An instance of TerminalService.
        """
        print(self._loss)
        print("the word is " + self._random_word_chose)
        return self._loss
    
    def _write_message(self, text):
        """Displays the given text on the terminal. 

        Args: 
            self (TerminalService): An instance of TerminalService.
        text (string): The text to display.
        """
        print(text)
        
    def _display(self):
        self._message = "welcome to the jumper game \ndon't let your parachute destroy."
        print(self._message)
        print("^^^^^^^^^^^^^^^^^^^")
        self._parachute.draw()
        print('What is the word?')