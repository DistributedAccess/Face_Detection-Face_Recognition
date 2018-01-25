import Reconocimiento
import Deteccion
import time
import cv2
import os

Texto = []

def Escoge_Directorio_Prediccion(Directorios):

    #   Esta funcion se encarga de leer cada imagen del directorio
    #   de entrada y retornar la imagen y su etiqueta, esto con el
    #   proposito de probar la prediccion del algoritmo de
    #   reconocimiento

    Directorio = os.listdir(Directorios)    #   Lista de los Directorios dentro de Directorios

    fotos   = []  #   En este array se guardaran los rostros de cada usuario
    etiquetas = []  #   En este array se guardara el numero de directorio

    #   Se leera cada directorio y las imagenes en cada uno
    for Nombre_Directorio in Directorio:

        #   Si no hay ningun directorio que comienze con U
        #   el programa se cerrara
        if not Nombre_Directorio.startswith("U"):
            continue;

        etiqueta = int(Nombre_Directorio.replace("U", ""))      #   Se guardara el numero de U, eg U2 -->2
        SubDirectorio = Directorios + "/" + Nombre_Directorio   #   Directorios/U1, Directorios/U2...

        Imagenes = os.listdir(SubDirectorio)    #   Lista de las imagenes dentro del Subdirectorio Un...

        #   Se leera cada imagen en el SubDirectorio
        for Nombre_Imagen in Imagenes:

            SubImagen = SubDirectorio + "/" + Nombre_Imagen     #   Directorios/U1/1.jpg, Directorios/U1/2.jpg...

            fotos.append(SubImagen)
            etiquetas.append(etiqueta)

    return fotos, etiquetas

def Predecir_Imagenes(fotos, etiquetas):

    for i in fotos:
        a = Reconocimiento.Prediccion(i,etiquetas)
        print a

if __name__ == "__main__":

    Op =  input("    Escoja una Base de Datos: ")
    Cl =  input("    Escoja un clasifcador: ")
    print("     Preparando los directorios...")
    face, labe = Reconocimiento.Preparar_Directorios(Op,Cl)
    print("     Entrenando al sistema...")
    Reconocimiento.Entrenamiento(face,labe)
    foto, etiqueta = Escoge_Directorio_Prediccion(Op)
    SCl =  input("    Escoja un Subclasifcador: ")
    print("     Predeciendo Imagenes...")
    Predecir_Imagenes(foto, SCl)
