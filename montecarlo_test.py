from montecarlo.montecarlo import Die, Game, Analyzer
import unittest
import numpy as np
import pandas as pd

class MontecarloTestSuite(unittest.TestCase):
    
    def test_die_init_array(self):

        die = Die(np.array([1,2,3,4,5,6]))
        message = "Faces must be of type Numpy array."
        self.assertIsInstance(die.faces, np.ndarray, message)

    def test_die_unique_faces(self):

        die = Die(np.array([1,2,3,4,5,6]))
        die_unique = np.unique(die.faces)

        expected = len(die.faces)
        actual = len(die_unique)
        
        message = "Faces of the die must be unique."
        self.assertEqual(expected, actual, message)

    def test_die_set_weight(self):
        
        die = Die(np.array([1,2,3,4,5,6]))
        die.set_weight(3, 10)

        expected = [1,1,10,1,1,1]
        actual = die.weights
        message = "Die weight was not set correctly."

        self.assertEqual(expected, actual, message)

    def test_die_roll_die(self):

        die = Die(np.array([1,2,3,4,5,6]))
        rolls = die.roll_die(5)

        actual = len(rolls)
        expected = 5
        message = "Number of results does not match number of rolls."

        self.assertEqual(actual, expected, message)


    def test_die_current_state(self):
        
        die = Die(np.array([1,2,3,4,5,6]))
        size = len(die.weights)
        state_df = die.current_state()

        message = "Size of DataFrame does not match number of weights."
        self.assertEqual(size, state_df.size, message)
    
    def test_game_init(self):
        
        die1 = Die(np.array([1,2,3,4,5,6]))
        die2 = Die(np.array([1,2,3,4,5,6]))
        game = Game([die1, die2])

        message = "Dice not a list of Die objects."
        self.assertIsInstance(game.dice[0], Die, message)


    def test_game_play(self):
        
        die1 = Die(np.array([1,2,3,4,5,6]))
        die2 = Die(np.array([1,2,3,4,5,6]))
        game = Game([die1, die2])
        game.play(4)

        expected = 8
        actual = game.play_df.size
        message = "Size of the play data frame does not match the number of dice and rolls."
        self.assertEqual(expected, actual, message)

    def test_game_recent_results(self):
        
        die1 = Die(np.array([1,2,3,4,5,6]))
        die2 = Die(np.array([1,2,3,4,5,6]))
        game = Game([die1, die2])
        game.play(4)

        game.recent_results(wide=False)
        message = "Play data frame does not have multi index."
        self.assertIsInstance(game.play_df.index, pd.MultiIndex)

    def test_analyzer_init(self):
        
        die1 = Die(np.array([1,2,3,4,5,6]))
        game = Game([die1])
        analyzer = Analyzer(game)

        message = "Argument game must be Game object."
        self.assertIsInstance(analyzer.game, Game, message)

    def test_analyzer_jackpot(self):
        
        results = {'1': [1,2,3,4],
                   '2': [1,1,1,1],
                   '3': [3,3,3,3]}
        results_df = pd.DataFrame(results)

        die1 = Die(np.array([1,2,3,4,5,6]))
        game = Game([die1])
        analyzer = Analyzer(game)
        analyzer.game.play_df = results_df

        expected = 2
        actual = analyzer.jackpot()
        message = "Incorrect number of jackpots."
        self.assertEqual(expected, actual, message)


    def test_analyzer_face_counts(self):

        results = {'1': [1,2,3,4],
                   '2': [1,2,2,6],
                   '3': [3,4,5,5]}
        results_df = pd.DataFrame(results)

        die1 = Die(np.array([1,2,3,4,5,6]))
        game = Game([die1])
        analyzer = Analyzer(game)
        analyzer.game.play_df = results_df

        expected = [0, 1, 1, 0, 1, 0]
        actual = analyzer.face_counts_per_roll().iloc[2].tolist()
        message = "Incorrect counts for faces per roll."
        self.assertEqual(expected, actual, message)

    def test_analyzer_combo_count(self):
        
        results = {'1': [1,2,1,2],
                   '2': [1,2,2,1],
                   '3': [2,2,1,1]}
        results_df = pd.DataFrame(results)

        die1 = Die(np.array([1,2,3,4,5,6]))
        game = Game([die1])
        analyzer = Analyzer(game)
        analyzer.game.play_df = results_df

        expected = 3
        actual = analyzer.combo_count().loc[(1, 1, 2)][0]
        message = "Incorrect number of combinations."
        self.assertEqual(expected, actual, message)

    def test_analyzer_perm_count(self):
        results = {'1': [1,2,1,2],
                   '2': [1,2,2,1],
                   '3': [2,2,1,1]}
        results_df = pd.DataFrame(results)

        die1 = Die(np.array([1,2,3,4,5,6]))
        game = Game([die1])
        analyzer = Analyzer(game)
        analyzer.game.play_df = results_df

        expected = 1
        actual = analyzer.permutation_count().loc[(1, 1, 2)]
        message = "Incorrect number of permutations."
        self.assertEqual(expected, actual, message)
        


if __name__ == '__main__':
    unittest.main(verbosity=3)