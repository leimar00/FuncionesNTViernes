def crear_lista_estudiantes(cantidadEstudiantes):
    estudiantes=[]
    for i in range(cantidadEstudiantes):
        estudiante={}
        estudiante["id"]=input("id: ")
        estudiante["nombres"]=input("nombres: ")
        estudiante["documento"]=input("documento: ")
        estudiante["correo"]=input("correo: ")
        estudiante["telefono"]=input("telefono: ")
        estudiante["promedio"]=input("promedio: ")
        estudiante["semestre"]=input("semestre: ")
        estudiante["esBecado"]=input("Tienes Beca?: ")
        estudiantes.append(estudiante)
    return estudiantes


#Invocando la funcion
#resultado=crear_lista_estudiantes(2000)
#print(resultado)
