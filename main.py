import clases
empleados = {}

def buscar_empleado(codigo):
    if codigo in empleados:
        empleado = empleados[codigo]

        print(f"Codigo: {codigo}, Nombre: {empleado['nombre']}, Departamento: {empleado['departamento']}, Antiguedad: {empleado['antiguedad']}")
        for clave, valor in empleado['evaluacion'].items():
            print(f"  {clave}: {valor}")
        for clave, valor in empleado['contacto'].items():
            print(f"  {clave.capitalize()}: {valor}")
    else:
        print("Empleado no encontrado.")

def satisfactorios():
    for codigo, datos in empleados.items():
        if datos['evaluacion']['estado'] == "Satisfactorio":
            print(f"Codigo: {codigo}, Nombre: {datos['nombre']}, Promedio: {datos['evaluacion']['promedio']}")


while True:
    print("\n## MENU EMPLEADOS ##")
    print("1. Registrar nuevo empleado")
    print("2. Mostrar todos empleados")
    print("3. Buscar empleado")
    print("4. Mostrar empleados satisfactorios")
    print("5. Empleado con mejor promedio")
    print("0. Salir")
    opcion = input("Eliga una opcion: ")

    if opcion == "1":
        cantidad = int(input("Cuantos empleados desea registrar?: "))
        for i in range(cantidad):
            print(f"\n## REGISTRO DE EMPLEADO {i + 1} ##")
            empleado = clases.Empleado(
                input("Ingrese el codigo del empleado: "),
                input("Ingrese el nombre del empleado: "),
                input("Ingrese el departamento del empleado: "),
                input("Ingrese la antiguedad del empleado: "))

            print("INGRESANDO EVALUACION DEL EMPLEADO")
            evaluacion = clases.Evaluacion(
                int(input("Ingrese la evaluacion de puntualidad(0-10): ")),
                int(input("Ingrese la evaluacion de trabajo en equipo(0-10): ")),
                int(input("Ingrese la evaluacion de productividad(0-10): ")),
                input("Ingrese las observaciones: "))

            contacto = clases.Contacto(
                input("Ingrese el telefono de contacto: "),
                input("Ingrese el correo de contacto: "))

            empleados[empleado.get_codigo()] = {
                "nombre": empleado.get_nombre(),
                "departamento": empleado.get_departamento(),
                "antiguedad": empleado.get_antiguedad(),
                "evaluacion": {
                    "puntualidad": evaluacion.get_puntualidad(),
                    "equipo": evaluacion.get_equipo(),
                    "productividad": evaluacion.get_productividad(),
                    "promedio": evaluacion.get_promedio(),
                    "observacion": evaluacion.get_observacion(),
                    "estado": evaluacion.get_estado()
                },
                "contacto": {
                    "telefono": contacto.get_telefono(),
                    "correo": contacto.get_correo()
                }
        }

    elif opcion == "2":
        for codigo, datos in empleados.items():
            print(f"Codigo: {codigo}, Nombre: {datos['nombre']}, Departamento: {datos['departamento']}, Antiguedad: {datos['antiguedad']}")
            for clave, valor in datos['evaluacion'].items():
                print("     Evaluacion:")
                print(f"        {clave}: {valor}")
            for clave, valor in datos['contacto'].items():
                print("     Contacto:")
                print(f"        {clave}: {valor}")

    elif opcion == "3":
        print("## BUSCAR EMPLEADO ##")
        codigo = input("Ingrese el codigo del empleado a buscar: ")
        buscar_empleado(codigo)

    elif opcion == "4":
        print("## EMPLEADOS SATISFACTORIOS ##")
        satisfactorios()
    elif opcion == "5":
        print("mejor promedio")
    elif opcion == "0":
        print("Saliendo del programa...")
        break
    else:
        print("\nIngrese una opcion valida")
