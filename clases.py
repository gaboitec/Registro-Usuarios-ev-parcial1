class Empleado:
    def __init__(self, codigo, nombre, departamento, antiguedad):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__departamento = departamento
        self.__antiguedad = antiguedad

    def get_codigo(self):
        return self.__codigo
    def get_nombre(self):
        return self.__nombre
    def get_departamento(self):
        return self.__departamento
    def get_antiguedad(self):
        return self.__antiguedad


class Evaluacion:
    def __init__(self, puntualidad, equipo, productividad, observacion):
        self.__puntualidad = puntualidad
        self.__equipo = equipo
        self.__productividad = productividad
        self.__promedio = (puntualidad + equipo + productividad) / 3
        self.__observacion = observacion
        if self.__promedio >= 7:
            self.__estado = "Satisfactorio"
        else:
            self.__estado = "Mejorar"

    def get_puntualidad(self):
        return self.__puntualidad
    def get_equipo(self):
        return self.__equipo
    def get_productividad(self):
        return self.__productividad
    def get_promedio(self):
        return self.__promedio
    def get_observacion(self):
        return self.__observacion
    def get_estado(self):
        return self.__estado

class Contacto:
    def __init__(self, telefono, correo):
        self.__telefono = telefono
        self.__correo = correo

    def get_telefono(self):
        return self.__telefono
    def get_correo(self):
        return self.__correo
