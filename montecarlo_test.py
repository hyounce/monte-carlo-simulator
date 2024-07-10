from montecarlo.montecarlo import Die
import unittest
import numpy as np

class MontecarloTestSuite(unittest.TestCase):
    
    def test_die_init_array(self):
        # Test faces is a numpy array
        die = Die(np.array([1,2,3,4,5,6]))
        message = "Faces must be of type Numpy array."
        self.assertIsInstance(die.faces, np.ndarray, message)

    def test_die_init_type_string(self):
        # Test faces has string or int values
        die = Die(np.array['a','b','c'])
        message = "Values of faces must be string."
        self.assertEquals(die.faces.kind, 'U', message)

    
    def test_die_set_weight(self):
        pass

    def test_die_roll_die(self):
        pass

    def test_die_current_state(self):
        pass


if __name__ == '__main__':
    unittest.main(verbosity=3)