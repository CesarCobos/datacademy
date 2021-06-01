#Calle de las librerías
import os #Librería para limpiar pantalla
import math
#Creando una función para limpiar pantalla
def cl():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

#Función para calcular el volumen de un cilindro
def cilindro():
    r = float(input("""
Elegiste conocer el volumen de un cilindro.

Recuerda que el volumen de un cilindro se obtiene con:

V = Ab * h

dónde:

Ab = área de la base        y Ab = pi * r²
h = altura.



¿Cuál es el radio?(cm): """))

    h = float(input("""
¿Y la altura? (cm): """))

    a = round(math.pi * (r*r),2)
    v = round((a *h),2)

    print("""

El área de la base del cilindro es de: """ + str(a) + " cm²")

    print("""

El volumen del cilindro es de: """ + str(v) + " cm³")

    option = input("""

¿Quieres conocer el volumen de otra figura?: s/n""")
    if option == 's':
        cl()
        run()
    else:
        cl()
        print("""

Muy bien, adiós!!

""")
        exit()
    return r,h,a,v


#Función par calcular el volumen de un cono
def cono():
    print("""
    
Muy bien! ahora vamos a calcular el volumen de un cono

¿Cuál es la fórmula para calcular su volumen?

V = 1/3 pi * r² * h""")

    r = float(input("""

Entonces, ¿Dime cuál es el raio de la base del cono? (cm): """))
    h = float(input("""

Ahora necesito conocer la altura de la figura (cm): """))
    v =round(( (1/3) * math.pi * (r *r) * h),2)
    
    print("""

Tu figura tiene un volumen de """ + str(v) + " cm³")
    option = input("""


¿Quieres conocer el volumen de otra figura?: s/n """)
    if option == 's':
        cl()
        run()
    else:
        cl()
        print("""

Muy bien, adiós!!

""")
        exit()
    return r,h,v

#Aquí va el cálculo de la esfera


def run():

#Aquí va un menú
    cl()
    option = '0'
    while option != 's':
        print("""
Bienvenido a tu programa para calcular volúmnes.

¿De qué figura quieres calcular el volumen?: 

1.- Cilindro
2.- Cono
3.- Esfera

""")

        option = input("""
Selecciona una opción: """)
        
        if option == '1':
            cl()
            cilindro()
        elif option == '2':
            cl()
            cono()
        elif option == '3':
            cl()
            esfera()



if __name__ == '__main__':
    run()