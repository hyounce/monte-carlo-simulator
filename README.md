# ds5100-finalproject-ksg8xy
Files and materials for DS5100's final project: a MonteCarlo module. Package includes Die, Game, and Analyzer classes with associated methods and unittests. 

## Installing the Montecarlo package. 
**Step 1:** Find and open the terminal on your computer. On Mac, click on the magnifying glass in the top right corner of the screen and type "Terminal". On Windows, search for an application called "Windows Powershell".

**Step 2:** Decide on a location where you want this module to download and copy the file path. Then inside the terminal, move inside this directory by typing
```
cd \path\to\location
```
**Step 3:** Use git to download the contents of this repository to your own computer by typing
```
git clone https://github.com/hyounce/ds5100-finalproject-ksg8xy/
```
**Step 4:** To work inside this folder, type
```
cd ds5100-finalproject-ksg8xy
```
**Step 5:** Install the montecarlo pacakge by running
```
pip install .
```
**Step 6:** Confirm the package installed correctly by running
```
cd ..
python
import montecarlo
```
If installed correctly, you should receive the following message: 
```
Welcome to the montecarlo module.
```

## API Reference: 

### Die Class:
A class representing a die object with N faces and W weights, which can be rolled to select a face one or more times.

Attributes: 
  - faces: A Numpy Array of unique symbols. Accepts numeric or string values.
  - weights: A list of weights corresponding to each face. Defaults to 1.0 for each face.
  - die_df: A pandas dataframe with faces as the index and a column for their corresponding weights.

**__init__(self, faces):**
  
    Initializes the Die with faces and default weights of 1.0. 
    
    Input:
    - faces: A Numpy Array of unique numeric or string values. 
    
    Raises:
    - TypeError: If faces not a Numpy Array.
    - ValueError: If values in array are not numerics or strings, or if there are repeating values.

**set_weight(self, face_val, new_weight):**

    Changes a face's weight to a new value.
  
    Input:
    - face_val: String or numeric value corresponding to a value in faces.
    - new_weight: int or float
  
    Raises:
    - IndexError: If face_val not in faces array.
    - TypeError: If new_weight not int or float.

**roll_die(self, n_rolls=1):**
  
    Selects a face one or more times and returns a list of results.
  
    Input:
    - n_rolls: int representing how many times to roll. Defaults to 1.
  
    Output:
    - rolls: Returns list of faces that were selected from each roll.

**current_state(self):**

    Returns a dataframe storing the die's faces and their corresponding weights.
  
    Output:
    - die_df: A Pandas dataframe.

### Game Class: 
A class representing a game object consisting of one or more similar dice (Die objects) one or more times.

Attributes:
  - __play_df: A private Pandas dataframe that stores roll numbers in an index and 
      columns with the results for each die.
  - dice: A list of one or more similar Die objects.

**__init__(self,dice):**

    Initializes the Game with a list of Die objects.
  
    Inputs: 
    - dice: A list of one or more similar Die objects.
  
    Raises:
    - TypeError: If values of dice are not Die objects.

**play(self, nrolls):**

    Rolls all the dice a specified number of times and stores the results in a dataframe.
  
    Inputs:
    - nrolls: int representing the number of times to roll the dice.

**recent_results(self, wide=True):**
  
    Returns the dataframe of results of the most recent play, either in wide or narrow format.
  
    Inputs:
    - wide: Boolean value corresponding to wide or narrow. Defaults to True.
  
    Raises:
  - ValueError: If wide not set to True or False.

### Analyzer Class: 
A class representing an Analyzer object that computes various statistics on the results of a Game object.

Attributes: 
  - game: A Game object. 
    
**__init__(self, game):**

    Initializes an Analyzer object with a Game object.
  
    Inputs:
    - game: A Game object. 
  
    Raises:
    - ValueError: If game is not a Game object.

**jackpot(self):**

    Returns the number of times all dice rolled the same face in a game. 
    
    Output:
    - count: An int representing the number of jackpots in a single game.

**face_counts_per_roll(self):**

    Computes the number of times each die face was rolled in a game and returns a Pandas dataframe
    of the results. 
  
    Output:
    - face_counts_df: A Pandas dataframe with an index of the roll number, face values as columns
        and count values in the cells.

**combo_count(self):**

    Computes the distinct combinations of faces rolled along with their counts and returns a 
    Pandas dataframe of the results. 
  
    Output:
    - combo_df: A Pandas dataframe with a MultiIndex of combinations and a column for the associated counts.

**permutation_count(self):**
  
    Computes the distinct permutations of faces rolled along with their counts and returns a Pandas
    dataframe of the results. 
  
    Output: 
    - perms: A Pandas dataframe with a MultiIndex of permutations and a column for the associated counts. 

## Usage:
To import and use the Die, Game, and Analyzer classes in a python file: 
```
from montecarlo.montecarlo import Die, Game, Analyzer
import numpy as np

# To instantiate a die object, pass a numpy array of faces (numerics or strings):
die = Die(np.array([1,2,3,4,5,6]))

# To instantiate a Game object, pass a list of Die objects:
game = Game([die])

# To instantiate an Analyzer, pass a Game object.
analyzer = Analyzer(game)
