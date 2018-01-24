# Deteccion y Reconocimiento de Rostros

## Introduccion

Este proyecto ha sido desarrollado con la intencion de medir la eficiencia de los algoritmos propuestos de detecion y 
reconocimiento facial de la libreria OpenCV en python. La libreria ofrece dos clasificadores para la deteccion de rostros 
y tres algoritmos de reconocimineto facial.

## OpenCV en Deteccion Facial.

Para poder detectar el rostro de una imagen es necesario contar con clasificador que el cual es un programa que ha sido 
entrenado con varias imagenes con rostros y sin ellos. OpenCV tiene dos clasificadores pre-entrenados de reconocmiento
facial los cuales son:

- **HaarCascades**
- **Local Binary Pattern (LBP)**

Ambos clasificadores trabajan en escalas de grises debido a que en la deteccion del rostro no es necesario considerar el
color para considerar si existe un rostro o no en la imagen
