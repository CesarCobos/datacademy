#Calle de las librerías
import os #Librería para limpiar pantalla

#Creando una función para limpiar pantalla
def cl():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
#Aquí va la función para hacer el cálculo
def conv(const, nombre_dist, nombre_dist2,letra):
    d = float(input("""


═══════════════════════════════════════════════════════
Perfecto‼, seleccionaste convertir """ + nombre_dist + " a " + nombre_dist2 +
    """. 
    

Ahora dime, ¿Cuánt""" + letra + "s " + nombre_dist + " quieres convertir? "))
    tot = round(const * d,2)
    print("""


Bien, """ + str(d) +" "+ nombre_dist2 + " equivalen a " + str(tot) + " " + nombre_dist)
    
    option = input("""

Deseas continuar?: s/n """)
    if option == 's':
        run()
    else:
        cl()
        print("""
¡Está bien!, Nos vemos. 👋

""")
        exit()
    return tot

    

#Conversor de millas a kilometros
def run():
    option = '0'
    cl()
    while option != 's': #mientras el usuario no seleccione "s" el programa va a seguir
        #Este es el menú
        option = input("""
▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀  
▀   Te doy a bienvenida a otra fabulosa aplicación, ahora         ▀ 
▀   te ayudaré a convertir tus millas en kilómetors o viceversa.  ▀ 
▀                                                                 ▀ 
▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ 

▶ Primero selecciona qué deseas convertir

1.- Convertir Millas a Kilometros 
2.- Convertir Kilometros a metros

'S' Para salir.

✔ Elige una opcion: """)
#Quí el usuario debe elegir una opción
        if option == '1':
            conv(1.60934,"kilómetros", "millas","o")
        elif option == '2':
            conv(0.621371,"millas", "kilómetros","a")
        elif option == 's':
            cl()
            print("""
¡Está bien!, Nos vemos. 👋

""")
            exit()
        else:
#En caso de que la opción elegida no esté dentro de lo establecido, mandará un mensaje y mostará el menú
            cl()
            print("Intentemos de nuevo . . .")
            

if __name__ == '__main__':
    run()