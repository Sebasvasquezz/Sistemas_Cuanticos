import Lib_Vect_Mat_Complex as lvmc
import math
import numpy as np
# Importar la constante de Planck reducida desde el módulo scipy.constants
from scipy.constants import hbar
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
    result = (abs(lvmc.internal_product(vector_a_normalize,vector_b_normalize)))**2
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

def eigenvalues_and_probability_of_transition_to_eigenvectors(estate, observable):
    eigenvalues = lvmc.eigenvalues_and_eigenvectors(observable)[0]
    eigenvectors = lvmc.eigenvalues_and_eigenvectors(observable)[1]
    probabilities = []
    for i in eigenvectors:
        probabilities.append(probability_of_transit(estate, i))
    return eigenvalues,probabilities

def dinamic_sistem(estate,matrix):
    final_estate = estate
    for i in matrix:
        final_estate = lvmc.matrix_action_vector(i,final_estate)
    return final_estate
    
if __name__ == '__main__':
    print(probability_pos([complex(2,-1),complex(0,2),complex(1,-1),complex(1,0),complex(0,-2),complex(2,0)],0))

    print(probability_of_transit([complex(1, 0), complex(0, 0)],
                                 [complex(math.sqrt(2)/2,0), complex(math.sqrt(2)/2,0)]))

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

    result = eigenvalues_and_probability_of_transition_to_eigenvectors([complex(1, 0), complex(0, 0)],[[complex(0, 0), complex(1/2, 0)],
                                                                                                                        [complex(1/2, 0), complex(0, 0)]])
    print("Valores propios:",result[0],"Probalididades:",result[1])

    print(dinamic_sistem([complex(-1, -1), complex(2, 3)],[[[complex(1, 2), complex(3, 4)],
                                                                        [complex(8, 4), complex(-2, 5)]],
                                                                        [[complex(1, 2), complex(3, 4)],
                                                                        [complex(8, 4), complex(-2, 5)]]]))

    print("Problema 4.3.1")
    print("Los posibles estados despues de haber realizado una medición son:")
    print(lvmc.eigenvalues_and_eigenvectors([[complex(0, 0), complex(hbar/2, 0)],
                                            [complex(hbar/2, 0), complex(0, 0)]])[1])

    print("----------------------------------------------------------------------------------")
    print("Problema 4.3.2")
    result = eigenvalues_and_probability_of_transition_to_eigenvectors([complex(1, 0), complex(0, 0)],
                                                                    [[complex(0, 0), complex(hbar / 2, 0)],
                                                                              [complex(hbar / 2, 0), complex(0, 0)]])
    landa1 = result[0][0]
    landa2 = result[0][1]
    p1 = result[1][0]
    p2 = result[1][1]
    print("p1 =", p1)
    print("p2 =", p2)
    print("p1 * landa1 + p2 * landa2 =", round((p1 * landa1 + p2 * landa2).real))

    print("----------------------------------------------------------------------------------")
    print("Problema 4.4.1")
    u1 = [[complex(0, 0), complex(1, 0)],
          [complex(1, 0), complex(0, 0)]]
    u2 = [[complex(math.sqrt(2)/2, 0), complex(math.sqrt(2)/2, 0)],
          [complex(math.sqrt(2)/2, 0), complex(-math.sqrt(2)/2, 0)]]
    print("u1 * u1 =", lvmc.mult_matrix(u1, lvmc.adjoint_matrix(u1)))
    print("u2 * u2 =", lvmc.mult_matrix(u2, lvmc.adjoint_matrix(u2)))
    u3 = lvmc.mult_matrix(u1, u2)
    print("u3 = u1 * u2 =", u3)
    print("u3 * u3 =", lvmc.mult_matrix(u3, lvmc.adjoint_matrix(u3)))

    print("----------------------------------------------------------------------------------")
    print("Problema 4.4.2")
    estate = [complex(1, 0), complex(0, 0), complex(0, 0), complex(0, 0)]
    u = [[complex(0, 0), complex(1/math.sqrt(2), 0), complex(1/math.sqrt(2), 0), complex(0, 0)],
         [complex(0, 1/math.sqrt(2)), complex(0, 0), complex(0, 0), complex(1/math.sqrt(2), 0)],
         [complex(1/math.sqrt(2), 0), complex(0, 0), complex(0, 0), complex(0, 1/math.sqrt(2))],
         [complex(0, 0), complex(1/math.sqrt(2), 0), complex(-1/math.sqrt(2), 0), complex(0, 0)]]
    for i in range(3):
        estate = lvmc.matrix_action_vector(u,estate)
    print("El estato despues de tres pasos es:")
    print(estate)
    print("La probabilidad de que la bola cuantica este en el punto 3 es :",abs(estate[3])**2)