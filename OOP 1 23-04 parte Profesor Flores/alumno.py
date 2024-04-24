class Alumno:

    def __init__(self, el_nombre_del_alumno):
        self.__nombre__ = el_nombre_del_alumno
        self.__inasistencias__ = 0
        self.__dieta__ = ""
        self.__mentor__ = None
    
    def falta(self):
        self.__inasistencias__ += 1

    def esta_libre(self):
        if self.__inasistencias__ > 5:
            return "Esta libre."
        else: 
            return "OK"


    def elegir_dieta(self, la_dieta):
        self.__dieta__ = la_dieta

    def es_vegano(self):
        self.__dieta__ = "vegano"

    def mentoria(self, profesor):
        self.__mentor__ = profesor