"""The puzzle class is a list of words. The responsibility of the class is to choose a
random word
from the list."""
import random
class Puzzle:
    def __init__(self):
        self._word = ["joel", "samoa", "limhi"]
        self._choice = random.choice(self._word)
        

    def get_word(self):
        return self._word
        
    def get_choice(self):
        return self._choice
        
#obj = Puzzle()
#print(obj._word)

 

 


