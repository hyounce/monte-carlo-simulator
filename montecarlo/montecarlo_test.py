from montecarlo import Die
import numpy as np

arr = np.array(['q', 'g', 'k', 'l'])
d = Die(arr)
print(d.weights)
d.set_weight('k', 5.0)
print(d.current_state())
print(d.roll_die(8))