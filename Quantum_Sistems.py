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

if __name__ == '__main__':
    print(probability_pos([complex(2,-1),complex(0,2),complex(1,-1),complex(1,0),complex(0,-2),complex(2,0)],0))
    print(probability_of_transit([complex(2,-1), complex(0, 2)],
                                 [complex(1,-1), complex(1, 0)]))


