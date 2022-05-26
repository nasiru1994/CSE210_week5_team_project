from game.parachute import Parachute
class TerminalService:
    def __init__(self):
        self._input = ""
        self._message = ""
        self._parachute = Parachute()


    """A service that handles terminal operations.
    
    The responsibility of a TerminalService is to provide input and output operations for the 
    terminal.
    """
     
    def read_text(self):
        self.input = input("please enter a lettter of the words [a-z]: ")
        """Gets text input from the terminal"""

        return self.input

    
    
    
    def write_message(self, text):
        """Give customize message to the user.

        Args:
            self (TerminaService): An instance of TerminalService.
        """
        
        print(text)
        
    def display(self):
        """Display the game start message.

        Args:
            self (TerminaService): An instance of TerminalService.
        """

       
        self._message = "welcome to the jumper game \ndon't let your parachute destroy."
        print(self._message)
        print("^^^^^^^^^^^^^^^^^^^")
        self._parachute.draw()
        print('What is the word?')
     

        