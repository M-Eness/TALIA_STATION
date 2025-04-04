# camera.py
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PySide6.QtGui import QPixmap, Qt
import CameraThread  # Doğru dosya adıyla import et

class CameraWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Raspberry Pi Kamera - Canlı Görüntü")
        self.setGeometry(200, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.camera_label = QLabel("Bağlantı bekleniyor...", self)
        self.camera_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.camera_label)

        self.camera_thread = CameraThread(host="IP_ADRESS", port=9001)  # Raspberry IP ve port
        self.camera_thread.frame_signal.connect(self.update_frame)
        self.camera_thread.start()

    def update_frame(self, image):
        pixmap = QPixmap.fromImage(image)
        self.camera_label.setPixmap(pixmap.scaled(
            self.camera_label.size(), Qt.KeepAspectRatio))

    def closeEvent(self, event):
        self.camera_thread.stop()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CameraWindow()
    window.show()
    sys.exit(app.exec())


""""
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PySide6.QtGui import QPixmap, Qt
import sys

from CameraThread import CameraThread


class CameraWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kamera Görüntüsü")

        # Ana widget ve layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Kamera görüntüsü için QLabel
        self.camera_label = QLabel(self)
        self.camera_label.setAlignment(Qt.AlignCenter)  # Ortala
        self.layout.addWidget(self.camera_label)

        # Kamera thread başlat
        self.camera_thread = CameraThread()
        self.camera_thread.frame_signal.connect(self.update_frame)  # Sinyali bağla
        self.camera_thread.start()

    def update_frame(self, image):
       
        self.camera_label.setPixmap(QPixmap.fromImage(image))

    def closeEvent(self, event):
        
        self.camera_thread.stop()
        self.camera_thread.wait()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CameraWindow()
    window.show()
    sys.exit(app.exec())
"""