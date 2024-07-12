import numpy as np
import pandas as pd
import random

class Die:
    '''
    A class representing a die object with N faces and W weights, 
    which can be rolled to select a face one or more times.  

    Attributes: 
    - faces: A Numpy Array of unique symbols. Accepts numeric or string values.
    - weights: A list of weights corresponding to each face. Defaults to 1.0 for each face.
    - die_df: A pandas dataframe with faces as the index and a column for their corresponding weights. 

    Methods:
    - set_weight(face, int): Changes a face's weight to a new value.
    - roll_die(n_rolls=1): Selects a face n_rolls times. 
    '''

    def __init__(self, faces):
        '''
        Initializes the Die with faces and default weights of 1.0. 

        Input:
        - faces: A Numpy Array of unique numeric or string values. 

        Raises:
        - TypeError: If faces not a Numpy Array.
        - ValueError: If values in array are not numerics or strings, or if there are repeating values.
        '''

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
        '''
        Changes a face's weight to a new value.

        Input:
        - face_val: String or numeric value corresponding to a value in faces.
        - new_weight: int or float

        Raises:
        - IndexError: If face_val not in faces array.
        - TypeError: If new_weight not int or float.
        '''

        if face_val not in self.faces:
            raise IndexError("Value not in faces array.")
        elif (type(new_weight) != int) and (type(new_weight) != float):
            raise TypeError("New weight must be int or float.")
        else:
            self.die_df.loc[face_val, "weights"] = new_weight
            self.weights = self.die_df['weights'].tolist()

    def roll_die(self, n_rolls=1):
        '''
        Selects a face one or more times and returns a list of results.

        Input:
        - n_rolls: int representing how many times to roll. Defaults to 1.

        Output:
        - rolls: Returns list of faces that were selected from each roll.
        '''

        rolls = random.choices(self.faces, weights=self.weights, k=n_rolls)
        return rolls

    def current_state(self):
        '''
        Returns a dataframe storing the die's faces and their corresponding weights.

        Output:
        - die_df: A Pandas dataframe. 
        '''

        return self.die_df

class Game:
    '''
    A class representing a game object consisting of one or more similar dice (Die objects) 
    one or more times. 

    Attributes:
    - __play_df: A private Pandas dataframe that stores roll numbers in an index and 
        columns with the results for each die.
    - dice: A list of one or more similar Die objects.

    Methods:
    - play(nrolls): Rolls the dice nrolls times and stores the results in the private dataframe.
    - recent_results(wide=True): Returns the private dataframe of game results in a wide or 
        narrow format. Defaults to wide=True.
    '''
    __play_df = pd.DataFrame()

    def __init__(self, dice):
        '''
        Initializes the Game with a list of Die objects.

        Inputs: 
        - dice: A list of one or more similar Die objects.

        Raises:
        - TypeError: If values of dice are not Die objects.
        '''

        for die in dice:
            if not isinstance(die, Die):
                raise TypeError("Values of dice must be Die objects.") 
            
        self.dice = dice

    def play(self, nrolls):
        '''
        Rolls all the dice a specified number of times and stores the results in a dataframe.

        Inputs:
        - nrolls: int representing the number of times to roll the dice.
        '''

        for die in self.dice:
            play = die.roll_die(nrolls)
            self.__play_df[str(self.dice.index(die))] = play

        self.__play_df.index.name = 'roll number'

    def recent_results(self, wide=True):
        '''
        Returns the dataframe of results of the most recent play, either in wide or narrow format.

        Inputs:
        - wide: Boolean value corresponding to wide or narrow. Defaults to True.

        Raises:
        - ValueError: If wide not set to True or False. 
        '''

        if wide == True:
            return self.__play_df
        elif wide == False:
            self.__play_df = self.__play_df.stack()
            self.__play_df.index.names = ['roll number', 'die number']
            return self.__play_df
        else:
            raise ValueError("Parameter wide accepts True or False.") 

class Analyzer:
    '''
    A class representing an Analyzer object that computes various statistics on the 
    results of a Game object.

    Attributes: 
    - game: A Game object. 

    Methods:
    - jackpot(): Returns the number of times all dice rolled the same face in a game. 
    - face_counts_per_roll(): Computes the number of times each die face was rolled in a game.
    - combo_count(): Computes the distinct combinations of faces rolled along with their counts.
    - permutation_count(): Computes the distinct permutations of faces rolled along with their counts.
    '''

    def __init__(self, game):
        '''
        Initializes an Analyzer object with a Game object.

        Inputs:
        - game: A Game object. 

        Raises:
        - ValueError: If game is not a Game object.
        '''

        if not isinstance(game, Game):
            raise ValueError("Parameter game must be Game object.")
        else:
            self.game = game

    def jackpot(self):
        '''
        Returns the number of times all dice rolled the same face in a game. 

        Output:
        - count: An int representing the number of jackpots in a single game. 
        '''

        results = self.game.recent_results()
        jackpot = results.nunique(axis=1) == 1
        count = int(jackpot.sum())
        return count

    def face_counts_per_roll(self):
        '''
        Computes the number of times each die face was rolled in a game and returns a Pandas dataframe
        of the results. 

        Output:
        - face_counts_df: A Pandas dataframe with an index of the roll number, face values as columns
            and count values in the cells. 
        '''

        results = self.game.recent_results()
        faces = self.game.dice[0].faces.tolist()

        face_counts_df = pd.DataFrame(columns = faces)
        face_counts_df.index.name = 'roll number'

        for i in range(len(results)): 
            face_counts_df.loc[len(face_counts_df)] = [results.iloc[i].tolist().count(x) for x in faces]

        return face_counts_df

    def combo_count(self):
        '''
        Computes the distinct combinations of faces rolled along with their counts and returns a 
        Pandas dataframe of the results. 

        Output:
        - combo_df: A Pandas dataframe with a MultiIndex of combinations and a column for the associated counts.
        '''

        results = self.game.recent_results()
        sorted_face_counts = results.apply(lambda row: sorted(row), axis=1)
        sorted_df = pd.DataFrame(sorted_face_counts.tolist(), columns = results.columns)

        combo_df = sorted_df.groupby(list(sorted_df.columns)).size().to_frame(name='count')
        return combo_df

    def permutation_count(self):
        '''
        Computes the distinct permutations of faces rolled along with their counts and returns a Pandas
        dataframe of the results. 

        Output: 
        - perms: A Pandas dataframe with a MultiIndex of permutations and a column for the associated counts. 
        '''

        results = self.game.recent_results()
        perms = results.groupby(list(results.columns)).size()
        return perms