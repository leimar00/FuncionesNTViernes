def crearListaEstudiantes(cantidadEstudiantes):
    
    estudiantes=[]
    for i in range(cantidadEstudiantes):
        estudiante={}
        estudiante["ID"]=input("ID: ")
        estudiante["Nombre"]=input("Nombre: ")
        estudiante["Documento"]=input("Documento: ")
        estudiante["telefono"]=input("Telefono: ")
        estudiante["promedio"]=input("Promedio: ")
        estudiante["semestre"]=input("Semestre: ")
        estudiante["esBecado"]=input("tiene beca?: ")
        estudiantes.append(estudiante)
    return estudiantes

#invocando la funcion
resultado=crearListaEstudiantes(2)
print(resultado)