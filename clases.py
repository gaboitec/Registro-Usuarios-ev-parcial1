class Empleado:
    def __init__(self, codigo, nombre, departamento, antiguedad):
        self.codigo = codigo
        self.nombre = nombre
        self.departamento = departamento
        self.antiguedad = antiguedad


class Evaluacion:
    def __init__(self, puntualidad, equipo, productividad, observacion, estado):
        self.puntualidad = puntualidad
        self.equipo = equipo
        self.productividad = productividad
        self.observacion = observacion
        self.estado = estado

class Contacto:
    def __init__(self, telefono, correo):
        self.telefono = telefono
        self.correo = correo
