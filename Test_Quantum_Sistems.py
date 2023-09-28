import math
import Quantum_Sistems as qs

import unittest

class Test_operations_vector_matriz_complex(unittest.TestCase):

    def test_provability_pos(self):
        prob = qs.probability_pos([complex(2,-1),complex(0,2),complex(1,-1),complex(1,0),complex(0,-2),complex(2,0)],3)
        self.assertAlmostEqual(prob, 0.05)

    def test_provability_pos2(self):
        prob = qs.probability_pos([complex(2,-1),complex(0,2),complex(1,-1),complex(1,0),complex(0,-2),complex(2,0)],0)
        self.assertAlmostEqual(prob, 0.25)

    def test_provability_transit(self):
        prob = qs.probability_of_transit([complex(math.sqrt(2)/2,0), complex(0, -math.sqrt(2)/2)],
                                         [complex(0,math.sqrt(2)/2), complex(-math.sqrt(2)/2, 0)])
        self.assertAlmostEqual(prob, 0.0)

    def test_provability_transit2(self):
        prob = qs.probability_of_transit([complex(2,-1), complex(0, 2)],
                                         [complex(1,-1), complex(1,0)])
        self.assertAlmostEqual(prob, 0.816496580927726)

if __name__ == '__main__':
    unittest.main()