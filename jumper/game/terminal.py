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
        self._message = ""
        self._parachute = Parachute()
     
    def read_text(self):
        """Gets text input from the terminal. Directs the user with the given prompt.

        Args: 
            self (TerminalService): An instance of TerminalService.
        """
        self._input = input("please enter a lettter of the words [a-z]: ")

        if self._input.lower() >= "a" and self._input.lower() <= "z":
            return self._input.lower()
        else:
            print("Wrong input, enter lettters (a-z): ")
    
    def game_win(self, text):
        """Displays the given text on the terminal. 

        Args: 
            self (TerminalService): An instance of TerminalService.
        """
        print(text)

    def game_loss(self, text):
        """Displays the given text on the terminal. 

        Args: 
            self (TerminalService): An instance of TerminalService.
        """
        print(text)
    
    def write_message(self, text):
        """Displays the given text on the terminal. 

        Args: 
            self (TerminalService): An instance of TerminalService.
            text (string): The text to display.
        """
        print(text)
        
    def display(self):
        """Prints the print statement on the terminal. 

        Args: 
            self (TerminalService): An instance of TerminalService.
        """
        self._message = "welcome to the jumper game \ndon't let your parachute destroy."
        print(self._message)
        print("^^^^^^^^^^^^^^^^^^^")
        self._parachute.draw()
        print('What is the word?')
    
    def output_letters(self, prompt):
        """Displays the given prompt to the terminal. 

        Args: 
            self (TerminalService): An instance of TerminalService.
        """
        print(prompt, end="")
