import numpy as np
import pandas as pd
import random

class Die:

    def __init__(self, faces):

        types = ['i', 'f', 'U']

        if not isinstance(faces, np.ndarray):
            raise TypeError("Must be of type NumPy array.")
        elif faces.dtype.kind not in types:
            raise ValueError("Values must be of type string or int.")
        elif len(faces) != len(np.unique(faces)):
            raise ValueError("Array's values must be distinct.")
        else:
            self.faces = faces

        self.weights = [1 for x in range(len(self.faces))]
        self.die_df = pd.DataFrame({'weights': self.weights}, index=self.faces)

    
    def set_weight(self, face_val, new_weight):

        if face_val not in self.faces:
            raise IndexError("Value not in faces array.")
        elif (type(new_weight) != int) and (type(new_weight) != float):
            raise TypeError("New weight must be int or float.")
        else:
            self.die_df.loc[face_val].iloc[0] = new_weight
            self.weights = self.die_df['weights'].tolist()

    def roll_die(self, n_rolls=1):
        rolls = random.choices(self.faces, weights=self.weights, k=n_rolls)
        return rolls

    def current_state(self):
        return self.die_df

class Game:
    
    def __init__(self, dice):
        for die in dice:
            if not isinstance(die, Die):
                raise TypeError("Value not Die object.") # clean 
        # check if die in dice have same faces
        self.dice = dice

    def play(self, nrolls):
        self.play_df = pd.DataFrame() # private?
        for die in self.dice:
            play = die.roll_die(nrolls)
            self.play_df[str(self.dice.index(die))] = play
        self.play_df.index.name = 'roll number'

    def recent_results(self, wide=True):
        if wide == True:
            return self.play_df
        elif wide == False:
            self.play_df = self.play_df.stack()
            self.play_df.index.names = ['roll number', 'die number']
            return self.play_df
        else:
            raise ValueError("Parameter wide accepts True or False.") 

class Analyzer:

    def __init__(self, game):
        if not isinstance(game, Game):
            raise ValueError("Parameter game must be Game object.")
        else:
            self.game = game

    def jackpot(self):
        pass

    def face_counts_per_roll(self):
        pass

    def combo_count(self):
        pass

    def permutation_count(self):
        pass