from game.terminal import TerminalService
from game.parachute import Parachute
from game.puzzle import Puzzle

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._isPlaying = True
        self._terminal = TerminalService()
        self._puzzle = Puzzle()
        self._parachute = Parachute()
        self._correct_guess_counter = 0
        self._player = ""
        self._random_word_chose = self._puzzle.get_choice()
        self._parachute_diagram = self._parachute.get_diagram()
        self._correct_guess = ["_", "_","_","_","_",]
        self._finalString = ""

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        self._terminal.display()
        while self._isPlaying:
            self._get_inputs()
            self._do_updates()
            self._do_output()
   
    def get_final_string(self):
        """Get final string from player guess.

        Args:
            self (Director): An instance of Director.
        """
        self._finalString = "".join(self._correct_guess)
        return self._finalString
        
    def _get_inputs(self):
        """do_updates methods check the letter input from the player and search the random word
        chose by the computer. If a match is found the letter is revaled otherwise, a portion 
        of the parachute is destroy

        Args:
            self (Director): An instance of Director.
        """
        self._player = self._terminal.read_text()

    def _do_updates(self):
        """Keeps track of game logic.

        Args:
            self (Director): An instance of Director.
        """
        if self._random_word_chose.find(self._player)== -1:
            self._parachute_diagram.pop(0)
            self._parachute.draw()
            self._terminal.write_message("wrong letter. Parachute destroy")
            return self._parachute_diagram
        
        if self._random_word_chose == "class" and self._player == "c":
            self._correct_guess[0] = "c"
            self._terminal.write_message(self.get_final_string())
            
        elif self._random_word_chose == "class" and self._player == "l":
            self._correct_guess[1] = "l"
            self._terminal.write_message(self.get_final_string())
            
        elif self._random_word_chose == "class"and self._player == "a":
            self._correct_guess[2] = "a"
            self._terminal.write_message(self.get_final_string())

        elif self._random_word_chose == "class" and self._player == "s":
            self._correct_guess[3] = "s"
            self._correct_guess[4] = "s"
            self._terminal.write_message(self.get_final_string())

        #logic for mango
        elif self._random_word_chose == "mango" and self._player == "m":
            self._correct_guess[0] = "m"
            self._terminal.write_message(self.get_final_string())
        
        elif self._random_word_chose == "mango" and self._player == "a":
            self._correct_guess[1] = "a"
            self._terminal.write_message(self.get_final_string())

        elif self._random_word_chose == "mango" and self._player == "n":
            self._correct_guess[2] = "n"
            self._terminal.write_message(self.get_final_string())
        
        elif self._random_word_chose == "mango" and self._player == "g":
            self._correct_guess[3] = "g"
            self._terminal.write_message(self.get_final_string())
        
        elif self._random_word_chose == "mango" and self._player == "o":
            self._correct_guess[4] = "o"
            self._terminal.write_message(self.get_final_string()) 
           
    
    def _do_output(self):
        """Check whether if all the words in the random words chose by the computer
        has been mentioned.
        If all are mentioned, the puzzle is solved it's a win the game ends.
        If all of the parachute is destroy because the player misses the words, it's a loss the game ends

        Args:
            self (Director): An instance of Director.
        """

        if self.get_final_string() == self._random_word_chose:
            self._terminal.write_message(f"you win\nThe word was {self._random_word_chose}")
            self._isPlaying = False


        if len(self._parachute_diagram)== 2 and self._random_word_chose.find(self._player) == -1:
            self._terminal.write_message("(.^.)parachute at critical condition. Two chances remains")

        if len(self._parachute._diagram)== 0:
            self._terminal.write_message(f"you loss (^ ^)\nThe word was {self._random_word_chose}")
            self._isPlaying = False