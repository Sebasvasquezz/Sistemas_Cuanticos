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

    def test_amplitude_of_transit(self):
        ampli = qs.amplitude_of_transit([complex(0, 1), complex(1, 0)],
                                        [complex(1, 0), complex(0, -1)])
        self.assertAlmostEqual(ampli, complex(0,-1))

    def test_amplitude_of_transit2(self):
        ampli = qs.amplitude_of_transit([complex(math.sqrt(2) / 2, 0), complex(0, -math.sqrt(2) / 2)],
                                        [complex(0, math.sqrt(2) / 2), complex(-math.sqrt(2) / 2, 0)])
        self.assertAlmostEqual(ampli, complex(0,0))

    def test_media_obervable_ket(self):
        media = qs.media_obervable_ket([[complex(3, 0), complex(1, 2)],
                                        [complex(1, -2), complex(-1, 0)]],
                                        [complex(math.sqrt(2)/2,0),complex(-math.sqrt(2)/2,0)])
        self.assertAlmostEqual(media, 0)

    def test_media_obervable_ket2(self):
        media = qs.media_obervable_ket([[complex(1, 0), complex(0, -1)],
                                       [complex(0, 1), complex(2, 0)]],
                                       [complex(math.sqrt(2) / 2, 0), complex(0, math.sqrt(2) / 2)])
        self.assertAlmostEqual(media, 2.5)

    def test_var_observable_ket(self):
        var = qs.var_observable_ket([[complex(3, 0), complex(1, 2)],
                                     [complex(1, -2), complex(-1, 0)]],
                                     [complex(math.sqrt(2)/2,0),complex(-math.sqrt(2)/2,0)])
        self.assertAlmostEqual(var, 8)

    def test_var_observable_ket2(self):
        var = qs.var_observable_ket([[complex(1, 0), complex(0, -1)],
                                    [complex(0, 1), complex(2, 0)]],
                                    [complex(math.sqrt(2) / 2, 0), complex(0, math.sqrt(2) / 2)])
        self.assertAlmostEqual(var, 0.25)
if __name__ == '__main__':
    unittest.main()