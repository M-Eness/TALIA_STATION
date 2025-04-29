from PySide6.QtGui import QPixmap, Qt
from PySide6.QtWidgets import QMainWindow

from Camera.CameraThread import CameraThread
from ClientServer.ClientThread import ClientThread
from GPS.GPSClientThread import GPSClientThread
from Windows.MainWindow_Controller import MainWindow_Controller
from Windows.MainWindow_UI import Ui_MainWindow
import socket


class MainWindow_Form(QMainWindow):
    def __init__(self):
        super(MainWindow_Form,self).__init__()
        self.ui=  Ui_MainWindow()
        self.ui.setupUi(self)
        self.cntlr= MainWindow_Controller(self, self.ui)

        # Soket istemcisi thread'i başlat
        self.client_thread = ClientThread(host="localhost", port=7001)
        self.client_thread.received_data.connect(self.add_log)
        self.client_thread.start()

        self.camera_thread = CameraThread()
        self.camera_thread.frame_signal.connect(self.update_camera_frame)  # Kamerayı QLabel'e bağla
        self.camera_thread.start()

        self.gps_thread = GPSClientThread("IP_ADRESS", 5000)
        self.gps_thread.received_gps.connect(self.update_gps_label)
        self.gps_thread.start()


    def add_log(self, text):
        """Terminale yeni satır ekler."""
        self.ui.terminal_plainTextEdit.appendPlainText(text)

    def update_camera_frame(self, image):
        """Kamera görüntüsünü QLabel içinde güncelle"""
        """Kamera görüntüsünü QLabel içine sığdırarak güncelle"""
        scaled_image = image.scaled(self.ui.camera_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.camera_label.setPixmap(QPixmap.fromImage(scaled_image))

    def update_gps_label(self, gps_text):
        self.ui.GorevYukuYukseklikLabel_2.setText(gps_text)
    def closeEvent(self, event):
        """Pencere kapatıldığında thread'leri durdur"""
        self.gps_thread.stop()
        self.client_thread.stop()
        self.client_thread.wait()
        self.camera_thread.stop()
        self.camera_thread.wait()
        event.accept()

        #self.initilizeComponents()

 #   def initilizeComponents(self):
