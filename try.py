keep = 1
pi = 3.14159


while keep == 1:


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

        # Radio circulo
            if cir == '1':
                
                r = float(input('Ingrese el radio (en número): '))

                a_cir = pi * r**2

                print('El área del círculo es: ', round(a_cir, 3))

        # Perimetro circulo    
            elif cir == '2':
                
                r = float(input('Ingrese el radio (en número): '))

                p_cir = 2 * pi * r 
                
                print('El perímetro del círculo es: ', round(p_cir, 3))
            
        # Diametro circulo
            elif cir == '3':

                r = float(input('Ingrese el radio (en número): '))
                
                d_cir = 2 * r

                print('El diámetro del círculo es: ', round(d_cir, 3))

            elif cir == '4':
                continue 

            elif cir == '5':
                print('Adiós.')
                keep = 0
        
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

        # Area triangulo
            if trg == '1':
                
                b = float(input('Ingrese valor de la base (en número): '))
                h = float(input('Ingrese valor de la altura (en número): '))

                a_tri = (b * h) / 2

                print('El área del triángulo es: ', round(a_tri, 3))
        
        # Perimetro triangulo
            elif trg == '2':
                
                a = float(input('Ingrese el valor del primer lado (en número): '))
                b = float(input('Ingrese el valor del segundo lado (en número): '))
                c = float(input('Ingrese el valor del tercer lado (en número): '))

                p_tri = a + b + c
                
                print('El perímetro del triángulo es: ', round(p_tri, 3))
        
        # Angulo triangulo
            elif trg == '3':

                ang_a = float(input('Ingrese el valor del primer ángulo (en número): '))
                ang_b = float(input('Ingrese el valor del segundo ángulo (en número): '))
                
                ang_tri = 180 - (ang_a + ang_b)

                print('El ángulo restante equivale a: ', round(ang_tri, 3))

            elif trg == '4':
                continue 

            elif trg == '5':
                print('Adiós.')
                keep = 0
        
            else:
                print('Opcion invalida, por favor intente de nuevo.')
                continue

    # Menu Trapecio
        elif opcion_twd == '3':
            
            def trpc():
                print('''
                    --- Seleccione una opcion:
                        
                        1. Área
                        2. Perímetro  
                        3. Volver
                        4. Salir
                ''')
            
            trpc()

            trap = input('Ingrese una opción: ')

        # Area trapecio
            if trap == '1':
                
                bm = float(input('Ingrese el valor de la base mayor (en número): '))
                b = float(input('Ingrese el valor de la base menor (en número): '))
                h = float(input('Ingrese el valor de la altura (en número): '))

                a_trap = ((bm + b) * h) / 2

                print('El área del trapecio es: ', round(a_trap, 3))
            
        # Perimetro trapecio 
            elif trap == '2':
                
                a = float(input('Ingrese el valor del lado 1 (en número): '))
                b = float(input('Ingrese el valor del lado 2 (en número): '))
                c = float(input('Ingrese el valor del lado 3 (en número): '))
                d = float(input('Ingrese el valor del lado 4 (en número): '))

                p_trap = a + b + c + d
                
                print('El perímetro del círculo es: ', round(p_cir, 3))

            elif trap == '3':
                continue 

            elif trap == '4':
                print('Adiós.')
                keep = 0
        
            else:
                print('Opcion invalida, por favor intente de nuevo.')
                continue

    # Menu Rectangulo
        elif opcion_twd == '4':
            
            def rctg():
                print('''
                    --- Seleccione una opcion:
                        
                        1. Área
                        2. Perímetro 
                        3. Diagonal
                        4. Volver
                        5. Salir
                ''')
            
            rctg()

            rect = input('Ingrese una opción: ')

        # Area rectangulo
            if rect == '1':
                
                b = float(input('Ingrese el valor de la base (en número): '))
                h = float(input('Ingrese el valor de la altura (en número): '))

                a_rec = b * h

                print('El área del rectángulo es: ', round(a_rec, 3))
            
        # Perimetro rectangulo
            elif rect == '2':
                
                b = float(input('Ingrese el valor de la base (en número): '))
                h = float(input('Ingrese el valor de la altura (en número): '))

                p_rec = 2 * (b + h)
                
                print('El perímetro del rectángulo es: ', round(p_rec, 3))
        
        # Diagonal rectangulo
            elif rect == '3':

                b = float(input('Ingrese el valor de la base (en número): '))
                h = float(input('Ingrese el valor de la altura (en número): '))
                
                d_rec = (b**2 + h**2)**(1/2)

                print('La diagonal del rectángulo es: ', round(d_rec, 3))

            elif rect == '4':
                continue 

            elif rect == '5':
                print('Adiós.')
                keep = 0
        
            else:
                print('Opcion invalida, por favor intente de nuevo.')
                continue

        elif opcion_twd == '5':
            continue 

        elif opcion_twd == '6':
            print('Adiós.')
            keep = 0
    
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

        # Volumen piramide
            if opcion_prmd == '1':
                Ab = float(input('Ingrese el valor del área base (en número): '))
                h = float(input('Ingrese el valor de la altura (en número): '))
                
                v_piramide = (Ab * h) / 3 

                print('El volumen de la pirámide es: ', round(v_piramide, 3))
        
        # Area pirámide
            elif opcion_prmd == '2':
                Ab = float(input('Ingrese el valor del área base (en número): '))
                Al = float(input('Ingrese el valor del área lateral (en número): '))
                
                a_piramide = Ab + Al
            
                print('El aŕea de la piramide es: ', round(a_piramide, 3))

            elif opcion_prmd == '3':
                continue

            elif opcion_prmd == '4':
                print('Adiós.')
                keep = 0

            else:
                print('Opcion invalida, por favor intente de nuevo.')
                continue

    # Menu Cilindro
        elif opcion_trd == '2':
            
            def clndr():
                print('''
                    --- Seleccione una opcion:

                        1. Volumen
                        2. Área lateral
                        3. Área total
                        4. Volver
                        5. Salir
                    ''')
            
            clndr()

            opcion_clndr = input('Ingrese una opción: ')

        # Volumen cilindro
            if opcion_clndr == '1':
                
                r = float(input('Ingrese el valor del radio (en número): '))
                h = float(input('Ingrese el valor de la altura (en número): '))
                
                v_cilindro = pi * r**2 * h

                print('El volumen del cilindro es: ', round(v_cilindro, 3))

        # Area lateral cilindro
            elif opcion_clndr == '2':
                r = float(input('Ingrese el valor del radio (en número): '))
                h = float(input('Ingrese el valor de la altura (en número): '))
                
                al_cilindro = 2 * pi * r * h 

                print('El área lateral del cilindro es: ', round(al_cilindro, 3))
        
        # Area total cilindro
            elif opcion_clndr == '3':
                r = float(input('Ingrese el valor del radio (en número): '))
                h = float(input('Ingrese el valor de la altura (en número): '))
                
                at_cilindro = 2 * pi * r * (r + h)

                print('El área total del cilindro es: ', round(at_cilindro, 3))

            elif opcion_clndr == '4':
                continue

            elif opcion_clndr == '5':
                print('Adiós.')
                keep = 0

            else:
                print('Opcion invalida, por favor intente de nuevo.')
                continue

    # Menu Cono   
        elif opcion_trd == '3':

            def cono():
                print('''
                    --- Seleccione una opcion:

                        1. Volumen
                        2. Generatriz
                        3. Área lateral
                        4. Área total
                        5. Volver
                        6. Salir
                    ''')
            
            cono()

            opcion_cono = input('Ingrese una opción: ')

        # Volumen cono
            if opcion_cono == '1':
                r = float(input('Ingrese el valor del radio (en número): '))
                h = float(input('Ingrese el valor de la altura (en número): '))
                
                v_cono = (pi * r**2 * h) / 3

                print('El volumen del cono es: ', round(v_cono, 3))
        
        # Generatriz cono
            elif opcion_cono == '2':
                r = float(input('Ingrese el valor del radio (en número): '))
                h = float(input('Ingrese el valor de la altura (en número): '))

                g_cono = (r**2 + h**2)**(1/2)

                print('La generatriz del cono es igual a: ', round(g_cono, 3))
        
        # Area lateral cono
            elif opcion_cono == '3':
                r = float(input('Ingrese el valor del radio (en número): '))
                h = float(input('Ingrese el valor de la altura (en número): '))

                g_cono = (r**2 + h**2)**(1/2)

                al_cono = pi * r * g_cono 
                
                print('El área lateral del cono es igual a: ', round(al_cono, 3))
        
        # Area total cono
            elif opcion_cono == '4':
                r = float(input('Ingrese el valor del radio (en número): '))
                h = float(input('Ingrese el valor de la altura (en número): '))

                g_cono = (r**2 + h**2)**(1/2)
                
                at_cono = pi * r * (r + g_cono) 

                print('El área total del cono es igual a: ', round(at_cono, 3))

            elif opcion_cono == '5':
                continue

            elif opcion_cono == '6':
                print('Adiós.')
                keep = 0

            else:
                print('Opcion invalida, por favor intente de nuevo.')
                continue

    # Menu Prisma
        elif opcion_trd == '4':
            def prsm():
                print('''
                    --- Seleccione una opcion:

                        1. Volumen
                        2. Área
                        3. Volver
                        4. Salir
                    ''')
            
            prsm()

            opcion_prsm = input('Ingrese una opción: ')

        # Volumen prisma
            if opcion_prsm == '1':
                Ab = float(input('Ingrese el valor del área base (en número): '))
                h = float(input('Ingrese el valor de la altura (en número); '))

                v_prisma = Ab * h 

                print('El volumen del prisma es igual a: ', round(v_prisma, 3))
        
        # Area lateral prisma
            elif opcion_prsm == '2':
                pb = float(input('Ingrese el valor del perímetro base (en número): '))
                h = float(input('Ingrese el valor de la altura (en número); '))

                al_prisma = pb * h

                print('El área lateral del prisma es igual a: ', round(al_prisma, 3))
        
        #Area total prisma
            elif opcion_prsm == '3':
                Ab = float(input('Ingrese el valor del área base (en número): '))
                pb = float(input('Ingrese el valor del perímetro base (en número): '))
                h = float(input('Ingrese el valor de la altura (en número); '))

                al_prisma = pb * h

                at_prisma = 2 * Ab + al_prisma

                print('El área total del prisma es igual a: ', round(at_prisma, 3))
            
            elif opcion_prsm == '4':
                continue

            elif opcion_prsm == '5':
                print('Adiós.')
                keep = False

            else:
                print('Opcion invalida, por favor intente de nuevo.')
                continue


        elif opcion_trd == '5':
            continue 

        elif opcion_trd == '6':
            print('Adiós.')
            keep = 0
    
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

            print('El valor del área es: ', a_tri_rect)

        elif opcion_tr == '3':
            continue

        elif opcion_tr == '4':
            print('Adiós.')
            keep = 0
        
        else:
            print('Opcion invalida, por favor intente de nuevo.')
            continue

# Cerrar

    elif opcion == '4':
        print('Adiós.')
        keep = 0

# Opción inválida 

    else:
        print('Opcion invalida, por favor intente de nuevo.')
        continue
