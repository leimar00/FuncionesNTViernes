#crear una funcion que permita generar 20 mediciones de una represa
#(0-800) y calcular el promedio de esas medidas
#debemos ser capaces de indicar cual es el nivel de operacion de la represa

def calcular_nivel_represa(promedioNivel):
    
    if promedioNivel>0 and promedioNivel<=250:
        return("operando a bajo nivel, se recomienda apagar algunas turbinas")
        
    elif promedioNivel>250 and promedioNivel<=400:
        return("operando a normalidad, se recomienda mantener el nivel de operacion")
    
    elif promedioNivel>400:
        return("operando sobre nivel, se recomienda abrir compuertas para bajar el nivel de agua")
    
    else:
        return("medicion promedio ingresada no es valida")
    

