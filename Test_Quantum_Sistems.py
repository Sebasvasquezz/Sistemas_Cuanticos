import math
import Quantum_Sistems as qs
from scipy.constants import hbar
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
        self.assertAlmostEqual(prob, 0.666666666666666666666)

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

    def test_eigenvalues_and_probability_of_transition_to_eigenvectors(self):
        result = qs.eigenvalues_and_probability_of_transition_to_eigenvectors([complex(1, 0), complex(0, 0)],
                                                                           [[complex(0, 0), complex(hbar / 2, 0)],
                                                                            [complex(hbar / 2, 0), complex(0, 0)]])
        values = result[0]
        probabilities = result[1]
        self.assertAlmostEqual(values[0], 5.27285908823078e-35)
        self.assertAlmostEqual(values[0], -5.27285908823078e-35)
        self.assertAlmostEqual(probabilities[0], 0.5)
        self.assertAlmostEqual(probabilities[1], 0.5)

    def test_eigenvalues_and_probability_of_transition_to_eigenvectors2(self):
        result = qs.eigenvalues_and_probability_of_transition_to_eigenvectors([complex(1, 0), complex(1, 0)],
                                                                           [[complex(0, 0), complex(hbar / 2, 0)],
                                                                                    [complex(hbar / 2, 0), complex(0, 0)]])
        values = result[0]
        probabilities = result[1]
        self.assertAlmostEqual(values[0], 5.27285908823078e-35)
        self.assertAlmostEqual(values[0], -5.27285908823078e-35)
        self.assertAlmostEqual(probabilities[0], 1)
        self.assertAlmostEqual(probabilities[1], 0)

    def test_dinamic_sistem(self):
        estate = qs.dinamic_sistem([complex(-1, 1), complex(2, 3)],[[[complex(1, 2), complex(3, 4)],
                                                                        [complex(8, 4), complex(-2, 5)]],
                                                                        [[complex(1, 2), complex(3, 4)],
                                                                        [complex(8, 4), complex(-2, 5)]]])
        self.assertAlmostEqual(estate[0], -166-102j)
        self.assertAlmostEqual(estate[1], -114-79j)

    def test_dinamic_sistem2(self):
        estate = qs.dinamic_sistem([complex(-1, -1), complex(2, 3)],[[[complex(1, 2), complex(3, 4)],
                                                                        [complex(8, 4), complex(-2, 5)]],
                                                                        [[complex(1, 2), complex(3, 4)],
                                                                        [complex(8, 4), complex(-2, 5)]]])
        self.assertAlmostEqual(estate[0], -70-112j)
        self.assertAlmostEqual(estate[1], -10-7j)

if __name__ == '__main__':
    unittest.main()