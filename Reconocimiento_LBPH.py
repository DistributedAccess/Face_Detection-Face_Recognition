import numpy as np
import time
import cv2
import os

face_recognizer = cv2.face.createLBPHFaceRecognizer(threshold=50)

def Deteccion_Rostro(Imagen):
    #   Este metodo Detecta el rostro de las fotografias y regresa el
    #   rostro de la persona para ser guardado posteriormente.
    gray = cv2.cvtColor(Imagen, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5);

    (x, y, w, h) = faces[0]

    return gray[y:y+h, x:x+w], faces[0]

def Preparar_Entrenamiento(Directorios):

    #   PRIMER_PASO!!!
    #   Obtener los Directorios (Un directorio por persona)
    dirs = os.listdir(Directorios)

    #   Lista que contiene todos los rostros
    faces = []
    #   Lista que contiene las etiquetas para todos los usuarios
    labels = []

    #   Se leera cada directorio y las imagenes en cada uno
    for dir_name in dirs:

        if not dir_name.startswith("U"):
        #    En caso de no existir ningun directorio D:
        #    el programa se sale y bye :(
            continue;

        #    SEGUNDO_PASO!!!
        #    Obtenemos el nombre de la etiqueta de la persona
        #    del dir_name

        label = int(dir_name.replace("U", ""))

        subject_dir_path = Directorios + "/" + dir_name

        subject_images_names = os.listdir(subject_dir_path)
        print subject_dir_path
        #    TERCER_PASO!!!
        #    Se leera cada imagen, de la cual se detectara
        #    el rostro y se agregara a la lista de rostros (faces = [$

	for image_name in subject_images_names:

            image_path = subject_dir_path + "/" + image_name

            print image_name

            #    Leemos la imagen
            image = cv2.imread(image_path)

            #    Imprimimos la imagen en una nueva ventana
            #   .
            #   .
            #   .

            #   Detectamos el Rostro

            face, rect = Deteccion_Rostro(image)

            if face is not None:
                faces.append(face)
                labels.append(label)

    return faces, labels

def Entrenamiento():

    inicio = time.time()
    faces, labels = Preparar_Entrenamiento("ATT")
    face_recognizer.train(faces, np.array(labels))
    fin = time.time()
    tiempo = fin - inicio
    print tiempo

def Prediccion(Imagen):
    #    AQUI SE HACE LA MAGIA, PARA ELLO YA DEBIO DE HABERSE
    #    ENTRENADO AL SISTEMA :3
    inicio = time.time()
    #    Creamos una copia de la imagen de Entrada

    Img = Imagen.copy()
    #    Se detecta el rostro desde la copia

    face, rect = Deteccion_Rostro(Imagen)

    #    Hacemos una prediccion del rostro usando
    #    el objeto global face_recognizer >:)
    label = face_recognizer.predict(face)

    #subjects es el vector que contiene el nombre de los
    #    usuarios variable global tambien
    print label

    text = Usuario_No(label)

    fin = time.time()
    tiempo = fin - inicio
    print tiempo

    return text
