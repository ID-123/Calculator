keep = True

while keep:

    def startup():
        print('''
              --- Bienvenido ---
              Seleccione una opcion:
              1. 
              2.
              3.
              4.
              ''')
    startup()

    opcion = input('Ingrese una opcion: ')

    if opcion == '1':
        def twd():
            print(
                '''Seleccione una opcion:
                    1.
                    2.
                    3.
                    4.
                    5.
                    6.
              ''')

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

    elif opcion == '4':
        print('adios')
        keep = False

    else:
        print('Opcion invalida')