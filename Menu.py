from time import sleep
import os
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

def Inicio(Opciones):
    os.system("clear||cls")
    print('\n\t{0}Escoja una opcion del menu:\n').format(WHITE)
    sleep(0.2)
    print('\t{0}[{1}1{2}]{3} Deteccion Comun....................{4}').format(YELLOW, RED, YELLOW, WHITE, Opciones[0])
    sleep(0.2)
    print('\t{0}[{1}2{2}]{3} Deteccion Ruido.......................{4}').format(YELLOW, RED, YELLOW, WHITE, Opciones[1])
    sleep(0.2)
    print('\t{0}[{1}3{2}]{3} Deteccion Experimental......................{4}').format(YELLOW, RED, YELLOW, WHITE, Opciones[2])
    sleep(0.2)
    print('\t{0}[{1}4{2}]{3} Configurar Umbral........................{4}').format(YELLOW, RED, YELLOW, WHITE, Opciones[3])
    sleep(0.2)
    print('\t{0}[{1}5{2}]{3} Configurar Componentes...................{4}').format(YELLOW, RED, YELLOW, WHITE, Opciones[4])
    sleep(0.2)
    print("\t{0}[{1}6{2}]{3} Let's Rock (Comenzar Prediccion)").format(YELLOW, RED, YELLOW, WHITE)
    sleep(0.2)
    print('\n\t{0}[{1}E{2}]{3} Salir\n').format(YELLOW, RED, YELLOW, WHITE)

    etiqueta = ('{0}Opcion{1}> '.format(BLUE, WHITE))
    Op = raw_input(etiqueta)

    return Op

def Menu_Principal(Opciones):
    os.system("clear||cls")
    print('\n{0}Escoja una opcion del menu:\n').format(WHITE)
    sleep(0.2)
    print('\t{0}[{1}1{2}]{3} Escojer Base de Datos....................{4}').format(YELLOW, RED, YELLOW, WHITE, Opciones[0])
    sleep(0.2)
    print('\t{0}[{1}2{2}]{3} Escojer Porcentaje.......................{4}').format(YELLOW, RED, YELLOW, WHITE, Opciones[1])
    sleep(0.2)
    print('\t{0}[{1}3{2}]{3} Escojer Clasifcador......................{4}').format(YELLOW, RED, YELLOW, WHITE, Opciones[2])
    sleep(0.2)
    print('\t{0}[{1}4{2}]{3} Configurar Umbral........................{4}').format(YELLOW, RED, YELLOW, WHITE, Opciones[3])
    sleep(0.2)
    print('\t{0}[{1}5{2}]{3} Configurar Componentes...................{4}').format(YELLOW, RED, YELLOW, WHITE, Opciones[4])
    sleep(0.2)
    print("\t{0}[{1}6{2}]{3} Let's Rock (Comenzar Prediccion)").format(YELLOW, RED, YELLOW, WHITE)
    sleep(0.2)
    print('\n\t{0}[{1}E{2}]{3} Salir\n').format(YELLOW, RED, YELLOW, WHITE)

    etiqueta = ('{0}Opcion{1}> '.format(BLUE, WHITE))
    Op = raw_input(etiqueta)

    return Op

def Base_Datos():
    os.system("clear||cls")
    Dir = next(os.walk('/home/verriva/Detection_Recognition'))[1]
    print('\n\t{0}Escoja una Base de Datos: \n').format(WHITE)
    Cont = 0
    for N_Dir in Dir:
        sleep(0.2)
        print('\t{0}[{1}{5}{2}]{3} Base de Datos {4}').format(YELLOW, RED, YELLOW, WHITE, N_Dir, Cont)
        Cont = Cont + 1
    sleep(0.2)
    #print('\t{0}[{1}E{2}]{3} Regresar al Menu Principal\n').format(YELLOW, RED, YELLOW, WHITE)

    etiqueta = ('{0}Opcion{1}> '.format(BLUE, WHITE))
    Op = raw_input(etiqueta)

    return Dir[int(Op)]

def Porcentaje():
    os.system("clear||cls")
    print('\n\t{0}Del 1 al 100 escriba el porcentaje de imagenes que utilizara para el Entrenamiento').format(WHITE)
    print('\t{0}NOTA: El porcentaje restante sera utilizado en la Prediccion \n').format(GREEN)

    etiqueta = ('{0}Porcentaje{1}> '.format(BLUE, WHITE))
    Op = raw_input(etiqueta)

    return int(Op)

def Clasifcador():
    os.system("clear||cls")
    print('\n\t{0}Escaja un clasificador').format(WHITE)
    sleep(0.2)
    print('\t{0}[{1}2{2}]{3} Haar Cascade').format(YELLOW, RED, YELLOW, WHITE)
    sleep(0.2)
    print('\t{0}[{1}3{2}]{3} Local Binary Pattern LBP').format(YELLOW, RED, YELLOW, WHITE)

    etiqueta = ('{0}Clasifcador{1}> '.format(BLUE, WHITE))
    Op = raw_input(etiqueta)

    return int(Op)

def Umbral():
    os.system("clear||cls")
    print('\n\t{0}Ingrese el Umbral a Utilizar en la Deteccion').format(WHITE)

    etiqueta = ('{0}Umbral{1}> '.format(BLUE, WHITE))
    Op = raw_input(etiqueta)

    return int(Op)

def Componentes():
    os.system("clear||cls")
    print('\n\t{0}Ingrese el numero de Componentes a Utilizar en EigenFace y FisherFace').format(WHITE)

    etiqueta = ('{0}Componentes{1}> '.format(BLUE, WHITE))
    Op = raw_input(etiqueta)

    return int(Op)
