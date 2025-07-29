class Empleado:
    def __init__(self, codigo, nombre, departamento, antiguedad):
        self.codigo = codigo
        self.nombre = nombre
        self.departamento = departamento
        self.antiguedad = antiguedad


class Evaluacion:
    def __init__(self, puntualidad, equipo, productividad, observacion):
        self.puntualidad = puntualidad
        self.equipo = equipo
        self.productividad = productividad
        self.promedio = (puntualidad + equipo + productividad) / 3
        self.observacion = observacion
        if self.promedio >= 7:
            self.estado = "Satisfactorio"
        else:
            self.estado = "Mejorar"

class Contacto:
    def __init__(self, telefono, correo):
        self.telefono = telefono
        self.correo = correo
