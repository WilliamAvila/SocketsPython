__author__ = 'william'


val = True


while val:
    print ("""
    1.Insertar Empleado
    2.Modificar Empleado
    3.Buscar Empleado
    4.Listar Empleados
    4.Salir """)
    try:
        val = int(input("Ingrese Numero"))
    except ValueError:
        print("That's not an int!")




