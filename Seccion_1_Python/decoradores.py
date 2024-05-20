"""
Decoradores

Pregunta: Escriba un decorador en Python llamado tiempo_ejecucion que calcule el tiempo que tarda en ejecutarse una función. Aplique este decorador a una función de ejemplo.
"""
import time


def tiempo_ejecucion(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        print(f"Tiempo de ejecucion de {function.__name__}: {
              end - start:.2f} segundos")
        return result

    return wrapper


@tiempo_ejecucion
def funcion_ejemplo(num):
    total = 0
    for i in range(num):
        total += 1
    return total


result = funcion_ejemplo(10000000)
print(result)
