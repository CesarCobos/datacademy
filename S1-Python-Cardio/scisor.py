import random
import os
def cl():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def aleatorio():
    dicionario = ['Piedra', 'Papel', 'Tijera']
    rand = random.choice(dicionario)
    pc = "".join(rand)
    return pc


        

def run():
    mpc = 0
    mus = 0
    print("""
        Bienvenido al juego de Piedra, Papel o tijera

        Escribe tu elección para comenzar a jugar: Piedra, Papel, Tijera
        
        
        """)
    while mpc < 3 and mus < 3:

        us = input("Escribe tu opcion: ")
        us = us.capitalize()
        spc = aleatorio()

        
        if spc == us:
            cl()
            print ("""Empate!!
            Puntuación: 
            Pc = """+ str(mpc)
            + """
            Tú = """ + str(mus))

        elif spc == 'Piedra' and us == 'Papel':
            mus = mus + 1
            cl()
            print("""Ganaste esta ronda!
            Puntuación: 
            Pc = """+ str(mpc)
            + """
            Tú = """ + str(mus))
            if mus == 3:
                print ("Haz ganado!!, hasta pronto!!")
                break

   

        elif spc == 'Piedra' and us == 'Tijera':
            cl()
            mpc = mpc + 1
            print("""Perdiste esta ronda!"""
            +  
            """Puntuación:
            Pc = """ + str(mpc)
            + """
            Tú = """ + str(mus))
            if mpc == 3:
                print ("Haz Perdido!!, hasta pronto!!")
                break

        elif spc == 'Papel' and us == 'Piedra':
            cl()
            mpc = mpc + 1
            print("""Perdiste esta ronda!
            Puntuación: 
            Pc = """ + str(mpc)
            + """
            Tú = """ + str(mus))
            if mpc == 3:
                print ("Haz Perdido!!, hasta pronto!!")
                break

        elif spc == 'Papel' and us == 'Tijera':
            mus = mus + 1
            cl()
            print("""Ganaste esta ronda!
            Puntuación: 
            Pc = """+ str(mpc)
            + """
            Tú = """ + str(mus))
            if mus == 3:
                print ("Haz ganado!!, hasta pronto!!")
                break

        elif spc == 'Tijera' and us == ' Piedra':
            mus = mus + 1
            cl()
            print("""Ganaste esta ronda!
            Puntuación: 
            Pc = """+ str(mpc)
            + """
            Tú = """ + str(mus))
            if mus == 3:
                print ("Haz ganado!!, hasta pronto!!")
                break

        elif spc == 'Tijera'  and us == 'Papel':
            cl()
            mpc = mpc + 1
            print("""Perdiste esta ronda!
            Puntuación: 
            Pc = """ + str(mpc)
            + """
            Tú = """ + str(mus))  
            if mpc == 3:
                print ("Haz perdido!!, hasta pronto!!")
                break
   

if __name__ ==  '__main__':
    run()