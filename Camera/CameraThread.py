# camera_thread.py
import socket
import struct
import pickle
import cv2
import numpy as np
from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QImage

class CameraThread(QThread):
    frame_signal = Signal(QImage)

    def __init__(self, host="IP_ADRESS", port=9001):
        super().__init__()
        self.running = True
        self.host = host
        self.port = port
        self.client_socket = None

    def run(self):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((self.host, self.port))
            data = b""
            payload_size = struct.calcsize("!I")

            while self.running:
                while len(data) < payload_size:
                    packet = self.client_socket.recv(4096)
                    if not packet:
                        return
                    data += packet

                packed_msg_size = data[:payload_size]
                data = data[payload_size:]
                msg_size = struct.unpack("!I", packed_msg_size)[0]

                while len(data) < msg_size:
                    data += self.client_socket.recv(4096)

                frame_data = data[:msg_size]
                data = data[msg_size:]

                frame = pickle.loads(frame_data)
                img = cv2.imdecode(frame, cv2.IMREAD_COLOR)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

                h, w, ch = img.shape
                bytes_per_line = ch * w
                qt_image = QImage(img.data, w, h, bytes_per_line, QImage.Format_RGB888)
                self.frame_signal.emit(qt_image)

        except Exception as e:
            print(f"💥 Socket Hatası: {e}")
        finally:
            if self.client_socket:
                self.client_socket.close()

    def stop(self):
        self.running = False
        self.quit()
        self.wait()


"""import cv2
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
        self.cap.release()"""