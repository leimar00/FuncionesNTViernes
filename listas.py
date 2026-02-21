#necesito un programa que almacene una lista de 200 personas
#[] -> simbolo de lista,plural y del mismo tipo
#indice(posicion espacio en la lista) osea numero consecutivo que empieza en 0
#se cargan fuera de los ciclos for

#{}-->simbolo de diccionario,singular y son diferentes
#en vez de indices usan clave(llave,propiedad o ket) y valor
#se carga dentro de los ciclos for para limpiarse cada vez que se carga un nuevo elemento

import random

notas=[]

for i in range(5):
    
    notaSimulada = random.randint(1,5)
    notas.append(notaSimulada)



#metodos para transformar, modificar o administrar listas
#append()-->agrega un elemento al final de la lista
#insert()-->agrega un elemento en una posicion especifica de la lista
#extend()-->agrega los elementos de una lista a otra lista
#remove()-->elimina un elemento de la lista
#pop()-->elimina un elemento de la lista y lo devuelve
#sort()-->ordena los elementos de la lista de menor a mayor
#sort(reverse=True)-->ordena los elementos de la lista de mayor a menor
#clear()-->elimina todos los elementos de la lista


notas.insert(0,80)
notas.remove(80) # Remove the element at index 1 (the value 1)
notas.pop(0)
notas.sort(reverse=True)
notas.clear()
print(notas)

