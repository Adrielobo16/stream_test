# Parte 1 - Importamos librerías.
import cv2 

cam = cv2.VideoCapture(0)       # Camara local de la laptop. 
if not cam.isOpened():
    print("No se puede abrir la cámara")
    exit()

while True:
    ret,frame = cam.read()      # Leerá el frame
    if not ret: 
        print("No se recibió el fotograma")
        break
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)   # Filtro escala de grises. 
    # Aplicar filtro
    bordes = cv2.Canny(gray,100,200)
    cv2.imshow('Video en vivo',frame)               # Muestra video de cámara.
    cv2.imshow('Detección de bordes',bordes)        # Muestra video con filtro.
    
    if cv2.waitKey(1) & 0xFF == ord('q'):           # Cierra la cámara oprimiendo la tecla.
        break
cam.release()
cv2.destroyAllWindows()