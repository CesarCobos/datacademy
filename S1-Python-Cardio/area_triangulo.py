import os #Librería para limpiar pantalla
import math #Libreria para operaciones matemáticas

#Creando una función para limpiar pantalla
def cl():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    


def run(): #Inicializando programa
    option = 's'

#Aquí comienza el ciclo, mientras option sea distinto de "n" el programa seguirá en bucle, en caso contrario se terminará
    while option != 'n':
#limpia pantalla
        cl()
#Pantalla de bienvenida
        print(""" 
▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀
▀   Bienvenid@ a este fantástico programa para calcular el área de tu triángulo   ▀
▀                                                                                 ▀
▀   Este programa te ayudará a conocer el área de cualquier triángulo,            ▀
▀   además de saber el tipo de triángulo que tienes, si es Equilatero,            ▀
▀   Isóceles o Escaleno.                                                          ▀
▀                                                                                 ▀
▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ 

Ejemplos:
    Triángulo Equilatero        Triángulo Isósceles              Triángulo Escaleno
        Base = 6 cm                 Base = 6 cm                     Base = 6 cm
        Altura = 5.2 cm             Altura = 4 cm                   Altura = 7 cm
        Ángulo = 60°                Ángulo = 53°                    Ángulo = 35°

Tips:
    La base debe ser el lado más grande de tu triángulo



Comencemos:


        """)
        
#Comenzando con el ingreso de datos por parte del usuario
#Las variables son:
#Triángulo del usuario
    #Base = b
    #Altura = h
    #Ángulo = ang

        b = float(input("""
    Ingresa el valor de la base (cm): """))
        h = float(input("""
    Ingresa el valor de la altura (cm): """))
        ang = float(input("""
    Ahora, ingresa un ángulo menor a 60° que sea adyacente a la base: """))
        if ang > 60:
            ang = float(input("""
    El Ángulo debe ser menor a 60° y adyacente a la base: """))
        else:


#Calculando el área
            area = (b * h) / 2
            area = round(area,2)
            print("""


    📐 Esta es el área de tu triángulo: """ + str (area) + " cm² !")

#Ahora, se debe dividir el triángulo del usuario en dos secciones que, con respecto a un ángulo y el cateto opuesto (h) se calcula el valor del cateto adyacente, luego de esto se optiene la hipotenusa de este trigángulo secundario, todo esto es para conocer la dimensión de uno de los lados (además de la ya conocida base).

#Variables a utilizar
    #Radian = Valor de 1 grado en radianes
    #angulo_radianes = el valor de los grados ingresados por el usuario en radianes
    #tan_radiantes = el valor de la tangente del Ángulo en radianes
    #Altura ingresada por el usuario = h que se convierte en el valor del cateto opuesto
    #Ángulo ingresado por el usuario = ang

#Primero debemos obtener el valor del cateto adyacente, eso se hace con
#CA = CO / tan(ángulo)

#obteniendo tangente del ángulo, primero se debe convertir a radianes

#Valor de 1° en Radianes
            radian = 0.0174533
    
            ángulo_radianes = (ang * radian)

            tan_radianes = math.tan(ángulo_radianes)
    
    
#Valor de cateto adyacente
            ca = (h / tan_radianes)

#Valor de la hipotenusa
            hip = math.sqrt((ca*ca)+(h*h))
            #print(str(hip))

#Ahora se debe obtener el valor del tercer triángulo para conocer su hipotenusa y por lo tanto el valor del 3 lado
#Tenemos estos datos.
#Altura = h, es el valor original introducido por el usuario
#De los datos calculados tenemos que ña base de este terecer triángulo = b(original) - CA
    
#Calculando la base
            bt = b - ca
            #print(str(bt))

#Ya tenemos la base del tercer triángulo y la altura, ahora a calcular su hipotenusa

            hipt = math.sqrt((bt * bt)+(h * h))
            # print(str(hipt))

#Por fin tenemos todos los datos, ahora hay que redondearlos
            hip = round(hip,0)
            # print(str(hip))
            hipt = round(hipt,0)
            # print(str(hipt))
            b = round(b,0)

#Vamos a determinar el tipo de triángulo, para ello se hace con las siguientes condiciones

            if hip == hipt and hip == b and hipt == b:
                print("""

    💥Tu triángulo es equilatero💥""")
            elif hip == hipt or hip == b or hipt == b:
                print("""

    💥Tu triángulo es Isósceles💥""")
            else:
                print("""

    💥Tu triángulo es Escaleno💥""")

#Aquí se termina el cálculo y se pregunta si se quiere continuar
        option = input("""

    ¿Quieres hacer otro cálculo? s / n: """)

 
#Si la repuesta es no, el programa limpia la pantalla y se despide
    cl()
    print("""
Muy bien!, Adiós!""")

        

if __name__ == '__main__':
    run()