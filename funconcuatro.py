#evaluar las bicicletas segun la ecuacion de negocio

def evaluar_bicicleta(promedioEstabilidad,promedioEficiencia,promedioParecido):
    evaluacion=0.4*promedioEficiencia+0.3*promedioParecido+0.3*promedioEstabilidad
    return evaluacion

