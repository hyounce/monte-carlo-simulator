from montecarlo import Die, Game
import numpy as np

faces = np.array([1,2,3,4,5,6])
die1 = Die(faces)
die2 = Die(faces)
die3 = Die(faces)
die4 = Die(faces)
die5 = Die(faces)
dice = [die1, die2, die3, die4, die5]
game = Game(dice)
game.play(2)
print(game.recent_results())