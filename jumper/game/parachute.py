class Parachute:
    """The parachute class create the parachute
    methods: 1. draw: which draws the parachute
    2. get_diagram which returns the list of diagram      
    """

    def __init__(self):
        """Constructs a new Parachute.

        Args:
            self (Parachute): An instance of Parachute.
        """
        self._line1 = " ___"
        self._line2 = '/___\\'
        self._line3 = '\\   /'
        self._line4 = ' \\ /'
        self._line5 = "  0"
        self._line6 = ' /|\\'
        self._line7 = ' / \\'
        self._diagram = [self._line1, self._line2,self._line3,self._line4,self._line5,self._line6,self._line7]

    def get_diagram(self):
        """Gets the diagram.

        Args:
            self (Parachute): An instance of Parachute.
        
        Returns:
            number: The diagram,
        """
        return self._diagram
        
    def draw(self):
        """Draws diagram.

        Args:
            self (Parachute): An instance of Parachute.
        """
        for i in self._diagram:
            print(i)

#obj = Parachute()
#obj._draw()
