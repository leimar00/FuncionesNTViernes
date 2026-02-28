#Crear una lista de 30 estudiantes


#crear una lista de 20 calificaciones de eficiencia
#crear una lista de 20 calificaciones de apariencia
#crear una lista de 20 calificaciones de estabilidad
#calcular el promedio de las notas
#evaluar la bicicleta ganadora

#como traer cosas de python?

from funcionUno import crear_lista_estudiantes
from funcionDos import crear_lista_notas
from funciontres import calcular_promedio_lista
from funconcuatro import evaluar_bicicleta

#equipo1
equipoUno=crear_lista_estudiantes(1)
notasEficienciaEquipoUno=crear_lista_notas(20)
notasParecidoEquipoUno=crear_lista_notas(20)
notasEstabilidadEquipoUno=crear_lista_notas(20)

promedioEficienciaUno=calcular_promedio_lista(notasEficienciaEquipoUno)
promedioParecidoUno=calcular_promedio_lista(notasParecidoEquipoUno)
promedioEstabilidadUno=calcular_promedio_lista(notasEstabilidadEquipoUno)


evaluacionEquipoUno=evaluar_bicicleta(promedioEstabilidadUno,promedioEficienciaUno,promedioParecidoUno)


print(f"el resultado global del equipo uno fue: {evaluacionEquipoUno}")

#equipo2


equipoDos=crear_lista_estudiantes(1)
notasEficienciaEquipoDos=crear_lista_notas(20)
notasParecidoEquipoDos=crear_lista_notas(20)
notasEstabilidadEquipoDos=crear_lista_notas(20)

promedioEficienciaDos=calcular_promedio_lista(notasEficienciaEquipoDos)
promedioParecidoDos=calcular_promedio_lista(notasParecidoEquipoDos)
promedioEstabilidadDos=calcular_promedio_lista(notasEstabilidadEquipoDos)

evaluacionEquipoDos=evaluar_bicicleta(promedioEstabilidadDos,promedioEficienciaDos,promedioParecidoDos)

print(f"el resultado global del equipo dos fue: {evaluacionEquipoDos}")