class enemy():
    """Creature of the void"""
    def __init__(self, stren, intel, agil, atten, charis):
        self.stren = stren
        self.intel = intel
        self.agil = agil
        self.atten = atten
        self.charis = charis
        
    def change_stren(self, stren, change):
        self.stren += change
        
    def change_intel(self, intel, change):
        self.intel += change
        
    def change_agil(self, agil, change):
        self.agil += change
        
    def change_atten(self, atten, change):
        self.atten += change

    def change_charis(self, charis,change):
        self.charis += change
      
class sphinx(enemy):
    def __init__(self, stren, intel, agil, atten, charis):
        super().__init__(stren, intel, agil, atten, charis)

class minotaur(enemy):
    def __init__(self, stren, intel, agil, atten, charis):
        super().__init__(stren, intel, agil, atten, charis)

class troll(enemy):
    def __init__(self, stren, intel, agil, atten, charis):
         super().__init__(stren, intel, agil, atten, charis)

