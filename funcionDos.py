#crear una lista de 20 notas

import random


def crear_lista_notas(cantidadNotas):


    notas=[]
    
    for _ in range(cantidadNotas):
        notas.append(random.randint(1,5))
    return notas






