from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PySide6.QtGui import QPixmap, Qt
import sys

from CameraThread import CameraThread


class CameraWindow(QMainWindow):
    a = "asdşak"
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
        """Görüntüyü QLabel içine yerleştir"""
        self.camera_label.setPixmap(QPixmap.fromImage(image))

    def closeEvent(self, event):
        """Pencere kapatıldığında kamerayı durdur"""
        self.camera_thread.stop()
        self.camera_thread.wait()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CameraWindow()
    window.show()
    sys.exit(app.exec())