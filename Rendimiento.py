from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from natsort import natsorted
import Reconocimiento
import numpy as np
import Deteccion
import random
import Matrix
import Menu
import time
import cv2
import os

def Preparar_Directorios(Directorios, Porcentaje, Detect_Op):
    """   Esta funcion se encarga de leer las imagenes que se encuentran
        en cada uno de los directorios que pertenezcan al directorio de
        entrada "Directorio" y retornar dos arrays, cada array contiene
        imagenes o rostros con sus respectivas clases o etiquetas.

        El argumento Porcentaje debera recibir un numero entre el 1 y el
        100, que represente el porcentaje de 1-100%  de imagenes a utlizar
        por SubDirectorio en el entrenamiento, el resto de imagenes se
        utilizaran en la prediccion.

        Este algoritmo escoje a las imagenes de forma aleatoria. Cada
        array corresponde al grupo de imagenes y etiquetas que se ocuparan
        en el entrenamiento y la prediccion.   """

    Directorio = os.listdir(Directorios)    #   Lista de los Directorios dentro de Directorios

    Directorio = natsorted(Directorio)      #   Ordenamos los Directorios

    Entrenamiento = []  #   Este array se retornara para el Entrenamiento
    Prediccion    = []  #   Este array se retornara para la Prediccion

    FaceE = []  #   En este array se guardaran los rostros de cada usuario para el entrenamiento
    LabeE = []  #   En este array se guardara el numero de directorio para el entrenamiento

    FaceP = []  #   En este array se guardaran los rostros de cada usuario para la prediccion
    LabeP = []  #   En este array se guardara el numero de directorio para la prediccion

    #   Se leera cada directorio y las imagenes en cada uno
    for Nombre_Directorio in Directorio:

        #   Si no hay ningun directorio que comienze con U
        #   el programa se cerrara
        if not Nombre_Directorio.startswith("U"):
            continue;


        etiqueta = int(Nombre_Directorio.replace("U", ""))      #   Se guardara el numero de U, eg U2 -->2
        SubDirectorio = Directorios + "/" + Nombre_Directorio   #   Directorios/U1, Directorios/U2...

        Imagenes = os.listdir(SubDirectorio)    #   Lista de las imagenes dentro del Subdirectorio U'n'...

        #print SubDirectorio
        I_E = len(Imagenes)
        I_E = round((I_E)*(Porcentaje/100.0))

        Contador = 0

        #   Se leera cada imagen en el SubDirectorio aleatoriamente
        random.shuffle(Imagenes)            #   Con esta linea nos aseguramos de tener imagenes aleatoriamente
        for Nombre_Imagen in Imagenes:

            SubImagen = SubDirectorio + "/" + Nombre_Imagen     #   Directorios/U1/1.jpg, Directorios/U1/2.jpg...
            #print Nombre_Imagen
            Image = SubImagen

            #   Detectamos el Rostro segun Detect_Op, puede ser: Haar cascades o LBP.
            if(Detect_Op == 1):
                rostro = Deteccion.Deteccion_Haar(Image)    #   Detector Haar Cascade
            else:
                rostro = Deteccion.Deteccion_LBP(Image)     #   Detector LBP

            #   Si se detecto un rostro este se concatenara al array
            #   faces y se le asigna al array labels correspondiente
            if rostro is not None:

                if Contador < I_E:
                    FaceE.append(np.asarray(rostro, dtype=np.uint8))
                    LabeE.append(etiqueta)
                    Contador = Contador + 1
                    #print Contador
                elif Contador >= I_E:
                    FaceP.append(np.asarray(rostro, dtype=np.uint8))
                    LabeP.append(etiqueta)

    Entrenamiento = [FaceE, LabeE]
    Prediccion = [FaceP, LabeP]

    return Entrenamiento, Prediccion

def Predecir_Imagenes(fotos, etiquetas, algoritmo):

    A = []
    c = 0
    for i in fotos:
        a = Reconocimiento.Prediccion(i,algoritmo)
        A.append(a[0][0])
        c = c+1
        print a
    return etiquetas, A

def Etiquetas(etiquetas):

    A = []
    B = len(etiquetas)
    a = etiquetas.count(etiquetas[0])
    c = a

    while(c <= B):
        A.append(etiquetas[c-1])
        c = c + a
    return A

if __name__ == "__main__":

    E   = True

    Op  = None
    BD  = None
    PO  = None
    CL  = None
    UM  = None
    CO  = None

    Entrenamiento = []
    Prediccion    = []

    while(True):

        Opciones = [BD,PO,CL,UM,CO]
        Op = Menu.Menu_Principal(Opciones)
        if(Op == '1'):
            BD = Menu.Base_Datos()
        elif(Op == '2'):
            PO = Menu.Porcentaje()
        elif(Op == '3'):
            CL = Menu.Clasifcador()
        elif(Op == '4'):
            UM = Menu.Umbral()
            Reconocimiento.Configurar_Umbrales(UM)
        elif(Op == '5'):
            CO = Menu.Componentes()
            Reconocimiento.Configurar_Componentes(CO)
        elif(Op == '6'):
            print('\n\t Preparando Directorios...')
            Entrenamiento, Prediccion = Preparar_Directorios(BD,PO,CL)
            print('\n\t Entrenado al Sistema...')
            Reconocimiento.Entrenamiento(Entrenamiento[0],Entrenamiento[1])
            real,pred=Predecir_Imagenes(Prediccion[0],Prediccion[1],1)
            f=Etiquetas(real)
            cnf_matrix = confusion_matrix(real,pred)
            plt.figure()
            Matrix.plot_confusion_matrix(cnf_matrix, classes=f,
                                  title='EigenFace')

            real,pred=Predecir_Imagenes(Prediccion[0],Prediccion[1],2)
            f=Etiquetas(real)
            cnf_matrix = confusion_matrix(real,pred)
            plt.figure()
            Matrix.plot_confusion_matrix(cnf_matrix, classes=f,
                                  title='FisherFace')

            real,pred=Predecir_Imagenes(Prediccion[0],Prediccion[1],3)
            cnf_matrix = confusion_matrix(real,pred)
            plt.figure()
            Matrix.plot_confusion_matrix(cnf_matrix, classes=f,
                                  title='LBPH')
            plt.show()

        elif(Op == 'E'):
            print("\n\t BYE!")
            break
