import Lib_Vect_Mat_Complex as lvmc
import math
import numpy as np
def probability_pos(vector,position):
    if position >= 0 and position <= len(vector):
        modulo = lvmc.norm_vector(vector)
        modulo_pos = abs((vector[position]))
        result = (modulo_pos**2)/(modulo**2)
        return result
    return "No existe la posicion dada en el vector dado"


def normalize_vector(vector):
    magnitude = math.sqrt(sum(abs(v) ** 2 for v in vector))
    if magnitude == 0:
        return vector
    normalized_vector = [v / magnitude for v in vector]
    return normalized_vector

def probability_of_transit(vector_a,vector_b):
    vector_a_normalize = normalize_vector(vector_a)
    vector_b_normalize = normalize_vector(vector_b)
    result = abs(lvmc.internal_product(vector_a_normalize,vector_b_normalize))
    return result
def amplitude_of_transit(vector_a,vector_b):
    vector_a_normalize = normalize_vector(vector_a)
    vector_b_normalize = normalize_vector(vector_b)
    result = lvmc.internal_product(vector_a_normalize,vector_b_normalize)
    return result
def media_obervable_ket(matrix,vector):
    if lvmc.hermitian_matrix(matrix):
        media = lvmc.internal_product(lvmc.matrix_action_vector(matrix,vector),vector).real
        return media
    return "El observable no es una matrix hermitiana"
def delta_operator(matrix,vector):
    filas = len(matrix)
    delta = matrix - lvmc.mult_scalar_matrix_complex(media_obervable_ket(matrix,vector),np.eye(filas))
    return delta
def var_observable_ket(matrix,vector):
    if lvmc.hermitian_matrix(matrix):
        delta = delta_operator(matrix,vector)
        varianza = media_obervable_ket(lvmc.mult_matrix(delta,delta),vector)
        return varianza
    return "El observable no es una matrix hermitiana"

if __name__ == '__main__':
    print(probability_pos([complex(2,-1),complex(0,2),complex(1,-1),complex(1,0),complex(0,-2),complex(2,0)],0))

    print(probability_of_transit([complex(2,-1), complex(0, 2)],
                                 [complex(1,-1), complex(1, 0)]))

    print(amplitude_of_transit([complex(0, 1), complex(1, 0)],
                                [complex(1, 0), complex(0, -1)]))

    print(media_obervable_ket([[complex(3, 0), complex(1, 2)],
                               [complex(1, -2), complex(-1, 0)]],
                              [complex(math.sqrt(2)/2,0),complex(-math.sqrt(2)/2,0)]))

    print(media_obervable_ket([[complex(1, 0), complex(0, -1)],
                               [complex(0, 1), complex(2, 0)]],
                              [complex(math.sqrt(2) / 2, 0), complex(0, math.sqrt(2) / 2)]))

    print(var_observable_ket([[complex(3, 0), complex(1, 2)],
                               [complex(1, -2), complex(-1, 0)]],
                              [complex(math.sqrt(2)/2,0),complex(-math.sqrt(2)/2,0)]))



