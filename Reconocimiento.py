import numpy as np
import Deteccion
import time
import cv2
import os

EigenFace = cv2.face.createEigenFaceRecognizer(num_components=80, threshold=50)
FisherFace = cv2.face.createFisherFaceRecognizer(num_components=80, threshold=50)
Face_LBP = cv2.face.createLBPHFaceRecognizer(threshold=50)

def Preparar_Directorios(Directorios, Detect_Op):

    #   Esta funcion se encarga de leer los directorios que esten
    #   dentro del argumento de entrada "Directorios" posteriormente
    #   leera directorio por directorio y las imagenes que esten dentro
    #   de este, detectando asi los rostros y retornarlos segun al
    #   numero de directorio al que pertenezcan.

    Directorio = os.listdir(Directorios)    #   Lista de los Directorios dentro de Directorios

    rostros   = []  #   En este array se guardaran los rostros de cada usuario
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
        print SubDirectorio

        #   Se leera cada imagen en el SubDirectorio
        for Nombre_Imagen in Imagenes:

            SubImagen = SubDirectorio + "/" + Nombre_Imagen     #   Directorios/U1/1.jpg, Directorios/U1/2.jpg...
            print Nombre_Imagen

            #    Leemos la SubImagen
            #Imagi = cv2.imread(SubImagen,cv2.IMREAD_GRAYSCALE)
            Imagi = cv2.imread(SubImagen)
            Image = SubImagen

            #   Detectamos el Rostro segun Detect_Op, puede ser: Haar cascades o LBP.
            if(Detect_Op == 1):
                rostro = Deteccion.Deteccion_Haar(Image)    #   Detector Haar Cascade
            else:
                rostro = Deteccion.Deteccion_LBP(Image)     #   Detector LBP

            #   Si se detecto un rostro este se concatenara al array
            #   faces y se le asigna al array labels correspondiente
            if rostro is not None:
                #for (x ,y, w, h) in rostro:
                #    imageNp=np.array(Imagi,'uint8')
                #    rostros.append(imageNp[y:y+h,x:x+w])

                #Recorte = Deteccion.Recortar_Rostros(Imagi,rostro)
                #Ajuste = Deteccion.Ajustar_Rostro(Recorte, 200, 200)

                #rostr = Ajustar_Imagen (rostro, 256, 256)
                rostros.append(np.asarray(rostro, dtype=np.uint8))
                #rostros.append(np.asarray(Imagi, dtype=np.uint8))
                etiquetas.append(etiqueta)

    return rostros, etiquetas

def Entrenamiento(faces, labels):
    #   Este metodo se encarga de entrenar al sistema en los tres diferentes
    #   metodos de deteccion de rostros.

    #faces, labels = Preparar_Directorios("Entrenamiento", 1)
    EigenFace.train(faces, np.array(labels))
    FisherFace.train(faces, np.array(labels))
    Face_LBP.train(faces, np.array(labels))



def Prediccion(Imagen):
    #    AQUI SE HACE LA MAGIA, PARA ELLO YA DEBIO DE HABERSE
    #    ENTRENADO AL SISTEMA :3
    inicio = time.time()
    #    Creamos una copia de la imagen de Entrada

    #face = Deteccion.Deteccion_Haar(Imagen)
    face = cv2.imread(Imagen)

    #    Hacemos una prediccion del rostro usando
    #    el objeto global face_recognizer >:)
    label1 = EigenFace.predict(face)
    label2 = FisherFace.predict(face)
    label3 = Face_LBP.predict(face)

    #subjects es el vector que contiene el nombre de los
    #    usuarios variable global tambien
    print label1, label2, label3


    fin = time.time()
    tiempo = fin - inicio
    print tiempo
