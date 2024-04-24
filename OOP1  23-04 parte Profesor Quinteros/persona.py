class Persona: 
    
    def __init__(self, nombre: str = "XXXX", apellido: str = "xxxx", du: int = 00000000): 
        self.__nombre__ = nombre
        self.__apellido__ = apellido
        self.__du__ = du #dni por defecto 000000000;

#Nota: una vez que insertamos un valor por defecto, todos los que esten a la derecha deben tener uno.
#Entonces, los campos obligatorios a la izq y opcionales a la derecha.

        
    def mostrar_datos(self):
        return f'Mis datos son nombre = {self.__nombre__}, apellido = {self.__apellido__}, du = {self.__du__}'

    def __str__(self):
        return f'Mis datos son nombre = {self.__nombre__}, apellido = {self.__apellido__}, du = {self.__du__}'