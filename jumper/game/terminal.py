from parachute import Parachute
from puzzle import Puzzle
class TerminalService:
    def __init__(self):
        self._input = ""
        self._win = "you win"
        self._loss = "you loss"
        self._message = ""
        self._parachute = Parachute()
        self._puzzle = Puzzle()
        self._random_word_chose = self._puzzle.get_choice()

    """A service that handles terminal operations.
    
    The responsibility of a TerminalService is to provide input and output operations for the 
    terminal.
    """
     
    def _read_text(self):
        self.input = input("please enter a lettter of the words [a-z]: ")
        """Gets text input from the terminal"""

        return self.input

    
    def _game_win(self):
        print(self._win)
        print("the word is " + self._random_word_chose)
        return self._win

    def _game_loss(self):
        print(self._loss)
        print("the word is " + self._random_word_chose)
        return self._loss
    
    def _write_message(self, text):
        print(text)
        
    def _display(self):

       
        self._message = "welcome to the jumper game \ndon't let your parachute destroy."
        print(self._message)
        print("^^^^^^^^^^^^^^^^^^^")
        self._parachute.draw()
        print('What is the word?')
     

        