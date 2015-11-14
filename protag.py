class Character:
    """ The base class for characters, including our Protag """
    def __init__(self):
        
        self.STR = 10
        self.DEX = 10
        self.CON = 10
        self.INT = 10
        self.WIS = 10
        self.CHA = 10

        self.INVENTORY_SPACE =  STR * 5

    def nhnewgame(self):
        """ Are you a boy/girl?
        What's your name?
        What's your occupation?
        What did you do in the army?"""
        
