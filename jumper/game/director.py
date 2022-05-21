"""The director class handles all the game functionalities and logics
It contains many methods which handle different operations in the game
"""

from parachute import Parachute
from puzzle import Puzzle
from terminal import TerminalService

class Director:
    def __init__(self):
        self._isPlaying = True
        self._terminal = TerminalService()
        self._puzzle = Puzzle()
        self._parachute = Parachute()
        self._correct_guess_counter = 0
        self._player = ''
        self._random_word_chose = self._puzzle.get_choice()
        self._parachute_diagram = self._parachute.get_diagram()
        self._player_guess_correctly = []
        self._finalString = ""
        
        
    def _give_player_hint(self):
        if self._random_word_chose == "joel":
            self._terminal._write_message("the word is a name of a person not more than 7 letters")
        elif self._random_word_chose == "samoa":
            self._terminal._write_message("The word is a country with letter s at begining")
        elif self._random_word_chose == "limhi":
            self._terminal._write_message("The word is a name in Book of Mormon")
    
    def get_final_string(self):
        self._finalString = "".join(self._player_guess_correctly)
        return self._finalString
        



    def _start_game(self):
        self._terminal._display()
        self._give_player_hint()
        while self._isPlaying:
            self._get_inputs()
            self._do_updates()
            self._do_output()
        
    def _get_inputs(self):
        
        self._player = self._terminal._read_text()

    """do_updates methods check the letter input from the player and search the random word
    chose by the computer. If a match is found the letter is revaled otherwise, a portion 
    of the parachute is destroy"""

    def _do_updates(self):
        
        
         
        if self._random_word_chose.find(self._player)== -1:
            self._parachute_diagram.pop(0) 
            self._parachute.draw()

            self._terminal._write_message("wrong letter")
            return self._parachute_diagram
        else:
            self._terminal._write_message(self._player +"______" + " is correct")
            self._player_guess_correctly.append(self._player)
            self._correct_guess_counter += 1
            #print (self._correct_guess_counter)
            
            
        
           
            
                
   
    """The do_output method check whether if  all the words in the random words chose by the computer
    has been mentioned. If all are mentioned, the puzzle is solved it's a win the game ends.
    if all of the parachute is destroy because the player misses the words, it a loss the game ends"""       
    
    def _do_output(self):
        self._finalString = "".join(self._player_guess_correctly)
        #self._terminal._write_message("building word if you guess a correct letter: " + self._finalString)
        
        
        if self._finalString == self._random_word_chose:
            self._terminal._game_win()
            self._isPlaying = False

        if self._correct_guess_counter == 7:
            self._terminal._write_message("Just a HINT!!, to win, you have to enter the letters of the word chronologically\nkeep goin")

        if len(self._parachute_diagram)== 2:
             self._terminal._write_message("(.^.)parachute at critical condition. Two chances remains")

        if len(self._parachute._diagram)== 0:
            self._terminal._game_loss()
            self._isPlaying = False
        