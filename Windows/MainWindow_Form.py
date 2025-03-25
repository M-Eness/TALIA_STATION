from PySide6.QtWidgets import QMainWindow

from ClientServer.ClientThread import ClientThread
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
        self.client_thread = ClientThread(host=socket.gethostname(), port=6000)
        self.client_thread.received_data.connect(self.add_log)
        self.client_thread.start()


    def add_log(self, text):
        """Terminale yeni satır ekler."""
        self.ui.terminal_plainTextEdit.appendPlainText(text)

    def closeEvent(self, event):
        """Pencere kapatıldığında istemciyi kapat"""
        self.client_thread.stop()
        self.client_thread.wait()
        event.accept()

        #self.initilizeComponents()

 #   def initilizeComponents(self):
