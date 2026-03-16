keep = True
pi = 3.14159


while keep:


# Menú inicio

    def startup():
        print('''
                 --- Bienvenido ---
              
              --- Seleccione una opcion:
              
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
                '''
                --- Seleccione una opcion:
                    
                    1. Circulo 
                    2. Triángulo 
                    3. Trapecio
                    4. Rectángulo 
                    5. Volver
                    6. Salir
              ''')
            
        twd()
            
        opcion_twd = input('Ingrese una opcion: ')

    # Menu Circulo
        if opcion_twd == '1':
            
            def circle():
                print('''
                    --- Seleccione una opcion:
                        
                        1. Área
                        2. Perímetro 
                        3. Diámetro
                        4. Volver
                        5. Salir
                ''')
            
            circle()

            cir = input('Ingrese una opción: ')

            if cir == '1':
                
                r = float(input('Ingrese el radio (en número): '))

                a_cir = pi * r**2

                print('El área del círculo es: ', round(a_cir, 3))
            
            elif cir == '2':
                
                r = float(input('Ingrese el radio (en número): '))

                p_cir = 2 * pi * r 
                
                print('El perímetro del círculo es: ', round(p_cir, 3))
            
            elif cir == '3':

                r = float(input('Ingrese el radio (en número): '))
                
                d_cir = 2 * r

                print('El diámetro del círculo es: ', round(d_cir, 3))

            elif cir == '4':
                continue 

            elif cir == '5':
                print('Adiós.')
                keep = False
        
            else:
                print('Opcion invalida, por favor intente de nuevo.')
                continue

    # Menu Triangulo
        elif opcion_twd == '2':
            
            def triangle():
                print('''
                    --- Seleccione una opcion:
                        
                        1. Área
                        2. Perímetro 
                        3. Ángulo
                        4. Volver
                        5. Salir
                ''')
            
            triangle()

            trg = input('Ingrese una opción: ')

            if trg == '1':
                
                b = float(input('Ingrese valor de la base (en número): '))
                h = float(input('Ingrese valor de la altura (en número): '))

                a_tri = (b * h) / 2

                print('El área del triángulo es: ', round(a_tri, 3))
            
            elif trg == '2':
                
                a = float(input('Ingrese el valor del primer lado (en número): '))
                b = float(input('Ingrese el valor del segundo lado (en número): '))
                c = float(input('Ingrese el valor del tercer lado (en número): '))

                p_tri = a + b + c
                
                print('El perímetro del triángulo es: ', round(p_tri, 3))
            
            elif trg == '3':

                ang_a = float(input('Ingrese el valor del primer ángulo (en número): '))
                ang_b = float(input('Ingrese el valor del segundo ángulo (en número): '))
                
                ang_tri = 180 - (ang_a + ang_b)

                print('El ángulo restante es igual a: ', round(ang_tri, 3))

            elif trg == '4':
                continue 

            elif trg == '5':
                print('Adiós.')
                keep = False
        
            else:
                print('Opcion invalida, por favor intente de nuevo.')
                continue

    # Menu Trapecio
        elif opcion_twd == '3':
            
            def circle():
                print('''
                    --- Seleccione una opcion:
                        
                        1. Área
                        2. Perímetro 
                        3. Diámetro
                        4. Volver
                        5. Salir
                ''')
            
            circle()

            cir = input('Ingrese una opción: ')

            if cir == '1':
                
                r = float(input('Ingrese el radio (en número): '))

                a_cir = pi * r**2

                print('El área del círculo es: ', round(a_cir, 3))
            
            elif cir == '2':
                
                r = float(input('Ingrese el radio (en número): '))

                p_cir = 2 * pi * r 
                
                print('El perímetro del círculo es: ', round(p_cir, 3))
            
            elif cir == '3':

                r = float(input('Ingrese el radio (en número): '))
                
                d_cir = 2 * r

                print('El diámetro del círculo es: ', round(d_cir, 3))

            elif cir == '4':
                continue 

            elif cir == '5':
                print('Adiós.')
                keep = False
        
            else:
                print('Opcion invalida, por favor intente de nuevo.')
                continue

    # Menu Rectangulo
        elif opcion_twd == '4':
            
            def circle():
                print('''
                    --- Seleccione una opcion:
                        
                        1. Área
                        2. Perímetro 
                        3. Diámetro
                        4. Volver
                        5. Salir
                ''')
            
            circle()

            cir = input('Ingrese una opción: ')

            if cir == '1':
                
                r = float(input('Ingrese el radio (en número): '))

                a_cir = pi * r**2

                print('El área del círculo es: ', round(a_cir, 3))
            
            elif cir == '2':
                
                r = float(input('Ingrese el radio (en número): '))

                p_cir = 2 * pi * r 
                
                print('El perímetro del círculo es: ', round(p_cir, 3))
            
            elif cir == '3':

                r = float(input('Ingrese el radio (en número): '))
                
                d_cir = 2 * r

                print('El diámetro del círculo es: ', round(d_cir, 3))

            elif cir == '4':
                continue 

            elif cir == '5':
                print('Adiós.')
                keep = False
        
            else:
                print('Opcion invalida, por favor intente de nuevo.')
                continue

        elif opcion_twd == '5':
            continue 

        elif opcion_twd == '6':
            print('Adiós.')
            keep = False
    
        else:
            print('Opcion invalida, por favor intente de nuevo.')
            continue

# Menú Figuras 3D

    elif opcion == '2':
        def trd():
            print(
                '''
                --- Seleccione una opcion:
                    1. Pirámide 
                    2. Cilindro
                    3. Cono
                    4. Prisma
                    5. Volver
                    6. Salir
              ''')
            
        trd()

        opcion_trd = input('Ingrese una opción: ')

    # Menu Piramide
        if opcion_trd == '1':
                
            def prmd():
                print('''
                    --- Seleccione una opcion:

                        1. Volumen
                        2. Área
                        3. Volver
                        4. Salir
                    ''')
            
            opcion_prmd = input('Ingrese una opción: ')

            if opcion_prmd == '1':
                print()
            
            elif opcion_prmd == '2':
                print()
            
            elif opcion_prmd == '3':
                print()

            elif opcion_prmd == '4':
                print('Adiós.')
                keep = False

            else:
                print('Opcion invalida, por favor intente de nuevo.')
                continue

    # Menu Cilindro
        elif opcion_trd == '2':
            
            def prmd():
                print('''
                    --- Seleccione una opcion:

                        1. Volumen
                        2. Área
                        3. Volver
                        4. Salir
                    ''')
            
            opcion_prmd = input('Ingrese una opción: ')

            if opcion_prmd == '1':
                print()
            
            elif opcion_prmd == '2':
                print()
            
            elif opcion_prmd == '3':
                print()

            elif opcion_prmd == '4':
                print('Adiós.')
                keep = False

            else:
                print('Opcion invalida, por favor intente de nuevo.')
                continue

    # Menu Cono   
        elif opcion_trd == '3':

            def prmd():
                print('''
                    --- Seleccione una opcion:

                        1. Volumen
                        2. Área
                        3. Volver
                        4. Salir
                    ''')
            
            opcion_prmd = input('Ingrese una opción: ')

            if opcion_prmd == '1':
                print()
            
            elif opcion_prmd == '2':
                print()
            
            elif opcion_prmd == '3':
                print()

            elif opcion_prmd == '4':
                print('Adiós.')
                keep = False

            else:
                print('Opcion invalida, por favor intente de nuevo.')
                continue

    # Menu Prisma
        elif opcion_trd == '4':
            def prmd():
                print('''
                    --- Seleccione una opcion:

                        1. Volumen
                        2. Área
                        3. Volver
                        4. Salir
                    ''')
            
            opcion_prmd = input('Ingrese una opción: ')

            if opcion_prmd == '1':
                print()
            
            elif opcion_prmd == '2':
                print()
            
            elif opcion_prmd == '3':
                print()

            elif opcion_prmd == '4':
                print('Adiós.')
                keep = False

            else:
                print('Opcion invalida, por favor intente de nuevo.')
                continue


        elif opcion_trd == '5':
            continue 

        elif opcion_trd == '6':
            print('Adiós.')
            keep = False
    
        else:
            print('Opcion invalida, por favor intente de nuevo.')
            continue

        

# Menú Triángulo Rectángulo 

    elif opcion == '3':
        def tr():
            print(
                '''
                --- Seleccione una opcion:
                    1. Hipotenusa 
                    2. Área 
                    3. Volver
                    4. Salir
              ''')
        
        tr()
        
        opcion_tr = input('Ingrese una opción: ')

        # Hipotenusa
        if opcion_tr == '1':
            a = int(input('Ingrese el valor del primer cateto (en número): '))
            b = int(input('Ingrese el valor del segundo cateto (en número): '))

            c = ((a**2 + b**2)**(1/2))

            print('El valor de la Hipotenusa es: ', c)

        # Área
        elif opcion_tr == '2':
            b = int(input('Ingrese el valor de la base (en número): '))
            h = int(input('Ingrese el valor de la altura (en número): '))

            a_tri_rect = (b * h) / 2

            print('El valor de la Hipotenusa es: ', a_tri_rect)

        elif opcion_tr == '3':
            continue

        elif opcion_tr == '4':
            print('Adiós.')
            keep = False
        
        else:
            print('Opcion invalida, por favor intente de nuevo.')
            continue

# Cerrar

    elif opcion == '4':
        print('Adiós.')
        keep = False

# Opción inválida 

    else:
        print('Opcion invalida, por favor intente de nuevo.')
        continue
