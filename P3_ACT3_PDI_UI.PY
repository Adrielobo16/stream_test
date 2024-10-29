# Parte 1 - Importar librerías
import cv2                                                              # Librería para trabajar con cámara.
import numpy as np                                                      # Librería para trabajar con matrices
from PyQt5 import QtWidgets,uic                                         # Librería para trabajar con interfaz gráfica
from PyQt5.QtCore import QTimer,QThread,pyqtSignal
from PyQt5.QtGui import QImage,QPixmap 

# Parte 2 - Configuraciones iniciales
app = QtWidgets.QApplication([])                    
gui = uic.loadUi('P3_ACT3.ui')                                          # Abrimos la interfaz
cap = cv2.VideoCapture(0)                                               # Camara local de la laptop.
proceso = 'normal'

# Parte 3 - Funciones de apoyo
def display_image(img, label):                                          # Muestra la imagen en QtDesigner
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)                           # Convertir el color de la imagen.
    h, w, ch = img.shape                                                # Tamaño de la interfaz de la imagen. / Alto, ancho, canal
    bytes_per_line = ch * w                                             # Número de bytes por línea
    qimg = QImage(img.data, w, h, bytes_per_line, QImage.Format_RGB888) # Convierte la imagen para que se pueda ser leida por QtDesigner
    pixmap = QPixmap.fromImage(qimg)                                    # Se lee la imagen convertida.
    label.setPixmap(pixmap)                                             # Muestra la imagen en el label.
    label.setScaledContents(True)                                       # Imagen escalada para no perder calidad.

def detect_edges(frame):                                                # Detectar bordes.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)                      # Convierte cámara en escala de grises.
    edges = cv2.Canny(gray, 100, 200)                                   # Aplica filtro Canny a la imagen gris.
    return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)                      # Regresa la imagen en vivo. 

def apply_filter(frame):                                                # Aplicamos filtro.
    return cv2.GaussianBlur(frame, (15,15), 0)                          # Regresa imagen con filtro con kernel.

def set_edge_detection_mode():
    global proceso
    proceso = 'bordes'

def set_filter_mode():
    global proceso
    proceso = 'filtro'

def set_normal_mode():
    global proceso 
    proceso = 'normal'

def stop_video():
    worker.stop()
    cap.release()
    gui.destroy()

class VideoThread(QThread):                                             # Trabajo en segundo plano.
    changePixmapOriginal = pyqtSignal(np.ndarray)                       # Convierte la imagen en una señal.
    changePixmapProcesado = pyqtSignal(np.ndarray)                      # Convierte la imagen en una señal.

    def run(self):                                                      # Abre cámara y pregunta en que modo estamos.
        global proceso
        while True: 
            ret, frame = cap.read()                                     # Se lee la cámara.
            if ret: 
                self.changePixmapOriginal.emit(frame)
                if proceso == 'bordes':
                    processed_frame = detect_edges(frame)
                elif proceso == 'filtro':
                    processed_frame = apply_filter(frame)
                else: 
                    processed_frame = frame
                self.changePixmapProcesado.emit(processed_frame)
    def stop(self):
        self.terminate()

worker = VideoThread()

# Parte 4 - Ejecución 
worker.changePixmapOriginal.connect(lambda frame: display_image(frame,gui.lbl_original))    # Lamba nos ayuda a crear una función en una sola línea.
worker.changePixmapProcesado.connect(lambda frame: display_image(frame,gui.lbl_procesado))  # Lamba nos ayuda a crear una función en una sola línea.
gui.btnStart.clicked.connect(set_normal_mode)                                               # Al oprimir botón se activa esa función.
gui.btnBordes.clicked.connect(set_edge_detection_mode)                                      # Al oprimir botón se activa esa función.
gui.btnGauss.clicked.connect(set_filter_mode)                                               # Al oprimir botón se activa esa función.
gui.actionSalir.triggered.connect(stop_video)                                               # Al oprimir se cierra la interfaz.
worker.start()
gui.show()                                                                                  # Muestra la interfaz.
app.exec()                                                                                  # Ejecuta acciones.
