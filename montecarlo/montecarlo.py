class Die:

    def __init__(self):
        pass
    
    def set_weight(self, face_val, new_weight):
        pass

    def roll_die(self, nrolls):
        pass

    def current_state(self):
        pass

class Game:
    
    def __init__(self, dice):
        pass

    def play(self, nrolls):
        pass

    def recent_results(self):
        pass

class Analyzer:

    def __init__(self, game):
        pass

    def jackpot(self):
        pass

    def face_counts_per_roll(self):
        pass

    def combo_count(self):
        pass

    def permutation_count(self):
        pass