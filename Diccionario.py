# Diccionario


pi = 3.1416


# Figuras 2D

# circulo

a_cir = pi * r**2 # area del circulo
p_cir = 2 * pi * r # perimetro del circulo
d_cir = 2 * r # diametro del circulo

# triangulo 
a_tri = (b * h) / 2 # area del triangulo
p_tri = a + b + c # perimetro del triangulo
ang_tri = 180 - (ang_a + ang_b) # angulo del triangulo

# trapecio
a_trap = ((bm + b) * h) / 2 # area del trapecio
p_trap = a + b + c + d  # perimetro del trapecio

# rectangulo
a_rec = b * h # area del rectangulo
p_rec = 2 * (b + h) # perimetro del rectangulo
d_rec = (b**2 + h**2)**(1/2) # diagonal del rectangulo


# Figuras 3D


# Piramide
v_piramide = (Ab * h) / 3 # volumen de la piramide
a_piramide = Ab + Al # area de la piramide

# Cilindro
v_cilindro = pi * r**2 * h # volumen del cilindro
al_cilindro = 2 * pi * r * h # area lateral del cilindro
at_cilindro = 2 * pi * r * (r + h) # area total del cilindro

# cono

v_cono = (pi * r**2 * h) / 3 # volumen del cono
g_cono = (r**2 + h**2)**(1/2) # generatriz del cono (podria calcular al momento de ingresar los datos)
al_cono = pi * r * g_cono # area lateral del cono
at_cono = pi * r * (r + g_cono) # area total del cono

# prisma de n lados
v_prisma = Ab * h # volumen del prisma
al_prisma = pb * h # area lateral del prisma
at_prisma = 2 * Ab + al_prisma # area total del prisma

# triangulo rectangulo
a_tri_rect = (b * h) / 2 # area del triangulo rectangulo
pit = (b**2 + h**2)**(1/2) # hipotenusa del triangulo rectangulo



