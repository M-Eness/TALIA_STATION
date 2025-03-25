from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow

from Windows.MainWindow_UI import Ui_MainWindow


class MainWindow_Controller():
    def __init__(self, mainWindow:QMainWindow, ui:Ui_MainWindow):
        self.mainWindow= mainWindow
        self.ui= ui
       # self.timer = QTimer()
       # self.timer.timeout.connect(self.receive_data)
       # self.timer.start(1000)  # 1000 ms = 1 saniye


    def pbtn_start_clicked(self):
        self.ui.pushButton.setText("")