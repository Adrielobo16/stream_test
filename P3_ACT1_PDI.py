# Parte 1 - Importar librerías 
# pip install opencv-python
import cv2 
img = cv2.imread('markrober.jpg')
cv2.imshow('Imagen referencia', img)    # Nombre de la imagen 

# Reescalado de imagen
img_res = cv2.resize(img,(200,400),interpolation=cv2.INTER_CUBIC)  # Comando de reescala.

# Separacion de canales (color)
img_red = img[:,:,2]                    # Canal rojo BGR (0,1,2)
cv2.imshow('Canal Rojo', img_red)       # Muestra la imagen del canal rojo.
img_blue = img[:,:,0]                   # Canal azul BGR (0,1,2)
cv2.imshow('Canal Azul', img_blue)      # Muestra la imagen del canal azul.
img_green = img[:,:,1]                  # Canal verde BGR (0,1,2)
cv2.imshow('Canal Verde', img_green)    # Muestra la imagen del canal verde.

# Filtros de imagenes 
    # Filtro Gaussiano
blur = cv2.GaussianBlur(img,(9,9),0)
cv2.imshow("Imagen suavizada", blur)    # Muestra la imagen con filtro.  
    # Filtro Canny.
bordes = cv2.Canny(img,100,200)
cv2.imshow("Bordes detectados",bordes)  # Muestra la imagen con filtro
    # Filtro contornos
contornos,_ = cv2.findContours(bordes,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
for contorno in contornos:
    area = cv2.contourArea(contorno)
    print(f"Área del objeto: {area}")

#tamano = img.shape                      # Conocer el tamaño de nuestra matriz.    
#print(tamano)                           # Imprime el tamaño en la terminal. 
 
cv2.waitKey(0)                          # Se oprime una tecla la imagen se cerrará.  
cv2.destroyAllWindows()                 # Se cierra la imagen. 