# Simulación de lo Clásico a lo Cuántico.

Esta librería de Python brinda funciones para llevar a cabo diferentes calculos de probabilidades de sistemas cuánticos. Adicionalmente se incluye una libreria de operaciones con numeros complejos, la cual permite manejar los numeros complejos y asi implementar las funciones de probabilidad.

## Requisitos
Antes de comenzar con la ejecución del material incluido en este repositorio, es necesario asegurarse de que se tiene instalado Python en su computador, debido a que este es el lenguaje en el cual esta desarrollado este repositorio. 

En caso de no tenerlo lleve a cabo los siguientes pasos:
1. Dirijase a la página https://www.python.org/downloads/
2. De click en la opción de descarga
   ![image](https://github.com/alexandrac1420/CNYT/assets/138069735/03d02dfb-a346-4bc8-8e9c-066816e2f80e)

4. Ejecute el programa que se descarga automáticamente.
4. Complete la instalacion.

## Operaciones Incluidas

La librería consta de las siguientes operaciones para vectores y matrices complejos, los números complejos parte de cada vector o matriz se representan por medio del tipo "complex" de la librería numpy de python, donde la primera componente es la parte real y la segunda, la imaginaria:

1. **Probabilidad de estar en una posisición dada dentro de un vector:** `probability_pos(vector,position)`
2. **Normalizar un vector:** `normalize_vector(vector)`
3. **Probabilidad de transitar de un vector a otro:** `probability_of_transit(vector_a,vector_b)`
4. **Amplitud de transito de un vector a otro:** `amplitude_of_transit(vector_a,vector_b)`
5. **Media de los valores obtenidos:** `media_obervable_ket(matrix,vector)`
6. **Operador delta:** `delta_operator(matrix,vector)`
7. **Varianza de los valores obtenidos:** `var_observable_ket(matrix,vector)`
8. **Valores propios y la probabilidad de transitar a alguno de sus vectores propios:** `eigenvalues_and_probability_of_transition_to_eigenvectors(estate, observable)`
9. **Calculo del estado final a partir de un estado inicial y una serie de matrices dada como una lista de matrices:** `dinamic_sistem(estate,matrix):`
## Uso
Para hacer uso del material deben llevar a cabo los siguientes pasos:
1. Abra la carpeta en donde desea guardar la librería.
2. De click derecho sobre dicha carpeta y seleccione la opción "Git Bash".
3. Clone el repositorio utilizando el comando "git clone" seguido del link brindado en la pagina principal del repositorio al presionar el boton verde "<>Code". 
2. Abre el proyecto en PyCharm.
3. Importa el módulo de la librería en tus scripts.
4. Utiliza las funciones de para realizar simulaciones de experimentos cuánticos.

## Ejemplo de Uso

```python
import Quantum_Sistems as qs

# Probabilidad de estar en una posicion dada dentro de un vector
vector = [complex(2,-1),complex(0,2),complex(1,-1),complex(1,0),complex(0,-2),complex(2,0)]
posicion = 3
result = qs.probability_pos(vector, posicion)
print("Probabilidad :",result)


```
## Autor
**Ing. Juan Sebastian Vasquez Vega**