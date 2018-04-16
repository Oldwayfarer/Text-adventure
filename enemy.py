class enemy():
    """Creature of the void"""
    def __init__(self, stren, intel, agil, atten, charis):
        self.stren = stren
        self.intel = intel
        self.agil = agil
        self. atten = atten
        self. charis = charis
    
class sphinx(enemy):
    def __init__(self, stren, intel, agil, atten, charis):
        super().__init__(stren, intel, agil, atten, charis)

class minotaur(enemy):
    def __init__(self, stren, intel, agil, atten, charis):
        super().__init__(stren, intel, agil, atten, charis)

class troll(enemy):
    def __init__(self, stren, intel, agil, atten, charis):
         super().__init__(stren, intel, agil, atten, charis)

