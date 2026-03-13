keep = True

while keep:


# Menú inicio
    def startup():
        print('''
              --- Bienvenido ---
              Seleccione una opcion:
              1. Figura 2D
              2. Figura 3D
              3. Triángulo Rectángulo 
              4. Salir
              ''')
    startup()

    opcion = input('Ingrese una opcion: ')

# Menú Figuras 2D
    if opcion == '1':
        def twd():
            print(
                '''Seleccione una opcion:
                    1. Circulo 
                    2. Triángulo 
                    3. Trapecio
                    4. Rectángulo 
                    5. Volver
                    6. Salir
              ''')

# Menú Figuras 3D
    elif opcion == '2':
        def trd():
            print(
                '''Seleccione una opcion:
                    1. 
                    2.
                    3.
                    4.
                    5.
                    6.
              ''')

# Menú Triángulo Rectángulo 
    elif opcion == '3':
        def tr():
            print(
                '''Seleccione una opcion:
                    1.
                    2.
                    3.
                    4.
                    5.
                    6.
              ''')

# Cerrar
    elif opcion == '4':
        print('adios')
        keep = False

# Opción inválida 
    else:
        print('Opcion invalida, por favor intente de nuevo.')
        continue