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
        self._player_guess_correctly = []
        self._finalString = ""

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        self._terminal.display()
        self._give_player_hint()
        while self._isPlaying:
            self._get_inputs()
            self._do_updates()
            self._do_output()
        
    def _give_player_hint(self):
        """Gives the player hints.

        Args:
            self (Director): An instance of Director.
        """
        if self._random_word_chose == "joel":
            self._terminal.write_message("the word is a name of a person not more than 7 letters")
        elif self._random_word_chose == "limhi":
            self._terminal.write_message("The word is a name in Book of Mormon")
        elif self._random_word_chose == "samoa":
            self._terminal.write_message("The word is a country with letter s at begining")
        
    
    def get_final_string(self):
        """Get final string from player guess.

        Args:
            self (Director): An instance of Director.
        """
        self._finalString = "".join(self._player_guess_correctly)
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
            self._player_guess_correctly.clear()
            self._finalString = "" 
            self._parachute.draw()

            self._terminal.write_message("wrong letter. Your word building is reset")
            return self._parachute_diagram
        else:
            self._terminal.write_message(self._player +"______" + " is correct")
            self._player_guess_correctly.append(self._player)
            self._correct_guess_counter += 1
            #print (self._correct_guess_counter) 
           
    
    def _do_output(self):
        """Check whether if all the words in the random words chose by the computer
        has been mentioned.
        If all are mentioned, the puzzle is solved it's a win the game ends.
        If all of the parachute is destroy because the player misses the words, it's a loss the game ends

        Args:
            self (Director): An instance of Director.
        """
        self._finalString = "".join(self._player_guess_correctly)
        self._terminal.write_message("building word if you guess a correct letter: " + self._finalString)
        if self._correct_guess_counter == 7:
            self._terminal.write_message("Just a HINT!!, to win, you have to enter the letters of the word chronologically\nStart the word spelling again")
            self._player_guess_correctly.clear()

        if self._finalString == self._random_word_chose:
            self._terminal.write_message(f"you win\nThe word was {self._random_word_chose}")
            self._isPlaying = False


        if len(self._parachute_diagram)== 2:
            self._terminal.write_message("(.^.)parachute at critical condition. Two chances remains")

        if len(self._parachute._diagram)== 0:
            self._terminal.write_message(f"you loss (^ ^)\nThe word was {self._random_word_chose}")
            self._isPlaying = False