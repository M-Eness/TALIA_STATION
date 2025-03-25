import cv2
import numpy as np
from PySide6.QtCore import QThread, Signal, Qt
from PySide6.QtGui import QImage, QPixmap

class CameraThread(QThread):
    frame_signal = Signal(QImage)  # Kameradan gelen görüntüyü sinyal olarak arayüze aktarır

    def __init__(self, camera_index=0):
        super().__init__()
        self.camera_index = camera_index
        self.running = True  # Thread kontrolü için flag
        self.cap = cv2.VideoCapture(self.camera_index)  # Kamerayı başlat

    def run(self):
        while self.running:
            ret, frame = self.cap.read()  # Kameradan bir kare oku
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # OpenCV BGR formatını RGB'ye çevir
                h, w, ch = frame.shape
                bytes_per_line = ch * w
                qt_image = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
                self.frame_signal.emit(qt_image)  # Arayüze görüntüyü aktar

    def stop(self):
        self.running = False
        self.cap.release()