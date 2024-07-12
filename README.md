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
