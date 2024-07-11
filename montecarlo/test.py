from montecarlo import Die, Game, Analyzer
import numpy as np
import pandas as pd

faces = np.array(['a','b', 'c'])
die1 = Die(faces)


die1 = Die(np.array([1,2,3,4,5,6]))
game = Game([die1])
game.play(5)
analyzer = Analyzer(game)

expected = 4
actual = sum(analyzer.permutation_count())
print(actual)


'''
die2 = Die(faces)
die3 = Die(faces)
die4 = Die(faces)
die5 = Die(faces)
dice = [die1, die2, die3, die4, die5]
game = Game(dice)
game.play(5)
# print(game.recent_results())
'''

# a = Analyzer(game)
# print(a.jackpot())
# print()
#print(a.face_counts_per_roll())
# print(a.combo_count())
# print()
# print(a.permutation_count())
