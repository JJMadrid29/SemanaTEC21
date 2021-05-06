# Importar librerías
import cv2
import imutils

# Capturar video, cambiar parametros segun nuestra camara
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

#Imagen a añadir/sobreponer
image = cv2.imread('sidd.png', cv2.IMREAD_UNCHANGED)

# Detector de rostros
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#Mover la imagenes del filtro en el eje Y
eje = 0

while True:

    #lee el frame actual de la camara
    ret, frame = cap.read()
    
    if ret == False: break
        
    #resolucion de la ventana
    frame = imutils.resize(frame, width=848)
    
    # Detección de los rostros presentes en el fotograma
    faces = faceClassif.detectMultiScale(frame, 1.3, 5)
 
#creación ciclo
for (x, y, w, h) in faces:
        #cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0),2)
        # Redimensionar la imagen de entrada de acuerdo al ancho del
        # rostro detectado
        resized_image = imutils.resize(image, width=w)
        #cv2.imshow('frome',resized_image) //Nota: Prueba
        filas_image = resized_image.shape[0]
        #print("filas_image ",resized_image.shape[0]) // Nota: Prueba
        col_image = w
        # Determinar una porción del alto de la imagen de entrada 
        # redimensionada
        
        porcion_alto = filas_image //4 

        
      
